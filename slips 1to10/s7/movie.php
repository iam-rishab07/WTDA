<!-- Q. 1) Write a PHP script to read “Movie.xml” file and print all MovieTitle and ActorName of
file using
OMDocument Parser. “Movie.xml” file should contain following information with at least 5
records
Wth values. M vieInfoMovieNo, MovieTitle, ActorName ,ReReleaseYear -->

<?php
// Create a new DOMDocument object
$dom = new DOMDocument();

// Load the XML file
if (!$dom->load("Movie.xml")) {
    die("Error: Failed to load XML file.");
}

// Get all 'MovieInfo' elements
$movies = $dom->getElementsByTagName('MovieInfo');

echo "<h2>Movie List</h2>";

// Loop through each MovieInfo node
foreach ($movies as $movie) {
    // Get MovieTitle and ActorName elements
    $title = $movie->getElementsByTagName('MovieTitle')->item(0)->nodeValue;
    $actor = $movie->getElementsByTagName('ActorName')->item(0)->nodeValue;

    echo "<strong>Movie Title:</strong> " . $title . " | ";
    echo "<strong>Actor Name:</strong> " . $actor . "<br>";
}
?>