
var markers = [];
var map;

var late = 49.214889;
var long = 16.561493;
 
function initMap() {
	var maxNum = Number($("#max").text());
	console.log(maxNum);
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 20,
    center: {lat: late, lng: long}
    
  });
	for (var i = maxNum; i > 0; i--) {

	console.log(parseFloat($("#lat"+i).text()));
	console.log(parseFloat($("#lng"+i).text()));

	markers.push(new google.maps.Marker({
		    position: {lat: parseFloat($("#lat"+i).text()), lng: parseFloat($("#lng"+i).text())},
		    animation: google.maps.Animation.DROP,
		    map: map
	      }));
		
	}

}
function centerOnReload() {
	var late = parseFloat($("#lat"));
	var long = parseFloat($("#lng"));
	var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 20,
    center: {lat: late, lng: long}
    
  });
}
function reLoad(){
	console.log('reload');
	//centerOnReload();
	
	initMap();
	$( ".table_view" ).load('tableData.php');
	setTimeout(reLoad, 10000);
}
$(window).on('load',function() {
	$( ".table_view" ).load('tableData.php');
    
    setTimeout(reLoad, 5000);
});
