function pre_check_check() {
	const pre_check_check = document.getElementById("pre_check_check");
	const pre_check_header_type = document.getElementById("pre-check-header-type");
	
	if (pre_check_check.checked == true) {
		pre_check_header_type.style.opacity = "100%";
	} else {
		pre_check_header_type.style.opacity = "0%";
	}
}

function pre_check_entry() {
	pre_check_type = document.getElementById("pre_check_type")
	pre_check_type_value = pre_check_type.options[pre_check_type.selectedIndex].value;
	console.log(pre_check_type_value)
	pre_check_entry_standard = document.getElementById("pre-check-entry-standard")
	pre_check_entry_opposed = document.getElementById("pre-check-entry-opposed")

	if (pre_check_type_value == 'skill') {
		pre_check_entry_standard.style.display = "grid";
		pre_check_entry_standard.style.padding = "1%";
		pre_check_entry_standard.style.maxHeight = pre_check_entry_standard.scrollHeight + "px";
		pre_check_entry_standard.style.padding = "1%";

		pre_check_entry_opposed.style.display = "none";
		pre_check_entry_opposed.style.padding = "0%";
		pre_check_entry_opposed.style.maxHeight = "0px"
	} else if (pre_check_type_value == 'opposed') {
		pre_check_entry_standard.style.display = "none";
		pre_check_entry_standard.style.padding = "0%";
		pre_check_entry_standard.style.maxHeight = "0px";

		pre_check_entry_opposed.style.display = "grid";
		pre_check_entry_opposed.style.padding = "1%";
		pre_check_entry_opposed.style.maxHeight = pre_check_entry_opposed.scrollHeight + "px";
		pre_check_entry_opposed.style.padding = "1%";
	} else {
		pre_check_entry_opposed.style.display = "none";
		pre_check_entry_standard.style.display = "none";

	}
}

standard_enter = 0;

function pre_check_standard_submit() {
	const standard_table = document.getElementById('pre-check-table-standard');

	standard_table.style.display = "grid";
	standard_table.style.padding = "1%";
	standard_table.style.maxHeight = standard_table.scrollHeight + "px";
	standard_table.style.padding = "1%";
	
	let standard_circ_value = document.getElementById('pre_check_circ').value;
	let standard_when_field = document.getElementById('pre_check_when');
	let standard_skill_field = document.getElementById('pre_check_skill');
	let standard_when_value =  standard_when_field.options[standard_when_field.selectedIndex].value; 
	let standard_skill_value =  standard_skill_field.options[standard_skill_field.selectedIndex].value; 

	console.log(standard_circ_value);
	console.log(standard_when_value);
	console.log(standard_skill_value);
	
	if (standard_skill_value != '' && standard_circ_value != '' && standard_when_value != '') {

		const skill = document.createElement('div');
		skill.className = 'pre-check-table-skill'
		skill.innerHTML = standard_skill_value;

		const when = document.createElement('div');
		when.className = 'pre-check-table-when'
		when.innerHTML = standard_when_value;

		const circ = document.createElement('div');
		circ.className = 'pre-check-table-circ'
		circ.innerHTML = standard_circ_value;
	
		const standardDelete = document.createElement('div');
		standardDelete.className = 'pre-check-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'pre-check-standard-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', standard_enter);
		standardDelete.appendChild(deleteBtn);

		standard_enter = standard_enter + 1;
	
		standard_table.appendChild(when);
		standard_table.appendChild(skill);
		standard_table.appendChild(circ);

		standard_table.appendChild(standardDelete);

		
		skill.style.maxHeight = skill.scrollHeight + "px";
		when.style.maxHeight = when.scrollHeight + "px";
		circ.style.maxHeight = circ.scrollHeight + "px";
		standardDelete.style.maxHeight = standardDelete.scrollHeight + "px";
		standard_table.style.maxHeight = standard_table.scrollHeight + 20 + "px";

		pre_check_standard_delete()
	}
};

pre_check_standard_delete = function() {
	const deletes = document.querySelectorAll('.pre-check-standard-xbox');
	const skills = document.getElementsByClassName('pre-check-table-skill');
	const circs = document.getElementsByClassName('pre-check-table-circ');
	const whens = document.getElementsByClassName('pre-check-table-when');
	const deletesDiv = document.getElementsByClassName('pre-check-table-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
			skills[i].style.maxHeight = "0px";
			skills[i].style.padding = "0px";
			skills[i].style.marginBottom = "0px";
			circs[i].style.maxHeight = "0px";
			circs[i].style.padding = "0px";
			circs[i].style.marginBottom = "0px";
			whens[i].style.maxHeight = "0px";
			whens[i].style.padding = "0px";
			whens[i].style.marginBottom = "0px";
			deletesDiv[i].style.maxHeight = "0px";
			deletesDiv[i].style.padding = "0px";
			deletesDiv[i].style.marginBottom = "0px";
		}
	}
};

