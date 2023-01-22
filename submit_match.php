<?php
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "kladionica";
	$conn = new mysqli($servername, $username, $password,$dbname);
	$rezultat=htmlspecialchars($_POST['rez']);
	$mecID=htmlspecialchars($_POST['mecevi']);
	$tiketID=htmlspecialchars($_POST['brTiketa']);
	$sql = "INSERT INTO stavka_tiketa(izab_ishod,mecevi_id_mec,tiket_id_tiket) VALUES('$rezultat','$mecID','$tiketID')";
	$conn->query($sql);
	$conn->close();
	
	header('Location: index.php');
?>
