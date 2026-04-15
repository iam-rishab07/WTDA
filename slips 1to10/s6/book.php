<!-- Assignment-6)
Q. 1) Write PHP script to read “book.xml” file into simpleXML object. Display attributes and
elements . -->


<?php
// Load the XML file into a SimpleXML object
$xml = simplexml_load_file("book.xml");

if ($xml === false) {
    die("Error: Cannot create object");
}

echo "<h2>Book Details</h2>";

// Displaying Attributes
echo "<strong>Attributes:</strong><br>";
echo "ISBN: " . $xml['isbn'] . "<br>";
echo "Publisher: " . $xml['publisher'] . "<br><br>";

// Displaying Elements
echo "<strong>Book Elements:</strong><br>";
echo "Title: " . $xml->title . "<br>";
echo "Author: " . $xml->author . "<br>";
echo "Description: " . $xml->description . "<br>";
?>