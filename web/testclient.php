<!DOCTYPE xhtml>
<html>
  <head>
    <title>Socket Testing</title>
  </head>
  <body>
  <h1>Test</h1>
    <?php
	$socket = socket_create (AF_INET, SOCK_STREAM, SOL_TCP );
	$address = "127.0.0.1";
	$port = 1337;
	$info = "stuff\n";
	$len = 7;
	socket_connect($socket, $address, $port);
	socket_send($socket, $info, strlen($info), MSG_DONTROUTE); 
	$buf = socket_read($socket, 1024, PHP_NORMAL_READ);
	echo $buf;
	//socket_shutdown($socket);
	socket_close($socket);
    ?>
  </body>
</html>