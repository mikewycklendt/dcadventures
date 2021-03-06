function circ_check() {
	const check = "circ_check";
	const title = "circ-title";
	const base = 'circ-base';
	const entry = "circ-entry";

	check_title(check, title, base, entry);
}

function circ_base() {
	const field = 'circ_extra';
	const field2 = 'circ_target';
	const entry = "circ-entry";

	base_two(field, field2, entry);
}

function circ_type() {
	const field = 'circ_type';
	const options = [{'val': 'range', 'div': 'circ-range'},
					{'val': 'check', 'div': 'circ-check'}] 
	const entry = 'circ-entry';

	select_maxheight_entry(field, options, entry);
}

function circ_null_type() {
	const select = 'circ_null_type';
	const options = [{'val': 'condition', 'div': 'circ-null-condition'},
					{'val': 'descriptor', 'div': 'circ-null-descriptor'},
					{'val': 'trait', 'div': 'circ-null-trait'}]

	select_opacity(select, options);
}

function circ_check_trait_type() {
	const select = 'circ_check_trait_type';
	const fill = 'circ_check_trait';
	
	id_select(select, fill, trait_select);
}

function circ_null_trait_type() {
	const select = 'circ_null_trait_type';
	const fill = 'circ_null_trait';

	id_select(select, fill, trait_select);
}

let circ_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function circ_submit() {

	const columns = circ_grid.columns;
	const created = circ_grid.titles;
	const font = circ_grid.font;

	const target = select("circ_target");
	const extra_id = select("circ_extra");
	const mod = select("circ_mod");
	const rounds = select("circ_rounds");
	const description = text("circ_des");
	const type = select("circ_type");
	const range = select("circ_range");
	const check_who = select("circ_check_who");
	const check_trait_type = select("circ_check_trait_type");
	const check_trait = select("circ_check_trait");
	const null_type = select("circ_null_type");
	const null_condition = select("circ_null_condition");
	const null_descriptor = select("circ_null_descriptor");
	const null_trait_type = select("circ_null_trait_type");
	const null_trait = select("circ_null_trait")

	const power_id = document.getElementById('power_id').value;

	const errors = 'circ-err';
	const err_line = 'circ-err-line';

	response = fetch('/power/circ/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'target': target,
			'mod': mod,
			'rounds': rounds,
			'description': description,
			'circ_type': type,
			'circ_range': range,
			'check_who': check_who,
			'check_trait_type': check_trait_type,
			'check_trait': check_trait,
			'null_type': null_type,
			'null_condition': null_condition,
			'null_descriptor': null_descriptor,
			'null_trait_type': null_trait_type,
			'null_trait': null_trait,
			'columns': columns,
			'created': created,
			'font': font
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			
			circ_grid.columns.length = 0;
			circ_grid.columns = jsonResponse.rows

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table(jsonResponse, circ_grid, route);
			clear_errors(err_line, errors)

			circ_grid.titles = true;
		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}