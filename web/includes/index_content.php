<div class="container">
			<div class="main">
				<div class="entry">
					<div class="title">Core Functions</div>
					<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
						<input type="submit" name="start_server" value="Start Server" />
						<input type="submit" name="stop_server" value="Stop Server" />
						<input type="submit" name="update_server" value="Update Server" />
					</form>
				</div><!-- entry -->
			</div><!-- main -->
			<?php
				include("./includes/log_parser.php");
			?>
		</div><!-- container -->
