function opposed_check() {
	const check = "opposed_check";
	const title = "opposed-title";
	const base = 'opposed-base';
	const entry = "opposed-entry";

	entry_check(check, title, base, entry);
}

function opposed_base() {
	const field = 'opposed_extra';
	const entry = "opposed-entry";

	base(field, entry);
	descriptor_base(field);
}

function opposed_attached() {
	const select = 'opposed_attached';
	const div = 'opposed-variable-title';
	const opposed_div = 'opposed-opponent-title'
	const options = [{'val': ['before_var', 'after_var'], 'div': 'opposed-variable'},
					{'val': ['before_opponent', 'after_opponent'], 'div': 'opposed-opponent'}]
	const values = [{'val': 'before_var', 'text': 'Before Variable Check:'}, 
					{'val': 'after_opponent', 'text': 'After Opponent Check:'}, 
					{'val': 'after_var', 'text': 'After Variable Check:'}, 
					{'val': 'before_opponent', 'text': 'Before Opponent Check:'}];
	const entry = "opposed-entry";
	const attached = [{'val': ['before', 'before_var', 'before_opponent'], 'div': 'opposed-before'},
					{'val': ['after', 'after_var', 'after_opponent'], 'div': 'opposed-after'},
					{'val': ['primary'], 'div': 'opposed-primary'}]
	const fields = ['opposed_before', 'opposed_after', 'opposed_frequency']

	reset_all(fields);
	select_opacity_shared(select, attached);
	select_maxheight_shared(select, options, entry);
	div_text(select, div, values);
	div_text(select, opposed_div, values);
}

function opposed_trait_type() {
	const select = 'opposed_trait_type'
	const fill = 'opposed_trait'

	id_select(select, fill, trait_select);
}

function opposed_trait() {
	const filter = select('opposed_trait_type');
	const fill = 'opposed_trait';

	id_select(fill, fill, trait_filter, filter);
}

function opposed_opponent_trait_type() {
	const select = 'opposed_opponent_trait_type'
	const fill = 'opposed_opponent_trait'

	id_select(select, fill, trait_select, variable_sub)
}

function opposed_opponent_trait() {
	const filter = select('opposed_opponent_trait_type');
	const fill = 'opposed_opponent_trait';

	id_select(fill, fill, trait_filter, filter);
}

function opposed_recurring() {
	const check = 'opposed_recurring';
	const div = 'opposed-recurring';
	const entry = 'opposed-entry';

	check_drop(check, div, entry);
}


function opposed_degree_check() {
	const check = "opposed_degree_check"
	const div = 'opposed-degree';
	const entry = 'opposed-entry';

	check_drop(check, div, entry);
}

function opposed_circ_check(){
	const check = "opposed_circ_check"
	const div = 'opposed-circ';
	const entry = 'opposed-entry';

	check_drop(check, div, entry);
}

function opposed_dc_check() {
	const check = "opposed_dc_check"
	const div = 'opposed-dc';
	const entry = 'opposed-entry';

	check_drop(check, div, entry);
}

function opposed_time_check() {
	const check = "opposed_time_check"
	const div = 'opposed-time';
	const entry = 'opposed-entry';

	check_drop(check, div, entry);
}

function opposed_opponent_check() {
	const select = 'opposed_opponent_check';
	const options = [{'val': '5', 'div': 'opposed-attack-opp'}];
	const entry = 'opposed-entry';
	const fields = ['opposed_attack_opp'];

	reset_all(fields);
	select_maxheight_entry(select, options, entry);
}

function opposed_player_check() {
	const select = 'opposed_player_check'
	const options = [{'val': '5', 'div': 'opposed-attack-player'}];
	const entry = 'opposed-entry';
	const fields = ['opposed_attack_player']

	reset_all(fields);
	select_maxheight_entry(select, options, entry);
}

let opposed_grid = {'titles': false,
					'columns': [],
					'font': 80,
					'mod': []}

