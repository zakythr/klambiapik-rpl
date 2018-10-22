<?php
	include('conn.php');

	if (!empty($_POST['nmr']) && !empty($_POST['sangar'])){

		$user_id = $_POST['nmr'];
		$sangar = $_POST['sangar'];
        
        
		$queryResult = $conn->query("INSERT INTO `api_andhika` (nmr, sangar) VALUES ('$user_id', '$sangar')");

		echo json_encode(array( 'flag'=>"1" ), JSON_PRETTY_PRINT);
	}

	else{
		echo json_encode(array( 'flag'=>"0" ), JSON_PRETTY_PRINT);
		// echo "data tidak ditemukan";
	}
?>