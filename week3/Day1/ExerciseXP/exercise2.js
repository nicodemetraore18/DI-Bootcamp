// 1 Add the code above, to your HTML file

// 2 Add a “light blue” background color and some padding to the <div>.
var div=document.getElementsByTagName("div");
div[0].style.background="lightblue";
div[0].style.padding="20px";


//3 Do not display the <li> that contains the text node “John”.

document.getElementsByTagName("ul")[0].firstElementChild.style.display="none"


//4  Add a border to the <li> that contains the text node “Pete”.
document.getElementsByTagName("ul")[0].firstElementChild.nextElementSibling.style.border="solid 1px black";

//5 Change the font size of the whole body.
document.body.style.fontSize="40px"

// Bonnus 
if (div[0].style.background=="lightblue"){
	div[0].textContent="Users : Nicodeme && Cheick"
	let table = div[0].textContent;
	let names=table.split(":");

	alert("Hello "+ names[1] );
}