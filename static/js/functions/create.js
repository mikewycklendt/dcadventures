


function null_hide_maxheight(field, item) {
	val = select(field);

	if (val == '' ) {
		hide_maxheight(item);
		shrink_entry(entry, item);
	}
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

function uncheck_all(checks_input) {
	let checks;
	for (checks of checks_input){
		const check = document.getElementById(checks)

		check.checked = false;
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

function select_maxheight_shared(select, options, entry) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;
	const adiv = options[0].div;

	let any_match = false;

	console.log(val);

	for (option of options) {
		const values = option.val;
		const div = option.div;
		let match = false;
		let value;
		for (value of values) {
			if (val == value) {
				match  = true;
				any_match = true;
			}
		}
		if (match == true) {
			show_maxheight(div);
		} else {
			hide_maxheight(div);
		}	
	};

	if (any_match == false) {
		shrink_entry(entry, adiv)
	} else {
		for (option of options) {
			const values = option.val;
			const div = option.div;
			let match = false;
			let value;
			for (value of values) {
				if (val == value) {
					match  = true;
					any_match = true;
				}
			}
			if (match == true) {
				grow_entry(entry, div); 
			}
		}
	}
}


function select_opacity_shared(select, options) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;
	let option;
	const adiv = options[0].div;

	let any_match = false;

	console.log(val);

	for (option of options) {
		const values = option.val;
		const div = option.div;
		let match = false;
		let value;
		for (value of values) {
			if (val == value) {
				match  = true;
				any_match = true;
			}
		}
		if (match == true) {
			show_opacity(div);
		} else {
			hide_opacity(div);
		}	
	};
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

function select_maxheight_any_entry(select, div, entry) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;

	if (val == '') {
		hide_maxheight(div);
	} else {
		show_maxheight(div);
	}

	if (val == '') {
		shrink_entry(entry, adiv);
	} else {
		grow_entry(entry, div);
	}
	
}

function select_maxheight_any(select, div) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;

	if (val == '') {
		hide_maxheight(div);
	} else {
		show_maxheight(div);
	}

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
	const select = document.getElementById(multiple_input);
	let values = [];
	const options = select.options;
	let o;

	for (o of options) {
		if (o.selected) {
			values.push(o.value);
 		}
	}

	return values;
}

function div_text(select_input, div_input, options) {
	const div = document.getElementById(div_input)
	const value = select(select_input);
	let o;

	div.style.opacity = '0%';

	setTimeout(function(){
		for (o of options) {
			const val = o.val;
			const text = o.text; 
	
			if (val == value) {
				div.innerHTML = text;
			}
		}
		div.style.opacity = '100%';
	}, 300)	
}


function div_text_multiple(select_input, options) {
	const value = select(select_input);
	let o;

	for (o of options) {
		const val = o.val;
		const div = document.getElementById(o.div);

		if (val == value) {
			div.style.opacity = '0%';
		}
	}

	setTimeout(function(){
		for (o of options) {
			const val = o.val;
			const text = o.text; 
			const div = document.getElementById(o.div);
	
			if (val == value) {
				div.innerHTML = text;
				div.style.opacity = '100%';
			}
		}
	}, 300)	
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

function selects_add_new(id, name, selects) {
	
	let div;
	let add = true;
	for (div of selects) {
		const selects = document.getElementsByClassName(div);
		let select;

		for (select of selects) {
			options = select.options;
			let option;

			for (option of options) {
				if (option.value == id) {
					add = false
				}
			}
		}
	}

	if (add == true) {
		selects_add(id, name, selects);
	}

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
