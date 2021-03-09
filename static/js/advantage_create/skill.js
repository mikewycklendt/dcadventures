function skill_check() {
	const check = "skill_check";
	const title = "skill-title";
	const base = 'skill-base';
	const entry = "skill-entry";

	entry_check(check, title, base, entry);
}

function skill_replaced_trait_type() {
	const select = 'skill_replaced_trait_type';
	const fill = 'skill_replaced_trait';

	id_select(select, fill, trait_select, variable_sub);
}

function skill_replaced_trait() {
	const select = 'skill_replaced_trait_type';
	const fill = 'skill_replaced_trait';

	id_select(fill, fill, trait_filter, select);
}

function skill_trait_type() {
	const select = 'skill_trait_type';
	const fill = 'skill_trait';

	id_select(select, fill, trait_select, variable_sub);
}

function skill_trait() {
	const select = 'skill_trait_type';
	const fill = 'skill_trait';

	id_select(fill, fill, trait_filter, select);
}

let skill_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function skill_submit() {

	const columns = skill_grid.columns;
	const created = skill_grid.titles;
	const font = skill_grid.font;


	const benefit = select("skill_benefit")
	const trait_type = select("skill_trait_type")
	const trait = select("skill_trait")
	const replaced_trait_type = select("skill_replaced_trait_type")
	const replaced_trait = select("skill_replaced_trait")
	const multiple = select("skill_multiple")
	
	///const advantage_id = document.getElementById('advantage_id').value;
	const advantage_id = select("create_advantage_select");
	
	const errors = 'skill-err';
	const err_line = 'skill-err-line';

	response = fetch('/advantage/skill/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'benefit': benefit,
			'trait_type': trait_type,
			'trait': trait,
			'replaced_trait_type': replaced_trait_type,
			'replaced_trait': replaced_trait,
			'multiple': multiple
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			multiple_field('skill-multiple');

			skill_grid.columns.length = 0;
			skill_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table('advantage', jsonResponse, skill_grid, route);
			clear_errors(err_line, errors)

			skill_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}