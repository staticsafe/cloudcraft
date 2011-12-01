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
	//socket_send($socket, $info, $len, MSG_DONTROUTE); 
	socket_write($socket, $info, $len);
	socket_shutdown($socket);
	socket_close($socket);
    ?>
  </body>
</html>