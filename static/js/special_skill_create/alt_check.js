function alt_check_entry() {
	const check = "alt_check_check";
	const entry = "alt-check-entry";
	const title = "alt-check-title";

	console.log('click')

	const dc_set_field = document.getElementById('dc_set');
	let dc_set = dc_set_field.options[dc_set_field.selectedIndex].value;

	
	const dc_table = document.getElementById('dc-levels');

	if (check.checked == true || dc_set == 'table') {
		dc_table.style.display = 'grid';
		setTimeout(function(){dc_table.style.opacity = '100%'}, 10);
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