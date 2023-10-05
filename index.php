<?php 
    include ("test.php");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div ="Top_Of_Page">
        <h1>Vehicle Display Test</h1>

        <table>
            <tr>
                <th>Year</th>
                <th>Make</th>
                <th>Name</th>
                <th>Price</th>
                <th>Dealer</th>
                <th>City</th>
            </tr>
            <tr>
                <td><?php echo $year; ?></td>
                <td><?php echo $make; ?></td>
                <td><?php echo $name; ?></td>
                <td><?php echo $price; ?></td>
                <td><?php echo $dealer; ?></td>
                <td><?php echo $city; ?></td>
            </tr>
        </table>
    </div>
</body>
</html>