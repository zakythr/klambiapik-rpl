<?php
	include('conn.php');

	if (!empty($_POST['nomer']) && !empty($_POST['namaku']) && !empty($_POST['daeasal']) && !empty($_POST['jurusanku'])){

		$nomer = $_POST['nomer'];
		$namaku = $_POST['namaku'];
		$daeasal = $_POST['daeasal'];
		$jurusanku = $_POST['jurusanku'];
        
        
		$queryResult = $conn->query("INSERT INTO `zaky-api` (nomer, namaku, daeasal, jurusanku) VALUES ('$nomer', '$namaku', '$daeasal', '$jurusanku')");

		echo json_encode(array( 'flag'=>"1" ), JSON_PRETTY_PRINT);
	}

	else{
		echo json_encode(array( 'flag'=>"0" ), JSON_PRETTY_PRINT);
		// echo "data tidak ditemukan";
	}
?>