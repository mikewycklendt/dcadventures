function resistance_check() {
	const deg_mod_check = document.getElementById("resistance_check");
	const deg_mod_base_form = document.getElementById("resistance-base-form");
	const title = document.getElementById("resistance-title");
	const entry = document.getElementById("resistance-entry");

	if (deg_mod_check.checked == true) {
		deg_mod_base_form.style.opacity = "100%";
		title.style.color = "#af0101";
		title.style.fontSize = "164%";
		setTimeout(function(){title.style.fontSize = "160%"}, 75);
	} else {
		deg_mod_base_form.style.opacity = "0%";
		title.style.color = "#245681";
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function resistance_base() {
	const target_field = document.getElementById("resistance_target");
	const extra_field = document.getElementById('resistance_extra')
	const extra = extra_field.options[extra_field.selectedIndex].value;
	const target =  target_field.options[target_field.selectedIndex].value;

	const entry = document.getElementById("resistance-entry");

	if (target != '' && extra != '') {
		entry.style.display = "grid";
		entry.style.padding = "1%";
		entry.style.maxHeight = entry.scrollHeight + "px";
		entry.style.padding = "1%";
	} else {
		entry.style.maxHeight = "0px";
		entry.style.padding = "0px";
		setTimeout(function(){entry.style.display = 'none'}, 400);
	}
}

function resistance_trait_type() {
	const select = 'resistance_trait_type'
	const fill = 'resistance_trait'

	trait_select(select, fill)
}

function resistance_check_type() {
	const field = document.getElementById('resistance_check_type');
	const value = field.options[field.selectedIndex].value;
	const des = document.getElementById('resistance-descriptor');
	const tra = document.getElementById('resistance-trait');

	if (value == 'trait') {
		tra.style.display = 'grid';
		setTimeout(function(){tra.style.opacity = '100%'}, 10)
		des.style.display = 'none';
		des.style.opacity = '0%';
	} else if (value = 'descriptor') {
		des.style.display = 'grid';
		setTimeout(function(){des.style.opacity = '100%'}, 10)
		tra.style.display = 'none';
		tra.style.opacity = '0%';
	} else {
		tra.style.display = 'none';
		tra.style.opacity = '0%';
		des.style.display = 'none';
		des.style.opacity = '0%';
	}
	
}