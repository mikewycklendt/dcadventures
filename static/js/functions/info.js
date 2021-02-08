
function show_info(item, divs, entry, multiple=false) {
	let d;
	for (d of divs) {
		const div = document.getElementById(d.div);
		div.style.opacity = '0%';
	}

	setTimeout(function(){
		for (d of divs) {
			const spot = document.getElementById(d.div);
			if (d.multiple) {
				if (d.class) {
					const classname = d.class;
					const olds = document.getElementsByClassName(classname);
					if (olds.length > 1)
					for (i = olds.length -1; i > -1; i-- ) {
						olds[i].remove();
					}
				}
			}
		}
	}, 300)


	if (multiple == true) {
		for (d of divs) {
			const spot = document.getElementById(d.div);
			let icon;
			if (d.icon) {
				icon = d.icon;
			}
			if (d.multiple) {
			//	if (d.class) {
			//		const classname = d.class;
			//		const olds = document.getElementsByClassName(classname);
			//		while (olds.length > 0) {olds[0].remove()};
			//	}
				const contents = d.val;
				setTimeout(function(){
					spot.style.opacity = '100%';
					let content;
					let item_text = ''
					for (content of contents) {
						if (d.class) {
							const classname = d.class;
							const div = document.createElement('div');
							div.className = classname;
							if (d.icon) {
								div.classList.add(icon)
							}
							div.innerHTML = content;
							spot.appendChild(div);
						} else {
							if (item_text == '') {
								item_text += content;
							} else {
								item_text += ', ' + content;
							}
						}
					}
					if (item_text != '') {
						spot.innerHTML = item_text
					}
				}, 300);
			} else {
				const text = d.val;
				setTimeout(function(){
					spot.innerHTML = text;
					spot.style.opacity = '100%';
				}, 310);
			}
		}
	} else {
		for (d of divs) {
			const div = document.getElementById(d.div);
			const text = d.val;
			setTimeout(function(){
				div.innerHTML = text;
				div.style.opacity = '100%';
			}, 300);
		}
	}

	show_maxheight(item);
	grow_entry(entry, item);
}
