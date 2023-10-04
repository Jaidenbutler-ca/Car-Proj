<?php
    $mysqli = new mysqli("Localhost","python","Weemee12","car","1433");

    if ($mysqli -> connect_errno) {
        echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
        exit();
    }
    else {
        echo "Connected to MySQL";
    }