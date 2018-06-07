<?php
    $a = "\x0";	
    preg_match("/^.*,($a)$/m", "1342,2234234", $temp);
	print $a===$temp[1]; 
?>
