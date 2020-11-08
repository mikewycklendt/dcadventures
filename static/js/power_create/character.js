function char_check() {
	const check = document.getElementById("char_check");
	const title = document.getElementById("char-title");
	const base = document.getElementById('char-base')

	if (check.checked == true) {
		base.style.opacity = '100%';
		title.style.color = "#af0101";
		title.style.fontSize = "220%";
		setTimeout(function(){title.style.fontSize = "200%"}, 75);
	} else {
		base.style.opacity = '0%'
		title.style.color = "#245681";
	}
}

function char_base() {
	const field = document.getElementById('char_extra')
	const value = field.options[field.selectedIndex].value;
	const entry = document.getElementById("char-entry")

	if (value != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
	}
}

function char_limited() {
	const check = document.getElementById('char_limited')
	const div = document.getElementById('char-limited')
	const entry = document.getElementById("char-entry")

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = div.scrollHeight + entry.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function char_reduced() {
	const check = document.getElementById('char_reduced')
	const div = document.getElementById('char-reduced')
	const entry = document.getElementById("char-entry")

	if (check.checked == true) {
		div.style.display = 'grid';
		div.style.maxHeight = div.scrollHeight + 'px';
		entry.style.maxHeight = div.scrollHeight + entry.scrollHeight + 'px';
	} else {
		div.style.maxHeight = '0px';
		entry.style.maxHeight = entry.scrollHeight - div.scrollHeight + 'px';
	}
}

function char_limited() {
	const field = document.getElementById('char_limited');
	const value = field.options[field.selectedIndex].value;
	const oth = document.getElementById('char-other')
	const emo = document.getElementById('char-emotion')

	if (value == 'other') {
		oth.style.display = 'grid';
		oth.style.maxHeight = oth.scrollHeight + 'px';
		emo.style.display = 'none';
		emo.style.maxHeight = '0px';
	} else if (value == 'emotion') {
		emo.style.display = 'grid';
		emo.style.maxHeight = emo.scrollHeight + 'px';
		oth.style.display = 'none';
		oth.style.maxHeight = '0px';
	} else {
		oth.style.display = 'none';
		oth.style.maxHeight = '0px';
		emo.style.display = 'none';
		emo.style.maxHeight = '0px'
	}
}

function char_limited() {
	const field = document.getElementById('char_limited');
	const value = field.options[field.selectedIndex].value;
	const oth = document.getElementById('char-other')
	const emo = document.getElementById('char-emotion')

	if (value == 'other') {
		oth.style.display = 'grid';
		oth.style.maxHeight = oth.scrollHeight + 'px';
		emo.style.display = 'none';
		emo.style.maxHeight = '0px';
	} else if (value == 'emotion') {
		emo.style.display = 'grid';
		emo.style.maxHeight = emo.scrollHeight + 'px';
		oth.style.display = 'none';
		oth.style.maxHeight = '0px';
	} else {
		oth.style.display = 'none';
		oth.style.maxHeight = '0px';
		emo.style.display = 'none';
		emo.style.maxHeight = '0px'
	}
}

function char_emotion() {
	const field = document.getElementById('char_emotion');
	const value = field.options[field.selectedIndex].value;
	const oth = document.getElementById('char-emotion-other')

	if (value == 'other') {
		oth.style.opacity = '100%';
	} else {
		oth.style.opacity = '0%';
	}
}