function other_check() {
	const other_check = document.getElementById("other_check");
	const other_entry = document.getElementById("other-entry");
	
	if (other_check.checked == true) {
		other_entry.style.display = "grid";
		other_entry.style.padding = "1%";
		other_entry.style.maxHeight = other_entry.scrollHeight + "px";
		other_entry.style.padding = "1%";
	} else {
		other_entry.style.maxHeight = "0px";
		other_entry.style.padding = "0px";
	}
}

other_enter = 0;

function other_submit() {
	const table = document.getElementById('other-table');

	table.style.display = "grid";
	table.style.padding = "1%";
	table.style.maxHeight = table.scrollHeight + "px";
	table.style.padding = "1%";
	
	let examples_value = document.getElementById('other_examples').value;
	let skill_field = document.getElementById('other_skill');
	let skill_value =  skill_field.options[skill_field.selectedIndex].value; 

	console.log
	
	if (skill_value != '' && examples_value != '') {

		const skill = document.createElement('div');
		skill.className = 'other-table-skill'
		skill.innerHTML = skill_value;

		const examples = document.createElement('div');
		examples.className = 'other-table-examples'
		examples.innerHTML = examples_value;
	
		const otherDelete = document.createElement('div');
		otherDelete.className = 'other-table-delete'
		const deleteBtn = document.createElement('button');
		deleteBtn.className = 'other-xbox';
		deleteBtn.innerHTML = '&cross;';
		deleteBtn.setAttribute('data-id', other_enter);
		otherDelete.appendChild(deleteBtn);

		other_enter = other_enter + 1;
	
		table.appendChild(skill);
		table.appendChild(examples);
		table.appendChild(otherDelete);

		table.style.maxHeight = table.scrollHeight + "px";
		skill.style.maxHeight = skill.scrollHeight + "px";
		examples.style.maxHeight = examples.scrollHeight + "px";
		otherDelete.style.maxHeight = otherDelete.scrollHeight + "px";
	}
}