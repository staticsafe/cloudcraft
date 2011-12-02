<!DOCTYPE xhtml>
<html>
	<head>
		<title>HillTing Minecraft Manager</title>
		<link rel="stylesheet" type="text/css" href="./style/style.css" />
		<?php
			include("./php_lib/communicate.php");
		?>
		<script type="text/javascript">
			timer = self.setInterval("blink()",1100);
			color = true;
			function blink() {
				if(color) {
					document.getElementById('blink').style.color="444444";
					color = false;
				} else if(!color) {
					document.getElementById('blink').style.color="7fff0";
					color = true;
				}
			}
		</script>
	</head>
	<body>
		<?php
			$comm = new communicate();
			if(isset($_POST['start_server'])) {
				$comm->send("start");
			}
			elseif(isset($_POST['stop_server'])) {
				$comm->send("stop");
			}
		?>
		<div class="navigation">
			<div class="links">
				<a class="active" href="">home</a>
				<a href="">permissions</a>
				<a href="">settings</a>
				<a href="">logs</a>
			</div><!-- links -->
		</div><!-- navigation -->
		<div class="container">
			<div class="main">
				<div class="entry">
					<div class="title">Core Functions</div>
					<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
						<input type="submit" name="start_server" value="Start Server" />
						<input type="submit" name="stop_server" value="Stop Server" />
					</form>
				</div><!-- entry -->
			</div><!-- main -->
			<div class="sub">
				<div class="prompt">
					<textarea id="output" readonly="readonly">Welcome to Hillting 0.0.0</textarea>
				</div><!-- prompt -->
				<div id="input">
						<textarea id="user">Input Here</textarea>
					</div>
			</div><!-- sub -->
		</div><!-- container -->
	</body>
</html>
