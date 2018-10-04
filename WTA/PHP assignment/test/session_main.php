<?php 
session_start();
?>
<!DOCTYPE html>
<html>
<body>

<?php
echo "Original session id";
echo session_id();
$_SESSION["session_id"] = mt_rand(1,100);
echo "<br> Session variables are set.";
?>

<br>

<?php
echo "Current session id is: ". $_SESSION["session_id"];
?>

<form id="fm" method="POST">
<button type="submit" onclick="return true;" name="btn">Delete Session</button>
</form>	

<?php
	if(isset($_POST['btn'])){
	echo "
	 	<script type=\"text/javascript\">
			 var e = document.getElementById('fm');
			 e.action='session.php';
			 e.submit();
		</script>	 
		";
	}
?>

</body>
</html>