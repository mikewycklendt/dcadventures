skill_create = function() {
	const skill_name = document.getElementById('skill_name').value;
	const add_skill = document.getElementById('add-skill');
	const edit_button = document.getElementById('edit-button');

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
			name_div.style.opacity = "100%"
			name_div.style.fontSize = "400%";
			setTimeout(function(){name_div.style.fontSize = "360%"}, 75);
			edit_button.style.display = "block";
			add_skill.style.display = "none";
		} else {
			const errors = document.getElementById('name-err');

			const error_msgs = jsonResponse.error

			for (i=0; i < error_msgs.length; i++) {
				const error = document.createElement('div');
				error.className = 'name-err-line';
				error.innerHTML = error_msgs[i];
			
				errors.appendChild(error);
			}

			errors.style.display = "grid";

			error.style.maxHeight = error.scrollHeight + "px";

			errors.style.maxHeight = error.scrollHeight + errors.scrollHeight + 15 + "px";
			errors.style.padding = "1%";
		}
	})
}