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
		function settings() {
			if(isset($_POST['submit_properties'])) {
				
			}
		}
		function logs() {
			
		}
		function remove_from_file($file_name,$option,$list) {
				$list = preg_grep('/^\s*\z/', $list, PREG_GREP_INVERT);
				for($i =0; $i < count($list); $i++) {
					if($list[$i] == $_POST['remove_choice_'.$option]) {
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
	}
?>
