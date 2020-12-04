function resist_check() {
	const check = "resist_check";
	const title = "resist-title";
	const base = 'resist-base';
	const entry = "resist-entry"

	check_title(check, title, base, entry);
}


function resist_base() {
	const field = 'resist_extra';
	const entry = "resist-entry";

	base(field, entry);
}
function resist_type() {
	const select = 'resist_trait_type';
	const fill = 'resist_trait';

	trait_select(select, fill);
}

function resist_effect() {
	const field = "resist_eft";
	const options = [{'val': 'condition', 'div': "resist-condition"},
					{'val': 'damage', 'div': "resist-damage"}];

	select_maxheight(field, options);
}