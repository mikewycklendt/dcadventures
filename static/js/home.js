function home_button_placement() {
	const sidebargrid = document.getElementById("sidebargrid");
	const splash = document.getElementsByClassName("splash")
	let sidebar_height = sidebargrid.scrollHeight;
	console.log(sidebar_height);
	splash.style.height = sidebar_height + "px";
}

window.onload = home_button_placement;
window.onresize = home_button_placement;