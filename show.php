<?php
	include('conn.php');
    //print_r($_GET);
    if (isset($_GET['nmr'])) {
        $user_id = $_GET['nmr'];
        
        $result = mysqli_query($conn, "SELECT * FROM `zaky_api` where nmr=".$user_id);
        // print_r($result);
        $data = array();
        
        while($row = $result->fetch_assoc()) {
            $data[] = $row;    
        }
        
        if(mysqli_num_rows ($result) > 0)
			echo json_encode(array('flag'=>"1",'data_angkatan' => $data ), JSON_PRETTY_PRINT);
		else 
			echo json_encode(array('flag'=>"0",'data_angkatan' => $data ), JSON_PRETTY_PRINT);
        
    }

?>