pre_check_standard_delete();

opposed_enter = 0;

function pre_check_opposed_submit() {
	const opposed_table = document.getElementById('pre-check-table-opposed');

	opposed_table.style.display = "grid";
	opposed_table.style.padding = "1%";
	opposed_table.style.maxHeight = opposed_table.scrollHeight + "px";
	opposed_table.style.padding = "1%";
	
	let opposed_circ_value = document.getElementById('pre_check_opposed_circ').value;
	let opposed_when_field = document.getElementById('pre_check_opposed_when');
	let opposed_skill_field = document.getElementById('pre_check_opposed_skill');
	let opposed_field = document.getElementById('pre_check_opposed');
	let opposed_when_value =  opposed_when_field.options[opposed_when_field.selectedIndex].value; 
	let opposed_skill_value =  opposed_skill_field.options[opposed_skill_field.selectedIndex].value;
	let opposed_value =  opposed_field.options[opposed_field.selectedIndex].value; 

	console.log(opposed_circ_value);
	console.log(opposed_when_value);
	console.log(opposed_skill_value);
	console.log(opposed_value);
	
	if (opposed_skill_value != '' && opposed_circ_value != '' && opposed_when_value != '' && opposed_value != '') {

		const skill = document.createElement('div');
		skill.className = 'pre-check-table-opposed-skill'
		skill.innerHTML = opposed_skill_value;

		const when = document.createElement('div');
		when.className = 'pre-check-table-opposed-when'
		when.innerHTML = opposed_when_value;
		
		const opposed = document.createElement('div');
		when.className = 'pre-check-table-opposedby'
		when.innerHTML = opposed_value;

		const circ = document.createElement('div');
		circ.className = 'pre-check-table-opposed-circ'
		circ.innerHTML = opposed_circ_value;
	
		const opposedDelete = document.createElement('div');
		opposedDelete.className = 'pre-check-table-opposed-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'pre-check-opposed-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', opposed_enter);
		opposedDelete.appendChild(deleteBtn);

		opposed_enter = opposed_enter + 1;
	
		opposed_table.appendChild(when);
		opposed_table.appendChild(skill);
		opposed_table.appendChild(opposed);
		opposed_table.appendChild(circ);

		opposed_table.appendChild(opposedDelete);

		
		skill.style.maxHeight = skill.scrollHeight + "px";
		when.style.maxHeight = when.scrollHeight + "px";
		circ.style.maxHeight = circ.scrollHeight + "px";
		opposed.style.maxHeight = opposed.scrollHeight + "px";
		opposedDelete.style.maxHeight = opposedDelete.scrollHeight + "px";
		opposed_table.style.maxHeight = opposed_table.scrollHeight + 20 + "px";

		pre_check_opposed_delete()
	}
};

pre_check_opposed_delete = function() {
	const deletes = document.querySelectorAll('.pre-check-opposed-xbox');
	const skills = document.getElementsByClassName('pre-check-table-opposed-skill');
	const circs = document.getElementsByClassName('pre-check-table-opposed-circ');
	const whens = document.getElementsByClassName('pre-check-table-opposed-when');
	const opposeds = document.getElementsByClassName('pre-check-table-opposedby');
	const deletesDiv = document.getElementsByClassName('pre-check-table-opposed-delete');
	for (let i = 0; i < deletes.length; i++) {
		const btn = deletes[i];
		btn.onclick = function(e) {
			console.log('click')
			skills[i].style.maxHeight = "0px";
			skills[i].style.padding = "0px";
			skills[i].style.marginBottom = "0px";
			circs[i].style.maxHeight = "0px";
			circs[i].style.padding = "0px";
			circs[i].style.marginBottom = "0px";
			whens[i].style.maxHeight = "0px";
			whens[i].style.padding = "0px";
			whens[i].style.marginBottom = "0px";
			opposeds[i].style.maxHeight = "0px";
			opposeds[i].style.padding = "0px";
			opposeds[i].style.marginBottom = "0px";
			deletesDiv[i].style.maxHeight = "0px";
			deletesDiv[i].style.padding = "0px";
			deletesDiv[i].style.marginBottom = "0px";
		}
	}
};

pre_check_opposed_delete();