function banner_size() {
	const banner_grid = document.getElementById("bannergrid");
	const banner_img = document.getElementById("the-banner");
	const banner_width = banner_img.scrollWidth
	const banner_height = banner_img.scrollHeight
	banner_grid.style.width = banner_width + "px";
}