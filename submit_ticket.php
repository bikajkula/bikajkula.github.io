<?php
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "kladionica";
	$conn = new mysqli($servername, $username, $password,$dbname);
	$uplata=htmlspecialchars($_POST['uplata']);
	$tiketID=htmlspecialchars($_POST['brTiketa']);
	$sql = "INSERT INTO tiket(id_tiket,uplata) VALUES('$tiketID','$uplata')";
	$sql1 = "SELECT * FROM mecevi m INNER JOIN stavka_tiketa s ON m.id_mec= s.mecevi_id_mec GROUP BY m.id_mec HAVING m.id_mec IN (SELECT mecevi_id_mec FROM stavka_tiketa WHERE tiket_id_tiket= '$tiketID')";
	$sqldobitak="SELECT uplata FROM tiket WHERE id_tiket = '$tiketID'";
	$results = mysqli_query($conn,$sql1);
	$resultsdobitak=mysqli_query($conn,$sqldobitak);
	$dobitak=1;
	while($rowitem = mysqli_fetch_array($resultsdobitak)){
		$dobitak*=$rowitem['uplata'];
	}
	$conn->query($sql);
	$conn->close();
?>


<!DOCTYPE html>
<html>
	<head>
		<title>FORMA</title>
		<meta charset="utf-8">
		<meta name="author" content="Mihajlo Karadzic & Strahinja Banjanac" />
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
		<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css" rel="stylesheet"/>
		<link rel="stylesheet" href="css/style.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
	</head>
	<body>
	<div class="container-fluid">
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
				<h2>Uspesno ste uplatili tiket broj :<?php echo $tiketID." !"?></h2><br>
				<table class="table table-dark">
					<tr>
						<td style="color:blue;">UTAKMICA</td>
						<td style="color:blue;">Tip</td>
						<td style="color:blue;">Kvota</td>
					</tr>
					<?php  while($rowitem = mysqli_fetch_array($results)) {
						switch($rowitem['izab_ishod']){
							case '1':{
								$dobitak*=$rowitem['domaci_kv'];
								echo "<tr>";
								echo "<td>" . $rowitem['naziv'] . "</td>";
								echo "<td>1</td>";
								echo "<td>" . $rowitem['domaci_kv'] . "</td>";
								echo "</tr>";
							}break;
							case '2':{
								$dobitak*=$rowitem['gosti_kv'];
								echo "<tr>";
								echo "<td>" . $rowitem['naziv'] . "</td>";
								echo "<td>2</td>";
								echo "<td>" . $rowitem['gosti_kv'] . "</td>";
								echo "</tr>";
							}break;
							case 'X':{
								$dobitak*=$rowitem['nereseno_kv'];
								echo "<tr>";
								echo "<td>" . $rowitem['naziv'] . "</td>";
								echo "<td>X</td>";
								echo "<td>" . $rowitem['nereseno_kv'] . "</td>";
								echo "</tr>";
							}
						} 
					}
					?>
				</table>
				<?php
					echo "<h2>Moguci dobitak za ovaj tiket iznosi : ".$dobitak." dinara.";
				?>
			</div>
		</div>
	</div>
	</body>
</html> 