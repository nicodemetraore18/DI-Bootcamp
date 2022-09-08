//Exercise4----------------------------------------------------


const pi=3.14;
form=document.forms[0];
function isLetter(str) {
  return  str.match(/[a-z]/i);
}
form.addEventListener('submit',function(event){
  event.preventDefault();
  radius=document.getElementById("radius").value;
  if(isNaN(radius) || radius=="" || isLetter(radius)){
  	alert("Veuillez renseignez un nombre SVP")

  }else{
  	let volume = (4*pi*radius*radius*radius)/3;
  	document.getElementById("volume").value=volume;
  }
  
});

//Exercise5----------------------------------------------------
button=document.body.lastElementChild.previousElementSibling;
button.addEventListener("click", clicked);
button.addEventListener("mouseover", over);
button.addEventListener("mouseout", out);
button.addEventListener("dbclick", db);
function clicked(event){
  event.preventDefault();
    form.style.fontSize="40px"
    form.radius.style.border="solid 5px red"
    form.radius.style.height="50px";
  
}

function over(event){


  let left=0;
  event.preventDefault();
  form.style.position="relative";
  left+=40
  form.style.left=left+"%";
      

}

function out(event){
    event.preventDefault();
    form.style.margin="50px";
    form.style.height="300px"
}
function db(event){
    event.preventDefault();

}
