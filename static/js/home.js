function home_button_placement() {
	const sidebargrid = document.getElementById("sidebargrid");
	const splashes = document.getElementsByClassName("splash");
	const splash = splashes[0];
	let sidebar_height = sidebargrid.scrollHeight;
	console.log(sidebar_height);
	splash.style.height = sidebar_height + "px";
}

window.onload = home_button_placement;
window.onresize = home_button_placement;