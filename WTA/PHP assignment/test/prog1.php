<?php
date_default_timezone_set('Asia/Kolkata');

$timestamp = time();
$date_time = date("d-m-Y (D) H:i:s", $timestamp);
echo "Current date and local time on this server is $date_time \n" ;
$strings = array(
    'Welcome',
    'Hello',
    'Hi',
    'Sup',
    'Yolo',
);
echo "\n";
$key = array_rand($strings);
echo $strings[$key];

?>