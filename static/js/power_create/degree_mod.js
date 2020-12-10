function deg_mod_check() {
	const deg_mod_check = "deg_mod_check";
	const deg_mod_base_form = "deg-mod-base-form";
	const title = "deg-mod-title";
	const entry = "deg-mod-entry";

	check_title_small(deg_mod_check, title, deg_mod_base_form, entry);
}

function deg_mod_base() {
	const target_field = "deg_mod_target";
	const extra_field = 'deg_mod_extra';
	const entry = "deg-mod-entry";

	base_two(target_field, extra_field, entry);
}

function deg_mod_type() {
	let select = 'deg_mod_type';
	const options = [{'val': 'circ', 'div':'deg-mod-circ'},
					{'val': 'measure', 'div':  'deg-mod-measure'},
					{'val': 'condition', 'div': 'deg-mod-condition'},
					{'val': 'level', 'div': 'deg-mod-level'}];
	
	select_opacity(select, options);
}

function deg_mod_circ_trait_type() {
	const select = 'deg_mod_circ_trait_type'
	const fill = 'deg_mod_circ_trait'

	trait_select(select, fill)
}

function deg_mod_condition_type() {
	const field = 'deg_mod_condition_type';
	const options = [{'val': 'damage', 'div': 'deg-mod-condition-damage'},
					{'val': 'condition', 'div': 'deg-mod-conditions'}];

	select_opacity(field, options);
}

function deg_mod_damage_type() {
	const field = 'deg_mod_damage_type';	
	const math = 'deg-mod-damage-math';
	const value = 'deg-mod-damage-value';

	value_type(field, math, value);
}

function deg_mod_measure_type() {
	const field = 'deg_mod_measure_type';
	const math = 'deg-mod-measure-math';
	const value = 'deg-mod-measure-value';
	
	value_type(field, math, value)
}

function deg_mod_measure_trait_type() {
	const select = 'deg_mod_measure_trait_type';
	const fill = 'deg_mod_measure_trait';

	trait_select(select, fill);
}

deg_mod_enter = 0;

function deg_mod_submit() {

	
	const target = select("deg_mod_target");
	const extra = select("deg_mod_extra");
	const value = select("deg_value");
	const type = select("deg_mod_type");
	const circ_value = select("deg_mod_circ_value");
	const circ_turns = select("deg_mod_circ_turns");
	const circ_trait_type = select("deg_mod_circ_trait_type");
	const circ_trait = select("deg_mod_circ_trait");
	const measure_type = select("deg_mod_measure_type");
	const measure_val1 = select("deg_mod_measure_val1");
	const measure_math = select("deg_mod_measure_math");
	const measure_trait_type = select("deg_mod_measure_trait_type");
	const measure_trait = select("deg_mod_measure_trait");
	const measure_value = select("deg_mod_measure_value");
	const measure_rank = select("deg_mod_measure_rank");
	const deg_condition_type = select("deg_mod_condition_type");
	const condition_damage_value = select("deg_mod_condition_damage_value");
	const condition_damage = select("deg_mod_condition_damage");
	const condition1 = select("deg_mod_condition1");	
	const condition2 = select("deg_mod_condition2");
	const keyword = text("deg_mod_keyword");
	const nullify = select("deg_mod_nullify");
	const cumulative = check("deg_mod_cumulative");
	const linked = check("deg_mod_linked");
	const level = select('deg_mod_level');

};
