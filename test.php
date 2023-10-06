<?php
    $user = "localhost";
    $pass = "aw";
    $year = 0;

    $makeVariable = '%';
    $modelVariable = '%';
    $yearVariable =  '%';


    $ODBCConnection = odbc_connect("DRIVER={ODBC Driver 18 for SQL Server};SERVER=DESKTOP-H10UUI9\SQLEXPRESS;Database=car", "gang", "091516");

    $query = strtoupper("SELECT year, make, name, price, dealer, city FROM info ORDER BY NEWID()");

# Testing  here
    
    $query2 = "SELECT year, make, name, price, dealer, city FROM info WHERE make LIKE ? AND name LIKE ? AND year LIKE ? ORDER BY NEWID()";
    $stmt = odbc_prepare($ODBCConnection, $query2);

    odbc_execute($stmt, array($makeVariable, $modelVariable, $yearVariable));

    while ($row = odbc_fetch_array($stmt)) {
        $year = $row['year'];
        $make = $row['make'];
        $name = $row['name'];
        $price = $row['price'];
        $dealer = $row['dealer'];
        $city = $row['city'];
    }












# End Testing




        odbc_close($ODBCConnection);
    ?>
