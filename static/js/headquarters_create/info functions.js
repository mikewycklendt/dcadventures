
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