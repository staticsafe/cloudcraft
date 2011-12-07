<?php
	class verify {
		function __construct() {
			if(!isset($_SESSION['logged_in'])) {
				if(file_exists("../pswd.rawr") != true) {
					die($this->createUser());
				}
				else {
					die($this->loginForm());
				}
			}
			else {
				if(time() - $_SESSION['time'] > 600) {
					die($this->timeout());
				}
				else {
					die(include("./includes/indexs.php"));
				}
			}
		}
		function timeout() {
			return '<span color="red">Session timed out. Please log in again.</span><br /><br />'.$this->loginForm();
		}
		function loginForm() {
			return '
				<form method="post" action="'.$_SERVER['PHP_SELF'].'">
					Username<br /><input type="text" name="username" /><br /><br />
					Password<br /><input type="password" name="password" /><br /><br />
					<input type="submit" name="submit_login" />
				</form>
			'.$this->if_submitted();
		}
		function if_submitted() {
			if(isset($_POST['submit_login'])) {
				$password_file = file_get_contents("../pswd.rawr");
				$password_file = explode("\n",$password_file);
				$encrypted_password = trim($password_file[1]);
				$timestamp_salt = trim($password_file[2]);
				$set_username = trim($password_file[0]);
				$user_username = $_POST['username'];
				$user_password = $_POST['password'];
				$user_password = $_POST['password'].$timestamp_salt;
				$user_password_e = sha1($user_password);
				if($user_password_e == $encrypted_password) {
					if($user_username == $set_username) {
						$_SESSION['logged_in'] = "true";
						header("Location: ".$_SERVER['PHP_SELF']);
					}
					else {
						echo '<span style="color:red">Username is incorrect. Please try again</span><br /><br />';
					}
				}
				else {
					echo '<span style="color:red">Wrong password entered. Please try again</span><br /><br />';
				}
			}
			if(isset($_POST['submit_new_user'])) {
				$time = time();
				$password = $_POST['password'];
				$confirm = $_POST['password2'];
				$username = $_POST['username'];
				if($password == $confirm) {
					$fop = fopen("../pswd.rawr","w");
					$pass_salt = $password.$time;
					$password_e = sha1($pass_salt);
					$str = $username."\n".$password_e."\n".$time;
					fwrite($fop,$str);
				}
				else {
					echo '<span style="color:red">Passwords did not match. Please try again</span><br /><br />'; 
				}
			}
		}
		function createUser() {
			return $this->if_submitted().'
				<form method="post" action="'.$_SERVER['PHP_SELF'].'">
					Username<br /><input type="text" name="username" /><br /><br />
					Password<br /><input type="password" name="password" /><br /><br />
					Confirm<br /><input type="password" name="password2" /><br /><br />
					<input type="submit" name="submit_new_user" value="Make" />
				</form>
			';
		}
	}
?>
