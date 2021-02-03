
const trait_select = '/skill/trait/select';
const level_select = '/power/level/select';
const action_select = '/advantage/action/select';
const skill_select = '/equipment/skill/select';
const weapon_type_select = '/equipment/weapontype/select';
const weapon_select = '/equipment/weapons/select';
const subsense_select = '/sense/subsense/select';
const equipment_select = '/equipment/select';
const feature_info_select = '/vehicle/feature/info';
const equipment_info_select = '/equipment/equipment/select/info';
const weapon_info_select = '/equipment/weapon/select/info';
const head_feature_info_select = '/headquarters/feature/select/info';
const unit_select = '/unit/select'
const skill_icon_select = '/skill/icon/select';


function icon_select(field, route, divid=false, classname=false, remove=false, fade=false) {
	const id = select(field);

	response = fetch(route, {
		method: 'POST',
		body: JSON.stringify({
			'id': id
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const icon = jsonResponse.icon;

			if (fade != false) {
				if (divid != false) {
					fade(divid);
				} if (classname != false) {
					fade(classname, true)
				}
			}

			if (divid != false) {
				const div = document.getElementById(divid);
				if (remove == true) {
					div.removeAttribute('class');
				}
				setTimeout(function(){div.classList.add(icon)}, 300);
			}
			
			if (classname != false) {
				const divs = document.getElementsByClassName(classname);
				let div; 
				for (div of divs) {
					if (remove == true) {
						div.removeAttribute('class');
					}
					div.className = classname;
					setTimeout(function(){div.classList.add(icon)}, 300);
				}
			}
		
		} else {
			console.log('error');
		}
	})	
}

function fade(div_input, classname=false) {
	
	if (classname == false) {
		const div = document.getElementById(div_input);
		div.style.opacity = '0%'
		setTimeout(function(){div.style.opacity = '100%'}, 300);
	}

	if (classname != false) {
		const divs = document.getElementsByClassName(div_input);
		let div;
		for (div of divs) {
			div.style.opacity = '0%';
		}
	}
	
	if (classname != false) {
		const divs = document.getElementsByClassName(div_input);
		let div;
		for (div of divs) {
			setTimeout(function(){div.style.opacity = '100%'}, 300);
		}
	}
}



function null_hide_maxheight(field, item) {
	val = select(field);

	if (val == '' ) {
		hide_maxheight(item);
		shrink_entry(entry, item);
	}
}

function show_info(item, divs, entry, multiple=false) {
	let d;
	for (d of divs) {
		const div = document.getElementById(d.div);
		div.style.opacity = '0%';
	}

	setTimeout(function(){
		for (d of divs) {
			const spot = document.getElementById(d.div);
			if (d.multiple) {
				if (d.class) {
					const classname = d.class;
					const olds = document.getElementsByClassName(classname);
					if (olds.length > 1)
					for (i = olds.length -1; i > -1; i-- ) {
						olds[i].remove();
					}
				}
			}
		}
	}, 300)


	if (multiple == true) {
		for (d of divs) {
			const spot = document.getElementById(d.div);
			let icon;
			if (d.icon) {
				icon = d.icon;
			}
			if (d.multiple) {
			//	if (d.class) {
			//		const classname = d.class;
			//		const olds = document.getElementsByClassName(classname);
			//		while (olds.length > 0) {olds[0].remove()};
			//	}
				const contents = d.val;
				setTimeout(function(){
					spot.style.opacity = '100%';
					let content;
					let item_text = ''
					for (content of contents) {
						if (d.class) {
							const classname = d.class;
							const div = document.createElement('div');
							div.className = classname;
							if (d.icon) {
								div.classList.add(icon)
							}
							div.innerHTML = content;
							spot.appendChild(div);
						} else {
							if (item_text == '') {
								item_text += content;
							} else {
								item_text += ', ' + content;
							}
						}
					}
					if (item_text != '') {
						spot.innerHTML = item_text
					}
				}, 300);
			} else {
				const text = d.val;
				setTimeout(function(){
					spot.innerHTML = text;
					spot.style.opacity = '100%';
				}, 310);
			}
		}
	} else {
		for (d of divs) {
			const div = document.getElementById(d.div);
			const text = d.val;
			setTimeout(function(){
				div.innerHTML = text;
				div.style.opacity = '100%';
			}, 300);
		}
	}

	show_maxheight(item);
	grow_entry(entry, item);
}





function show_opacity(div_input) {
	const div = document.getElementById(div_input);

	setTimeout(function(){div.style.display = 'grid';}, 300);
	setTimeout(function(){div.style.opacity = '100%';}, 310);
}

function hide_opacity(div_input) {
	const div = document.getElementById(div_input);

	div.style.opacity = '0%';
	setTimeout(function(){div.style.display = 'none';}, 300);
}


function show_opacity_class(div_input) {
	const divs = document.getElementsByClassName(div_input);
	let div;
	
	setTimeout(function(){
		for (div of divs) {			
			div.style.display = 'grid';
		}
	}, 300);
	setTimeout(function(){
		for (div of divs) {
			div.style.opacity = '100%';
		}
	}, 310);
}

function hide_opacity_class(div_input) {
	const divs = document.getElementsByClassName(div_input);
	let div;
	for (div of divs) {
		div.style.opacity = '0%';
	}

	setTimeout(function(){
		for (div of divs) {
			div.style.display = 'none';
		}
	}, 300);		
}

function math_div_select(select, val, math, containdiv ) {
	const field = document.getElementById(select);
	const value = field.options[field.selectedIndex].value;
	const div = document.getElementById(containdiv)

	if (value == 'math') {
		div.style.display = 'grid';
		hide_opacity(val);
		show_opacity(math);
	} else if (value == 'value') {
		div.style.display = 'grid';
		hide_opacity(math);
		show_opacity(val);
	} else {
		hide_opacity(math);
		hide_opacity(val);
		setTimeout(function(){div.style.display = 'none'}, 300);
	}
}

function math_mod_div_select(select, val, math, mod, containdiv ) {
	const field = document.getElementById(select);
	const value = field.options[field.selectedIndex].value;
	const div = document.getElementById(containdiv)

	if (value == 'math') {
		div.style.display = 'grid';
		hide_opacity(val);
		hide_opacity(mod);
		show_opacity(math);
	} else if (value == 'value') {
		div.style.display = 'grid';
		hide_opacity(math);
		hide_opacity(mod);
		show_opacity(val);
	} else if (value == 'mod') {
		div.style.display = 'grid';
		hide_opacity(math);
		hide_opacity(val);
		show_opacity(mod);
	} else {
		hide_opacity(math);
		hide_opacity(mod);
		hide_opacity(val);
		setTimeout(function(){div.style.display = 'none'}, 300);
	}
}

function value_type(select, math, val) {
	const field = document.getElementById(select);
	const value = field.options[field.selectedIndex].value;

	if (value == 'math') {
		hide_opacity(val);
		show_opacity(math);
	} else if (value == 'value') {
		hide_opacity(math);
		show_opacity(val)
	} else {
		hide_opacity(math);
		hide_opacity(val);
	}
}

function check_drop(field, divdrop, entrydrop) {
	const check = document.getElementById(field);
	const div = document.getElementById(divdrop);
	const entry = document.getElementById(entrydrop);

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = div.scrollHeight + entry.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
		setTimeout(function(){div.style.display = 'none'}, 400);
	}
}


