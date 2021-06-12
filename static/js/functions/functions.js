function show_div(div_input, display='grid') {
	const div = document.getElementById(div_input);

	div.style.display = display;
	setTimeout(function(){div.style.opacity = '100%';}, 10)
	
}

function hide_div(div_input, time=3) {
	const div = document.getElementById(div_input);
	time = time * 100;
	time = time + 10;

	div.style.opacity = '0%';
	setTimeout(function(){div.style.display = 'none';}, time);
}


function show_modal(div_input) {
	const div = document.getElementById(div_input);
	const modal = 'modal';

	show_div(modal, 'flex');

	div.style.display = 'block';
	div.style.overflow = 'scroll';
	setTimeout(function(){div.style.opacity = '100%';}, 10)
	
}

function hide_modal(div_input) {
	const modal = 'modal';
	const div = document.getElementById(div_input);

	hide_div(modal, 2);

	div.style.opacity = '0%';
	div.style.overflow = 'hidden';
	setTimeout(function(){div.style.display = 'none';}, 200);
}
