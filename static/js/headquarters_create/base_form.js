
let costs = {'size_rank': 'Small',
	'size_cost': 0,
	'toughness': 6,
	'toughness_cost': 0,
	'features': 0,
	'cost': 0
}

function size_calculate() {
	const select = 'size';
	const route = '/headquarters/size/select';

	get_size(select, route)
}

function get_size(field, route) {
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
		if (jsonResponse.success) {
			
			costs.size_cost = jsonResponse.cost;
			costs.size_rank = jsonResponse.rank;
			calculate_cost()

		} else {
			console.log('error');``
		}
	})	
}



function calculate_cost() {

	const size_cost = costs.size_cost;
	const size_rank = costs.size_rank;
	const toughness_cost = parseInt(select('toughness'));
	const toughness = (toughness_cost * 2) + 6
	const features = costs.features;

	const size_div = document.getElementById("cost-size");
	const toughness_div = document.getElementById("cost-toughness");
	const features_div = document.getElementById("cost-feature");

	const size_rank_div = document.getElementById("rank-size");
	const toughness_rank_div = document.getElementById("rank-toughness");

	const total_div = document.getElementById("cost-total");

	size_rank_div.innerHTML = size_rank;
	toughness_rank_div.innerHTML = toughness;

	const cost = toughness_cost + features + size_cost;

	size_div.innerHTML = size_cost;
	toughness_div.innerHTML = toughness_cost;
	features_div.innerHTML = features;
	total_div.innerHTML = cost;

	costs.cost = cost;
	costs.toughness = toughness;
}

