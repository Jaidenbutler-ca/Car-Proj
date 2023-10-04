<?php
    $user = "localhost";
    $pass = "aw";


    $ODBCConnection = odbc_connect("DRIVER={ODBC Driver 18 for SQL Server};SERVER=DESKTOP-H10UUI9\SQLEXPRESS;Database=car", "gang", "091516");

    $query = "SELECT * FROM info";
    $RecordSet = odbc_exec($ODBCConnection, $query);

        while (odbc_fetch_row($RecordSet)) {
            $result = odbc_result_all($RecordSet, "border=1");
        }
        odbc_close($ODBCConnection);
    ?>
