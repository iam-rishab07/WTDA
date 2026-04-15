<!-- Q. 1) Create employee table as follows EMP (eno, ename, designation, salary). Write Ajax

program to

Select the employees name and print the selected employee’s details. -->

<?php
$conn = pg_connect("host=localhost dbname=my_db user=postgres password=root");

$name = $_POST['name'];

$query = "SELECT * FROM EMP WHERE ename = '$name'";
$result = pg_query($conn, $query);

if ($row = pg_fetch_assoc($result)) {
    echo "<b>Number:</b> " . $row['eno'] . "<br>";
    echo "<b>Designation:</b> " . $row['designation'] . "<br>";
    echo "<b>Salary:</b> " . $row['salary'];
} else {
    echo "Employee not found.";
}

pg_close($conn);
?>