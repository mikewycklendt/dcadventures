function banner_size() {
	const banner_grid = document.getElementById("bannergrid");
	const banner_img = document.getElementById("the-banner");
	const banner_width = banner_img.scrollWidth
	const banner_height = banner_img.scrollHeight
	banner_grid.style.width = banner_width + "px";
	
	const splashes = document.getElementsByClassName("splash");

	function home_resize () {
		if (splashes != null) {	
			const sidebargrid = document.getElementById("sidebargrid");
			console.log('sidebargrid: ' + sidebargrid.scrollHeight)
			const homeimg = document.getElementById("home-img");
			console.log('home-img: ' + homeimg.scrollHeight)
			const splashes = document.getElementsByClassName("splash");
			const splash = splashes[0];
			let sidebar_height = sidebargrid.scrollHeight;
			let homeimg_height = homeimg.scrollHeight
			splash.style.height = homeimg_height + "px";
			blank = document.getElementById("blank");
			buttons = document.getElementById("buttons");
			below - document.getElementById("below");
			splash_60 = homeimg_height * .70;
			splash_15 = homeimg_height * .15;
			splash_25 = homeimg_height * .15;
			console.log(splash_60);
			blank.style.height = splash_60 + "px";
			buttons.style.height = splash_15 + "px";
			below.style.height = splash_25 + "px";
		}
		homeimg.onresize - home_resize;
	}

	home_resize();
}

window.onresize = banner_size; 
