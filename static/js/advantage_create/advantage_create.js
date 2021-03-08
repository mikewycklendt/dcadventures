
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

advantage_edit = function() {
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

	///const advantage_id = document.getElementById('advantage_id').value;
	const advantage_id = select("create_advantage_select");

	const description = text("description");
	const adv_type = select("type");
	const action = select("action");
	const check_type = select("check");
	const ranked = check("ranked");
	const ranked_ranks = select("ranked_ranks");
	const ranked_max = select("ranked_max");
	const trait_type = select("trait_type");
	const trait = select("trait");
	const replaced_trait_type = select("replaced_trait_type");
	const replaced_trait =  select("replaced_trait");
	const skill_type = select("skill_type");
	const skill = select("skill");
	const skill_description = text("skill_description");
	const skill_untrained = check("skill_untrained");
	const no_pre_check = check("no_pre_check");
	const expertise = select("expertise");
	const conflict = select("conflict");
	const consequence = select("consequence");
	const conflict_immune = select("conflict_immune");
	const dc_type = select("advantage_dc_type");
	const dc_value = select("advantage_dc_value");
	const dc_mod = select("advantage_dc_mod");
	const alter_target = select("alter_target");
	const simultaneous = check("simultaneous");
	const simultaneous_type = select("simultaneous_type");
	const extra_action = check("extra_action");
	const action1 = select("action1");
	const action2 = select("action2");
	const invent = check("invent");
	const invent_permanence = select("invent_permanence");
	const invent_trait_type = select("invent_trait_type");
	const invent_trait = select("invent_trait");
	const rituals = check("rituals");
	const gm_secret_check = check("gm_secret_check");
	const gm_trait_type = select("gm_trait_type");
	const gm_trait = select("gm_trait");
	const gm_veto = check("gm_veto");
	const language = check("language");
	const languages = select("languages");
	const language_rank = select("language_rank");
	const multiple = check("multiple");
	const groups = check("groups");
	const pressure = check("pressure");
	const check_check = check("check_check");
	const circumstance = check("circ_check");
	const combined = check("combined_check");
	const condition = check("condition_check");
	const dc = check("dc_check");
	const degree = check("deg_mod_check");
	const effort = check("effort_check");
	const levels = check("levels_check");
	const minion = check("minion_check");
	const mods = check("modifiers_check");
	const mods_multiple = select("modifiers_multiple");
	const mods_count = select("modifiers_multiple_count");
	const opposed = check("opposed_check");
	const opposed_multiple = select("opposed_multiple");
	const points = check("points_check");
	const resist = check("resist_check");
	const resist_multiple = select("resist_which");
	const rounds = check("rounds_check");
	const swap = check("skill_check");
	const swap_multiple = select("skill_multiple");
	const time = check("time_check_check");
	const variable = check("variable_check");
	const move = check("move_check");
	const variable_multiple = select("variable_multiple");
	const equipment = select("equipment");
	const unarmed = check("unarmed");


	const errors = 'advantage-err';
	const err_line = 'advantage-err-line';

	response = fetch('/advantage/save', {
		method: 'POST',
		body: JSON.stringify({
			'advantage_id': advantage_id,
			'description': description,
			'adv_type': adv_type,
			'action': action,
			'check_type': check_type,
			'ranked': ranked,
			'ranked_ranks': ranked_ranks,
			'ranked_max': ranked_max,
			'trait_type': trait_type,
			'trait': trait,
			'replaced_trait_type': replaced_trait_type,
			'replaced_trait': replaced_trait,
			'skill_type': skill_type,
			'skill': skill,
			'skill_description': skill_description,
			'skill_untrained': skill_untrained,
			'no_pre_check': no_pre_check,
			'expertise': expertise,
			'conflict': conflict,
			'consequence': consequence,
			'conflict_immune': conflict_immune,
			'dc_type': dc_type,
			'dc_value': dc_value,
			'dc_mod': dc_mod,
			'alter_target': alter_target,
			'simultaneous': simultaneous,
			'simultaneous_type': simultaneous_type,
			'extra_action': extra_action,
			'action1': action1,
			'action2': action2,
			'invent': invent,
			'invent_permanence': invent_permanence,	
			'invent_trait_type': invent_trait_type,
			'invent_trait': invent_trait,
			'rituals': rituals,
			'gm_secret_check': gm_secret_check,
			'gm_trait_type': gm_trait_type,
			'gm_trait': gm_trait,
			'gm_veto': gm_veto,
			'language': language,
			'languages': languages,
			'language_rank': language_rank,
			'multiple': multiple,
			'groups': groups,
			'pressure': pressure,
			'check_check': check_check,
			'circumstance': circumstance,
			'combined': combined,
			'condition': condition,
			'dc': dc,
			'degree': degree,
			'effort': effort,
			'levels': levels,
			'minion': minion,
			'mods': mods,
			'mods_multiple': mods_multiple,
			'mods_count': mods_count,
			'opposed': opposed,
			'opposed_multiple': opposed_multiple,
			'points': points,
			'resist': resist,
			'resist_multiple': resist_multiple,
			'rounds': rounds,
			'swap': swap,
			'swap_multiple': swap_multiple,
			'time': time,
			'variable': variable,
			'move': move,
			'variable_multiple': variable_multiple,
			'equipment': equipment,
			'unarmed': unarmed
		}),
		headers: {
		'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			window.location.replace('/advantage/save/success/' + advantage_id)

		} else {
			back_errors(err_line, errors, jsonResponse)

		}
	})

}

