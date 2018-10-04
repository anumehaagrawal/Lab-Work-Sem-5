<?php
	$handle = fopen("counter.txt", "r");
	if(!$handle){
		echo "Could not open file";
	}
	else{
		$counter = (int )fread($handle,20);
		fclose($handle);
		$counter++;
		echo" Number of visitors". $counter ."
		";
		$handle= fopen("counter.txt", "w");
		fwrite($handle, $counter);
		fclose($handle);

	}
	$serverName = gethostname();
	echo "Server name " . $serverName ."
	";
?>