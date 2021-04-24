
const trait_select = '/select/trait';
const trait_filter = '/select/trait/filter'
const level_select = '/select/level';
const action_select = '/select/action';
const skill_select = '/select/skill';
const weapon_type_select = '/select/weapon/type';
const weapon_select = '/select/weapon';
const subsense_select = '/select/sense/subsense';
const equipment_select = '/select/equipment';
const unit_select = '/select/unit';
const feature_select = '/select/feature';
const medium_select = '/select/medium';
const medium_subtype_select = '/select/medium/subtype';
const descriptor_select = '/select/descriptor';
const power_cost_select = '/select/power/cost';
const power_ranks_select = '/select/power/ranks';
const narrow_creature_select = '/select/creature/narrow';

const head_feature_info_select = '/info/headquarters/feature';
const feature_info_select = '/info/feature';
const equipment_info_select = '/info/equipment';
const weapon_info_select = '/info/weapon';

const skill_icon_select = '/select/icon/skill';
const ability_icon_select = '/select/icon/ability';

const variable_sub = 'variable';
const any_var_sub = 'any-var';
const other_var_sub = 'variable-other';

function id_select(id_field, fill, route, sub=false, classname=false, titles=false, multiple=false, power_id=false) {
	const id = select(id_field);

	response = fetch(route, {
		method: 'POST',
		body: JSON.stringify({
			'id': id,
			'sub': sub,
			'fields': fill,
			'titles': titles,
			'power_id': power_id
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			if (jsonResponse.titles) {
				titles = jsonResponse.titles;
				let t;
				for (t of titles) {
					const div = document.getElementById(t.div)
					const title = t.title

					div.style.opacity = '100%';
					div.innerText = title;
				}
			}

			const options = jsonResponse.options;
		
			if (multiple == false) {	
				if (classname == false) {
					const update = document.getElementById(fill);
					update.innerText = null;
					update.style.backgroundColor = 'lightblue';
					setTimeout(function(){update.style.backgroundColor = "white"}, 200)
					let option;
					for (option of options)  {
						let o = document.createElement("option")
						o.value = option.id;
						o.text = option.name;
						update.add(o);
					}
				} else {
					const selects = document.getElementsByClassName(fill);
					let update;
					for (update of selects) {
						update.innerText = null;
						update.style.backgroundColor = 'lightblue';
						setTimeout(function(){update.style.backgroundColor = "white"}, 200)
						let option;
						for (option of options)  {
							let o = document.createElement("option")
							o.value = option.id;
							o.text = option.name;
							update.add(o);
						}
					}
				}		
			} else {
				let field;
				for (field of options) {
					const select = field.select;
					const update = document.getElementById(select)
					const inserts = field.options;
					let option;
					for (option of inserts) {
						let o = document.createElement("option")
						o.value = option.id;
						o.text = option.name;
						update.add(o);
					}
				}
			}
		} else {
			console.log('no results');
		}

	})	
}


function get_descriptors(origin_input, source_input, medium_type_input, medium_subtype_input, medium_input, update_input, rarity=false, classsname=false) {
	const origin = select(origin_input);
	const source = select(source_input);
	const medium_type = select(medium_type_input);
	const medium_subtype = select(medium_subtype_input);
	const medium = select(medium_input);
	
	response = fetch('/power/descriptor/select', {
		method: 'POST',
		body: JSON.stringify({
			'origin': origin,
			'source': source,
			'medium_type': medium_type,
			'medium_subtype': medium_subtype,
			'medium': medium,
			'rarity': rarity
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const select = document.getElementById('descriptor_field');
			let old_options = select.options;
			
			for (i = old_options.length - 1; i > -1; i--) {
				if (old_options[i].value == 'new' || old_options[i].value == 'all' || old_options[i].value == '') {
					console.log('keep');
				} else {
					old_options[i].remove();
				}
			}

			let options = jsonResponse.options;
			let option;

			for (option of options)  {
				console.log(option)
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
