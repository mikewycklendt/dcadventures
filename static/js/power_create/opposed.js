function opposed_check() {
	const check = "opposed_check";
	const title = "opposed-title";
	const base = 'opposed-base';
	const entry = "opposed-entry";

	check_title(check, title, base, entry);
}

function opposed_base() {
	const field = 'opposed_extra';
	const entry = "opposed-entry";

	base(field, entry);
}

function opposed_trait_type() {
	const select = 'opposed_trait_type'
	const fill = 'opposed_trait'

	trait_select(select, fill)
}


function opposed_opponent_trait_type() {
	const select = 'opposed_opponent_trait_type'
	const fill = 'opposed_opponent_trait'

	trait_select(select, fill)
}

function opposed_submit() {

	const extra = select("opposed_extra");
	const trait_type = select("opposed_trait_type");
	const trait = select("opposed_trait");
	const mod = select("opposed_mod");
	const opponent_trait_type = select("opposed_opponent_trait_type");
	const opponent_trait = select("opposed_opponent_trait");
	const opponent_mod = select("opposed_opponent_mod");
	const player_check = select("opposed_player_check");
	const opponent_check = select("opposed_opponent_check");

}