<div class="sub">
	<?php
	if(file_exists("../minecraft/server.log.lck")) {
		echo '<div class="server_status" style="color:green">Server: UP</div>';
	}
	else {
		echo '<div class="server_status" style="color:red">Server: DOWN</div>';
	}
	?>
	<div class="prompt">
		<textarea id="output" readonly="readonly">
		<?php
			$file = file_get_contents("../minecraft/server.log");
			$file = explode("\n",$file);
			for($i = 0; $i < count($file); $i++) {
				echo $file[$i]."\n";
			}
		?></textarea>
	</div><!-- prompt -->
</div><!-- sub -->
