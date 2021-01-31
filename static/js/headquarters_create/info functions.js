
function addon_info(field, route) {
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

			const item = 'addon-item';
			const divs = [{'val': jsonResponse.name, 'div': 'addon-name'},
					{'val': jsonResponse.description, 'div': 'addon-description'}]
			const entry = 'addon-entry';
			
			show_info(item, divs, entry);
			
			show_info(item, divs, entry);


		} else {
			console.log('error');
		}
	})	
}

function feature_info(field, item, entry, route) {
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


			
			const divs = [{'val': jsonResponse.name, 'div': 'head-feature-name'},
					{'val': jsonResponse.description, 'div': 'head-feature-description'},
					{'val': jsonResponse.cost, 'div': 'feature-cost'},
					{'val': jsonResponse.weapons, 'multiple': true, 'class': 'head-feature-item', 'icon': 'weapon-icon', 'div': 'head-feature-weapons'},
					{'val': jsonResponse.features, 'multiple': true, 'class': 'head-feature-item', 'icon': 'feature-icon', 'div': 'head-feature-features'},
					{'val': jsonResponse.equipment, 'multiple': true, 'class': 'head-feature-item', 'icon': 'equipment-icon', 'div': 'head-feature-equipment'}]
			
			show_info(item, divs, entry, true);

			

		} else {
			console.log('error');

			hide_maxheight(item)
			shrink_entry(entry, item)
		}
	})	
}