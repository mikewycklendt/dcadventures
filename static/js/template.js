function banner_size() {
	const banner_grid = document.getElementById("bannergrid");
	const banner_img = document.getElementById("the-banner");
	const banner_width = banner_img.scrollWidth
	const banner_height = banner_img.scrollHeight
	banner_grid.style.width = banner_width + "px";
}

const splashes = document.getElementsByClassName("splash");

function home_button_placement() {
	const sidebargrid = document.getElementById("sidebargrid");	
	const splash = splashes[0];
	splash_height = splash.scrollHeight;
	console.log(splash_height)
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
	banner_size;
	if (splashes != null) {
		home_button_placement;
	}	
}

window.onresize = resize_item; 
window.onload = resize_item;
