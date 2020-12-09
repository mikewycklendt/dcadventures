function circ_check() {
	const check = "circ_check";
	const title = "circ-title";
	const base = 'circ-base';
	const entry = "circ-entry";

	check_title(check, title, base, entry);
}

function circ_base() {
	const field = 'circ_extra';
	const field2 = 'circ_target';
	const entry = "circ-entry";

	base_two(field, field2, entry);
}

function circ_type() {
	const field = 'circ_type';
	const options = [{'val': 'range', 'div': 'circ-range'},
					{'val': 'check', 'div': 'circ-check'}] 
	const entry = 'circ-entry';

	select_maxheight_entry(field, options, entry);
}

function circ_null_type() {
	const select = 'circ_null_type';
	const options = [{'val': 'condition', 'div': 'circ-null-condition'},
					{'val': 'descriptor', 'div': 'circ-null-descriptor'},
					{'val': 'trait', 'div': 'circ-null-trait'}]

	select_opacity(select, options);
}

function circ_null_trait_type() {
	const select = 'circ_null_trait_type';
	const fill = 'circ_null_trait';

	trait_select(select, fill);
}

function circ_submit() {

	const target = select("circ_target");
	const extra = select("circ_extra");
	const mod = select("circ_mod");
	const rounds = select("circ_rounds");
	const description = text("circ_des");
	const type = select("circ_type");
	const range = select("circ_range");
	const check_who = select("circ_check_who");
	const check_trait_type = select("circ_check_trait_type");
	const check_trait = select("circ_check_trait");
	const null_type = select("circ_null_type");
	const null_condition = select("circ_null_condition");
	const null_descriptor = select("circ_null_descriptor");
	const null_trait_type = select("circ_null_trait_type");
	const null_trait = select("circ_null_trait")

}