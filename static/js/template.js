function banner_size() {
	const banner_grid = document.getElementById("bannergrid");
	const banner_img = document.getElementById("the-banner");
	const banner_width = banner_img.scrollWidth
	const banner_height = banner_img.scrollHeight
	const banner_height_less = banner_height - 5;
	banner_grid.style.width = banner_width + "px";
	banner_grid.style.height = banner_height_less + "px";
}