function opposed_submit() {

	const columns = opposed_grid.columns;
	const created = opposed_grid.titles;
	const font = opposed_grid.font;

	const extra_id = select("opposed_extra");
	const attached = select("opposed_attached");
	const frequency = select("opposed_frequency");
	const trait_type = select("opposed_trait_type");
	const trait = select("opposed_trait");
	const mod = select("opposed_mod");
	const opponent_trait_type = select("opposed_opponent_trait_type");
	const opponent_trait = select("opposed_opponent_trait");
	const opponent_mod = select("opposed_opponent_mod");
	const player_secret = check("opposed_secret_player");
	const player_check = select("opposed_player_check");
	const opponent_check = select("opposed_opponent_check");
	const secret = check("opposed_secret");
	const recurring = check("opposed_recurring");
	const multiple = select("opposed_multiple");
	const recurring_value = text("opposed_recurring_value");
	const description = text("opposed_description");
	const keyword = text("opposed_keyword");
	const degree = select("opposed_degree");
	const circ = select("opposed_circ");
	const dc = select("opposed_dc");
	const time = select("opposed_time");
	const degree_check = check("opposed_degree_check");
	const circ_check = check("opposed_circ_check");
	const dc_check = check("opposed_dc_check");
	const time_check = check("opposed_time_check");
	const degree_value = select("opposed_degree_value");
	const dc_type = select("opposed_dc_type");
	const dc_player = select("opposed_dc_player");
	const circ_value = select("opposed_circ_value");
	const time_type = select("opposed_time_type");
	const recurring_type = select("opposed_recurring_type");
	const recurring_degree_type = select("opposed_recurring_degree_type");
	const recurring_fail = check("opposed_recurring_fail");
	const variable = select("opposed_variable");
	const title = text("opposed_title");
	const opposed = select("opposed_opposed");
	const opponent = select("opposed_opponent");
	const variable_type = select("opposed_variable_type");
	const before = select("opposed_before");
	const after = select("opposed_after");
	const power_check = select("check");
	const power_action = select("action");
	const attack_player = select("opposed_attack_player");
	const attack_opp = select("opposed_attack_opp");

	///const power_id = document.getElementById('power_id').value;
	const power_id = select("create_power_select");
	
	const errors = 'opposed-err';
	const err_line = 'opposed-err-line';

	const opposed_selects = 'opposed-sml';
	const selects_type = 'opposed-title-sml';

	response = fetch('/power/opposed/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': power_id,
			'extra_id': extra_id,
			'columns': columns,
			'created': created,
			'font': font,
			'attached': attached,
			'frequency': frequency,
			'trait_type': trait_type,
			'trait': trait,
			'mod': mod,
			'opponent_trait_type': opponent_trait_type,
			'opponent_trait': opponent_trait,
			'opponent_mod': opponent_mod,
			'player_secret': player_secret,
			'player_check': player_check,
			'opponent_check': opponent_check,
			'secret': secret,
			'recurring': recurring,
			'multiple': multiple,
			'recurring_value': recurring_value,
			'description': description,
			'keyword': keyword,
			'degree': degree,
			'circ': circ,
			'dc': dc,
			'time': time,
			'degree_check': degree_check,
			'circ_check': circ_check,
			'dc_check': dc_check,
			'time_check': time_check,
			'degree_value': degree_value,
			'dc_type': dc_type,
			'dc_player': dc_player,
			'circ_value': circ_value,
			'time_type': time_type,
			'recurring_type': recurring_type,
			'recurring_degree_type': recurring_degree_type,
			'recurring_fail': recurring_fail,
			'variable': variable,
			'title': title,
			'opponent': opponent,
			'opposed': opposed,
			'variable_type': variable_type,
			'before': before,
			'after': after,
			'power_check': power_check,
			'power_action': power_action,
			'attack_player': attack_player,
			'attack_opp': attack_opp
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			extra_effect_check(jsonResponse);
			
			const id = jsonResponse.id;

			multiple_field('opposed-multiple');
			
			selects_add(id, keyword, opposed_selects);
			
			const title_id = jsonResponse.title_id;
			const add_title = jsonResponse.add_title;

			if (add_title == true) {
				selects_add(title_id, title, selects_type);
			}

			opposed_grid.columns.length = 0;
			opposed_grid.columns = jsonResponse.rows;

			const table_id = jsonResponse.table_id;
			const route = '/power/' + table_id + '/delete/'
			create_table('power', jsonResponse, opposed_grid, route, [opposed_selects], title_id, [selects_type]);
			clear_errors(err_line, errors)

			opposed_grid.titles = true;

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})
}