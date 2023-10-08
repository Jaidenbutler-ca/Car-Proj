<?php
// session_start();
$modelVariable = "%";
$makeVariable = "%";
$yearMinVariable = 0;
$yearMaxVariable = 2025;
$minPrice = '%';
$maxPrice = '';





if (isset($_SESSION["makeVariable"])) {
    $makeVariable = $_SESSION["makeVariable"];
} else {
    $makeVariable = "";
}
if (isset($_SESSION["modelVariable"])) {
    $modelVariable = $_SESSION["modelVariable"];
} else {
    $modelVariable = "";
}

if(isset($_SESSION["yearMinVariable"])) {
    $yearMinVariable = $_SESSION["yearMinVariable"];
} else {
    $yearMinVariable = 0;
}

if (isset($_SESSION["yearMaxVariable"])) {
    $yearMaxVariable = $_SESSION["yearMaxVariable"];
} else {
    $yearMaxVariable = 9999;
}

$yearVariable = '%';

$minePriceVariable = 0;
$maxPriceVariable = 999999999; # 9 9's
$ODBCConnection = odbc_connect("DRIVER={ODBC Driver 18 for SQL Server};SERVER=JAIDENBUTLER-CA\SQLEXPRESS;Database=car", "Python", "Weemee12");

$query = strtoupper("SELECT year, make, name, price, dealer, city FROM info ORDER BY NEWID()");

# Testing  here

$query2 = "SELECT year, make, name, price, dealer, city FROM info WHERE make LIKE ? AND name LIKE ? AND year LIKE ? and year > ? and year < ? ORDER BY NEWID()";
$stmt = odbc_prepare($ODBCConnection, $query2);

odbc_execute($stmt, [$makeVariable, $modelVariable, $yearVariable, $yearMinVariable, $yearMaxVariable]);

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
echo "  Year variable test.php is: " . $yearMinVariable;
echo " Max year variable test.php: " . $yearMaxVariable;

# End Testing

odbc_close($ODBCConnection);
?>
