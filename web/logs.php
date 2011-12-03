<?php $page = "logs"; ?>
<!DOCTYPE xhtml>
<html>
	<head>
		<title>HillTing Minecraft Manager</title>
		<link rel="stylesheet" type="text/css" href="./style/style.css" />
		<?php
			include("./php_lib/parse.php");
			$properties_file = new parse();
			if(isset($_POST['submit_properties'])) {
				$fop = fopen("../minecraft/server.properties","w");
				fwrite($fop,$_POST['property_text']);
				fclose($fop);
			}
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
		<?php include("./includes/header.php"); ?>
		</div><!-- navigation -->
		<div class="container">
			<div class="main">
				<div class="entry">
					<div class="title">Logs</div>
				
				</div><!-- entry -->
			</div><!-- main -->
			<?php include("./includes/log_parser.php"); ?>
		</div><!-- container -->
	</body>
</html>


