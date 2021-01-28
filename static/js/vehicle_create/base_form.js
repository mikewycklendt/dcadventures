


let costs = {'size_rank': 0,
			'size_cost': 0,
			'size_strength': 0,
			'size_toughness': 0,
			'size_defense': 0,
			'strength': 0,
			'strengths': 0,
			'speed': 0,
			'toughness': 0,
			'toughnesses': 0,
			'defense': 0,
			'defenses': 0,
			'features': 0,
			'powers_rank': 0,
			'powers_cost': 0,
			'cost': 0}

function size_field() {
	const type_id = select('size_field');

	response = fetch('/vehicle/size/select', {
		method: 'POST',
		body: JSON.stringify({
			'id': type_id
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
	
			costs.size_cost = jsonResponse.cost;
			costs.size_rank = jsonResponse.rank;
			costs.size_defense = jsonResponse.defense;
			costs.size_strength = jsonResponse.strength;
			costs.size_toughness = jsonResponse.toughness;
			calculate_cost();

		} else {
			console.log('error');``
		}
	})	
}

function calculate_cost() {
	
	const size_cost = costs.size_cost;
	const size_rank = costs.size_rank
	const size_strength = costs.size_strength;
	const size_toughness = costs.size_toughness;
	const size_defense = costs.size_defense;
	const strengths = parseInt(select('strengths'));
	const speed = parseInt(select('speed'));
	const toughnesses = parseInt(select('toughnesses'));
	const defenses = parseInt(select('defenses'));
	const features = costs.features;
	const powers_rank = costs.powers_rank;
	const powers_cost = costs.powers_cost;
	
	const size_div = document.getElementById("cost-size");
	const strength_div = document.getElementById("cost-strength");
	const speed_div = document.getElementById("cost-speed");
	const toughness_div = document.getElementById("cost-toughness");
	const defense_div = document.getElementById("cost-defense");
	const features_div = document.getElementById("cost-features");
	const powers_div = document.getElementById("cost-powers");
	
	const size_rank_div = document.getElementById("rank-size");
	const strength_rank_div = document.getElementById("rank-strength");
	const speed_rank_div = document.getElementById("rank-speed");
	const toughness_rank_div = document.getElementById("rank-toughness");
	const defense_rank_div = document.getElementById("rank-defense");
	const powers_rank_div = document.getElementById("rank-powers");

	const total_div = document.getElementById("cost-total");

	const strength_rank = strengths + size_strength;
	const toughness_rank = toughnesses + size_toughness;
	const defense_rank = defenses + size_defense;

	size_rank_div.innerHTML = size_rank;
	strength_rank_div.innerHTML = strength_rank;
	speed_rank_div.innerHTML = speed;
	toughness_rank_div.innerHTML = toughness_rank;
	defense_rank_div.innerHTML = defense_rank;
	powers_rank_div.innerHTML = powers_rank;
	
	const cost = strengths + speed + toughnesses + defenses + features + powers_cost;
	
	size_div.innerHTML = size_cost;
	strength_div.innerHTML = strengths;
	speed_div.innerHTML = speed;
	toughness_div.innerHTML = toughnesses;
	defense_div.innerHTML = defenses;
	features_div.innerHTML = features;
	powers_div.innerHTML = powers_cost;
	total_div.innerHTML = cost;

	costs.cost = cost;
	costs.speed = speed;
	costs.strength = strength_rank;
	costs.toughness = toughness_rank;
	costs.defense = defense_rank;
}
