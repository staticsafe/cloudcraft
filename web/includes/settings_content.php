<div class="container">
	<div class="main">
		<div class="entry">
			<div class="title">Settings</div>
				<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
					<?php
						$mcp->form_options();
					?>
				</form>
			</div><!-- entry -->
	</div><!-- main -->
	<?php include("./includes/log_parser.php"); ?>
</div><!-- container -->