function check_maxheight(field, divdrop) {
	const check = document.getElementById(field);
	const div = document.getElementById(divdrop);

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
		setTimeout(function(){div.style.display = 'none'}, 400);
	}
}

function check_opacity(field, divopacity) {
	const check = document.getElementById(field);
	const div = document.getElementById(divopacity);

	if (check.checked == true) {
		div.style.opacity = '100%';
	} else {
		div.style.opacity = '0%';
	}
}

function check_display(field, divdisplay) {
	const check = document.getElementById(field);
	const div = document.getElementById(divdisplay);

	if (check.checked == true) {
		div.style.display = 'grid';
		setTimeout(function(){div.style.opacity = '100%'}, 10);
	} else {
		div.style.opacity = '0%';
		setTimeout(function(){div.style.display = 'none'}, 300);
	}
}

function clear_errors(line, div) {
		
	const errors_delete = document.getElementsByClassName(line);

	if (typeof errors_delete[0] === "undefined") {
		console.log('no errors defined')
	} else {
		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.maxHeight = "0px";
			errors_delete[i].style.padding = "0px";
			errors_delete[i].style.marginBottom = "0px";
			setTimeout(function(){errors_delete[i].style.display = 'none'}, 400)
		}

		const errors = document.getElementById(div)

		errors.style.display = "none";
		errors.style.padding = "0px";
		errors.style.maxHeight = "0px";
	}
}

function clear_error_lines(line) {
	const errors_delete = document.getElementsByClassName('extras-err-line');

	for (i = 0; i < errors_delete.length; i++) {
		errors_delete[i].style.display = "none";
	}
}

function new_error(description, error_line, errors, errors_height) {
	const error = document.createElement('div');
	error.className = error_line;
	error.innerHTML = description;

	errors.appendChild(error);

	error.style.maxHeight = error.scrollHeight + "px";
	errors_height = errors_height + error.scrollHeight; 
}	

function json_errors(line, div, all_errors) {					
	const errors = document.getElementById(div);

	errors.style.display = "grid";
	errors.style.padding = "1%";

	
	let error_msg;

	for (error_msg of all_errors) {

		const error = document.createElement('div');
		error.className = line;
		error.innerHTML = error_msg;
	
		errors.appendChild(error);
	
		error.style.maxHeight = error.scrollHeight + "px";
	
		errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
		errors.style.padding = "1%";
	}
}

function show_maxheight(div_input) {
	const div = document.getElementById(div_input);

	setTimeout(function(){
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
	}, 300)
}

function hide_maxheight(div_input) {
	const div = document.getElementById(div_input);

	div.style.maxHeight = '0px';
	setTimeout(function(){div.style.display = 'none'}, 300)
}

function shrink_entry(entry_input, div_input) {
	const entry = document.getElementById(entry_input);
	const div = document.getElementById(div_input);

	entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
}

