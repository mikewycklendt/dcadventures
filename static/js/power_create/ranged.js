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

function ranged_submit() {

	const extra = select("ranged_extra");
	const range_type = select("ranged_type");
	const flat_value = text("ranged_flat_value");
	const flat_units = select("ranged_flat_units");
	const flat_rank = select("ranged_flat_rank");
	const flat_rank_value = text("ranged_flat_rank_value");
	const flat_rank_units = select("ranged_flat_rank_units");
	const flat_rank_rank = select("ranged_flat_rank_rank");
	const flat_rank_distance = select("ranged_flat_rank_distance");
	const flat_rank_distance_rank = select("ranged_flat_rank_distance_rank");
	const units_rank_start_value = text("ranged_units_rank_start_value");
	const units_rank_value = text("ranged_units_rank_value");
	const units_rank_units = select("ranged_units_rank_units");
	const units_rank_rank = select("ranged_units_rank_rank");
	const rank_distance_start = select("ranged_rank_distance_start");
	const rank_distance = select("ranged_rank_distance");
	const rank_effect_rank = select("ranged_rank_effect_rank");
	const effect_mod_math = select("ranged_effect_mod_math");
	const effect_mod = select("ranged_effect_mod");
	const check_trait_type = select("ranged_check_trait_type");
	const check_trait = select("ranged_check_trait");
	const check_math = select("ranged_check_math");
	const check_mod = select("ranged_check_mod");
	const trait_trait_type = select("ranged_trait_trait_type");
	const trait_trait = select("ranged_trait_trait");
	const trait_math = select("ranged_trait_math");
	const trait_mod = select("ranged_trait_mod");
	const distance_mod_rank = select("ranged_distance_mod_rank");
	const distance_mod_math = select("ranged_distance_mod_math");
	const distance_mod_trait_type = select("ranged_distance_mod_trait_type");
	const distance_mod_trait = select("ranged_distance_mod_trait");
	const dc = check("ranged_dc");
	const dc_value = select("ranged_dc_value");
	const dc_trait_type = select("ranged_dc_trait_type");
	const dc_trait = select("ranged_dc_trait");

	const power_id = document.getElementById('power_id').value;

	const errors = 'ranged-err';
	const err_line = 'ranged-err-line';

	response = fetch('/power/ranged/create', {
		method: 'POST',
		body: JSON.stringify({
			'power_id': self.power_id,
			'extra_id': self.extra_id,
			'range_type': self.range_type,
			'flat_value': self.flat_value,
			'flat_units': self.flat_units,
			'flat_rank': self.flat_rank,
			'flat_rank_value': self.flat_rank_value,
			'flat_rank_units': self.flat_rank_units,
			'flat_rank_rank': self.flat_rank_rank,
			'flat_rank_distance': self.flat_rank_distance,
			'flat_rank_distance_rank': self.flat_rank_distance_rank,
			'units_rank_start_value': self.units_rank_start_value,
			'units_rank_value': self.units_rank_value,
			'units_rank_units': self.units_rank_units,
			'units_rank_rank': self.units_rank_rank,
			'rank_distance_start': self.rank_distance_start,
			'rank_distance': self.rank_distance,
			'rank_effect_rank': self.rank_effect_rank,
			'effect_mod_math': self.effect_mod_math,
			'effect_mod': self.effect_mod,
			'check_trait_type': self.check_trait_type,
			'check_trait': self.check_trait,
			'check_math': self.check_math,
			'check_mod': self.check_mod,
			'trait_trait_type': self.trait_trait_type,
			'trait_trait': self.trait_trait,
			'trait_math': self.trait_math,
			'trait_mod': self.trait_mod,
			'distance_mod_rank': self.distance_mod_rank,
			'distance_mod_math': self.distance_mod_math,
			'distance_mod_trait_type': self.distance_mod_trait_type,
			'distance_mod_trait': self.distance_mod_trait,
			'dc': self.dc,
			'dc_value': self.dc_value,
			'dc_trait_type': self.dc_trait_type,
			'dc_trait': self.dc_trait
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

		} else {

		}
	})
}