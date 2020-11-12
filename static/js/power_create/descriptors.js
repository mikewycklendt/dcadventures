	
function descriptor_opacity(value, div) {
	if (value == 'new') {
		div.style.opacity = '100%;'
	} else {
		div.style.opacity = '0%';
	}
}

function get_mediums(medium_type, type_id, update) {
	update.innerText = null;

	update.style.backgroundColor = 'lightblue';
	setTimeout(function(){update.style.backgroundColor = "white"}, 100)

	response = fetch('/power/trait/select', {
		method: 'POST',
		body: JSON.stringify({
			'medium_type': medium_type,
			'type_id': type_id
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
				o.value = option;
				o.text = option;
				update.add(o);
			}

		} else {
			console.log(jsonResponse.options);
		}
	})	
}

function descriptor_des(value, div) {
	if (value == 'new') {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px'
		row3.style.maxHeight = div.scrollHeight + row3.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		setTimeout(function(){div.style.display = 'none'}, 400);
	}
}

function medium_type_show(div1, div2) {
	div1.style.display = 'grid';
	setTimeout(function(){div1.style.opacity = '100%'}, 10);
	div2.style.display = 'grid';
	setTimeout(function(){div2.style.opacity = '100%'}, 10);
}

function medium_type_hide(div3, div4) {
	div3.style.display = 'none';
	div3.style.opacity = '0%';
	div4.style.display = 'none';
	div4.style.opacity = '0%';
}

function descriptor() {
	const origin_field  = document.getElementById('descriptor_origin');
	const origin = origin_field.options[origin_field.selectedIndex].value;

	const source_field  = document.getElementById('descriptor_source');
	const source = source_field.options[source_field.selectedIndex].value;

	const medium_type_field  = document.getElementById('descriptor_medium_type');
	const medium_type = medium_type_field.options[medium_type_field.selectedIndex].value;

	const material_type_field  = document.getElementById('descriptor_material_type');
	const material_type = material_type_field.options[material_type_field.selectedIndex].value;

	const energy_type_field  = document.getElementById('descriptor_energy_type');
	const energy_type = energy_type_field.options[energy_type_field.selectedIndex].value;

	const medium_field  = document.getElementById('descriptor_medium');
	const medium = medium_field.options[medium_field.selectedIndex].value;

	const descriptor_field  = document.getElementById('descriptor_field');
	const descriptor = descriptor_field.options[descriptor_field.selectedIndex].value;

	const origin_name = document.getElementById('descriptor_origin_name').value;
	const source_name = document.getElementById('descriptor_source_name').value;
	const medium_type_name = document.getElementById('descriptor_medium_type_name').value;
	const material_type_name = document.getElementById('descriptor_material_type_name').value;
	const energy_type_name = document.getElementById('descriptor_energy_type_name').value;
	const medium_name = document.getElementById('descriptor_medium_name').value;
	const descriptor_name = document.getElementById('descriptor_name').value;

	const origin_des = document.getElementById('descriptor_origin_des').value;
	const source_des = document.getElementById('descriptor_source_des').value;
	const medium_type_des = document.getElementById('descriptor_medium_type_des').value;
	const medium_des = document.getElementById('descriptor_medium_des').value;
	const descriptor_result = document.getElementById('descriptor_result').value;

	const ene_title_row1 = document.getElementById('descriptor-energy-title');
	const mat_title_row1 = document.getElementById('descriptor-material-title');
	const ene_row1 = document.getElementById('descriptor-energy');
	const mat_row1 = document.getElementById('descriptor-material');
	const med_title_row1 = document.getElementById('descriptor-medium-title');
	const des_title_row1 = document.getElementById('descriptor-field-title');
	const med_row1 = document.getElementById('descriptor-medium');
	const des_field = document.getElementById('descriptor-field');

	const ori_text = document.getElementById('descriptor-origin-field');
	const sou_text = document.getElementById('descriptor-source-field');
	const typ_text = document.getElementById('descriptor-medium-type-field');
	const med_text = document.getElementById('descriptor-medium-field');
	const des_text = document.getElementById('descriptor-new');

	const type_des_title = document.getElementById('descriptor-medium-type-des-title');

	const ori_des = document.getElementById('descriptor-origin-des');
	const sou_des = document.getElementById('descriptor-source-des');
	const typ_des = document.getElementById('descriptor-medium-type-des');
	const med_des = document.getElementById('descriptor-medium-des');
	const des_des = document.getElementById('descriptor-descriptor-result');

	const row2 = document.getElementById('descriptor-row2');
	const row3 = document.getElementById('descriptor-row3');

	if (origin == 'new' || source == 'new' || material_type == 'new' || energy_type ==  'new' || medium == 'new' || descriptor == 'new') {
		row2.style.display = 'grid';
		row2.style.maxHeight = row2.scrollHeight + 'px';
		row3.style.display = 'grid';
		row3.style.maxHeight = row3.scrollHeight + 'px';
	}

	if (origin != 'new' && source != 'new' && material_type != 'new' && energy_type !=  'new' && medium != 'new' && descriptor != 'new') {
		row2.style.display = 'grid';
		row2.style.maxHeight = row2.scrollHeight + 'px';
		row3.style.display = 'grid';
		row3.style.maxHeight = row3.scrollHeight + 'px';
	}

	descriptor_opacity(origin, ori_text);
	descriptor_des(origin, origin_des);
	descriptor_opacity(source, sou_text);
	descriptor_des(source, sou_des);
	descriptor_opacity(material_type, typ_text);
	descriptor_des(material_type, typ_des);
	descriptor_opacity(energy_type, typ_text);
	descriptor_des(energy_type, typ_des);
	descriptor_opacity(medium, med_text);
	descriptor_des(medium, med_des);
	descriptor_opacity(descriptor, des_text);
	descriptor_des(descriptor, des_des);

	if (medium_type == 1) { 
		medium_type_show(mat_title_row1, mat_row1);
		medium_type_hide(ene_row1, ene_title_row1)
	}
	else if (medium_type == 2) {
		medium_type_show(ene_title_row1, ene_row1)
		medium_type_hide(mat_title_row1, mat_row1)
	} else {
		medium_type_hide(mat_title_row1, mat_row1)
		medium_type_hide(ene_row1, ene_title_row1)
	}
}
