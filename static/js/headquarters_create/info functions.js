
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

			const item = 'head-feature';
			const divs = [{'val': jsonResponse.name, 'div': 'head-feature-name'},
					{'val': jsonResponse.description, 'div': 'head-feature-description'},
					{'val': jsonResponse.weapons, 'class': 'head-feature-item', 'icon': 'weapon-icon', 'div': 'head-feature-weapon'},
					{'val': jsonResponse.features, 'class': 'head-feature-item', 'icon': 'feature-icon', 'div': 'head-feature-features'},
					{'val': jsonResponse.equipment, 'class': 'head-feature-item', 'icon': 'equipment-icon', 'div': 'head-feature-equipment'}]
			const entry = 'addon-entry';
			
			show_info(item, divs, entry, true);

			
			show_info(item, divs, entry);


		} else {
			console.log('error');
		}
	})	
}

function feature_info(field, route) {
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

			const item = 'feature-item';
			const divs = [{'val': jsonResponse.name, 'div': 'item-name'},
					{'val': jsonResponse.description, 'div': 'item-description'}]
			const entry = 'feature-entry';
			
			show_info(item, divs, entry);

		} else {
			console.log('error');
		}
	})	
}