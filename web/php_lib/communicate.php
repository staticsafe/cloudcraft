<?php
	class communicate {
		function start() {
			$this->connect();
			$cmd = "start";
			socket_send($this->socket, $cmd, strlen($cmd), MSG_DONTROUTE);
			//$buf = socket_read($this->socket, 1024, PHP_NORMAL_READ);
			//echo $buf;
			$this->disconnect();
		}
		function stop() {
			$this->connect();
			$cmd = "stop";
			socket_send($this->socket,$cmd,strlen($cmd),MSG_DONTROUTE);
			//$buf = socket_read($this->socket, 1024, PHP_NORMAL_READ);
			//echo $buf;
			$this->disconnect();
		}
		function connect() {
			$this->socket = socket_create (AF_INET, SOCK_STREAM, SOL_TCP );
			$this->address = "127.0.0.1";
			$this->port = 1337;
			socket_connect($this->socket, $this->address, $this->port);
		}
		function disconnect() {
			socket_close($this->socket);
		}
	}
?>
