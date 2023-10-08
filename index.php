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

<?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $makeVariable = $_POST["selectMake"];
            $modelVariable = $_POST["inputModel"];
            $yearVariable = $_POST["inputYear"];
            $minPriceVariable = $_POST["MinPrice"];
            $maxPriceVariable = $_POST["MaxPrice"];
            // Save $makeVariable to a session variable
            $_SESSION["makeVariable"] = $makeVariable;
            header("Location: index.php?make= " . urlencode($makeVariable));
        }
        session_start();
        if (isset($GET["make"])) {
            $makeVariable = $_GET["make"];
        }
    ?>
    <div class="Top_Of_Page">
        <h1>Vehicle Display Test</h1>
        <img id="Placeholder_Image"src="placeholder.jpg" style="width:500px;height:500px;" alt="Placeholder Image">

        <table class="Top_Of_Page">
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

    <!-- making a variable to hold the make in order to use it for search -->


    <!-- Testing Here -->

<!-- Changed this -->
<form method="POST">
<!-- hopefully it works, do it when you get home -->
    
    
<label for="selectMake">Make:</label>
<select name="selectMake" id="selectMake">
    <option value="Any" 
    selected>Any</option>
    <option value="Acura">Acura</option>
    <option value="BMW">BMW</option>
    <option value="Chevrolet">Chevrolet</option>
    <option value="Dodge">Dodge</option>
    <option value="Ford">Ford</option>
    <option value="GMC">GMC</option>
    <option value="Honda">Honda</option>
    <option value="Hyundai">Hyundai</option>
    <option value="Infiniti">Infiniti</option>
    <option value="Jeep">Jeep</option>
    <option value="Kia">Kia</option>
    <option value="Mercedes-Benz">Mercedes-Benz</option>
    <option value="Nissan">Nissan</option>
    <option value="Porsche">Porsche</option>
    <option value="RAM">RAM</option>
    <option value="Toyota">Toyota</option>
</select>
<button type="submit">Submit</button>
    </form>

<label for="inputYear">Year:</label>
<input type="text" id="inputYear" name="inputYear" placeholder="Year">
    
    
<!-- working here -->
<label for"dateSelect">Year:</label>

    
    
    

<label for="inputModel">Model:</label>
<input type="text" id="inputModel" name="inputModel" placeholder="Model">

<label for="MinPrice">Min Price:</label>
<input type="text" id="MinPrice" name="MinPrice" placeholder="Min Price">

<label for="MaxPrice">Max Price:</label>
<input type="text" id="MaxPrice" name="MaxPrice" placeholder="Max Price">

</body>
</html>