		<div class="container">
			<div class="main">
				<div class="entry">
					<div class="title">Whitelist</div>
						<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
							Add name to whitelist <br /><input type="text" name="whitelist" /><input type="submit" name="add_whitelist" value="Go" /><br /><br />
							Remove name from whitelist<br />
							<?php
								$parse->make_whitelist_select();
							?>
						</form>
				</div><!-- entry -->
				<div class="entry">
					<div class="title">
						Ops
					</div>
					<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
						Add op <br /><input type="text" name="op" /><input type="submit" name="add_op" value="Go" /><br /><br />
						Remove op<br />
						<?php
							$parse->make_op_select();
						?>
					</form>
				</div><!-- entry -->
				<div class="entry">
					<div class="title">
						Bans
					</div>
						<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
							Add ip to ban list<br /> <input type="text" name="banip" /><input type="submit" name="add_banip" value="Go" /><br /><br />
							Remove banned ip<br />
							<?php
								$parse->make_banip_select();
							?>
						</form><br />
						<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
							Add name to ban list<br /><input type="text" name="banname" /><input type="submit" name="add_banname" value="Go" /><br /><br />
							Remove banned name<br />
							<?php
								$parse->make_banname_select();
							?>
						</form>
				</div><!-- entry -->
			</div><!-- main -->
			<?php include("./includes/log_parser.php"); ?>
		</div><!-- container -->
