//Part1*******************************************
var     select=document.getElementById("container");
var taill;
var timer

function  bonjour(){
	alert("hello world");
}

setTimeout(bonjour, 1000);

//Part2********************************************
function addp() {
	p=document.createElement("p");

	text=document.createTextNode("Hello world");
    p.appendChild(text)
    select.appendChild(p);
    if(select.children.length==5){
      clearInterval(timer)

    }
  }

let id=setTimeout(addp,2000);
clearTimeout(id);

//Part 3***************************************************
button=document.getElementById("clear");

button.addEventListener("click",stop)

timer=setInterval(addp,2000);



function stop(){
clearInterval(timer)
}
