function descriptor_check() {
	const check = "descriptor_check";
	const title = "descriptor-title";
	const base = 'descriptor-base';
	const entry = "descriptor-entry";

	entry_check(check, title, base, entry);
}


function get_medium_subtypes() {
	
	const select = 'descriptor_medium_type';
	const fill = {'subtypes': 'descriptor_medium_subtype',
					'mediums': 'descriptor_medium'};
	const titles = {'title': 'descriptor-medium-subtype-title'}

	id_select(select, fill, medium_subtype_select, false, false, titles, true);
}

function get_medium() {
	
	const select = 'descriptor_medium_subtype';
	const fill = 'descriptor_medium';

	id_select(select, fill, medium_select);
}

function descriptor() {
	const origin  = 'descriptor_origin'
	const source  = 'descriptor_source';
	const medium_type  = 'descriptor_medium_type';
	const medium_subtype = 'descriptor_medium_subtype';
	const medium  = 'descriptor_medium';
	const descriptor_field = 'descriptor_fIeld';

	const sub_title_row1 = 'descriptor-medium-subtype-title';
	const med_title_row1 = 'descriptor-medium-title';
	const sub_row1 = 'descriptor-medium-subtype';
	const med_row1 = 'descriptor-medium';
	const des_field = 'descriptor-field';

	field_show(medium_type, sub_title_row1, sub_row1)
	field_show(medium_subtype, med_title_row1, med_row1)

	show_descriptor_field(origin, source, medium_subtype, medium, des_field);	

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

	const equip_id = document.getElementById('equip_id').value;
	const effect = select("descriptor_effect");
	const feature = select("descriptor_feature");
	const descriptor = select("descriptor_field");

	const errors = 'descriptor-err';
	const err_line = 'descriptor-err-line';

	response = fetch('/equipment/descriptor/create', {
		method: 'POST',
		body: JSON.stringify({
			'equip_id': equip_id,
			'columns': columns,
			'created': created,
			'font': font,
			'effect': effect,
			'feature': feature,
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
			const route = '/equipment/' + table_id + '/delete/'
			create_table(jsonResponse, descriptor_grid, route);
			clear_errors(err_line, errors)

			descriptor_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}