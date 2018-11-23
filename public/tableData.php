<?php  require 'dataServer.php'; ?>
<?php 
	if (isset($_SESSION["id"])) {
		if ($_SESSION["id"] < $sqlData[0]["id"]) {
			$_SESSION["id"] = $sqlData[0]["id"];
			echo '<script type="text/javascript">reLoad();</script>';
		}		
	}
	else{
		$_SESSION["id"] = $sqlData[0]["id"];
	}
 ?>
<table class="table"> 
	<tr>
		<th class="bg-primary">Tracking number</th>
		<th class="bg-info">GPS coordinates</th>
		<th class="bg-light text-dark">Image</th>
		<th class="bg-danger">Difficulty</th>
		<th class="bg-light text-dark">State</th>
	</tr>
	
	<!-- loop na data -->
	<?php foreach ($sqlData as $key => $value): ?>
	
		<tr>
			<td class="bg-primary"><?php echo $value["id"] ?></td>
			<td class="bg-info" ><?php echo $value["lat"].$value["lng"]; ?></td>

			<div class="hidden" id='lat<?php echo $value["id"] ?>'><?php echo $value["lat"]; ?></div>
			<div class="hidden" id='lng<?php echo $value["id"] ?>'><?php echo $value["lng"]; ?></div>
			<div class="hidden" id='max'><?php echo $_SESSION["id"];?></div>

			<td class="bg-light"><img class="image"src='<?php echo $value["img"] ?>'></td>
			<td class="bg-danger"><?php echo $value["dif"] ?></td>	

			<?php $stateColor = ($value["st"]=='cleaned'?"badge-success":($value["st"]=='pending'?" badge-warning":" badge-danger"));?>				
			<td class='text-white <?php echo $stateColor;?>'>

				<?php echo $value["st"]; ?>
			</td>
		</tr>

	<?php endforeach ?>

</table>