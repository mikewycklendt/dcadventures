const modal = 'modal';

function show_login() {
	const div = 'login';

	show_div(modal, 'flex');
	show_div(div, 'block');

}

function login_close() {
	const div = 'login';

	hide_div(div, 2);
}