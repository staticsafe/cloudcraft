<?php
	$links = array(array("home","./"),array("permissions","./permissions.php"),array("settings","./settings.php"),array("logs","./logs.php"));
	echo '<div class="navigation"><div class="links">';
	for($i = 0;$i < count($links);$i++) {
		echo '<a href="'.$links[$i][1].'" ';
		if($links[$i][0] == str_replace(".php","",basename($_SERVER["PHP_SELF"]))) {
			echo 'class="active" ';
		}
		elseif($links[$i][0] == "home" && str_replace(".php","",basename($_SERVER["PHP_SELF"])) == "index") {
			echo 'class="active"';
		}
		echo '>'.$links[$i][0].'</a>';
	}
	echo '</div></div>';
?>
