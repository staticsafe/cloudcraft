<!DOCTYPE xhtml>
<html>
	<head>
		<title>HillTing Minecraft Manager</title>
		<link rel="stylesheet" type="text/css" href="./style/style.css" />
	</head>
	<body>
		<?php
			if(str_replace(".php","",basename($_SERVER['PHP_SELF'])) != "index" && str_replace(".php","",basename($_SERVER['PHP_SELF'])) != "logs") {
				include("./php_lib/file_parser.php");
				$parse = new file_parser();
			}
			if(isset($_POST)) {
				include("./php_lib/submit.php");
				$submit = new submit();
				if(str_replace(".php","",basename($_SERVER['PHP_SELF'])) == "permissions") {
					global $paramater;
					$parameter = $parse->get_all_lists();
				}
				else {
					$parameter = "";
				}
				$submit->{str_replace(".php","",basename($_SERVER['PHP_SELF']))}($parameter);
			}
		?>
		<?php
			include("./includes/header.php"); 
			include("./includes/".str_replace(".php","",basename($_SERVER['PHP_SELF']))."_content.php");
		?>
	</body>
</html>
