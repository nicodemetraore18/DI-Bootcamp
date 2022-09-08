let timer=setInterval(myMove,1);
let pos=0;
function myMove() {
	select=document.getElementById("animate");
	select.style.left=pos+"px";
	pos+=1;
	if(pos==350){
		clearInterval(timer)
	}
	
}