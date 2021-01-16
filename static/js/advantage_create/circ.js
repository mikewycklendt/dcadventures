function circ_check() {
	const check = "circ_check";
	const title = "circ-title";
	const base = 'circ-base';
	const entry = "circ-entry";

	check_title(check, title, base, entry);
}

function circ_base() {
	const field = 'circ_target';
	const entry = "circ-entry";

	base(field, entry);
}

function circ_type() {
	const field = 'circ_type';
	const options = [{'val': 'range', 'div': 'circ-range'},
					{'val': 'check', 'div': 'circ-check'},
					{'val': 'conflict', 'div': 'circ-conflict'}]
	const entry = 'circ-entry';

	select_maxheight_entry(field, options, entry);
}

function circ_null_type() {
	const select = 'circ_null_type';
	const options = [{'val': 'condition', 'div': 'circ-null-condition'},
					{'val': 'trait', 'div': 'circ-null-trait'},
					{'val': 'override', 'div': 'circ-null-override'}]

	select_opacity(select, options);
}

function circ_check_trait_type() {
	const select = 'circ_check_trait_type';
	const fill = 'circ_check_trait';
	
	trait_select(select, fill);
}

function circ_null_trait_type() {
	const select = 'circ_null_trait_type';
	const fill = 'circ_null_trait';

	trait_select(select, fill);
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
	const benefit = select("circ_benefit");
	const mod = select("circ_mod");
	const rounds = select("circ_rounds");
	const circumstance = text("circ_des");
	const circ_type = select("circ_type");
	const circ_range = select("circ_range");
	const conflict = select("circ_conflict");
	const check_who = select("circ_check_who");
	const check_trait_type = select("circ_check_trait_type");
	const check_trait = select("circ_check_trait");
	const null_type = select("circ_null_type");
	const null_condition = select("circ_null_condition");
	const null_trait_type = select("circ_null_trait_type");
	const null_trait = select("circ_null_trait");
	const null_override_trait_type = select("circ_null_override_trait_type");
	const null_override_trait = select("circ_null_override_trait");
	

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'circ-err';
	const err_line = 'circ-err-line';

	response = fetch('/advantage/circ/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'target': target,
			'benefit': benefit,
			'mod': mod,
			'rounds': rounds,
			'circumstance': circumstance,
			'circ_type': circ_type,
			'circ_range': circ_range,
			'conflict': conflict,
			'check_who': check_who,
			'check_trait_type': check_trait_type,
			'check_trait': check_trait,
			'null_type': null_type,
			'null_condition': null_condition,
			'null_trait_type': null_trait_type,
			'null_trait': null_trait,
			'null_override_trait_type': null_override_trait_type,
			'null_override_trait': null_override_trait			
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