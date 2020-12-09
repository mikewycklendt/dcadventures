function degree_check() {
	const check = "degree_check";
	const title = "degree-title";
	const base = 'degree-base';
	const entry = "degree-entry";

	check_title_small(check, title, base, entry);
}

function degree_base() {
	const field = 'degree_extra';
	const type = 'degree_type';
	const entry = "degree-entry";

	base_text(field, type, entry);
}

function degree_submit() {
	
	const degree_type = text("degree_type");
	const extra = select("degree_extra");
	const degree = select("degree_degree");
	const keyword = text("degree_keyword");
	const desscription = text("degree_desscription");
	const extra_effort = check("mod_extra_effort");
	const cumulative = check("mod_cumulative");
	const target = select("degree_target");

}