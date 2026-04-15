<!-- Q. 1) Write a PHP script to accept Employee details (Eno, Ename, Address) on first page.
On second
Page accept earning (Basic, DA, HRA). On third page print Employee information (Eno,
Ename, Address,
Basic, DA, HRA, Total) [ Use Session] -->

<?php
session_start();
if (isset($_POST['next'])) {
    $_SESSION['eno'] = $_POST['eno'];
    $_SESSION['ename'] = $_POST['ename'];
    $_SESSION['addr'] = $_POST['addr'];
    header("Location: page2.php");
    exit();
}
?>
<html>
<body>
    <h2>Step 1: Employee Details</h2>
    <form method="post">
        No: <input type="text" name="eno"><br>
        Name: <input type="text" name="ename"><br>
        Address: <input type="text" name="addr"><br>
        <input type="submit" name="next" value="Next">
    </form>
</body>
</html>