<?php
// session_start();

if (isset($_SESSION["makeVariable"])) {
    $makeVariable = $_SESSION["makeVariable"];
} else {
    $makeVariable = "";
}


$user = "localhost";
$pass = "aw";
$year = 0;

// $makeVariable = '%';
$yearVariable = '%';
$modelVariable = '%';


$minePriceVariable = 0;
$maxPriceVariable = 999999999; # 9 9's
$ODBCConnection = odbc_connect("DRIVER={ODBC Driver 18 for SQL Server};SERVER=JAIDENBUTLER-CA\SQLEXPRESS;Database=car", "Python", "Weemee12");

$query = strtoupper("SELECT year, make, name, price, dealer, city FROM info ORDER BY NEWID()");

# Testing  here

$query2 = "SELECT year, make, name, price, dealer, city FROM info WHERE make LIKE ? AND name LIKE ? AND year LIKE ? ORDER BY NEWID()";
$stmt = odbc_prepare($ODBCConnection, $query2);

odbc_execute($stmt, [$makeVariable, $modelVariable, $yearVariable]);

while ($row = odbc_fetch_array($stmt)) {
    $year = $row['year'];
    $make = $row['make'];
    $name = $row['name'];
    $price = $row['price'];
    $dealer = $row['dealer'];
    $city = $row['city'];
}

echo "Make variable test.php is: " . $makeVariable;
echo "  Model variable test.php is: " . $modelVariable;

# End Testing

odbc_close($ODBCConnection);
?>
i