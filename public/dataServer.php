<?php 
	session_start();
	//Define připojení
	define('DB_HOST', 'localhost');
	define('DB_USER', 'root',true);
	define('DB_PASS', '',true);
	define('DB_NAME', 'hackathon',true);
	define('DB_CHARSET', 'utf8_mb4_czech_ci');
	define('DB_COLLATE', '');

	//Tvorba připojení
	$conn = new mysqli(DB_HOST,DB_USER,DB_PASS,DB_NAME);

	if ($conn->connect_error) {
	    die("Chyba spojení s db: " . $conn->connect_error);
	} 
	//Vem data
	$sqlSelect = "SELECT * FROM tabulka ORDER BY id DESC LIMIT 2";
	$sqlResult = $conn->query($sqlSelect);
	//Když existuje výsledek 
	if ($sqlResult->num_rows > 0) {
	    //Output
	   	while ($output = $sqlResult->fetch_assoc()) {
	   	 	 $sqlData[]=$output;
	   	 }
	} 
	else {
	    echo "Nenašel záznamy";
	}
	

	$conn->close();
 ?>