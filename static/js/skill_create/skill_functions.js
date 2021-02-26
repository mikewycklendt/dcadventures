


function rule_specific(jsonResponse) {
	console.log('no specific rules');
}

function create_table(rule, jsonResponse, object, route, selects=false, title=false, title_selects=false) {

	const spot_string = jsonResponse.spot;
	const created = jsonResponse.created;
	const id = jsonResponse.id; 
	const title_string = jsonResponse.title;
	const grid = jsonResponse.grid;
	const mods = jsonResponse.mods;
	const cells = jsonResponse.cells;
	const rows = jsonResponse.rows;
	const size = jsonResponse.font;

	const base_header= rule + '-header-'

	let determine_id;
	let determine_title;
	if (title == false) {
		determine_id = jsonResponse.table_id;
		determine_title = base_header + jsonResponse.table_id;
	} else {
		determine_id = jsonResponse.table_id + '-' + title;
		determine_title = base_header + title;
	}
	
	const table_id = determine_id;

	const table_class = table_id + '-table'

	console.log(size);

	console.log(id)

	const cells_class = table_id + '-cells';
	const base_table = rule + '-table-table';
	const base_cell_title = 'skill-table-cell-title ';
	const base_title = rule + '-table-title'
	const base_titles = rule + '-table-titles';	
	console.log(created)


	if (created == false) {

		let grow =  0;

		create_titles(rule, jsonResponse, grow, object, route, selects, title, title_selects);
	
	} else {

		let grow = 0

		
		const table = document.getElementById(table_class)

		cells_create(rule, table, grow, jsonResponse, object, route, selects, title, title_selects);
	}


}

