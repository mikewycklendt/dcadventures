
let costs = {'size_rank': 'Small',
	'size_cost': 0,
	'toughness': 6,
	'toughness_cost': 0,
	'features': 0,
	'cost': 0
}

function size_calculate() {
	const route = '/headquarters/size/select';
	const select = 'size';

	calculate_cost();
}

function calculate_cost() {

	const size_cost = costs.size_cost;
	const size_rank = costs.size_rank;
	const toughness_cost = parseInt(select('toughness'));
	const toughness = (toughness_cost * 2) + 6
	const features = costs.features;

	const size_div = document.getElementById("cost-size");
	const toughness_div = document.getElementById("cost-toughness");
	const features_div = document.getElementById("rank-features");

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

