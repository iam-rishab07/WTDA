<!-- Q. 1) Write a PHP script to keep track of number of times the web page has been accessed
(Use Session
Tracking) -->

<?php

session_start();

if(isset($_SESSION['visit_count']))
    {
        $_SESSION['visit_count']+=1;
    }else{
        $_SESSION['visit_count']=1;
    }

echo"<h1>Page Access Tracker</h1>";
echo"<p>You have accessesd this page <b>".$_SESSION['visit_count']."</b> Times.</p>";

?>
