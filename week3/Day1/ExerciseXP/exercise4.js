//1
newdiv = document.createElement('div');
newdiv.setAttribute("class", "listBooks");
document.body.appendChild(newdiv);

//2

var allBooks;

//3
allBooks=[
book1={
	title:"Dreams",
	author:"Nicodeme",
	image:"image1.jpeg",
	alreadyRead : false

},
book2={
	title:"God's Plans",
	author:"Nicodeme",
	image:"image2.jpeg",
	alreadyRead : true

}
		  ];




//4
		//1
		table=document.createElement(
			'table');
		thead=document.createElement(
			'thead');
		th1=document.createElement(
			'th');
		th2=document.createElement(
			'th');
		th3=document.createElement(
			'th');
		titre=document.createTextNode("Titre & Auteur");
		Image=document.createTextNode("Image du Livre");
	    Detail=document.createTextNode("Detail");

	    th1.appendChild(titre);
	    th2.appendChild(Image);
	    th3.appendChild(Detail);

	    thead.appendChild(th1);
	     thead.appendChild(th2);
	      thead.appendChild(th3);




        table.appendChild(thead);
		
		data=document.createElement(
			'td');
		//

		for(element of allBooks ){
			row=document.createElement(
			'tr');
			td1=document.createElement('td')
			text=document.createTextNode(element.title+" written by "+element.author);
			td1.appendChild(text);
			td2=document.createElement('td')
			ima=document.createElement('img');
			ima.setAttribute("src",element.image);
			ima.style.width="100px";
			td2.appendChild(ima)
			td3=document.createElement('td')


			if(element.alreadyRead==true){
				

				detailText=document.createTextNode("Deja lu");
				td3.style.background="red";
				}else{
				detailText=document.createTextNode("Non lu");
				td3.style.background="blue";
				}
				td3.appendChild(detailText);


				row.appendChild(td1);
			    row.appendChild(td2);
			    row.appendChild(td3);
				 table.appendChild(row);

		}
	 newdiv.appendChild(table);