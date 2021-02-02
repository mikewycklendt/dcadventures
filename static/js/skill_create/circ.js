function circ_check() {
	const check = "circ_check";
	const title = "circ-title";
	const base = 'circ-base';
	const entry = "circ-entry";

	entry_check(check, title, base, entry);
}

function circ_effect() {
	const select = 'circ_effect';
	const options = [{'val': 'condition', 'div': 'circ-condition'},
					{'val': 'measure', 'div': 'circ-measure'}]

	select_opacity(select, options);
}

function circ_condition_type() {
	const select = 'circ_condition_type';
	const options = [{'val': 'condition', 'div': 'circ-condition-condition'},
					{'val': 'damage', 'div': 'circ-condition-damage'}]

	select_opacity(select, options);
}

function circ_measure_effect() {
	const select = 'circ_measure_effect';
	const options = [{'val': 'rank', 'div': 'circ-measure-rank'},
					{'val': 'unit', 'div': 'circ-measure-unit'},
					{'val': 'skill', 'div': 'circ-measure-skill'}]

	select_opacity(select, options);
}

function circ_unit_type() {
	const select = 'circ_unit_type';
	const fill = 'circ_unit';

	id_select(select, fill, unit_select);
}

function circ_measure_trait_type() {
	const select = 'circ_measure_trait_type';
	const fill = 'circ_measure';

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

	const skill_id = document.getElementById('skill_id').value;

	const errors = 'circ-err';
	const err_line = 'circ-err-line';

	response = fetch('/skill/circ/create', {
		method: 'POST',
		body: JSON.stringify({
			'skill_id': skill_id,
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
			circ_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/skill/' + table_id + '/delete/'
			create_table(jsonResponse, circ_grid, route);
			clear_errors(err_line, errors)

			circ_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}