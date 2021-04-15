function show_div(div_input, display='grid') {
	const div = document.getElementById(div_input);

	div.style.display = display;
	div.style.opacity = '100%';
}

function hide_div(div_input, time=300) {
	const div = document.getElementById(div_input);
	
	div.style.opacity = '0%';
	setTimeout(function(){div.style.display = 'none';}, time);
}
