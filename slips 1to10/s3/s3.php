<?php
session_start(); // Corrected: session_start (lowercase)

// Initialize attempts at 3 if not already set
if (!isset($_SESSION['attempts'])) {
    $_SESSION['attempts'] = 3;
}

// Check if login form has been submitted
if (isset($_POST['submit'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Credentials
    $correct_username = 'myusername';
    $correct_password = 'mypassword';

    // 1. Check if user is already locked out
    if ($_SESSION['attempts'] <= 0) {
        echo "Maximum login attempts exceeded. Please try again later.";
    } 
    // 2. Check if credentials are correct
    else if ($username == $correct_username && $password == $correct_password) {
        $_SESSION['loggedin'] = true;
        $_SESSION['attempts'] = 3; // Reset attempts on success
        header('Location: welcome.php');
        exit;
    } 
    // 3. Wrong credentials
    else {
        $_SESSION['attempts']--; // Decrement
        
        if ($_SESSION['attempts'] <= 0) {
            echo "Maximum login attempts exceeded. Access Denied.";
        } else {
            echo "Invalid username or password. You have " . $_SESSION['attempts'] . " attempt(s) left.";
        }
    }
}
?>

<form method="post" action="">
    User: <input type="text" name="username"><br>
    Pass: <input type="password" name="password"><br>
    <input type="submit" name="submit" value="Login">
</form>