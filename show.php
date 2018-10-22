<?php
	include('conn.php');
    //print_r($_GET);
    if (isset($_GET['nomer'])) {
        $nrpku = $_GET['nomer'];
        
        $result = mysqli_query($conn, "SELECT * FROM `zaky-api` where nomer=".$nomer);
        // print_r($result);
        $data = array();
        
        while($row = $result->fetch_assoc()) {
            $data[] = $row;    
        }
        
        if(mysqli_num_rows ($result) > 0)
			echo json_encode(array('flag'=>"1",'data_mhs' => $data ), JSON_PRETTY_PRINT);
		else 
			echo json_encode(array('flag'=>"0",'data_mhs' => $data ), JSON_PRETTY_PRINT);
        
    }

?>