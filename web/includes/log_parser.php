<div class="sub">
	<div class="prompt">
		<textarea id="output" readonly="readonly">Welcome to Hillting 0.0.0
		<?php
			$file = file_get_contents("../minecraft/server.log");
			$file = explode("\n",$file);
			for($i = 0; $i < count($file); $i++) {
				echo $file[$i]."\n\n\n\n";
			}
		?></textarea>
		
	</div><!-- prompt -->
</div><!-- sub -->
