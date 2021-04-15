const modal = 'modal';

function show_login() {
	const div = 'login';

	show_div(modal, 'flex');
	show_div(div, 'flex');
}

function login_close() {
	const div = 'login';

	hide_div(div, 200);
	hide_div(modal, 200);
}