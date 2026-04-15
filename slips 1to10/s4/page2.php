<?php
session_start();
if (isset($_POST['next'])) {
    $_SESSION['basic'] = $_POST['basic'];
    $_SESSION['da'] = $_POST['da'];
    $_SESSION['hra'] = $_POST['hra'];
    header("Location: page3.php");
    exit();
}
?>
<html>
<body>
    <h2>Step 2: Earning Details</h2>
    <form method="post">
        Basic: <input type="text" name="basic"><br>
        DA: <input type="text" name="da"><br>
        HRA: <input type="text" name="hra"><br>
        <input type="submit" name="next" value="Finish">
    </form>
</body>
</html>