<!DOCTYPE HTML>
<html>

<head>
    <title>Spam Detector</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>
</head>

<?php
// Function to reformat input data to help prevent attacks
function reformat_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// define variables and set to empty values
$username = $usernameErr = "";
$keyword = $keywordErr = "";
$algorithm = 0;
$algorithmErr = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (!empty($_POST["username"])) {
        $username = reformat_input($_POST["username"]);
        $username = str_replace('@', '', $username);
    }
    else {
        $usernameErr = "Username is required";
    }

    if (!empty($_POST["keyword"])) {
        $keyword = reformat_input($_POST["keyword"]);
    }
    else {
        $keywordErr = "Keyword is required";
    }

    if (!empty($_POST["algorithm"])) {
        if ($_POST["algorithm"] == "kmp") {
            $algorithm = 1;
        }
        else if ($_POST["algorithm"] == "boyer-moore") {
            $algorithm = 2;
        }
        else if ($_POST["algorithm"] == "regex") {
            $algorithm = 3;
        }
    }
    else {
        $algorithmErr = "Please pick one algorithm";
    }
}
?>

<body>
<nav class="navbar navbar-default">
</nav>

<div class="container">
<form class="form" method="POST" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
    <div class="form-group">
        <label class="control-label" for="username">Username</label>
        <input type="text" name="username" class="form-control" value="<?php echo $username;?>" placeholder="@twitteruser">
        <span class="error"><?php echo $usernameErr;?></span>
    </div>
    <div class="form-group">
        <label class="control-label" for="keyword">Keyword</label>
        <input type="text" name="keyword" class="form-control" value="<?php echo $keyword;?>" placeholder="words in tweets">
        <span class="error"><?php echo $keywordErr;?></span>
    </div>
    <div class="form-group">
        <p class="control-label">Algorithm</p>
        <label class="radio-inline"><input type="radio" name="algorithm" value="kmp" <?php if ($algorithm == 1) echo "checked"?>> KMP</label>
        <label class="radio-inline"><input type="radio" name="algorithm" value="boyer-moore" <?php if ($algorithm == 2) echo "checked"?>> Boyer-Moore</label>
        <label class="radio-inline"><input type="radio" name="algorithm" value="regex" <?php if ($algorithm == 3) echo "checked"?>> Regex</label>
        <span class="error"><?php echo $algorithmErr;?></span>
    </div>
    <input class="btn btn-primary" type="submit" name="submit" value="Submit">
</form>

<?php
$is_form_valid = false;
if (empty($usernameErr) && empty($keywordErr) && empty($algorithmErr)) {
    $is_form_valid = true;
}

if(isset($_POST['submit']) && $is_form_valid) {
    $userid = $userimg = "";

    // Make query to execute userinfo script and get userid and profile picture
    $is_user_valid = false;
    $userinfo_query = "python userinfo.py " . $username;
    exec($userinfo_query, $userinfo_output, $retval);
    if ($retval == 0) {
        $is_user_valid = true;
        $userid = $userinfo_output[0];
        $userimg = $userinfo_output[1];
    }
    if ($is_user_valid) {
?>

<h3>Tweets from <i><?php echo "@".$username?></i></h2>
<img src="<?php echo $userimg?>" alt="profile-picture">

<?php
        /* INI KENAPA GABISA */
        $get_post_query = "python get_post.py ".$algorithm." ".$userid." ".$keyword;
        echo $get_post_query; // for debugging
        exec($get_post_query, $get_post_output, $ret);
        echo $ret; // for debugging
        foreach ($get_post_output as $tweet) {
            echo $tweet;
        }
    }
}
?>
</div>
</body>

</html>