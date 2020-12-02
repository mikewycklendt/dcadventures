function defense_check() {
	const check = "defense_check";
	const title = "defense-title";
	const base = 'defense-base';
	const entry = "defense-entry";

	check_title(check, title, base, entry);
}

function defense_base() {
	const field = 'defense_extra';
	const entry = "defense-entry";

	base(field, entry);
}

function defense_reflect() {
	const check = document.getElementById('defense_reflect')
	const base = document.getElementById('defense-reflect-action')

	if (check.checked == true) {
		base.style.opacity = '100%';
	} else {
		base.style.opacity = '0%'
	}	
}