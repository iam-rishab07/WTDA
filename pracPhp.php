<?php

$xml = simplexml_load_file("book.xml");

if($xml==false)
    {
        die("Error!");
    }

    echo"<h2>Book Details</h2>";
    echo"<strong>Attributes :</strong><br>";
    echo"ISBN : ".$xml['isbn']."<br>";
    echo" Publisher : ".$xml['publisher']."<br>";

    echo"<strong>Details :</strong><br>";
    echo"Title : ".$xml->title."<br>";
    echo"Author : ".$xml->author."<br>";
    echo"Descripton : ".$xml->description."<br>";
?> 