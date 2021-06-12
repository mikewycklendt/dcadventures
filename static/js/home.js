
function show_about() {
	const div = 'about';

	show_div(modal, 'flex');
	show_div(div, 'block');
}

function about_close() {
	const div = 'about';

	hide_div(div, 2);
	hide_div(modal, 2);
}
function show_signup() {
	const div = 'signup';

	show_div(modal, 'flex');
	show_div(div, 'block');
}

function login_signup() {
	const div = 'signup';

	hide_div(div, 2);
	hide_div(modal, 2);
}