<div class="sub">
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
	<?php
		echo 'Server Status: ';
		if(file_exists("../minecraft/server.log.lck")) {
			echo '<div class="server_status" style="background-color:green"></div>';
		}
		else {
			echo '<div class="server_status" style="background-color:red"></div>';
		}
		?>
</div><!-- sub -->
