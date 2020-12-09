function change_action_check() {
	const check = "change_action_check";
	const title = "action-title";
	const base = 'action-base';
	const entry = "action-entry";

	check_title(check, title, base, entry);
}

function action_base() {
	const field = 'action_extra';
	const entry = "action-entry";

	base(field, entry);
}

function action_submit() {

	const extra = select("action_extra");
	const action = select("action_change");
	const mod = select("action_mod");
	const objects = check("mod_objects");
	const circumstance = text("action_circ");

}