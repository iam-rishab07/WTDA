<?php
session_start();

$eno = $_SESSION['eno'];
$ename = $_SESSION['ename'];
$addr = $_SESSION['addr'];
$basic = $_SESSION['basic'];
$da = $_SESSION['da'];
$hra = $_SESSION['hra'];

$total = $basic + $da + $hra;
?>
<html>
<body>
    <h2>Employee Payslip</h2>
    <table border="1">
        <tr><td>Emp No:</td><td><?php echo $eno; ?></td></tr>
        <tr><td>Name:</td><td><?php echo $ename; ?></td></tr>
        <tr><td>Address:</td><td><?php echo $addr; ?></td></tr>
        <tr><td>Basic:</td><td><?php echo $basic; ?></td></tr>
        <tr><td>DA:</td><td><?php echo $da; ?></td></tr>
        <tr><td>HRA:</td><td><?php echo $hra; ?></td></tr>
        <tr><td><b>Total Salary:</b></td><td><b><?php echo $total; ?></b></td></tr>
    </table>
    <br>
    <a href="page1.php">Start Again</a>
</body>
</html>