function grow_entry(entry_input, div_input) {
	const entry = document.getElementById(entry_input);
	const div = document.getElementById(div_input);

	setTimeout(function(){
		entry.style.maxHeight = entry.scrollHeight + div.scrollHeight + 'px';
	}, 310)
}

function select_maxheight_entry(select, options, entry) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;
	const adiv = options[0].div;

	console.log(val);

	for (option of options) {
		let valu = option.val;
		let div = option.div;

		if (val != valu) {
			hide_maxheight(div);
		} else {
			show_maxheight(div);
		}
	};

	if (val == '') {
		shrink_entry(entry, adiv)
	} else {
		for (option of options) {
			let valu = option.val;
			let div = option.div;
	
			if (val == valu) {
				grow_entry(entry, div);
			}
		}
	}
}

function hide_secondary(select_input, options, entry) {
	const select = document.getElementById(select_input)
	const value = select.options[select.selectedIndex].value;

	for (o of options) {
		const val = o.val;
		const div = o.div;
		if (value != val) {
			hide_maxheight(div);
			shrink_entry(entry)
		}
	} 
}

function hide_secondary_double(select1_input, select2_input, options, row, entry) {
	const field1 = document.getElementById(select1_input)
	const val1 = field1.options[field1.selectedIndex].value;
	const field2 = document.getElementById(select2_input);
	const val2 = field2.options[field2.selectedIndex].value;

	let shrink = true;

	for (o of options) {
		const val = o.val;
		if (val1 == val) {
			shrink = false;
		}

		if (val2 == val) {
			shrink = false;
		}
	}

	if (shrink == true) {
		hide_maxheight(row);
		shrink_entry(entry, row);
	}

	for (o of options) {
		const v = o.val;
		const s1 = o.select1;
		const s2 = o.select2;
		const select1 = document.getElementById(s1);
		const select2 = document.getElementById(s2);

		if (val1 != v && val2 != v) {
			select1.setAttribute('previousValue', 'empty');
			select2.setAttribute('previousValue', 'empty');
			select1.selectedIndex=0;
			select2.selectedIndex=0;
		}

		if (val1 != v) {
			const divs = o.divs;
			let div;
			for (div of divs) {
				hide_opacity(div);
			}
		}
	} 
}

function select_opacity(select, options) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;

	console.log(val);

	for (option of options) {
		let valu = option.val;
		let div = option.div;

		if (val != valu) {
			hide_opacity(div);
		} else {
			show_opacity(div);
		}
	};
}


function select_opacity_class(select, options) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;

	console.log(val);

	for (option of options) {
		let valu = option.val;
		let div = option.div;

		if (val != valu) {
			hide_opacity_class(div);
		} else {
			show_opacity_class(div);
		}
	};
}

function select_opacity_reverse(select, options) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;

	console.log(val);

	for (option of options) {
		let valu = option.val;
		let div = option.div;

		if (val == valu) {
			hide_opacity(div);
		} else {
			show_opacity(div);
		}
	};
}


function select_reset(select_input, selects) {
	const field = document.getElementById(select_input);
	const val = field.options[field.selectedIndex].value;
	let s;

	for (s of selects) {
		const select = document.getElementById(s);
		const value = select.options[select.selectedIndex].value

		if (val != value) {
			select.selectedIndex=0;
		}
	};
}

function reset(select_input) {
	const select = document.getElementById(select_input);

	select.selectedIndex=0;

}

function reset_all(selects) {
	let select;

	for (select of selects) {
		reset(select)
	}
}

function select_opacity_any(select, div) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;

	if (val != '') {
		show_opacity(div);
	} else {
		hide_opacity(div);
	}
}

function multiple_field(div_input) {
	const div = document.getElementById(div_input);
	
	div.style.display = 'grid';
	setTimeout(function(){div.style.opacity = '100%'}, 10);
	
}



function select_other(select, options, db) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;

	console.log(val);

	for (option of options) {
		let valu = option.val;
		let div = option.div;

		if (val != valu) {
			hide_opacity(div);
			show_opacity(db)
		} else {
			show_opacity(div);
			hide_opacity(db);
		}
	};
}

function select_maxheight(select, options) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;

	console.log(val);

	for (option of options) {
		let valu = option.val;
		let div = option.div;

		if (val != valu) {
			hide_maxheight(div);
		};
	}
	
	for (option of options) {
		let valu = option.val;
		let div = option.div;

		if (val == valu) {
			show_maxheight(div);
		}
	};
}

