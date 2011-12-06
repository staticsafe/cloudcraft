<?php
	class minecraft_properties {
		function form_options() {
			$this->setVals();
			
			//$this->file = file_get_contents("../minecraft/server.properties");
			//echo "<textarea name='property_text'>".$this->file."</textarea><input type='submit' name='submit_properties' value='Submit' />";
			echo '
			<form action="'.$_SERVER['PHP_SELF'].'" method="post">
  Allow Nether <br />
  <select name="allow-nether">
  <option value="true" '.$this->checkValueForSelect("allow-nether","true").'>true</option>
  <option value="false" '.$this->checkValueForSelect("allow-nether","false"). '>false</option>
  </select>
  <br />
  <br />Level Name<br />
  <input type="text" name="level-name" value="'.$this->getValueForTextField("level-name").'" /><br />
  <br />Allow-Flight<br />
  <select name="allow-flight">
  <option value="true" '.$this->checkValueForSelect("allow-flight","true").'>true</option>
  <option value="false" '.$this->checkValueForSelect("allow-flight","false"). '>false</option>
  </select>
  <br />
  <br />Enable White-list<br />
  <select name="white-list">
  <option value="true" '.$this->checkValueForSelect("white-list","true").'>true</option>
  <option value="false" '.$this->checkValueForSelect("white-list","false"). '>false</option>
  </select>
  <br />
  <br />GameMode<br />
  <select name="gamemode">
  <option value="0" '.$this->checkValueForSelect("gamemode","0").'>Survival</option>
  <option value="1" '.$this->checkValueForSelect("gamemode","1"). '>Creative</option>
  </select>
  <br />
  <br />PVP<br />
  <select name="pvp">
  <option value="true" '.$this->checkValueForSelect("pvp","true").'>true</option>
  <option value="false" '.$this->checkValueForSelect("pvp","false"). '>false</option>
  </select>
  <br />
  <br />Online-Mode<br />
  <select name="online-mode">
  <option value="true" '.$this->checkValueForSelect("online-mode","true").'>true</option>
  <option value="false" '.$this->checkValueForSelect("online-mode","false"). '>false</option>
  </select>
  <br />
  <br />Enable Monsters<br />
  <select name="spawn-monsters">
  <option value="true" '.$this->checkValueForSelect("spawn-monsters","true").'>true</option>
  <option value="false" '.$this->checkValueForSelect("spawn-monsters","false"). '>false</option>
  </select>
  <br />
  <br />Enable Animals<br />
  <select name="spawn-animals">
  <option value="true" '.$this->checkValueForSelect("spawn-animals","true").'>true</option>
  <option value="false" '.$this->checkValueForSelect("spawn-animals","false"). '>false</option>
  </select>
  <br />
  <br />Message of the Day<br />
  <input type="text" name="motd" value="'.$this->getValueForTextField("motd").'" />
  <br />
  <br />Difficulty<br />
  <select name="difficulty">
  <option value="0" '.$this->checkValueForSelect("difficulty","0").'>Peaceful (no monsters)</option>
  <option value="1" '.$this->checkValueForSelect("difficulty","1"). '>Easy</option>
  <option value="2" '.$this->checkValueForSelect("difficulty","2"). '>Normal</option>
  <option value="3" '.$this->checkValueForSelect("difficulty","3"). '>Hard</option>
  </select>
  <br />
  <br />Player Slots<br />
  <select name="max-players">
  ';
		for($i =1; $i <= 64; $i++) {
			echo '
				<option value="'.$i.'" '.$this->checkValueForSelect("max-players",$i).'>'.$i.'</option>
			';
			}
			echo '</select>
				<br />
				<br />Render Distance<br />
				<select name="view-distance">
			';
			for($i=3; $i <= 15; $i++) {
				echo '
				<option value="'.$i.'" '.$this->checkValueForSelect("view-distance",$i).'>'.$i.'</option>
				';
			}
	echo '
</select><br />
<br />
<input type="submit" name="submit_properties" value="submit" />
</form>';
		}
		function setVals() {
			$this->properties = file_get_contents("../minecraft/server.properties");
			$this->properties = explode("\n",$this->properties);
		}
		function getValue($name) {
			for($i = 0; $i < count($this->properties); $i++) {
				$epos = strpos($this->properties[$i],"=");
				if(substr($this->properties[$i],0,$epos) == $name ) {
					return substr($this->properties[$i],$epos + 1);	
				}
			}
		}
		function getValueForTextField($name) {
			for($i=0; $i < count($this->properties); $i++) {
				$epos = strpos($this->properties[$i],"=");
				if(substr($this->properties[$i],0,$epos) == $name) {
					$sub = substr($this->properties[$i],$epos +1);
					return $sub;
				}
			}
		}
		function checkValueForSelect($name,$value) {
			for($i = 0; $i < count($this->properties); $i++) {
				if(substr($this->properties[$i],0,1) == "#") {
					continue;
				}
				else {
					$epos = strpos($this->properties[$i],"=");
					if(trim(substr($this->properties[$i],0,$epos)) == $name) {
						if(trim(substr($this->properties[$i],$epos +1)) == $value) {
							return 'selected="selected"';
						}
						break;
					}
				}
			}
		}
	}
?>
