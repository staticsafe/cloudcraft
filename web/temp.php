<form action="'.$_SERVER['PHP_SELF'];.'" method="post">
  Allow Nether <br />
  <select name="allow-nether">
  <option value="true" '.$this->checkValueForSelect.'>true</option>
  <option value="false" '.$this->checkValueForSelect. '>false</option>
  </select>
  <br />Level Name<br />
  <input type="text" name="level-name" value="'.$this->getValueForTextField.'" />
  <br />Allow-Flight<br />
  <select name="allow-flight">
  <option value="true" '.$this->checkValueForSelect.'>true</option>
  <option value="false" '.$this->checkValueForSelect. '>false</option>
  </select> <br />
  <br />Enable White-list<br />
  <select name="white-list">
  <option value="true" '.$this->checkValueForSelect.'>true</option>
  <option value="false" '.$this->checkValueForSelect. '>false</option>
  </select> <br />
  <br />GameMode<br />
  <select name="gamemode">
  <option value="0" '.$this->checkValueForSelect.'>Survival</option>
  <option value="1" '.$this->checkValueForSelect. '>Creative</option>
  </select> <br />
  <br />PVP<br />
  <select name="pvp">
  <option value="true" '.$this->checkValueForSelect.'>true</option>
  <option value="false" '.$this->checkValueForSelect. '>false</option>
  </select> <br />
  <br />Online-Mode<br />
  <select name="online-mode">
  <option value="true" '.$this->checkValueForSelect.'>true</option>
  <option value="false" '.$this->checkValueForSelect. '>false</option>
  </select> <br />
  <br />Enable Monsters<br />
  <select name="spawn-monsters">
  <option value="true" '.$this->checkValueForSelect.'>true</option>
  <option value="false" '.$this->checkValueForSelect. '>false</option>
  </select> <br />
  <br />Enable Animals<br />
  <select name="spawn-animals">
  <option value="true" '.$this->checkValueForSelect.'>true</option>
  <option value="false" '.$this->checkValueForSelect. '>false</option>
  </select> <br />
  <br />Message of the Day<br />
  <input type="text" name="motd" value="'.$this->getValueForTextField.'" />
  <br />Difficulty<br />
  <select name="difficulty">
  <option value="0" '.$this->checkValueForSelect.'>Peaceful</option>
  <option value="1" '.$this->checkValueForSelect. '>Easy</option>
  <option value="2" '.$this->checkValueForSelect. '>Normal</option>
  <option value="3" '.$this->checkValueForSelect. '>Hard</option>
  <br />Player Slots<br />
  <input type="text" name="max-players" value="'.$this->getValueForTextField.'" />
  <br />Render Distance<br />
  <input type="text" name="view-distance" value="'.$this->getValueForTextField.'" />
</form>
<!--you should reorganize all of this :P-->