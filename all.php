<?php
	include('conn.php');
    //print_r($_GET);

        $result = mysqli_query($conn, "SELECT * FROM `zaky_api`");
        $data = array();
        $i=0;
        while ($row = mysqli_fetch_array($result)) {
            $j=0;
            foreach($row as $field) {
                $data[$i][$j]=$field;
                $j++;
            }
            $i++;
        }
        
        if(mysqli_num_rows ($result) > 0)
			echo json_encode(array('flag'=>"1",'data_angkatan' => $data ), JSON_PRETTY_PRINT);
		else 
			echo json_encode(array('flag'=>"0",'data_angkatan' => $data ), JSON_PRETTY_PRINT);
        

?>