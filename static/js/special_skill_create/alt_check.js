function alt_check_entry() {
	const check = document.getElementById("alt_check_check");
	const title = "alt-check-title";


	const dc_set_field = document.getElementById('dc_set');
	let dc_set = dc_set_field.options[dc_set_field.selectedIndex].value;

	
	const dc_table = document.getElementById('dc-levels');

	if (check.checked == true || dc_set == 'table') {
		dc_table.style.display = 'grid';
		setTimeout(function(){dc_table.style.opacity = '100%'}, 10);
	} else if (check.checked == false && dc_set != 'table'){
		dc_table.style.opacity  = '0%';
		setTimeout(function(){dc_table.style.display = 'none';}, 400);
	}
}

function check_type() {
	const check_field = document.getElementById('check');
	let check_value = check_field.options[check_field.selectedIndex].value;

	alt_check = document.getElementById('alt-check');

	if (check_value != 1) {
		alt_check.style.display = 'grid';
	}
}