<?php
	class submit {
		function index() {
			include("./php_lib/communicate.php");
			$comm = new communicate();
			if(isset($_POST['start_server'])) {
				$comm->send("start");
			}
			elseif(isset($_POST['stop_server'])) {
				$comm->send("stop");
			}
			elseif(isset($_POST['update_server'])) {
				$comm->send("update");
			}
		}
		function permissions($all_lists) {
			if(isset($_POST['add_whitelist'])) {
				$this->add_to_file("../minecraft/white-list.txt","whitelist");
			}
			elseif(isset($_POST['remove_whitelist'])) {
				$this->remove_from_file("../minecraft/white-list.txt","whitelist",$all_lists["white_list"]);
			}
			elseif(isset($_POST['add_op'])) {
				$this->add_to_file("../minecraft/ops.txt","op");
			}
			elseif(isset($_POST['remove_op'])) {
				$this->remove_from_file("../minecraft/ops.txt","op",$all_lists["ops_list"]);
			}
			elseif(isset($_POST['add_banip'])) {
				$this->add_to_file("../minecraft/banned-ips.txt","banip",$all_lists["banips_list"]);
			}
			elseif(isset($_POST['remove_banip'])) {
				$this->remove_from_file("../minecraft/banned-ips.txt","banip",$all_lists["banips_list"]);
			}
			elseif(isset($_POST['add_banname'])) {
				$this->add_to_file("../minecraft/banned-players.txt","banname",$all_lists["bannames_list"]);
			}
			elseif(isset($_POST['remove_banname'])) {
				$this->remove_from_file("../minecraft/banned-players.txt","banname",$all_lists["bannames_list"]);
			}
		}
		function settings($properties) {
			if(isset($_POST['submit_properties'])) {
				$props = file_get_contents("../minecraft/server.properties");
				$this->properties = explode("\n",$props);
				$this->submit_settings($properties);
			}
		}
		function logs() {
			
		}
		function remove_from_file($file_name,$option,$list) {
				$list = preg_grep('/^\s*\z/', $list, PREG_GREP_INVERT);
				for($i =0; $i < count($list); $i++) {
					if(!isset($list[$i]) || $list[$i] == "") {
						continue;
					}
					elseif($list[$i] == $_POST['remove_choice_'.$option]) {
						unset($list[$i]);
					}
				}
				$imploded_list = implode("\n",$list);
				$fop = fopen($file_name,"w");
				fwrite($fop,$imploded_list."\n");
				fclose($fop);
		}
		function add_to_file($file_name,$option) {
			$fop = fopen($file_name,"a");
			fwrite($fop,$_POST[$option]."\n");
		}
		function submit_settings($properties) {
			$this->all_settings = array();
			for($i = 0; $i < count($this->properties); $i++) {
				if(substr($this->properties[$i],0,1) == "#") {
					$this->all_settings[$i] = $this->properties[$i];
				}
				else {
					$epos = strpos($this->properties[$i],"=");
					if(!isset($_POST[substr($this->properties[$i],0,$epos)])) {
						$this->all_settings[$i] = $this->properties[$i];
					}
					else {
						$this->all_settings[$i] = substr($this->properties[$i],0,$epos +1).$_POST[substr($this->properties[$i],0,$epos)];
					}
				}
			}
			$fop = fopen("../minecraft/server.properties","w");
			$this->all_settings = implode("\n",$this->all_settings);
			fwrite($fop,$this->all_settings);
		}
	}
?>
