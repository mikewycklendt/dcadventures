	
function descriptor_new(value_input, div_input, des_title_input, des_field_input) {
	const value = select(value_input);
	const div = document.getElementById(div_input);
	const des_title_row1 = document.getElementById(des_title_input);
	const des_field = document.getElementById(des_field_input);

	if (value == 'new') {
		div.style.opacity = '100%';
		des_title_row1.style.opacity = '0%'
		des_field.style.opacity = '0%'
	} else {
		div.style.opacity = '0%';
	}
}

function descriptor_des(value_input, div_input, row3_input) {
	const row3 = document.getElementById(row3_input) 
	const value = select(value_input)
	const div = document.getElementById(div_input);

	if (value == 'new') {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		row3.style.display = 'grid';
		row3.style.maxHeight = div.scrollHeight + row3.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		setTimeout(function(){div.style.display = 'none'}, 400);
	}
}

function new_entry_show(row2, row3, damage) {
	row2.style.display = 'grid';
	row2.style.maxHeight = row2.scrollHeight + 'px';
	row3.style.display = 'grid';
	row3.style.maxHeight = row3.scrollHeight + 'px';
	damage.style.display = 'grid';
	damage.style.maxHeight = damage.scrollHeight + 'px';
}

function new_entry_hide(row2_input, row3_input, damage_input) {
	const row2 = document.getElementById(row2_input);
	const row3 = document.getElementById(row3_input);
	const damage_input = document.getElementById(damage_input);

	row2.style.maxHeight = '0px';
	setTimeout(function(){row2.style.display = 'none'}, 400);
	row3.style.maxHeight = '0px';
	setTimeout(function(){row3.style.display = 'none'}, 400);
	damage.style.maxHeight = '0px';
	setTimeout(function(){damage.style.display = 'none'}, 400);
}

function descriptor_create_fields(origin_input, source_input, medium_subtype_input, medium_input, descriptor_input, row2, row3, damage) {
	const origin = select(origin_input);
	const source = select(source_input);
	const medium_subtype = select(medium_subtype_input);
	const medium = select(medium_input);
	const descriptor = select(descriptor_input);

	if (origin == 'new' || source == 'new' || medium_subtype ==  'new' || medium == 'new' || descriptor == 'new') {
		new_entry_show(row2, row3, damage);
	}

	if (origin != 'new' && source != 'new' && medium_subtype !=  'new' && medium != 'new' && descriptor != 'new') {
		new_entry_hide(row2, row3, damage);
	}
}

function show_descriptor_field(origin_input, source_input, medium_subtype_input, medium_input, descriptor_field, descriptor_title=false) {
	const origin = select(origin_input);
	const source = select(source_input);
	const medium_subtype = select(medium_subtype_input);
	const medium = select(medium_input);
	const des_field =  document.getElementById(descriptor_field)

	if ((origin != 'all' && origin != '') || (source != 'all' && source != '') || (medium_type != 'all' && medium_type != '') || 
		(medium_subtype != 'all' && medium_subtype != '') || (medium != 'all' && medium != '')) {
			if (descriptor_title != false) {
				const des_title_row1 = document.getElementById(descriptor_title);
				des_title_row1.style.opacity = '100%';
			}
			des_field.style.opacity = '100%';
	} else {
		if (descriptor_title != false) {
			const des_title_row1 = document.getElementById(descriptor_title);
			des_title_row1.style.opacity = '0%';
		}
		des_field.style.opacity = '0%';
	}
}

function field_show(value_input, title_input, field_input) {
	const title = document.getElementById(title_input);
	const field = document.getElementById(field_input);
	const value = select(value_input)

	if (value != '' && value != 'all') {
		title.style.opacity = '100%';
		field.style.opacity = '100%';
	} else {
		title.style.opacity = '0%';
		field.style.opacity = '0%';
	}
}
