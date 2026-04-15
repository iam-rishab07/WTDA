<!-- Q. 1Write a PHP script to change the preferences of your web page like font style, font size,
font color,
Background color using cookie. Display selected setting on next web page and actual
implementation
(with new settings) on third page (Use Cookies). -->

<?php
if(isset($_POST['ok'])) {
    $st = $_POST['s1'];
    $sz = $_POST['s2'];
    $cl = $_POST['s3'];
    $bg = $_POST['s4'];

    setcookie("style", $st);
    setcookie("size", $sz);
    setcookie("color", $cl);
    setcookie("back", $bg);

    header("location:s2page2.php");
}
?>
<html>
<body>
<form action="s2index.php" method="post">
    Select Font Style: <input type="text" name="s1"><br>
    Select Font Size: <input type="text" name="s2"><br>
    Select Font Color: <input type="text" name="s3"><br>
    Select Background Color: <input type="text" name="s4"><br>
    <input type="submit" name="ok" value="Next">
</form>
</body>
</html>