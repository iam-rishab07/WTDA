<?php
$conn = mysqli_connect("localhost", "root", "", "my_db");

$user = $_POST['username'];
$pass = $_POST['password'];

// Simple query to check credentials
$query = "SELECT * FROM users WHERE username='$user' AND password='$pass'";
$result = mysqli_query($conn, $query);

if(mysqli_num_rows($result) > 0) {
    echo "valid";
} else {
    echo "invalid";
}

mysqli_close($conn);
?>