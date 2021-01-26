function descriptor_check() {
	const check = "descriptor_check";
	const title = "descriptor-title";
	const base = 'descriptor-base';
	const entry = "descriptor-entry";

	entry_check(check, title, base, entry);
}


function get_medium_subtypes() {

	const title = document.getElementById('descriptor-medium-subtype-title')

	const medium_type_field  = document.getElementById('descriptor_medium_type');
	const medium_type = medium_type_field.options[medium_type_field.selectedIndex].value;

	const update = document.getElementById('descriptor_medium_subtype');
	const update_medium  = document.getElementById('descriptor_medium');

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)
	update_medium.style.backgroundColor = 'lightblue';
	setTimeout(function(){update_medium.style.backgroundColor = "white"}, 200)

	response = fetch('/equipment/medium/subtype/select', {
		method: 'POST',
		body: JSON.stringify({
			'medium_type': medium_type
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			update.innerText = null;
			update_medium.innerText = null;

			title.innerText = jsonResponse.title;
			title.style.opacity = '100%';

			const options = jsonResponse.options;
			let option;

			for (option of options)  {
				let o = document.createElement("option")
				o.value = option.id;
				o.text = option.name;
				update.add(o);
			}

			const options_medium = jsonResponse.options_medium
			let option_medium;

			for (option_medium of options_medium) {
				o = document.createElement('option')
				o.value = option_medium.id;
				o.text = option_medium.name;
				update_medium.add(o);
			}

		} else {
			console.log(jsonResponse.options);
		}
	})	
}

function get_medium() {

	const medium_subtype_field = document.getElementById('descriptor_medium_subtype');
	const medium_subtype = medium_subtype_field.options[medium_subtype_field.selectedIndex].value;
	
	const update  = document.getElementById('descriptor_medium');

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

	response = fetch('/equipment/medium/select', {
		method: 'POST',
		body: JSON.stringify({
			'medium_subtype': medium_subtype
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const options = jsonResponse.options;
			let option;

			update.innerText = null;

			for (option of options)  {
				let o = document.createElement("option")
				o.value = option.id;
				o.text = option.name;
				update.add(o);
			}

		} else {
			console.log(jsonResponse.options);
		}
	})	
}

function get_descriptors(origin, source, medium_type, medium_subtype, medium, update) {

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

	response = fetch('/power/descriptor/select', {
		method: 'POST',
		body: JSON.stringify({
			'origin': origin,
			'source': source,
			'medium_type': medium_type,
			'medium_subtype': medium_subtype,
			'medium': medium
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const select = document.getElementById('descriptor_field');
			let old_options = select.options;
			
			for (i = old_options.length - 1; i > -1; i--) {
				if (old_options[i].value == 'new' || old_options[i].value == 'all' || old_options[i].value == '') {
					console.log('keep');
				} else {
					old_options[i].remove();
				}
			}

			let options = jsonResponse.options;
			let option;

			for (option of options)  {
				console.log(option)
				let o = document.createElement("option")
				o.value = option.id;
				o.text = option.name;
				update.add(o);
			}

		} else {
			console.log(jsonResponse.options);
		}
	})	
}

function field_show(value, title, field) {
	if (value != '' && value != 'all') {
		title.style.opacity = '100%';
		field.style.opacity = '100%';
	} else {
		title.style.opacity = '0%';
		field.style.opacity = '0%';
	}
}
function descriptor() {
	const origin  = select('descriptor_origin');
	const source  = select('descriptor_source');
	const medium_type  = select('descriptor_medium_type');
	const medium_subtype = select('descriptor_medium_subtype');
	const medium  = select('descriptor_medium');

	const descriptor_field  = document.getElementById('descriptor_field');
	const descriptor = descriptor_field.options[descriptor_field.selectedIndex].value;

	const sub_title_row1 = document.getElementById('descriptor-medium-subtype-title')
	const med_title_row1 = document.getElementById('descriptor-medium-title');
	const des_title_row1 = document.getElementById('descriptor-field-title');
	const sub_row1 = document.getElementById('descriptor-medium-subtype');
	const med_row1 = document.getElementById('descriptor-medium');
	const des_field = document.getElementById('descriptor-field');

	field_show(medium_type, sub_title_row1, sub_row1)
	field_show(medium_subtype, med_title_row1, med_row1)
	
	if ((origin != 'all' && origin != '') || (source != 'all' && source != '') || (medium_type != 'all' && medium_type != '') || 
		(medium_subtype != 'all' && medium_subtype != '') || (medium != 'all' && medium != '')) {
		des_field.style.opacity = '100%';
	} else {
		des_field.style.opacity = '0%';
	}

	get_descriptors(origin, source, medium_type, medium_subtype, medium, descriptor_field)
}


let descriptor_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function descriptor_submit() {

	const columns = descriptor_grid.columns;
	const created = descriptor_grid.titles;
	const font = descriptor_grid.font;

	const weapon_id = document.getElementById('weapon_id').value;
	const descriptor = select("descriptor_field");

	const errors = 'descriptor-err';
	const err_line = 'descriptor-err-line';

	response = fetch('/weapon/descriptor/create', {
		method: 'POST',
		body: JSON.stringify({
			'weapon_id': weapon_id,
			'columns': columns,
			'created': created,
			'font': font,
			'descriptor': descriptor
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			descriptor_grid.columns.length = 0;
			descriptor_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/weapon/' + table_id + '/delete/'
			create_table(jsonResponse, descriptor_grid, route);
			clear_errors(err_line, errors)

			descriptor_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}