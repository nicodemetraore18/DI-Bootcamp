//Exercise1-------------------------------------------------------------------------------------
//1

h1=document.getElementsByTagName("h1")[0];
console.log(h1.textContent);

//2
document.getElementsByTagName("p")[3].outerHTML="";

//3
h2=document.getElementsByTagName("h2")[0];
h2.addEventListener("click", changecolor );
function changecolor(){
	let color=prompt("Entrez la couleur que vous desiriez voir en background");
	h2.style.background=color;

} 

//4 
h3=document.getElementsByTagName('h3')[0];
h3.addEventListener("click",desappear);
function desappear(){
	h3.style.display="none"
}

//5
text=document.createTextNode("bold font");
button=document.createElement("button");
button.addEventListener("click", bold );
button.appendChild(text);
document.getElementsByTagName("article")[0].appendChild(button);

function bold(){
	p=document.getElementsByTagName("p");
	for (i in p){
		p[i].style.fontWeight="bold";
	}
}
//6 
h1.addEventListener('mouseover',changeSize);
function changeSize(){
	random = Math.floor(Math.random()*100)+1;
	h1.style.fontSize=(random+"px")
}

//7 
p2=document.getElementsByTagName("p")[1];
p2.addEventListener('mouseover',fade);
function fade(){

}



// Exercise2 --------------------------------------------------------------------------------

//1 
 form=document.forms[0];
 console.log(form)

 //2 
in1=document.getElementById("fname");
console.log(in1);
in2=document.getElementById("lname");
console.log(in2);
in3=document.getElementById("submit");
console.log(in3);

//3 

 input=document.getElementsByTagName('input');
 console.log(input.fname);
 console.log(input.lname);
 console.log(input.submit);

//4
function isLetter(str) {
  return  str.match(/[a-z]/i);
}

form.addEventListener('submit',function(event){
  event.preventDefault();
  fname=input.fname.value;
  lname=input.lname.value;
  if(fname=="" || lname=="" || !isLetter(fname) || !isLetter(lname)){
  	alert("Veuillez renseignez votre nom et prenom")

  }else{
  console.log("hello "+fname+" "+lname)}

for(let i=0 ; i<(input.length-1);i++){
	li=document.createElement('li');
	text=document.createTextNode(input[i].value);
	li.appendChild(text);
    document.getElementsByTagName('ul')[0].appendChild(li)
}




});



 // Exercise3 --------------------------------------------------------------
 //1
 var allBoldItems;
var selec=document.body.lastElementChild.previousElementSibling;

 //2
function getBold_items() {
return selec.getElementsByTagName("strong");
}

allBoldItems=getBold_items();




function highlight() {
	for(i of allBoldItems){
		i.style.color="blue"
	}
}

function return_normal() {
	for(i of allBoldItems){
		i.style.color="black"
	}
}
selec.addEventListener('mouseover', highlight);
selec.addEventListener('mouseout', return_normal);



