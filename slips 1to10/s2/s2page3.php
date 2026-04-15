<?php
$st = $_COOKIE['style'];
$sz = $_COOKIE['size'];
$cl = $_COOKIE['color'];
$bg = $_COOKIE['back'];
?>
<html>
<head>
<style>
    body {
        font-family: <?php echo $st; ?>;
        font-size: <?php echo $sz; ?>;
        color: <?php echo $cl; ?>;
        background-color: <?php echo $bg; ?>;
    }
</style>
</head>
<body>
    <h1>Hello! This is the Final Page</h1>
    <p>The settings you chose are now applied to this text and background.</p>
</body>
</html>