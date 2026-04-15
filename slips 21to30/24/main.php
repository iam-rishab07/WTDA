<!-- Q. 1) Write a PHP script to create student.xml file which contains student roll no, name,
address, college
And course. Print students detail of specific course in tabular format after accepting
course as input. -->

<?php
// 1. Create the XML file if it doesn't exist
$students = [
    ["r" => 1, "n" => "John", "a" => "Pune", "clg" => "ABC", "c" => "CS"],
    ["r" => 2, "n" => "Jane", "a" => "Mumbai", "clg" => "DEF", "c" => "IT"],
    ["r" => 3, "n" => "Tom", "a" => "Nashik", "clg" => "GHI", "c" => "CS"]
];

$xml = new SimpleXMLElement('<Bookstore/>');
foreach ($students as $s) {
    $student = $xml->addChild('student');
    $student->addChild('rollno', $s['r']);
    $student->addChild('name', $s['n']);
    $student->addChild('address', $s['a']);
    $student->addChild('college', $s['clg']);
    $student->addChild('course', $s['c']);
}
$xml->asXML('student.xml');

// 2. Logic to filter and display
$search = $_POST['course'] ?? '';
?>

<form method="post">
    Enter Course (e.g., CS or IT): <input type="text" name="course">
    <input type="submit" value="Search">
</form>

<?php
if ($search) {
    $xmlData = simplexml_load_file('student.xml');
    // Using XPath to find specific course
    $res = $xmlData->xpath("//student[course='$search']");

    echo "<table border='1'><tr><th>RollNo</th><th>Name</th><th>College</th></tr>";
    foreach ($res as $st) {
        echo "<tr><td>{$st->rollno}</td><td>{$st->name}</td><td>{$st->college}</td></tr>";
    }
    echo "</table>";
}
?>