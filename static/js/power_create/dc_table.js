function dc_check() {
	const check = "dc_check";
	const title = "dc-title";
	const base = 'dc-base';
	const entry = "dc-entry";

	check_title(check, title, base, entry);
}

function dc_base() {
	const field = 'dc_extra';
	const field2 = 'dc_target';
	const entry = "dc-entry";

	base_two(field, field2, entry);
}

function dc_math_trait_type() {
	const select  = 'dc_math_trait_type';
	const fill = 'dc_math_trait';

	trait_select(select, fill);
}

function dc_dc() {
	const field = 'dc_dc';
	const options = [{'val': 'value', 'div': 'dc-value'},
				{'val': 'math', 'div': 'dc-math'}]
	const entry = 'dc-entry';

	select_maxheight_entry(field, options, entry);
}

function dc_time() {
	const check = 'dc_time';
	const div = 'dc-time';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_descriptor() {
	const check = 'dc_descriptor';
	const div = 'dc-descriptor';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_condition() {
	const check = 'dc_condition';
	const div = 'dc-condition';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_keyword() {
	const check = 'dc_keyword';
	const div = 'dc-keyword';
	const entry = 'dc-entry';

	check_drop(check, div, entry)
}

function dc_check_type() {
	const check = 'dc_check_type';
	const div = 'dc-check'
	const entry = 'dc-entry';

	check_drop(check, div, entry)
}

function dc_check_trait_type() {
	const select = 'dc_check_trait_type';
	const fill = 'dc_check_trait';

	trait_select(select, fill)
}

function dc_levels() {
	const check = 'dc_levels';
	const div = 'dc-levels';
	const entry = 'dc-entry';

	check_drop(check, div, entry);
}

function dc_submit() {

	const target = select("dc_target");
	const extra = select("dc_extra");
	const dc = select("dc_dc");
	const description = text("dc_description");
	const value = select("dc_value_value");
	const math_vqlue = select("dc_math_vqlue");
	const math = select("dc_math_math");
	const math_trait_type = select("dc_math_trait_type");
	const math_trait = select("dc_math_trait");
	const descriptor_check = check("dc_descriptor_check");
	const condition = check("dc_condition");
	const keyword_check = check("dc_keyword_check");
	const check_type = check("dc_check_type");
	const descriptor = select("dc_descriptor");
	const descriptor_possess = select("dc_descriptor_possess");
	const condition1 = select("dc_condition1");
	const condition2 = select("dc_condition2");
	const keyword = text("dc_keyword");
	const check_trait_type = select("dc_check_trait_type");
	const check_trait = select("dc_check_trait");
	const check_mod = select("dc_check_mod");
	const levels = check('dc_levels');
	const level = select('dc_level');
}