function base(field_inputs, entry_input, texts=false) {
	const entry = document.getElementById(entry_input)

	let satisfied = true
	let field;
	for (field of field_inputs) {
		const f = document.getElementById(field);
		const select = f.options[f.selectedIndex].value;

		if (select == '') {
			satisfied = false
		}
	}

	if (texts != false) {
		let text;
		for (text of texts) {
			const field = document.getElementById(text);
			const value = field.value;
			if (value == '') {
				satisfied = false;
			}
		}
	}

	if (satisfied == true) {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";	
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function base_text(textfield, entry_input) {
	const entry = document.getElementById(entry_input);
	const text = document.getElementById(textfield);

	if (text != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";	
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function entry_check(check_input, title_input, base_input, entry_input, size=200) {
	const check = document.getElementById(check_input);
	const entry = document.getElementById(entry_input);
	const title = document.getElementById(title_input);
	const base = document.getElementById(base_input)

	const size2 = size + '%';
	const size1 = size + 8 + '%';
	
	if (check.checked == true) {
		base.style.opacity = '100%'
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		title.style.color = "#af0101";
		title.style.fontSize = size1;
		setTimeout(function(){title.style.fontSize = size2}, 75);
	} else {
		base.style.opacity = '0%'
		entry.style.maxHeight = "0px";
		setTimeout(function(){entry.style.display = 'none';}, 400);
		title.style.color = "#245681";
	}
}

function check_title(check_input, title_input, base_input, entry_input, size=200) {
	const check = document.getElementById(check_input);
	const title = document.getElementById(title_input);
	const base = document.getElementById(base_input);
	const entry = document.getElementById(entry_input);

	const size2 = size + '%';
	const size1 = size + 8 + '%';

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = size1;
		setTimeout(function(){title.style.fontSize = size2}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function select(field_input) {
	const field = document.getElementById(field_input);
	const value = field.options[field.selectedIndex].value;

	return value;
}

function text(text_input) {
	const input = document.getElementById(text_input);
	const value = input.value;

	return value;
}

function check(check_input) {
	const checkbox = document.getElementById(check_input);
	const value = checkbox.checked;

	return value;
}

function multiple(multiple_input) {
	let selectElement = document.getElementById(multiple_input);
	let selectedValues = Array.from(selectElement.selectedOptions).map(option => option.value);

	return selectedValues;
}


function select_entry(check_input, base_input, entry_input, field_input, value) {
	const check = document.getElementById(check_input);
	const base = document.getElementById(base_input);
	const entry = document.getElementById(entry_input);
	const field = select(field_input);

	if (field == value) {
		base.style.opacity = '100%';
		entry.style.display = "grid";
		entry.style.maxHeight = entry.scrollHeight + "px";
		check.checked = true;
	} else {
		base.style.opacity = '0%';
		check.checked = false;
		entry.style.maxHeight = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function select_entry_nocheck(base_input, entry_input, field_input, value) {
	const base = document.getElementById(base_input);
	const entry = document.getElementById(entry_input);
	const field = select(field_input);

	if (field == value) {
		base.style.opacity = '100%';
		entry.style.display = "grid";
		entry.style.maxHeight = entry.scrollHeight + "px";
	} else {
		base.style.opacity = '0%';
		entry.style.maxHeight = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function new_items(insert, items) {
	
	if (insert == true) {
		let i;
		for (i of items) {
			const id = i.id;
			const name = i.name;
			const class_check = i.class;
			const field = i.field;

			if (class_check == true) {
				const selects = document.getElementsByClassName(field);
				let select;
					
				for (select of selects) {
					const o = document.createElement('option');
					o.value = id;
					o.text = name;
					select.add(o);
				}
			} else {
				const select = document.getElementById(field);
				const o = document.createElement('option');
				o.value = id;
				o.text = name;
				select.add(o);
			}
		}
	}
}

function deleted_item(divs, id) {
	
	if (divs != false) {
		let div;
		for (div of divs) {
			const selects = document.getElementsByClassName(div);
			let select;

			for (select of selects) {
				options = select.options;
				let option;

				for (option of options) {
					if (option.value == id) {
						console.log(option.value);
						option.remove();
					}
				}
			}
		}
	}
}

function selects_add(id, name, selects_input) {
	let selects = document.getElementsByClassName(selects_input);
	let select;

	for (select of selects) {
		const o = document.createElement('option');
		o.value = id;
		o.text = name;
		select.add(o);
	}
}


function id_select(select, fill, route) {
	const field = document.getElementById(select)
	const type_id = field.options[field.selectedIndex].value
	const update = document.getElementById(fill);

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

	response = fetch(route, {
		method: 'POST',
		body: JSON.stringify({
			'id': type_id
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const options = jsonResponse.options;
			let option;

			for (option of options)  {
				let o = document.createElement("option")
				o.value = option.id;
				o.text = option.name;
				update.add(o);
			}

		} else {
			console.log(jsonResponse.options);
		}
	})	
}

function update_divs(data) {
	for (d of data) {
		const div = document.getElementById(d.div);
		const text = d.val;

		div.innerHTML = text;
	}
}

function double_select(select1, select2, options, row, entry) {
	const field1 = document.getElementById(select1);
	const val1 = field1.options[field1.selectedIndex].value;
	const field2 = document.getElementById(select2);
	const val2 = field2.options[field2.selectedIndex].value;

	const old1 = field1.getAttribute('previousValue');
	field1.setAttribute('previousValue', val1);

	let o;
	let grown = false;
	let grow = false;
	let div;
	
	let shrink = true;
	let start = false;

	for (o of options) {
		let val = o.val
		if (val1 == val) {
			start = true
		}

		if (old1 == val) {
			start = true;
		}

		if (val2 == val) {
			start = true;
		}
	}

	console.log(start)

	if (start == true) { 
		for (o of options) {
			let val = o.val;
			if (old1 == val ) {
				grown = true;
				div = o.div;
			} 

			if (val2 == val) {
				grown = true
				shrink = false;
			}

			if (val1 == val) {
				grow = true;
				shrink = false;
				div = o.div;
			}
		}

		console.log('start');
		console.log(start);
		console.log('grown');
		console.log(grown);

		if (grown == false) {
			if (grow == true) {
				const d = document.getElementById(div);
				d.style.display = 'grid';
				grow_entry(entry, div);
				show_maxheight(row)
			}
		} 
		
		if (shrink == false) {
			let option;

			for (option of options) {
				let valu = option.val;
				let di = option.div;

				if (val1 != valu) {
					hide_opacity(di);
				} else {
					show_opacity(di);
				}
			}
		} else {
			for (option of options) {
				let valu = option.val;
				let di = option.div;

				if (val1 != valu) {
					hide_opacity(di)
				}
			}

			hide_maxheight(row)
			shrink_entry(entry, div)
		}
	} else {
		console.log('nothing')
	}
}


function double_select_second(select1, select2, options, others, row, entry) {
	const field1 = document.getElementById(select1);
	const val1 = field1.options[field1.selectedIndex].value;
	const field2 = document.getElementById(select2);
	const val2 = field2.options[field2.selectedIndex].value;

	const old1 = field1.getAttribute('previousValue');
	field1.setAttribute('previousValue', val1);

	let o;
	let grown = false;
	let grow = false;
	let div;
	
	let shrink = true;
	let start = false;

	for (o of options) {
		let val = o.val
		if (val1 == val) {
			start = true
		}

		if (old1 == val) {
			start = true;
		}

		if (val2 == val) {
			start = true;
		}
	}

	console.log(start)

	if (start == true) { 
		for (o of options) {
			let val = o.val;
			if (old1 == val ) {
				grown = true;
				div = o.div;
			} 

			if (val2 == val) {
				grown = true
				shrink = false;
			}

			if (val1 == val) {
				grow = true;
				shrink = false;
				div = o.div;
			}
		}

		console.log('start');
		console.log(start);
		console.log('grown');
		console.log(grown);

		if (grown == false) {
			if (grow == true) {
				const d = document.getElementById(div);
				d.style.display = 'grid';
				grow_entry(entry, div);
				show_maxheight(row)
			}
		} 
		
		if (shrink == false) {
			let option;

			for (option of options) {
				let valu = option.val;
				let di = option.div;

				if (val1 != valu) {
					hide_opacity(di);
				} else {
					show_opacity(di);
				}
			}
		} else {
			for (option of options) {
				let valu = option.val;
				let di = option.div;

				if (val1 != valu) {
					hide_opacity(di)
				}
			}

			let clear = true;
			let other;
			for (other of others) {
				const s = document.getElementById(other.select);
				const value = s.options[s.selectedIndex].value;
				const values = other.values;
				let v;
				for (v of values) {
					if (v == value) {
						clear = false
					}
				}
			}

			if (clear == true) { 
				hide_maxheight(row)
				shrink_entry(entry, div)
			}
		}
	} else {
		console.log('nothing')
	}
}


function clear_errors(line, div) {
	const errors_delete = document.getElementsByClassName(line);
	const errors = document.getElementById(div);

	if (typeof errors_delete[0] === "undefined") {
		console.log('no errors defined')
	} else {

		errors.style.maxHeight = "0px";
		errors.style.padding = "0px";

		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.maxHeight = "0px";
			errors_delete[i].style.padding = "0px";
			errors_delete[i].style.marginBottom = "0px";
		};
		setTimeout(function(){
			for (i = 0; i < errors_delete.length; i++) {
				errors_delete[i].style.display = 'none';
				errors.style.display = 'none';
			}
		}, 400);

	}
}

function descriptor_add_type()  {
	const fields = document.getElementsByClassName('descriptor-sml');
	
	options = [{'type': 11223344, 'name': 'Any Chosen Rare'}, 
				{'type': 22334455, 'name': 'Any Chosen Uncommon'}, 
				{'type': 33445566, 'name': 'Any Chosen Common'}, 
				{'type': 44556677, 'name': 'Any Chosen Very Common'}, 
				{'type': 55667788, 'name': 'Any Chosen Damage'},
				{'type': 66778899, 'name': 'Any Chosen Origin'},
				{'type': 77889900, 'name': 'Any Chosen Source'},
				{'type': 88990011, 'name': 'Any Chosen Medium Type'},
				{'type': 99001122, 'name': 'Any Chosen Medium Subtype'},
				{'type': 11002233, 'name': 'Any Chosen Medium'},
				{'type': 12121212, 'name': 'Any Chosen Descriptor'}]

	let field;
	let option;

	for (field of fields) {
		for (option of options) {
			let o = document.createElement('option');
			o.value = option.type;
			o.text = option.name;
			field.add(o);
		}
	}
}

descriptor_add_type()

function create_id(create_name, create_add, create_route, create_name_div, hidden_id) {
	const item_name = document.getElementById(create_name).value;
	const add_item = document.getElementById(create_add);
	const edit_button = document.getElementById('edit-button');

	const err_line = 'name-err-line';
	const errors = 'name-err';


	response = fetch(create_route, {
		method: 'POST',
		body: JSON.stringify({
		  'name': item_name,
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			const all_fields = document.getElementById('all-fields');
			const name_div = document.getElementById(create_name_div);
			const item_id = document.getElementById(hidden_id);
			name_div.innerHTML = jsonResponse.name;
			item_id.value = jsonResponse.id;
			name_div.style.display = "block"
			name_div.style.opacity = "100%"
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);
			edit_button.style.display = "block";
			add_item.style.display = "none";
			all_fields.style.display = "grid";
			setTimeout(function(){all_fields.style.opacity = "100%"}, 10);

			clear_errors(err_line, errors);

		} else {

			back_errors(err_line, errors, jsonResponse);

		}
	})
}

function item_edit_form(item_name_edit, name_div, item_edit_grid) {
	const edit_field = document.getElementById(item_name_edit);
	const name = document.getElementById(name_div).innerHTML;
	const edit_grid = document.getElementById(item_edit_grid);

	edit_field.value = name;
	edit_grid.style.display = "grid";
	edit_grid.style.maxHeight = edit_grid.scrollHeight + "px";
	edit_grid.style.padding = "1%";
}

function item_edit(item_id, item_name_edit, edit_route, item_name_div, item_edit_grid) {
	const id = document.getElementById(item_id).value;
	const name = document.getElementById(item_name_edit).value;

	const err_line = 'name-err-line';
	const errors = 'name-err';
	
		response = fetch(edit_route, {
		method: 'POST',
		body: JSON.stringify({
			'id': id,
			'name': name
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			const name_div = document.getElementById(item_name_div);
			const edit_grid = document.getElementById(item_edit_grid);
			edit_grid.style.display = "none";
			name_div.innerHTML = jsonResponse.name;
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);

			clear_errors(err_line, errors);

		} else {
				
			back_errors(err_line, errors, jsonResponse);

		}
	})
}

function create_table(jsonResponse, object, route, selects=false) {

	const spot_string = jsonResponse.spot;
	const table_id = jsonResponse.table_id;
	const created = jsonResponse.created;
	const id = jsonResponse.id; 
	const title_string = jsonResponse.title;
	const grid = jsonResponse.grid;
	const mods = jsonResponse.mods;
	const cells = jsonResponse.cells;
	const rows = jsonResponse.rows;
	const size = jsonResponse.font;

	console.log(size);

	console.log(id)

	const cells_class = table_id + '-cells';
	const table_class = table_id + '-table'
	const base_table = 'skill-table-table';
	const base_cell_title = 'skill-table-cell-title ';
	const base_title = 'skill-table-title'
	const base_titles = 'skill-table-titles';

	
	console.log(created)


	if (created == false) {

		let grow =  0;

		create_titles(jsonResponse, grow, object, route, selects);
	
	} else {

		let grow = 0

		const table = document.getElementById(table_class)

		cells_create(table, grow, jsonResponse, object, route, selects);
	}


}

function create_titles(jsonResponse, grow, object, route, selects=false) {
	
	const spot_string = jsonResponse.spot;
	const table_id = jsonResponse.table_id;
	const title_string = jsonResponse.title;
	const grid = jsonResponse.grid;
	const cells = jsonResponse.cells;

	const cells_class = table_id + '-cells';
	const table_class = table_id + '-table';
	const title_class = table_id + '-title';
	const base_table = 'skill-table-table';
	const base_cell_title = 'skill-table-cell-title';
	const base_title = 'skill-table-title-table';
	const base_titles = 'skill-table-titles';

	const spot = document.getElementById(spot_string);
	if (title_string != '') {
		const title = document.createElement('div');
		title.className = base_title;
		title.innerHTML = title_string;
		spot.appendChild(title)
	}
	const new_table = document.createElement('div');
	new_table.className = base_table;
	new_table.setAttribute('id', table_class);
	spot.appendChild(new_table);

	const title_row = document.createElement('div');
	title_row.className = base_titles;
	title_row.classList.add(cells_class);
	title_row.style.gridTemplateColumns = grid;
	grow = grow + title_row.scrollHeight;
	new_table.appendChild(title_row);
	
	let cell;
	for (cell of cells) {
		const cell_title = document.createElement('div');
		cell_title.className = title_class;
		cell_title.classList.add(base_cell_title);
		cell_title.innerHTML = cell.title;
		console.log(cell.title);
		title_row.appendChild(cell_title);
	}
	
	grow += title_row.scrollHeight

	cells_create(new_table, grow, jsonResponse, object, route, selects)
	
}

function grow_table(table, grow) {

	table.style.display = 'grid';
	table.style.maxHeight = table.scrollHeight + grow + 'px';
}

function grid__update(columns, cells, table_id, grid, cells_class, size, table) {

	table.style.fontSize = size + '%';
	
	const title_class = table_id + '-title';
	const titles = document.getElementsByClassName(title_class)
	
	for (let i = 0; i < cells.length; i++) {
		if (columns[i] > 1) {
			titles[i].style.maxHeight = titles[i].scrollHeight + 'px';
			titles[i].style.opacity = '100%';
		}
		else {
			titles[i].style.opacity = '0%';
			titles[i].style.maxHeight = '0px';
		}
	}

	const cells_rows = document.getElementsByClassName(cells_class);
	for (let i = 0; i < cells_rows.length; i++) {
		cells_rows[i].style.gridTemplateColumns = grid;
		console.log(size)
	}

}

function cells_create(table_input, grow, jsonResponse, object, route, selects=false) {

	const table = table_input;
	const table_id = jsonResponse.table_id;
	const id = jsonResponse.id; 
	const grid = jsonResponse.grid;
	const mods = jsonResponse.mods;
	const cells = jsonResponse.cells;
	const size = jsonResponse.font;
	const columns = jsonResponse.columns;

	console.log(size)


	const cells_class = table_id + '-cells';
	const entry_class = table_id + '-row';
	const delete_class = table_id + '-xbox';
	const check_button_class = table_id + '-button'
	const base_cells = 'skill-table-cells';
	const base_cell = 'skill-table-cell'
	const base_button_check = 'skill-check-button ';
	const base_check = 'skill-check';
	const base_entry = 'skill-table-row';
	const base_delete = 'xbox ';

	const entry = document.createElement('div');
	entry.className = base_entry
	entry.classList.add(entry_class);
	table.appendChild(entry);
	const row = document.createElement('div');
	row.className = base_cells;
	row.classList.add(cells_class);	
	row.style.gridTemplateColumns = grid;
	entry.appendChild(row);

	let create_mod = false;
	let cell;
	let cell_heights = [];
	for (cell of cells) {
		const cell_class = table_id + 'cell';
		const new_cell = document.createElement('div');
		new_cell.className = base_cell;
		new_cell.classList.add(cell_class);
		if (cell.content == false) {
			new_cell.innerHTML = '';
		} else if (cell.content == true && cell.content != 1 && cell.content != '1') {
			if (cell.mod_check == true) {
				create_mod = true;
				const check = document.createElement('button');
				check.className = base_button_check;
				check.classList.add(check_button_class);
				new_cell.appendChild(check);
				const cell_height = new_cell.scrollHeight;
				cell_heights.push(cell_height);
			} else {
				const check = document.createElement('div');
				check.className = base_check;
				new_cell.appendChild(check);
				const cell_height = new_cell.scrollHeight;
				cell_heights.push(cell_height);
			}
		} else {
			new_cell.innerText = cell.content;
			const cell_height = new_cell.scrollHeight;
			cell_heights.push(cell_height);
		}
		row.appendChild(new_cell);
	}

	let height;
	for (height of cell_heights) {
		if (height > grow) {
			grow += height;
		}
	}

	const empty_cell = document.createElement('div');
	empty_cell.className = base_cell;
	row.appendChild(empty_cell);

	const delete_cell = document.createElement('div');
	delete_cell.className = base_cell;
	const delete_btn = document.createElement('button');
	delete_btn.className = base_delete + delete_class;
	delete_btn.setAttribute('data-id', id);
	delete_cell.appendChild(delete_btn)
	row.appendChild(delete_cell)

	table.style.display = 'grid';
	row.style.maxHeight = row.scrollHeight + 'px';
	grow += row.scrollHeight; 

	if (create_mod) {
		mod_create(mods, id, entry, table_id, object, table);
	}
	
	grow_table(table, grow)
	
	grid__update(columns, cells, table_id, grid, cells_class, size, table)

	row_delete(jsonResponse, route, object, selects) 
}



function mod_create(mods_input, id_input, entry_input, table_id_input, object, table) {

	const mods = mods_input;
	const id = id_input;
	const entry = entry_input;
	const table_id = table_id_input;

	const mod_class = table_id + '-mod'; 
	const base_mod = 'mod-row';
	const mod_cell_empty = 'mod-cell-empty';
	const mod_cell_mod = 'mod-cell-mod';
	const mod_cell_sub = 'mod-cell-sub';
	const mod_cell_title = 'mod-cell-title';
	const mod_cell_content = 'mod-cell-content';
	
	const entry_class = table_id + '-row';

	const entries = document.getElementsByClassName(entry_class);

	let new_mod;
	for (new_mod of mods) {
		const grid = new_mod.grid;		
		const cells = new_mod.cells;
		const mod_title = new_mod.title;
		const variable = new_mod.variable;
		console.log(entries.length)
		object.mod.push(false)

		const mod = document.createElement('div');
		mod.className = mod_class;
		mod.classList.add(base_mod);
		mod.style.gridTemplateColumns = grid;
		entry.appendChild(mod);
		
		const empty = document.createElement('div');
		empty.className = mod_cell_empty
		mod.appendChild(empty);

		const title = document.createElement('div');
		title.className = mod_cell_mod;
		title.innerHTML = mod_title;
		mod.appendChild(title);

		if (variable == true) {
			const sub_title = new_mod.sub_title;
			const sub = document.createElement('div');
			sub.className = mod_cell_sub;
			sub.innerHTML = sub_title;
			mod.appendChild(sub)
		}

		let new_cell;
		for (new_cell of cells) {
			const tit = document.createElement('div');
			tit.className = mod_cell_title;
			tit.innerHTML = new_cell.title;
			mod.appendChild(tit);

			const con = document.createElement('div');
			con.className = mod_cell_content;
				
			if (new_cell.content == true) {
				mod.appendChild(con);
				const check = document.createElement('div');
				check.className = 'skill-check';
				con.appendChild(check)
			} else {
				con.innerHTML = new_cell.content;
				mod.appendChild(con);
			}
		}
		
	}

	
	check_buttons(table_id, object, table);

}

function check_buttons(table_id, object, table) {
	console.log(object)
	const check_button_class = table_id + '-button'
	const mod_class = table_id + '-mod';
	const entry_class = table_id + '-row';

	const entries = document.getElementsByClassName(entry_class)
	const btns = document.getElementsByClassName(check_button_class);
	const mods = document.getElementsByClassName(mod_class);

	for (let i = 0; i < btns.length; i++) {
		const btn = btns[i];
		btn.onclick = function(e) {
			console.log('click');
			console.log(object.mod)
			console.log(object.mod[i])

			const mod = mods[i]
			const entry = mod.parentNode;

			console.log(mod.style.maxHeight);

			if (object.mod[i] == true) {
				mod.style.maxHeight = '0px';
				table.style.maxHeight = table.scrollHeight - mod.scrollHeight + 'px';
				entry.style.maxHeight = entry.scrollHeight - mod.scrollHeight;
				setTimeout(function(){mod.style.display = 'none'}, 400);
				object.mod[i] = false;
			} else {
				mod.style.display = 'grid';
				mod.style.maxHeight = mod.scrollHeight + 'px';
				table.style.maxHeight = table.scrollHeight + mod.scrollHeight + 'px';
				entry.style.maxHeight = entry.scrollHeight + mod.scrollHeight + 'px';
				object.mod[i] = true;
			}

			console.log(mod)
		}
	}
}

function row_delete(jsondata, route, object, selects=false) {
	const table_id = jsondata.table_id;
	const cells = jsondata.cells;
	const rows = object.columns;
	const size = object.font;
	console.log(rows)

	const cells_class = table_id + '-cells';
	const table_class = table_id + '-table'
	const entry_class = table_id + '-row';
	const delete_class = table_id + '-xbox';
	const entry = document.getElementsByClassName(entry_class)
	const all_cells = document.getElementsByClassName(cells_class);
	const deletes = document.getElementsByClassName(delete_class);
	const table_change = document.getElementById(table_class)
	
	const errors = table_id + '-err';
	const err_line = table_id + '-err-line';

	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click');
			
			entry[i].style.maxHeight = '0vw';

			const delId = e.target.dataset['id']
			fetch(route + delId, {
				method: 'DELETE'
			})
			.then(response => response.json())
			.then(jsonResponse => {
			console.log(jsonResponse)
				if (jsonResponse.success) {

					clear_errors(err_line, errors);
					const remove = jsonResponse.id;
					deleted_item(selects, remove)


					console.log(delId)
					console.log(rows)

					for (i = 0; i < rows.length; i++) {
						if (rows[i].id == delId){
							console.log(delId)
							rows.splice(i, 1);
						}
					}

					console.log(rows);

					response = fetch('/power/grid', {
						method: 'POST',
						body: JSON.stringify({
							'font': size,
							'rows': rows
						}),
						headers: {
						'Content-Type': 'application/json',
						}
					})
					.then(response => response.json())
					.then(jsonResponse => {
						console.log(jsonResponse)
						if (jsonResponse.success) {
							const grid = jsonResponse.grid;
							const newsize = jsonResponse.font;
							const columns = jsonResponse.columns;
							console.log(grid)

							if (grid == 'hide') {
								table_change.style.maxHeight = '0px';
								setTimeout(function(){table_change.style.display = 'none'}, 400);
							} else {
								grid__update(columns, cells, table_id, grid, cells_class, newsize, table_change)
							}
						} else {
							console.log('error')
						}
					})
				} else {
					back_errors(err_line, errors, jsonResponse)
				}
			
			})
		}
	}
}

function back_errors(line, table, jsonResponse) {
	const errors_delete = document.getElementsByClassName(line);

	if (typeof errors_delete[0] === "undefined") {
		console.log('no errors defined')
	} else {
		for (i = 0; i < errors_delete.length; i++) {
			errors_delete[i].style.maxHeight = "0px";
			errors_delete[i].style.padding = "0px";
			errors_delete[i].style.marginBottom = "0px";
		};
		setTimeout(function(){
			for (i = 0; i < errors_delete.length; i++) {
				errors_delete[i].style.display = 'none';
			}
		}, 400);
	}


	setTimeout(function(){
		const errors = document.getElementById(table);

		errors.style.display = "grid";
		errors.style.padding = "1%";

		const error_msgs = jsonResponse.error_msgs;
		let li;

		let errors_height = errors.scrollHeight;
		for (li of error_msgs) {
			const error = document.createElement('div');
			error.className = line;
			error.classList.add('err-line');
			error.innerHTML = li;
				
			errors.appendChild(error);
					
			error.style.maxHeight = error.scrollHeight + "px";

			errors_height = errors_height + error.scrollHeight;
			console.log(errors_height)
			errors.style.padding = "1%";	
		}

		errors.style.maxHeight = errors.scrollHeight + errors_height + 20 + 'px';
	}, 420)
}

