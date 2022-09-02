//Exercise1
//Part1
function infoAboutMe(){
	console.log("My name is Nicodeme Traore i'm 19 years old and I play basket ball every times ");

}
infoAboutMe();

//part2
function infoAboutPerson(personName, personAge, personFavoriteColor){
	console.log("Your name is "+personName+" ,your are "+personAge+
		"years old , your favorite color is "+personFavoriteColor);
}
infoAboutPerson("David" ,45 ,"blue");
infoAboutPerson("Josh" ,12 ,"yellow");


//Exercise2

function calculatorTip(){
	let bill=prompt("Enter the amount of the bill in $USD");
	let tip;
if (Number(bill)<50) {

tip=(bill*20)/100;

}else if (Number(bill)>=50 && Number(bill)<=200) {

tip=(bill*15)/100;

}else{
	tip=(bill*10)/100;
}
bill=Number(bill)+Number(tip)
console.log("******************************** \n Tip: "+tip+" $ \n Final bill: "+ bill+ "$" )
}
calculatorTip();


//Exercise3
//1
function isDivisible() {
	// body...
	let divisor=[];
	let sum=0;
	for (var i = 0; i < 500; i++) {
		if ( i%23==0) {
         divisor.push(i);
         sum=Number(sum)+Number(i);
		}
	}
	console.log(divisor.join(" ")+"\n Sum : "+sum );
}
isDivisible();


//Exercise4
//1
let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
//2
let shoppingList=["banana","orange","apple"]
console.log(stock["banana"]);

function myBill(){
	let price=0;

	for(let i of shoppingList){
if(i in stock){
	if (stock[i]>0) {
		price=Number(price)+Number(prices[i])
		stock[i]--;
	}

	

}

/*if (stock[i] >0) {
	price=Number(price)+Number(price.i);
	stock.shoppingList[i]--;

}*/

}
return console.log("The bill is "+price );

};

myBill();





// Exercise 5

let change = [0.25, 0.10, 0.05, 0.01];

function changeEnough(itemPrice, amountOfChange){
	let sum=0;
for(let i in amountOfChange){
sum=Number(sum) + (Number(amountOfChange[i])*change[i]);

}
console.log(sum)
if( sum>=itemPrice){
	return true;

	}else{
		return false;
	}

}

console.log(changeEnough(4.25, [25,20,5,0]));
console.log (changeEnough(14.11, [2,100,0,0])) ;
console.log( changeEnough(0.75, [0,0,20,5]) );


//Exercise 6

//1
function hotelCost(){

let numNight=prompt("Enter the number of nights you would stay in the hotel");
while(numNight == "" || !(numNight >0) || (numNight > 365)){
	//on pourrait utilise NaN dans la comparaison ex 
	numNight=prompt("Enter the number of nights you would stay in the hotel");

}
let total = Number(numNight)*140
alert("The total price is: " +total+ "$")
}
//hotelCost();

//2
console.log(Number("10") == NaN )
/*
function planeRideCost(){

let destination=prompt("Enter the destination you wish reach");
while(destination == "" ){
destination=prompt("Enter the destination you wish reach");
}
let pr = Number(numNight)*140
alert("The  price is: " +price+ "$")
}
hotelCost();
*/