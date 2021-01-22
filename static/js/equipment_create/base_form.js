function alternate() {
	const check = "effect_check";
	const alt = 'alternate';
	const title = "effect-title";
	const base = 'effect-base';
	const entry = "effect-entry";

	entry_check(alt, title, base, entry);
	check.checked = true;
}

function equip_type() {
	const select = 'equip_type';
	const options = [{'val': '6', 'div': 'equip-cost'}]
	const value = '6';
	const title = "belt-title";
	const base = 'belt-base';
	const entry = 'belt-entry';

	select_opacity_reverse(select, options);
	select_entry_nocheck(base, entry, select, value)
}