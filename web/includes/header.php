<?php
	$links = array(array("home","./"),array("permissions","./permissions.php"),array("settings","./settings.php"),array("logs","./logs.php"));
	echo '<div class="navigation"><div class="links">';
	for($i = 0;$i < count($links);$i++) {
		echo '<a href="'.$links[$i][1].'" ';
		if($links[$i][0] == $page) {
			echo 'class="active" ';
		}
		echo '>'.$links[$i][0].'</a>';
	}
	echo '</div></div>';
?>
