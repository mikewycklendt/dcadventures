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

function damage_submit() {

	const extra = select("damage_extra")
	const trait_type = select("dam_trait_type");
	const trait = select("dam_trait");
	const mod = select("dam_mod");
	const strength = check("dam_strength");
	const damage_type = select("damage_damage_type");
	const descriptor = select("damage_descriptor");

}