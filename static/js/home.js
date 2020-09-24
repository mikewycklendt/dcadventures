function home_button_placement() {
	const sidebargrid = document.getElementById("sidebargrid");
	const blank = document.getElementById("blank");
	let sidebar_height = sidebargrid.scrollHeight;
	console.log(sidebar_height);
	let sidebar_60 = sidebar_height * .6;
	blank.style.height = sidebar_60 + "px";
};

window.onload = home_button_placement;
window.onresize = home_button_placement;