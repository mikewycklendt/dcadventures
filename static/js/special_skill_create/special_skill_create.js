skill_create = function() {
	const skill_name = document.getElementById('skill_name').value;

	response = fetch('/skill/create', {
		method: 'POST',
		body: JSON.stringify({
		  'name': skill_name,
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {
			const name_div = document.getElementById('skill-name');
			const skill_id = document.getElementById('bonus_id');
			name_div.innerHTML = jsonResponse.name;
			skill_id.value = jsonResponse.id;
			name_div.style.display = "block"
		} else {
			const errors = document.getElementById('name-err');

			const error = document.createElement('div');
			error.className = 'name-err-line';
			error.innerHTML = jsonResponse.error;

			errors.appendChild(error);

			error.style.maxHeight = error.scrollHeight + "px";

			errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
			errors.style.padding = "1%";
		}
	})
}