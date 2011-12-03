<?php $page = "permissions"; ?>
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
			include("./php_lib/write.php");
			$write = new write();
			if(isset($_POST['add_whitelist'])) {
				$write->to("../minecraft/white-list.txt",$_POST['whitelist']);
			}
			elseif(isset($_POST['add_op'])) {
				$write->to("../minecraft/ops.txt",$_POST['op']);
			}
			elseif(isset($_POST['add_banip'])) {
				$write->to("../minecraft/banned-ips.txt",$_POST['banip']);
			}
			elseif(isset($_POST['add_banname'])) {
				$write->to("../minecraft/banned-players.txt",$_POST['banname']);
			}
		?>
		<?php include("./includes/header.php"); ?>
		</div><!-- navigation -->
		<div class="container">
			<div class="main">
				<div class="entry">
					<div class="title">Permissions</div>
						<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
							Add name to whitelist: <input type="text" name="whitelist" /><input type="submit" name="add_whitelist" value="Go" /><br />
							Add op: <input type="text" name="op" /><input type="submit" name="add_op" value="Go" /><br />
							Add ip to ban list: <input type="text" name="banip" /><input type="submit" name="add_banip" value="Go" /><br />
							Add name to ban list: <input type="text" name="banname" /><input type="submit" name="add_banname" value="Go" /><br />
						</form>
				</div><!-- entry -->
			</div><!-- main -->
			<?php include("./includes/log_parser.php"); ?>
		</div><!-- container -->
	</body>
</html>
