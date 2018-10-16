<?php
	include('conn.php');
    
    if (isset($_POST['nrpku'])) {
        $nrpku = $_POST['nrpku'];
        
        if($result = mysqli_query($conn, "DELETE FROM `zaky-api` where nrpku=".$nrpku)) 
            echo json_encode(array('flag'=>"1"), JSON_PRETTY_PRINT);    
        else
            echo json_encode(array('flag'=>"0"), JSON_PRETTY_PRINT);
        
    }

?>