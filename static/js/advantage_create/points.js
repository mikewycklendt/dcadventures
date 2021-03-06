function points_check() {
	const check = "points_check";
	const title = "points-title";
	const base = 'points-base';
	const entry = "points-entry";

	entry_check(check, title, base, entry);
}

function points_spend() {
	const select = 'points_spend';
	const options = [{'val': 'ranks', 'div': 'points-ranks'},
					{'val': 'benefit', 'div': 'points-benefit'},
					{'val': 'check', 'div': 'points-check'},
					{'val': 'equip', 'div': 'points-equipment'},
					{'val': 'condition', 'div': 'points-condition'},
					{'val': 'initiative', 'div': 'points-initiative'},
					{'val': '20', 'div': 'points-twenty'},
					{'val': 'success', 'div': 'points-success'}]

	select_opacity(select, options)
}

function points_benefit_choice() {
	const select = 'points_benefit_choice';
	const options = [{'val': 'x', 'div': 'points-benefit-count'}]
	const benefit_count = document.getElementById('points_benefit_count');
	
	benefit_count.selectedIndex=0;

	select_opacity(select, options);
}

function points_ranks_trait_type() {
	const select = 'points_ranks_trait_type';
	const fill = 'points_ranks_trait';

	id_select(select, fill, trait_select, any_var_sub);
}

function points_ranks_trait() {
	const filter = select('points_ranks_trait_type');
	const fill = 'points_ranks_trait';
	const points_trait = 'points_trait'

	id_select(fill, fill, trait_filter, filter);
}

let points_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function points_submit() {

	const columns = points_grid.columns;
	const created = points_grid.titles;
	const font = points_grid.font;


	const benefit = select("points_benefit");
	const spend = select("points_spend");
	const condition_cost = select("points_condition_cost");
	const condition1 = select("points_condition1");
	const condition2 = select("points_condition2");
	const equipment_points = select("points_equipment_points");
	const equipment_vehicles = check("points_equipment_vehicles");
	const equipment_headquarters = check("points_equipment_headquarters");
	const initiative_cost = select("points_initiative_cost");
	const twenty = select("points_twenty");
	const check_bonus = select("points_check_bonus");
	const check_cost = select("points_check_cost");
	const check_turns = select("points_check_turns");
	const check_target = select("points_check_target");
	const check_all = check("points_check_all");
	const benefit_choice = select("points_benefit_choice");
	const benefit_count = select("points_benefit_count");
	const benefit_cost = select("points_benefit_cost");
	const benefit_turns = select("points_benefit_turns");
	const ranks_gained = select("points_ranks_gained");
	const ranks_max = select("points_ranks_max");
	const ranks_lasts = select("points_ranks_lasts");
	const ranks_trait_type = select("points_ranks_trait_type");
	const ranks_trait = select("points_ranks_trait");
	const success = select("points_success");
	
	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'points-err';
	const err_line = 'points-err-line';

	response = fetch('/advantage/points/create', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'columns': columns,
			'created': created,
			'font': font,
			'benefit': benefit,
			'spend': spend,
			'condition_cost': condition_cost,
			'condition1': condition1,
			'condition2': condition2,
			'equipment_points': equipment_points,
			'equipment_vehicles': equipment_vehicles,
			'equipment_headquarters': equipment_headquarters,
			'initiative_cost': initiative_cost,
			'twenty': twenty,
			'check_bonus': check_bonus,
			'check_cost': check_cost,
			'check_turns': check_turns,
			'check_target': check_target,
			'check_all': check_all,
			'benefit_choice': benefit_choice,
			'benefit_count': benefit_count,
			'benefit_cost': benefit_cost,
			'benefit_turns': benefit_turns,
			'ranks_gained': ranks_gained,
			'ranks_max': ranks_max,
			'ranks_lasts': ranks_lasts,
			'ranks_trait_type': ranks_trait_type,
			'ranks_trait': ranks_trait,
			'success': success
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			points_grid.columns.length = 0;
			points_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/advantage/' + table_id + '/delete/'
			create_table('advantage', jsonResponse, points_grid, route);
			clear_errors(err_line, errors)

			points_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}