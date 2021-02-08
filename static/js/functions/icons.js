
function icon_select(field, route, divid=false, classname=false, remove=false, fade_check=false) {
	const id = select(field);

	response = fetch(route, {
		method: 'POST',
		body: JSON.stringify({
			'id': id
		}),
		headers: {
		  'Content-Type': 'application/json',
		}
	})
	.then(response => response.json())
	.then(jsonResponse => {
		console.log(jsonResponse)
		if (jsonResponse.success) {

			const icon = jsonResponse.icon;

			if (fade_check != false) {
				if (divid != false) {
					fade(divid);
				} 
				
				if (classname != false) {
					fade(classname, true)
				}
			}

			if (divid != false) {
				const div = document.getElementById(divid);
				if (remove == true) {
					setTimeout(function(){div.removeAttribute('class')}, 300);
				}
				setTimeout(function(){div.classList.add(icon)}, 310);
			}
			
			if (classname != false) {
				const divs = document.getElementsByClassName(classname);
				let div; 
				for (div of divs) {
					if (remove == true) {
						setTimeout(function(){div.removeAttribute('class')}, 300);
					}
					div.className = classname;
					setTimeout(function(){div.classList.add(icon)}, 310);
				}
			}
		
		} else {
			console.log('error');
		}
	})	
}

function fade(div_input, classname=false) {
	
	if (classname == false) {
		const div = document.getElementById(div_input);
		div.style.opacity = '0%'
		setTimeout(function(){div.style.opacity = '100%'}, 310);
	}

	if (classname != false) {
		const divs = document.getElementsByClassName(div_input);
		let div;
		for (div of divs) {
			div.style.opacity = '0%';
		}
	}
	
	if (classname != false) {
		const divs = document.getElementsByClassName(div_input);
		let div;
		for (div of divs) {
			setTimeout(function(){div.style.opacity = '100%'}, 310);
		}
	}
}
