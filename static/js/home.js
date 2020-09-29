function home_button_placement() {
	const sidebargrid = document.getElementById("sidebargrid");
	console.log('sidebargrid: ' + sidebargrid.scrollHeight)
	const homeimg = document.getElementById("home-img");
	console.log('home-img: ' + homeimg.scrollHeight)
	const splashes = document.getElementsByClassName("splash");
	const splash = splashes[0];
	let sidebar_height = sidebargrid.scrollHeight;
	console.log(sidebar_height);
	splash.style.height = sidebar_height + "px";
	blank = document.getElementById("blank");
	buttons = document.getElementById("buttons");
	below - document.getElementById("belos");
	splash_60 = sidebar_height * .6;
	splash_15 = sidebar_height * .15;
	splash_25 = sidebar_height * .25;
	console.log(splash_60);
	blank.style.height = splash_60 + "px";
	buttons.style.height = splash_15 + "px";
	below.style.height = splash_25 + "px";
}

function resize_item() {
	window.onresize = home_button_placement;
}



