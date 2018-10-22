<?php
	include('conn.php');

	if (!empty($_POST['nomer']) && !empty($_POST['namaku']) && !empty($_POST['daeasal'])  && !empty($_POST['jurusanku'])) {

		$nomer = $_POST['nomer'];
		$namaku = $_POST['namaku'];
		$daeasal = $_POST['daeasal'];
		$jurusanku = $_POST['jurusanku'];
        $nmr_lama = $_POST['nmr_lama'];
		$queryResult = $conn->query("UPDATE `zaky-api` SET nomer = '$nomer', namaku = '$namaku', daeasal = '$daeasal', jurusanku= '$jurusanku' WHERE nomer ='$nmr_lama'");
        if($queryResult==true)
    		echo json_encode(array( 'flag'=>"1" ), JSON_PRETTY_PRINT);
    	else
    	    echo json_encode(array( 'flag'=>"0" ), JSON_PRETTY_PRINT);
	}

	else{
		echo json_encode(array( 'flag'=>"0" ), JSON_PRETTY_PRINT);
		// echo "data tidak ditemukan";
	}
?>