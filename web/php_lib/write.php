<?php
	class write {
		function to($path,$value) {
			$fop = fopen($path,"a");
			fwrite($fop,$value."\n");
			fclose($fop);
		}
	}
?>
