<?php
$name = $_POST['name'];
$age = (int)$_POST['age'];
$nationality = $_POST['nationality'];

$errors = [];

// 1. Name validation (Regex for Uppercase letters and spaces)
if (!preg_match("/^[A-Z ]+$/", $name)) {
    $errors[] = "Name must be in UPPERCASE letters only.";
}

// 2. Age validation
if ($age < 18) {
    $errors[] = "Age must be at least 18 years.";
}

// 3. Nationality validation
if (strtolower($nationality) !== "indian") {
    $errors[] = "Nationality must be Indian.";
}

// Output result
if (empty($errors)) {
    echo "<b style='color:green'>Success: $name is eligible to vote!</b>";
} else {
    echo "<b style='color:red'>Errors: " . implode(", ", $errors) . "</b>";
}
?>