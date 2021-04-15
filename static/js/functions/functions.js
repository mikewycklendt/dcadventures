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
