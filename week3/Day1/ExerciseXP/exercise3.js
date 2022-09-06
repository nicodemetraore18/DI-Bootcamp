/* 2 In the <div>, change the value 
of the id attribute from navBar to socialNetworkNavigation,
 using the setAttribute method. */

 document.getElementById("navBar").setAttribute("id","socialNetworkNavigation");

 /* 3
 We are going to add a new <li> to the <ul>.
First, create a new <li> tag (use the createElement method).
Create a new text node with “Logout” as its specified text.
Append the text node to the newly created list node (<li>).
Finally, append this updated list node to the
 unordered list (<ul>), using the appendChild method. */
 //1
 newli = document.createElement("li");

 //2 	
 newTextNode = document.createTextNode('Logout');

 //3

newli.appendChild(newTextNode);

//4
 select= document.body.firstElementChild.firstElementChild
 select.appendChild(newli);


// bonus

console.log(select.firstElementChild);
console.log(select.lastElementChild);

