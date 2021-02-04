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
					{'val': 'measure', 'div': 'circ-measure'},
					{'val': 'level', 'div': 'circ-level'},
					{'val': 'speed', 'div': 'circ-speed'}]

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
	const fill = 'circ_measure_trait';

	id_select(select, fill, trait_select);
}

function circ_level_type() {
	const select = 'circ_level_type';
	const fill = 'circ_level';

	id_select(select, fill, level_select);
}

function circ_lasts() {
	const select = 'circ_lasts';
	const options = [{'val': 'turns', 'div': 'circ-turns'}, 
					{'val': 'time', 'div': 'circ-time'}, 
					{'val': 'rank', 'div': 'circ-time-rank'}]

	select_opacity(select, options);
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

	const keyword  = text('circ_keyword');

	const errors = 'circ-err';
	const err_line = 'circ-err-line';

	const circ_selects = 'circ-sml'

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

			const id = jsonResponse.id

			selects_add(id, keyword, circ_selects);

			circ_grid.columns.length = 0;
			circ_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/skill/' + table_id + '/delete/'
			create_table(jsonResponse, circ_grid, route, [circ_selects]);
			clear_errors(err_line, errors)

			circ_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}