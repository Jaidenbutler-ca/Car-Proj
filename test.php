<?php
    $user = "localhost";
    $pass = "aw";
    $year = 0;


    $ODBCConnection = odbc_connect("DRIVER={ODBC Driver 18 for SQL Server};SERVER=JAIDENBUTLER-CA\SQLEXPRESS;Database=car", "Python", "Weemee12");

    $query = strtoupper("SELECT year, make, name, price, dealer, city FROM info ORDER BY NEWID()");
    $RecordSet = odbc_exec($ODBCConnection, $query);

        while (odbc_fetch_row($RecordSet)) {
           # $result = odbc_result($RecordSet, "year") . " " . odbc_result($RecordSet, "make") . " " . odbc_result($RecordSet, "name") . " " . odbc_result($RecordSet, "price") . " " . odbc_result($RecordSet, "dealer") . " " . odbc_result($RecordSet, "city");

            $year = odbc_result($RecordSet, "year");
            $make = odbc_result($RecordSet, "make");
            $name = odbc_result($RecordSet, "name");
            $price = odbc_result($RecordSet, "price");
            $dealer = odbc_result($RecordSet, "dealer");
            $city = odbc_result($RecordSet, "city");
        }
        



        odbc_close($ODBCConnection);
    ?>
