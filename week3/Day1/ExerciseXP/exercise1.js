//Exercise1
//1 Retrieve the div and console.log it

		var Content=document.getElementById("container").innerHTML;
		console.log(Content);
//2 Change the name “Pete” to “Richard”.
document.getElementsByTagName('li')[1].innerHTML="Richard"

		
//3 Change each first name of the two <ul>'s to your name.
		
		var myName=document.getElementsByTagName("ul");
		myName[0].firstElementChild.innerHTML="Nicodème"
		myName[1].firstElementChild.innerHTML="Nicodème"
			
		
//4 Delete the <li> that contains the text node “Sarah”.

		var change3=document.getElementsByTagName("li");
		change3[3].outerHTML="";
				
	

// Bonus - Using Javascript:
//Add a class called student_list to both of the <ul>'s.
		var selected=document.getElementsByTagName("ul");
		for (const element of selected){
			element.classList.add("student_list");
			console.log(selected);
		}
//Add the classes university and attendance to the first <ul>.		
		
		var select=document.body.firstElementChild.nextElementSibling;
		select.classList.add("university","attendance");
		console.log(select);		