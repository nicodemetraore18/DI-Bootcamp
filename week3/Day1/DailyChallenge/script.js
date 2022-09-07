let planets= [
     Mercure={nom:"Mercure",
     	"couleur":"Peru"},

	 Vénus={
	 	nom:"Vénus",
	 	},

	 Terre={nom:"Terre",
	 	},

	 Mars={nom:"Mars",
	 	} ,

	 Jupiter={nom:"Jupiter",
	 	},

	 Saturne={nom:"Saturne",
	 	},

	 Uranus={nom:"Uranus",
	 	},

	Neptune={nom:"Neptune",
		} ]

 select= document.getElementsByTagName("section")[0];


for (planet of planets)
	{
		
		
 		newdiv=document.createElement('div');
 		newh1=document.createElement('h1')
 		newdiv.appendChild(newh1)
 		text=document.createTextNode(planet.nom)
 		newh1.appendChild(text)
 		newdiv.classList.add("planet",planet.nom);
 		
 		
      select.appendChild(newdiv);
 	}
