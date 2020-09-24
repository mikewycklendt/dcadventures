function banner_size() {
	const banner_grid = document.getElementById("bannergrid");
	const banner_img = document.getElementById("the-banner");
	const banner_width = banner_img.scrollWidth
	const banner_height = banner_img.scrollHeight
	banner_grid.style.width = banner_width + "px";
	const sidebargrid = document.getElementById("sidebargrid");
	const sidebar_height = sidebargrid.scrollHeight
	console.log(sidebar_height)
}

window.onresize = banner_size;