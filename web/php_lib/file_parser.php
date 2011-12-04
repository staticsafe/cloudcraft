<?php
	class file_parser {
		function make_generic_list($list,$name) {
			echo '<select name="remove_choice_'.$name.'">';
			for($i = 0; $i <= count($list); $i++) {
				if(!isset($list[$i])) {
					continue;
				}
				else {
					echo '<option value="'.$list[$i].'">'.$list[$i].'</option>';
				}
			}
			echo '</select><input type="submit" name="remove_'.$name.'" value="Go" />';
		}
		function make_whitelist_select() {
			$name = "whitelist";
			$this->make_generic_list($this->get_whitelist(),$name);
		}
		function make_op_select() {
			$name = "op";
			$this->make_generic_list($this->get_ops(),$name);
		}
		function make_banip_select() {
			$name = "banip";
			$this->make_generic_list($this->get_banips(),$name);
		}
		function make_banname_select() {
			$name = "banname";
			$this->make_generic_list($this->get_bannames(),$name);
		}
		function parse_whitelist() {
			$this->white_list = file_get_contents("../minecraft/white-list.txt");
			$this->white_list = explode("\n",$this->white_list);
			$this->white_list = array_unique($this->white_list);
			$this->white_list = preg_grep('/^\s*\z/', $this->white_list, PREG_GREP_INVERT);
		}
		function get_whitelist() {
			$this->parse_whitelist();
			return $this->white_list;
		}
		function parse_ops() {
			$this->ops_list = file_get_contents("../minecraft/ops.txt");
			$this->ops_list = explode("\n",$this->ops_list);
			$this->ops_list = array_unique($this->ops_list);
			$this->ops_list = preg_grep('/^\s*\z/', $this->ops_list, PREG_GREP_INVERT);
		}
		function get_ops() {
			$this->parse_ops();
			return $this->ops_list;
		}
		function parse_banips() {
			$this->banips_list = file_get_contents("../minecraft/banned-ips.txt");
			$this->banips_list = explode("\n",$this->banips_list);
			$this->banips_list = array_unique($this->banips_list);
			$this->banips_list = preg_grep('/^\s*\z/', $this->banips_list, PREG_GREP_INVERT);
		}
		function get_banips() {
			$this->parse_banips();
			return $this->banips_list;
		}
		function parse_bannames() {
			$this->bannames_list = file_get_contents("../minecraft/banned-players.txt");
			$this->bannames_list = explode("\n",$this->bannames_list);
			$this->bannames_list = array_unique($this->bannames_list);
			$this->bannames_list = preg_grep('/^\s*\z/', $this->bannames_list, PREG_GREP_INVERT);
		}
		function get_bannames() {
			$this->parse_bannames();
			return $this->bannames_list;
		}
		function get_all_lists() {
			$this->lists = array("white_list" => $this->get_whitelist(),"ops_list" => $this->get_ops(),"banips_list" => $this->get_banips(),"bannames_list" => $this->get_bannames());
			return $this->lists;
		}
	}
?>
