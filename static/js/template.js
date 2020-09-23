function banner_size() {
	const banner = document.getElementById("banner");
	const banner_img = document.getElementById("banner-img");
	const banner_height = banner_img.scrollHeight;
	banner.style.height = banner_height + "px";
}