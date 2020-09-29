function dc_set() {
	const dc_set_field = document.getElementById('dc_set');
	let dc_set = dc_set_field.options[dc_set_field.selectedIndex].value;

	const dc_table = document.getElementById('dc-levels');

	if (dc_set == 'table') {
		dc_table.style.display = 'grid';
	}

}