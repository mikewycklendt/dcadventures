function defense_check() {
	const check = "defense_check";
	const title = "defense-title";
	const base = 'defense-base';
	const entry = "defense-entry";

	check_title(check, title, base, entry);
}

function defense_base() {
	const field = 'defense_extra';
	const entry = "defense-entry";

	base(field, entry);
}

function defense_reflect() {
	const check = 'defense_reflect';
	const div = 'defense-reflect';
	const entry = 'defense-entry';

	check_drop(check, div, entry);
}

function defense_immunity() {
	const check = 'defense_immunity';
	const div = 'defense-immunity';
	const entry = 'defense-entry'

	check_drop(check, div, entry);
}

function defense_reflect_opposed_trait_type() {
	const select = 'defense_reflect_opposed_trait_type';
	const fill = 'defense_reflect_opposed_trait';
	
	trait_select(select, fill);
}

function defense_reflect_resist_trait_type() {
	const select = 'defense_reflect_resist_trait_type';
	const fill = 'defense_reflect_resist_trait';
	
	trait_select(select, fill);
}

function defense_reflect_check() {
	const select = 'defense_reflect_check';
	const options = [{'val': 1, 'div': 'defense-reflect-dc'},
					{'val': 2, 'div': 'defense-reflect-opposed'},
					{'val': 6, 'div': 'defense-reflect-resist'}];

	select_opacity(select, options);
}

function defense_immunity_trait_type() {
	const select = 'defense_immunity_trait_type';
	const fill = 'defense_immunity_trait';

	trait_select(select, fill);
}

function defense_immunity_type() {
	const select = 'defense_immunity_type';
	const options = [{'val': 'trait', 'div': 'defense-immunity-trait'},
					{'val': 'damage', 'div': 'defense-immunity-damage'},
					{'val': 'descriptor', 'div': 'defense-immunity-descriptor'},
					{'val': 'rule', 'div': 'defense-immunity-rule'}]

	select_opacity(select, options);
}

function defense_cover() {
	const check = 'defense_cover';
	const div = 'defense-cover';

	check_opacity(check, div);
}