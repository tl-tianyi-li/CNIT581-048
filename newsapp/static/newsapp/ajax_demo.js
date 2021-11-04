$(document).ready(function(){
	url = "/static/newsapp/mydata.txt";
	$("#ajax-btn").click(loadWebAPI);

	$("#tmp-loading-img").hide();
});

function loadWebAPI(){
	// url = "https://www.swapi.tech/api/people/1"
	url = "https://api.openweathermap.org/data/2.5/weather?zip=47906&appid=9367be43d33c103efa4de2fb0ca675a6"
	// url = "https://google.com"
	// url = "https://api.chucknorris.io/jokes/random"
	$.get(url, function(data, status){

		let mydata = data;
		// console.log(data.icon_url);
		// $("#ajax-test").html("<img style=\'width: 20px\' src=\""+ mydata.icon_url +"\">+<p>"+mydata.value+"</p>");
		console.log(data);
	});
}

function loadText(){
	let myXHR = new XMLHttpRequest();

	// method -- which type of http request
	// url -- where to send the request
	// async -- optional, default = true
	url = "/static/newsapp/mydata.txt"
	myXHR.open('GET', url, true);

	myXHR.onload = function(){
		// check the status of the response.
		if(myXHR.status == 200){
			// 200: OK
			document.getElementById("ajax-test").innerHTML = myXHR.responseText;
		}
	}

	// myXHR.onreadystatechange = function(){
	// 	console.log(this.readyState);
	// 	// this function will be triggered every time the ready state changes
	// 	// 0: request is not initialized
	// 	// 1: server connection established
	// 	// 2: request received
	// 	// 3: processing request
	// 	// 4: request finished, response ready
	// 	if(this.readyState == 3){
	// 		$("#tmp-loading-img").show();
	// 	}
	// 	if(this.readyState == 4 && this.status == 200){
	// 		$("#tmp-loading-img").hide();
	// 		document.getElementById("ajax-test").innerHTML = "<span>using onreadystatechange:</span>"+myXHR.responseText;
	// 	}else if(this.status == 404){
	// 		document.getElementById("ajax-test").innerHTML = "Wrong file requested."
	// 	}
	// }
	// myXHR.onerror = function(msg){
	// 	console.log(msg);
	// 	document.getElementById("ajax-test").innerHTML = "Request error...";
	// }
	myXHR.send();

	
	// console.log(myXHR);
}