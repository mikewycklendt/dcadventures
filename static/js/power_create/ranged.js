function ranged_check() {
	const check = "ranged_check";
	const title = "ranged-title";
	const base = 'ranged-base';
	const entry = "ranged-entry";

	check_title(check, title, base, entry);
}

function ranged_base() {
	const field = 'ranged_extra';
	const entry = "ranged-entry";

	base(field, entry);
}

function ranged_check_trait_type() {
	const select = 'ranged_check_trait_type'
	const fill = 'ranged_check_trait'

	trait_select(select, fill)
}

function ranged_distance_mod_trait_type() {
	const select = 'ranged_distance_mod_trait_type';
	const fill = 'ranged_distance_mod_trait';

	trait_select(select, fill);
}

function ranged_trait_trait_type() {
	const select = 'ranged_trait_trait_type';
	const fill = 'ranged_trait_trait';

	trait_select(select, fill);
}

function ranged_dc() {
	const check = 'ranged_dc';
	const div = 'ranged-dc';

	check_opacity(check, div);
}

function ranged_type() {
	const select = 'ranged_type';
	const options = [{'val': 'flat_units', 'div': 'ranged-flat-units'}, 
					{'val': 'distance_rank', 'div': 'ranged-flat-distance-rank'}, 
					{'val': 'flat_rank_units', 'div': 'ranged-flat-rank-units'}, 
					{'val': 'flat_rank_distance', 'div': 'ranged-flat-rank-distance'}, 
					{'val': 'units_rank', 'div': 'ranged-units-rank'}, 
					{'val': 'rank_rank', 'div': 'ranged-rank-rank'}, 
					{'val': 'effect_mod', 'div': 'ranged-effect-mod'}, 
					{'val': 'check', 'div': 'ranged-check'}, 
					{'val': 'trait_mod', 'div': 'ranged-trait-mod'}, 
					{'val': 'distance_mod', 'div': 'ranged-distance-mod'}]

	select_opacity(select, options);
}

function ranged_dc_trait_type() {
	const select = 'ranged_dc_trait_type';
	const fill = 'ranged_dc_trait';

	trait_select(select, fill);
}