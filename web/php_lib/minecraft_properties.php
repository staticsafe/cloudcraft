<?php
	class minecraft_properties {
		public function form_options() {
			$this->file = file_get_contents("../minecraft/server.properties");
			echo "<textarea name='property_text'>".$this->file."</textarea><input type='submit' name='submit_properties' value='Submit' />";
		}
	}
?>
