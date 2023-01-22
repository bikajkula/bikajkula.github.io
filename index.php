<?php
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "kladionica";
	$conn = new mysqli($servername, $username, $password,$dbname);
	$sql = "SELECT * FROM `mecevi`";
	$results = mysqli_query($conn,$sql);
	$result = mysqli_query($conn,$sql);
?>



<!DOCTYPE html>
<html>
	<head>
		<title>FORMA</title>
		<meta charset="utf-8">
		<meta name="author" content="Mihajlo Karadzic" />
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
		<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css" rel="stylesheet"/>
		<link rel="stylesheet" href="css/style.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
	</head>
	<body>
		<nav class="navbar navbar-expand-md navbar-dark justify-content-center" id="top">
			<div class="justify-content-center">
				<ul class="navbar-nav">
					<li class="nav-item">
						<a class="nav-link" href="index.php">Kreiraj tiket</a>
					</li>
				</ul>
			</div>
		</nav>
		<div class="row justify-content-center mt-5 mb-5">
			<div class="col-lg-8 justify-content-center text-center mt-3">
				<h2><?php 
					$idd="SELECT MAX(id_tiket) FROM tiket";
					$get=mysqli_query($conn,$idd);
					while ($row = $get->fetch_assoc()) {
						
						echo "BROJ TIKETA: ".++$row['MAX(id_tiket)'] ."<br>";
						$tiketID=$row['MAX(id_tiket)'];
					}
				?>
				</h2>
				<table class="table table-dark">
					<tr>
						<td style="color:blue;">UTAKMICA</td>
						<td style="color:blue;">1</td>
						<td style="color:blue;">X</td>
						<td style="color:blue;">2</td>
					</tr>
					<?php  while($rowitem = mysqli_fetch_array($results)) {
						echo "<tr>";
						echo "<td>" . $rowitem['naziv'] . "</td>";
						echo "<td>" . $rowitem['domaci_kv'] . "</td>";
						echo "<td>" . $rowitem['nereseno_kv'] . "</td>";
						echo "<td>" . $rowitem['gosti_kv'] . "</td>";
						echo "</tr>";
					}
					?>
				</table>
				<form method="POST" action="submit_match.php">
					Izaberi mec</br>
					<select name="mecevi">
						<?php
							$sql1="SELECT * FROM mecevi WHERE id_mec NOT IN (SELECT mecevi_id_mec FROM stavka_tiketa WHERE tiket_id_tiket = '$tiketID')";
							$rezultat= mysqli_query($conn,$sql1);
							while ($row = mysqli_fetch_array($rezultat)) {
								
							echo "<option value='" . $row['id_mec'] ."' >" . $row['naziv'] ."</option>";
							}
						?>
					</select></br>
					<input type="radio" value="1" name="rez" required>1</input>
					<input type="radio" value="X" name="rez">X</input>
					<input type="radio" value="2" name="rez">2</input><br>
					<select style="display:none;" name="brTiketa">
						<option value="<?php echo $tiketID;?>"></option>
					</select>
					<input type="submit" value="Dodaj mec"></br>
				</form>
				<form method="POST" action="submit_ticket.php">
					Uplata(din)<br>
					<select style="display:none;" name="brTiketa">
						<option value="<?php echo $tiketID;?>"></option>
					</select>
					<input type="text" name="uplata"><br>
					<input type="submit" value="UPLATI TIKET"></br>
				</form>
			</div>
		</div>
	</body>
</html> 