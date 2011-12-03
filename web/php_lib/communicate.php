<?php
	class communicate {
		function send($cmd) {
			$this->connect();
			socket_send($this->socket, $cmd, strlen($cmd), MSG_DONTROUTE);
			$reply = socket_read($this->socket, 1024, PHP_NORMAL_READ);
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
