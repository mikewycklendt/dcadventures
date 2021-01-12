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



function trait_select(select, fill) {
	const field = document.getElementById(select)
	const trait = field.options[field.selectedIndex].value
	const update = document.getElementById(fill);

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

	response = fetch('/advantage/trait/select', {
		method: 'POST',
		body: JSON.stringify({
			'trait': trait
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

function level_select(select, fill) {
	const field = document.getElementById(select)
	const level_type_id = field.options[field.selectedIndex].value
	const update = document.getElementById(fill);

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

	response = fetch('/power/level/select', {
		method: 'POST',
		body: JSON.stringify({
			'level_type_id': level_type_id
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

function action_select(select, fill) {
	const field = document.getElementById(select)
	const action = field.options[field.selectedIndex].value
	const update = document.getElementById(fill);

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

	response = fetch('/advantage/action/select', {
		method: 'POST',
		body: JSON.stringify({
			'action': action
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


function subsense_select(select, fill) {
	const field = document.getElementById(select);
	const sense_id = field.options[field.selectedIndex].value;
	const update = document.getElementById(fill);

	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 200)

	response = fetch('/sense/subsense/select', {
		method: 'POST',
		body: JSON.stringify({
			'sense_id': sense_id
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


function select_opacity_any(select, div) {
	const field = document.getElementById(select);
	const val = field.options[field.selectedIndex].value;

	if (val != '') {
		show_opacity(div);
	} else {
		hide_opacity(div);
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


function double_select_second(selects, row, entry) {

	for (s of selects) {
		const select1 = s.select1;
		const select2 = s.select2;
		const options = s.options;
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
}


function double_select_secondary(options, row, entry) {
	let o;
	let grown = false;
	let grow = false;
	let div	
	let shrink = true;
	let start = false;

	for (o of options) {
		const select1 = o.select1;
		const select2 = o.select2;
		const field1 = document.getElementById(select1);
		const value1 = field1.options[field1.selectedIndex].value;
		const field2 = document.getElementById(select2);
		const value2 = field2.options[field2.selectedIndex].value;
		const old1 = field1.getAttribute('previousValue');
		field1.setAttribute('previousValue', value1);
	
		let val = o.val
		if (value1 == val) {
			start = true
		}

		if (old1 == val) {
			start = true;
		}

		if (value2 == val) {
			start = true;
		}
	}

	console.log(start)

	if (start == true) { 
		for (o of options) {
			const sel1 = o.select1;
			const sel2 = o.select2;
			const fi1 = document.getElementById(sel1);
			const val1 = fi1.options[fi1.selectedIndex].value;
			const fi2 = document.getElementById(sel2);
			const val2 = fi2.options[fi2.selectedIndex].value;
			const old1 = field1.getAttribute('previousValue');
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
		
			let option;

		for (option of options) {
			const s1 = o.select1;
			const f1 = document.getElementById(s1);
			const v1 = f1.options[f1.selectedIndex].value;
			let valu = option.val;
			let di = option.div;

			if (shrink == false) {
				if (v1 != valu) {
					hide_opacity(di);
				} else {
					show_opacity(di);
				}
			} else {
				if (v1 != valu) {
					hide_opacity(di)
				}

				hide_maxheight(row)
				shrink_entry(entry, div)
			}
		}
	} else {
		console.log('nothing')
	}
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

function base(field_input, entry_input) {
	const field = document.getElementById(field_input)
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById(entry_input)

	if (value != '') {
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

function base_multiple(field_inputs, entry_input) {
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


function base_multiple_text(field_inputs, textfield_input, entry_input) {
	const entry = document.getElementById(entry_input);
	const textfield = document.getElementById(textfield_input);
	const text = textfield.value;

	let satisfied = true
	let field;
	for (field of field_inputs) {
		const f = document.getElementById(field);
		const select = f.options[f.selectedIndex].value;

		if (select == '') {
			satisfied = false
		}
	} 

	if (text == '') {
		satisfied = false
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

function entry_check(check_input, title_input, base_input, entry_input) {
	const check = document.getElementById(check_input);
	const entry = document.getElementById(entry_input);
	const title = document.getElementById(title_input);
	const base = document.getElementById(base_input)
	
	if (check.checked == true) {
		base.style.opacity = '100%'
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		title.style.color = "#af0101";
		title.style.fontSize = "207%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = '0%'
		entry.style.maxHeight = "0px";
		setTimeout(function(){entry.style.display = 'none';}, 400);
		title.style.color = "#245681";
	}
}

function base_two(field_input, field2_input, entry_input) {
	const field = document.getElementById(field_input);
	const value = field.options[field.selectedIndex].value;
	
	const field2 = document.getElementById(field2_input);
	const target = field2.options[field2.selectedIndex].value;
	const entry = document.getElementById(entry_input);

	if (value != '' && target != '') {
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

function base_text(field_input, text_input, entry_input) {
	const field = document.getElementById(field_input);
	const value = field.options[field.selectedIndex].value;
	const type = document.getElementById(text_input).value;
	const entry = document.getElementById(entry_input);

	if (value != '' && type != '') {
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


function base_only_text(text_input, entry_input) {
	const type = document.getElementById(text_input).value;
	const entry = document.getElementById(entry_input);

	if (type != '') {
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

function check_title(check_input, title_input, base_input, entry_input) {
	const check = document.getElementById(check_input);
	const title = document.getElementById(title_input);
	const base = document.getElementById(base_input);
	const entry = document.getElementById(entry_input);

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function check_title_small(check_input, title_input, base_input, entry_input) {
	const check = document.getElementById(check_input);
	const title = document.getElementById(title_input);
	const base = document.getElementById(base_input);
	const entry = document.getElementById(entry_input);

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "165%";
		setTimeout(function(){title.style.fontSize = "160%"}, 75);
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

advantage_create = function() {
	const advantage_name = document.getElementById('advantage_name').value;
	const add_advantage = document.getElementById('add-advantage');
	const edit_button = document.getElementById('edit-button');

	response = fetch('/advantage/create', {
		method: 'POST',
		body: JSON.stringify({
		  'name': advantage_name,
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
			const name_div = document.getElementById('advantage-name');
			const advantage_id = document.getElementById('advantage_id');
			name_div.innerHTML = jsonResponse.name;
			advantage_id.value = jsonResponse.id;
			name_div.style.display = "block"
			name_div.style.opacity = "100%"
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);
			edit_button.style.display = "block";
			add_advantage.style.display = "none";
			all_fields.style.display = "grid";
			setTimeout(function(){all_fields.style.opacity = "100%"}, 10);

			errors_delete = document.getElementsByClassName('name-err-line');

			if (typeof errors_delete[0] === "undefined") {
				console.log('no errors defined')
			} else {
				for (i = 0; i < errors_delete.length; i++) {
					errors_delete[i].style.maxHeight = "0px";
					errors_delete[i].style.padding = "0px";
					errors_delete[i].style.marginBottom = "0px";
				}

			errors = document.getElementById('name-err')

				errors.style.display = "none";
				errors.style.padding = "0px";
				errors.style.maxHeight = "0px";
			}

		} else {
			const errors = document.getElementById('name-err');
			errors.style.display = "grid";

			const error_msgs = jsonResponse.error
			let i;

			for (i of error_msgs) {
				const error = document.createElement('div');
				error.className = 'name-err-line';
				error.innerHTML = i;
		
				errors.appendChild(error);
			
				error.style.maxHeight = error.scrollHeight + "px";

				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";
			}
		}
	})
}

edit_form = function() {
	const advantage_id = document.getElementById('advantage_id').value;
	const edit_field = document.getElementById('advantage_name_edit');
	const name = document.getElementById('advantage-name').innerHTML;
	const edit_grid = document.getElementById('advantage-edit-grid');

	edit_field.value = name;
	edit_grid.style.display = "grid";
	edit_grid.style.maxHeight = edit_grid.scrollHeight + "px";
	edit_grid.style.padding = "1%";
}

power_edit = function() {
	const id = document.getElementById('advantage_id').value;
	const name = document.getElementById('advantage_name_edit').value;
	
	response = fetch('/advantage/edit_name', {
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
			const name_div = document.getElementById('advantage-name');
			const edit_grid = document.getElementById('advantage-edit-grid');
			edit_grid.style.display = "none";
			name_div.innerHTML = jsonResponse.name;
			name_div.style.fontSize = "460%";
			setTimeout(function(){name_div.style.fontSize = "400%"}, 75);

			errors_delete = document.getElementsByClassName('name-err-line');

			if (typeof errors_delete[0] === "undefined") {
				console.log('no errors defined')
			} else {
				for (i = 0; i < errors_delete.length; i++) {
					errors_delete[i].style.maxHeight = "0px";
					errors_delete[i].style.padding = "0px";
					errors_delete[i].style.marginBottom = "0px";
				}

			errors = document.getElementById('name-err')

				errors.style.display = "none";
				errors.style.padding = "0px";
				errors.style.maxHeight = "0px";
			}

		} else {
			const errors = document.getElementById('name-err');
			errors.style.display = "grid";

			const error_msgs = jsonResponse.error
			let i;

			for (i of error_msgs) {
				const error = document.createElement('div');
				error.className = 'name-err-line';
				error.innerHTML = i;
		
				errors.appendChild(error);
			
				error.style.maxHeight = error.scrollHeight + "px";

				errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
				errors.style.padding = "1%";	
			}
		}
	})
}

advantage_save = function() {

	const advantage_id = document.getElementById('advantage_id').value;

	const errors = 'advantage-err';
	const err_line = 'advantage-err-line';

	response = fetch('/advantage/save', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			
		}),
		headers: {
		'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			window.location.replace('/advantage/save/success/' + power_id)

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}



function create_table(jsonResponse, object, route) {

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
	const base_table = 'power-table-table';
	const base_cell_title = 'power-table-cell-title ';
	const base_title = 'power-table-title'
	const base_titles = 'power-table-titles';

	
	console.log(created)


	if (created == false) {

		let grow =  0;

		create_titles(jsonResponse, grow, object, route);
	
	} else {

		let grow = 0

		const table = document.getElementById(table_class)

		cells_create(table, grow, jsonResponse, object, route);
	}


}

function create_titles(jsonResponse, grow, object, route) {
	
	const spot_string = jsonResponse.spot;
	const table_id = jsonResponse.table_id;
	const title_string = jsonResponse.title;
	const grid = jsonResponse.grid;
	const cells = jsonResponse.cells;

	const cells_class = table_id + '-cells';
	const table_class = table_id + '-table';
	const title_class = table_id + '-title';
	const base_table = 'power-table-table';
	const base_cell_title = 'power-table-cell-title';
	const base_title = 'power-table-title-table';
	const base_titles = 'power-table-titles';

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

	cells_create(new_table, grow, jsonResponse, object, route)
	
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

function cells_create(table_input, grow, jsonResponse, object, route) {

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
	const base_cells = 'power-table-cells';
	const base_cell = 'power-table-cell'
	const base_button_check = 'power-check-button ';
	const base_check = 'power-check';
	const base_entry = 'power-table-row';
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
		} else if (cell.content == true) {
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

	row_delete(jsonResponse, route, object) 
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
				check.className = 'power-check';
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

function row_delete(jsondata, route, object) {
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

	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click');
			
			entry[i].style.maxHeight = '0vw';

			const delId = e.target.dataset['id']
			fetch(route + delId, {
				method: 'DELETE'
			})
			.then(function() {

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


function clear_errors(line, div) {
	const errors_delete = document.getElementsByClassName(line);
	const errors = document.getElementById(div);

	errors.style.maxHeight = "0px";
	errors.style.padding = "0px";

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
				errors.style.display = 'none';
			}
		}, 400);

	}
}

