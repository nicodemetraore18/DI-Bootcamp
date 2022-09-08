let planets= [
     Mercure={nom:"Mercure",
     	nbrelune:2},

	 Vénus={
	 	nom:"Vénus",
	 	nbrelune:2
	 	},

	 Terre={nom:"Terre",
	 nbrelune:1
	 	},

	 Mars={nom:"Mars",
	 nbrelune:2
	 	} ,

	 Jupiter={nom:"Jupiter",
	 nbrelune:2
	 	},

	 Saturne={nom:"Saturne",
	 nbrelune:2
	 	},

	 Uranus={nom:"Uranus",
	 nbrelune:2
	 	},

	Neptune={nom:"Neptune",
	nbrelune:2
		} ]

 select= document.getElementsByTagName("section")[0];


for (planet of planets)
	{
		let positionleft=5;
		let positionbottom=40;
		divparent=document.createElement('div');
		divparent.classList.add("divpar");
 		newdiv=document.createElement('div');
 		newh1=document.createElement('h1')
 		newdiv.appendChild(newh1)
 		for(let i=0; i<planet.nbrelune; i++){
 		moon=document.createElement("div")	
 		moon.classList.add("moon");
 		divparent.appendChild(moon);
 		moon.style.left=positionleft+"px";
 		moon.style.top=positionbottom+"px";
          positionleft+=50;
          positionbottom+=140;

 		}
 		

 		
 		
 		text=document.createTextNode(planet.nom)
 		newh1.appendChild(text)
 		newdiv.classList.add("planet",planet.nom);
 		
 		divparent.appendChild(newdiv);
      select.appendChild(divparent);
 	}