<?php
	session_start();
	$_SESSION['time'] = time();
	include("./php_lib/verify.php");
	$verify = new verify();
?>

