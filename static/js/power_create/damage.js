function damage_check() {
	const check = "damage_check";
	const title = "damage-title";
	const base = 'damage-base';
	const entry = "damage-entry";

	check_title(check, title, base, entry);
}

function damage_base() {
	const field = 'damage_extra';
	const entry = "damage-entry";

	base(field, entry);
}

function dam_trait_type() {
	const select = 'dam_trait_type'
	const fill = 'dam_trait'

	trait_select(select, fill)
}

function damage_immunity_trait_type() {
	const select = 'damage_immunity_trait_type';
	const fill = 'damage_immunity_trait';

	trait_select(select, fill);
}

function damage_immunity_type() {
	const select = 'damage_immunity_type';
	const options = [{'val': 'trait', 'div': 'damage-immunity-trait'},
					{'val': 'damage', 'div': 'damage-immunity-damage'},
					{'val': 'descriptor', 'div': 'damage-immunity-descriptor'}]

	select_opacity(select, options);
}