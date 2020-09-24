function home_button_placement() {
	const sidebargrid = document.getElementById("sidebargrid");
	const splashes = document.getElementsByClassName("splash");
	const splash = splashes[0];
	let sidebar_height = sidebargrid.scrollHeight;
	console.log(sidebar_height);
	splash.style.height = sidebar_height + "px";
	blank = document.getElementById("blank")
	buttons = document.getElementById("buttons")
	below - document.getElementById("belos")
	splash_60 = sidebar_height * .6;
	splash_15 = sidebar_height * .15;
	splash_25 = sidebar_height * .25;
	console.log(splash_60);
	blank.style.height = splash_60 + "px";
	buttons.style.height = splash_15 + "px";
	below.style.height = splash_25 + "px";
}

window.onload = home_button_placement;
window.onresize = home_button_placement;