function create_titles(rule, jsonResponse, grow, object, route, selects=false, title=false, title_selects=false) {
	
	const spot_string = jsonResponse.spot;
	const title_string = jsonResponse.title;
	const grid = jsonResponse.grid;
	const cells = jsonResponse.cells;

	const base_header= rule + '-header-'
	
	let determine_id;
	let determine_title;
	if (title == false) {
		determine_id = jsonResponse.table_id;
		determine_title = base_header + jsonResponse.table_id;
	} else {
		determine_id = jsonResponse.table_id + '-' + title;
		determine_title = base_header + title;
	}

	const title_id = determine_title;
	const table_id = determine_id;	
	const cells_class = table_id + '-cells';
	const title_class = table_id + '-title';
	const base_table = rule + '-table-table';
	const base_cell_title = rule + '-table-cell-title';
	const base_title = rule + '-table-title-table';
	const base_titles = rule + '-table-titles';
	
	const table_class = table_id + '-table';

	const spot = document.getElementById(spot_string);
	if (jsonResponse.add_title) {
		const title = document.createElement('div');
		title.className = base_title;
		title.innerHTML = title_string;
		title.setAttribute('id', title_id);
		spot.appendChild(title)
		title.style.maxHeight = title.scrollHeight + 'px';
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

	cells_create(rule, new_table, grow, jsonResponse, object, route, selects, title, title_selects)
	
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

function cells_create(rule, table_input, grow, jsonResponse, object, route, selects=false, title=false, title_selects=false) {

	const table = table_input;
	const id = jsonResponse.id; 
	const grid = jsonResponse.grid;
	const mods = jsonResponse.mods;
	const cells = jsonResponse.cells;
	const size = jsonResponse.font;
	const columns = jsonResponse.columns;

	console.log(size)
	
	let determine_id;
	let determine_title;
	if (title == false) {
		determine_id = jsonResponse.table_id;
	} else {
		determine_id = jsonResponse.table_id + '-' + title;
	}
	
	const table_id = determine_id;

	const table_class = table_id + '-table'


	const cells_class = table_id + '-cells';
	const entry_class = table_id + '-row';
	const delete_class = table_id + '-xbox';
	const check_button_class = table_id + '-button'
	const base_cells = rule + '-table-cells';
	const base_cell = rule + '-table-cell'
	const base_button_check = rule + '-check-button';
	const base_check = rule + '-check';
	const base_entry = rule + '-table-row';
	const base_delete = 'xbox ';
	const base_circ_btn = 'circ-btn';
	const circ_btn_class = table_id + '-circ-btn'

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
	let circ_check = false;
	let cell;
	let cell_heights = [];
	for (cell of cells) {
		const cell_class = table_id + 'cell';
		const new_cell = document.createElement('div');
		new_cell.className = base_cell;
		new_cell.classList.add(cell_class);
		if (cell.content === false) {
			new_cell.innerHTML = '';
		} else if (cell.content === true) {
			if (cell.mod_check == true) {
				create_mod = true;
				const check = document.createElement('div');
				check.className = base_button_check;
				check.classList.add(check_button_class);
				check.setAttribute('data-state', 'closed');
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
			if (cell.circ === true) {
				circ_check = true;
				const circ_btn = document.createElement('div');
				circ_btn.className =  base_circ_btn;
				circ_btn.classList.add(circ_btn_class);
				circ_btn.classList.add('fas')
				circ_btn.setAttribute('data-state', 'closed');
				new_cell.appendChild(circ_btn);
			} else {
				new_cell.innerHTML = cell.content;
				const cell_height = new_cell.scrollHeight;
				cell_heights.push(cell_height);
			}
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
	const delete_btn = document.createElement('div');
	delete_btn.className = base_delete + delete_class;
	delete_btn.classList.add('fas')
	delete_btn.setAttribute('data-id', id);
	delete_cell.appendChild(delete_btn)
	row.appendChild(delete_cell)

	table.style.display = 'grid';
	row.style.maxHeight = row.scrollHeight + 'px';
	grow += row.scrollHeight; 

	if (create_mod) {
		mod_create(rule, mods, id, entry, table_id, table);
	}

	if (circ_check) {
		circ_create(jsonResponse, entry, table_id, table);
	}
	
	grow_table(table, grow)
	
	grid__update(columns, cells, table_id, grid, cells_class, size, table)

	row_delete(rule, jsonResponse, route, object, selects, title, title_selects)
}



function mod_create(rule, mods_input, id_input, entry_input, table_id_input, table) {

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
	const check_div = rule + '-check';
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
				
			if (new_cell.content === true) {
				mod.appendChild(con);
				const check = document.createElement('div');
				check.className = check_div;
				con.appendChild(check)
			} else {
				con.innerHTML = new_cell.content;
				mod.appendChild(con);
			}
		}
		
	}

	
	check_buttons(table_id, table);

}

function circ_create(jsonResponse, entry_input, table_id_input, table) {

	const circs = jsonResponse.circ;
	const entry = entry_input;
	const table_id = table_id_input;

	const circ_class = table_id + '-circ';
	const base_circ = 'circ-row';
	const circ_cell_empty = 'circ-cell-empty';
	const circ_title = 'circ-cell-title';
	const entry_class = table_id + '-row';

	const entries = document.getElementsByClassName(entry_class);

	let circ;
	for (circ of circs) {
		const circ_row = document.createElement('div');
		circ_row.className = circ_class;
		circ_row.classList.add(base_circ);
		entry.appendChild(circ_row);
		
		const empty = document.createElement('div');
		empty.className = circ_cell_empty;
		circ_row.appendChild(empty);

		const title = document.createElement('div');
		title.className = circ_title;
		title.innerHTML = circ.title;
		circ_row.appendChild(title);
		console.log(circ.title)

		const content = document.createElement('div');
		content.className = 'circ-cell-circ';
		content.innerHTML = circ.content;
		circ_row.appendChild(content)
		console.log(circ.content)
	}
	
	circ_button(table_id, table);
}

function circ_button(table_id, table) {
	
	const circ_class = table_id + '-circ';
	const entry_class = table_id + '-row';
	const circ_btn_class = table_id + '-circ-btn'

	const entries = document.getElementsByClassName(entry_class)
	const btns = document.getElementsByClassName(circ_btn_class);
	const circs = document.getElementsByClassName(circ_class);

	for (let i = 0; i < btns.length; i++) {
		const btn = btns[i];
		btn.onclick = function(e) {
			console.log('click');

			const circ = circs[i]
			const entry = circ.parentNode;

			const status = btn.getAttribute('data-state');
			console.log(status);
			if (status == 'open') {
				btn.style.opacity = '0%';
				setTimeout(function(){
					btn.style.opacity = '100%'
					btn.classList.remove('circ-btn-up');
					btn.classList.add('circ-btn')
					}, 100);
				circ.style.maxHeight = '0px';
				table.style.maxHeight = table.scrollHeight - circ.scrollHeight + 'px';
				entry.style.maxHeight = entry.scrollHeight - circ.scrollHeight;
				setTimeout(function(){circ.style.display = 'none'}, 400);
				btn.setAttribute('data-state', 'closed');
			} else {
				btn.style.opacity = '0%';
				setTimeout(function(){
					btn.style.opacity = '100%'
					btn.classList.remove('circ-btn');
					btn.classList.add('circ-btn-up');
				}, 100);
				circ.style.display = 'grid';
				circ.style.maxHeight = circ.scrollHeight + 'px';
				table.style.maxHeight = table.scrollHeight + circ.scrollHeight + 'px';
				entry.style.maxHeight = entry.scrollHeight + circ.scrollHeight + 'px';
				btn.setAttribute('data-state', 'open');
			}
		}
	}
}

function check_buttons(table_id, table) {

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

			const mod = mods[i]
			const entry = mod.parentNode;
			const state = btn.getAttribute('data-state');
			console.log(mod.style.maxHeight);

			if (state == 'open') {
				mod.style.maxHeight = '0px';
				table.style.maxHeight = table.scrollHeight - mod.scrollHeight + 'px';
				entry.style.maxHeight = entry.scrollHeight - mod.scrollHeight;
				setTimeout(function(){mod.style.display = 'none'}, 400);
				btn.setAttribute('data-state', 'closed');
			} else {
				mod.style.display = 'grid';
				mod.style.maxHeight = mod.scrollHeight + 'px';
				table.style.maxHeight = table.scrollHeight + mod.scrollHeight + 'px';
				entry.style.maxHeight = entry.scrollHeight + mod.scrollHeight + 'px';
				btn.setAttribute('data-state', 'open')
			}

			console.log(mod)
		}
	}
}

function row_delete(rule, jsondata, route, object, selects=false, title=false, title_selects=false) {

	const cells = jsondata.cells;
	const size = object.font;
	
	let which_table; 
	if (title == false) {
		which_table = object.columns;
	} else {
		let the_table;
		const the_tables = object.columns;
		for (the_table of the_tables) {
			if (the_table.id == title) {
				which_table = the_table.rows;
			}
		}
	}
	
	const rows = which_table;
	console.log(rows)
	
	const base_header= rule + '-header-'
	
	let determine_id;
	let determine_title;
	if (title == false) {
		determine_id = jsondata.table_id;
		determine_title = base_header + jsondata.table_id;
	} else {
		determine_id = jsondata.table_id + '-' + title;
		determine_title = base_header + title;
	}

	const header_id = determine_title;
	const table_id = determine_id;	

	const cells_class = table_id + '-cells';
	const table_class = table_id + '-table'
	const entry_class = table_id + '-row';
	const delete_class = table_id + '-xbox';
	const entry = document.getElementsByClassName(entry_class)
	const all_cells = document.getElementsByClassName(cells_class);
	const deletes = document.getElementsByClassName(delete_class);
	const table_change = document.getElementById(table_class)
	const header = document.getElementById(header_id)	
	const errors = jsondata.table_id + '-err';
	const err_line = jsondata.table_id + '-err-line';

	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click');
			

			const delId = e.target.dataset['id']
			fetch(route + delId, {
				method: 'DELETE'
			})
			.then(response => response.json())
			.then(jsonResponse => {
			console.log(jsonResponse)
				if (jsonResponse.success) {

					const hide_table = jsonResponse.hide_table;
					const title_id = jsonResponse.title_id;

					clear_errors(err_line, errors);

					rule_specific(jsonResponse);

					const remove = jsonResponse.id;
					deleted_item(selects, remove)
	
					entry[i].style.maxHeight = '0vw';

					console.log(delId)
					console.log(rows)

					for (i = 0; i < rows.length; i++) {
						if (rows[i].id == delId){
							console.log(delId)
							rows.splice(i, 1);
						}
					}

					if (title != false) {
						const tables = object.columns;
						for (i = 0; i < tables.length; i++) {
							if (tables[i].id == title) {
								object.columns[i].rows = rows;
							}
						}
					} else {
						object.columns = rows;
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

							if (title == false) {
								if (grid == 'hide') {
									table_change.style.maxHeight = '0px';
									setTimeout(function(){table_change.style.display = 'none'}, 400);
								} else {
									grid__update(columns, cells, table_id, grid, cells_class, newsize, table_change)
								}
							} else {
								if (hide_table == true) {
									table_change.style.maxHeight = '0px';
									setTimeout(function(){table_change.style.display = 'none'}, 400);
									header.style.maxHeight = '0px';
									setTimeout(function(){header.style.display = 'none'}, 400);
									deleted_item(title_selects, title_id);
								} else {
									grid__update(columns, cells, table_id, grid, cells_class, newsize, table_change)
								}
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

