<?php
	include('conn.php');

	if (!empty($_POST['nrpku']) && !empty($_POST['namaku']) && !empty($_POST['daeasal'])  && !empty($_POST['jurusanku'])) {

		$nrpku = $_POST['nrpku'];
		$namaku = $_POST['namaku'];
		$daeasal = $_POST['daeasal'];
		$jurusanku = $_POST['jurusanku'];
        $nrplama = $_POST['nrplama'];
		$queryResult = $conn->query("UPDATE `zaky-api` SET nrpku = '$nrpku', namaku = '$namaku', daeasal = '$daeasal', jurusanku= '$jurusanku' WHERE nrpku ='$nrplama'");
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