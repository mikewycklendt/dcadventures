function minion_check() {
	const check = "minion_check";
	const title = "minion-title";
	const base = 'minion-base';
	const entry = "minion-entry";

	check_title(check, title, base, entry);
}

function minion_base() {
	const field = 'minion_extra';
	const entry = "minion-entry";

	base(field, entry);
}

function minion_multiple() {
	const check = 'minion_multiple'
	const div = 'minion-multiple';
	const entry = 'minion-entry';

	check_drop(check, div, entry);
}

function minion_attitude() {
	const check = 'minion_attitude';
	const div = 'minion-attitude';
	const entry = 'minion-entry';

	check_drop(check, div, entry);
}

function minion_resitable() {
	const check = 'minion_resitable';
	const div = 'minion_resitable';
	const entry = 'minion-entry';

	check_drop(check, div, entry);
}

function minion_sacrifice() {
	const check = 'minion_sacrifice';
	const div = 'minion-sacrifice';

	check_display(check, div);
}