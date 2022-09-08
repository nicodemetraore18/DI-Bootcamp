//1 
button = document.getElementById("lib-button")
button.addEventListener("click",getELement)
function getELement(event) {
	event.preventDefault();
	data=document.getElementsByTagName("input");
	
		let noun =data.noun.value;

		let adjective =data.adjective.value;

		let person =data.person.value;

		let verb =data.verb.value;

		let place =data.place.value;
	let story=[noun,adjective,verb,person,place];


		function isLetter(str) {
  return  str.match(/[a-z]/i);
}
	for(let i of data){
		if(!isLetter(i.value) ){
			alert("Entrez un "+i.id +" valide !");
				document.getElementById("story").textContent="";

		}
		else{
	document.getElementById("story").textContent=story.join(" ");
		}
	}	

	
}
shuffle=document.createElement("button");
shuffle.setAttribute("id","shuffle");
text=document.createTextNode("shuffle");
shuffle.appendChild(text);
document.forms[0].appendChild(shuffle);
shuffle.addEventListener("click", shuffl);
function shuffl(event) {
	event.preventDefault();
	let story=[noun,adjective,verb,person,place];
    let sstory=[];
    let old;
	for (let i=0 ; i<story.length; i++){
	    
		indice =Math.floor(Math.random()*story.length);
	   while(indice==old){
	   			indice =Math.floor(Math.random()*story.length);

	   }
	   	

	   sstory.push(story[indice].value);
	   old=indice;


	}
document.getElementById("story").textContent=sstory.join(" ");



}
