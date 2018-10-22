<?php
	include('conn.php');
    
    if (isset($_POST['nomer'])) {
        $nrpku = $_POST['nomer'];
        
        if($result = mysqli_query($conn, "DELETE FROM `zaky-api` where nomer=".$nomer)) 
            echo json_encode(array('flag'=>"1"), JSON_PRETTY_PRINT);    
        else
            echo json_encode(array('flag'=>"0"), JSON_PRETTY_PRINT);
        
    }

?>