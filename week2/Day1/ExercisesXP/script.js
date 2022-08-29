//Exercise 1
/*
Instructions
Store your favorite food into a variable.

Store your favorite meal of the day into a variable (ie. breakfast, lunch or dinner)

Console.log I eat <favorite food> at every <favorite meal>
*/


		//Code
		 	  let favoriteFood="Beens";
		 	  let favoriteMeal="lunch";
		 	  console.log("I eat " +favoriteFood + " at every " + favoriteMeal);


//Exercise 2
/*
Instructions
Part I
Using this array : let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

Create a variable named myWatchedSeriesLength that is equal to the number of series in the myWatchedSeries array.

Create a variable named myWatchedSeriesSentence, that is equal to a sentence describing the series you watched
For example : black mirror, money heist, and the big bang theory

Console.log a sentence using both of the variables created above
For example : I watched 3 series : black mirror, money heist, and the big bang theory


Part II
Change the series “the big bang theory” to “friends”. Hint : You will need to use the index of “the big bang theory” series.
Add, at the end of the array, the name of another series you watched.
Add, at the beginning of the array, the name of your favorite series.
Delete the series “black mirror”.
Console.log the third letter of the series “money heist”.
Finally, console.log the myWatchedSeries array, to see all the modifications you’ve made.
*/
		//Code

		//Part1
			  let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
			  let myWatchedSeriesLength=myWatchedSeries.length;
			  let myWatchedSeriesSentence=myWatchedSeries.toString();
			  console.log("I watched 3 series : "+ myWatchedSeriesSentence );

	    //Part2	

	    	  myWatchedSeries.splice(2,1,"friends");
	    	  myWatchedSeries.push("Avengers");
	    	  myWatchedSeries.unshift("Dreams");
	    	  myWatchedSeries.splice(1,1);
	    	  console.log(myWatchedSeries[1].substring(0,3));
	    	  console.log(myWatchedSeries) 
	      			  


//Exercise3
/*
Instrucions

Store a celsius temperature into a variable.

Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.
Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32
*/
			

		//Code

		let celsiusTemperature=20;
		//we don't need to create another variable to hold the temperature in fahrenheit
	    console.log(celsiusTemperature +" °C"+" is " +(celsiusTemperature/5*9+32));






//Execise4
//Instructions

	//code

   let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    //Prediction: 55 because 34 and 21 are respectivly the values of a and b and we add 21 to 34 the result is 55
    // Actual:55

    a = 2;

    console.log(a+b) //second expression
    // Prediction:23 because the a value's change and is 2 now when we add  21 to 2 we got 23
    // Actual:23



//What will be the outcome of a + b in the first expression ?
//55
//What will be the outcome of a + b in the second expression ?
//2
//What is the value of c?
//null
console.log(c);
//Analyse the code below, what will be the outcome?
//outcome will be 12
console.log(3 + 4 + '5');



		





//Exercise5
/*
Instructions
For each expression, predict what you think the output will be in a comment (//) without first running the command.
Of course, explain each prediction.
Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.
*/

		//Code

 		typeof(15)
// Prediction:integer because 15 is an integer
console.log(typeof(15));
// Actual:number

typeof(5.5)
// Prediction:number because 5.5 is a number
console.log(typeof(5.5));
// Actual:number

typeof(NaN)
// Prediction:Boolean because NAN is testing if it is a number or no
console.log(typeof(NaN));

// Actual:number

typeof("hello")
// Prediction:string because hello is between quotes 
console.log(typeof("hello"));

// Actual: string

typeof(true)
// Prediction: boolean because true is a boolean value
console.log(typeof(true));
// Actual:boolean

typeof(1 != 2)
// Prediction:boolean cause 1 !=2 is a comparison and it will return true or false
console.log(typeof(1 != 2));
// Actual:boolean

"hamburger" + "s"
// Prediction: hamburgers because it is a concat method
// Actual: humburgers

"hamburgers" - "s"
// Prediction: hamburger because like a "+"operator it should substract the s to hamburgers
// Actual:NaN

"1" + "3"
// Prediction:13 because it is a concat operation
// Actual:13

"1" - "3"
// Prediction:NaN error because we are doing math not number 
// Actual:NaN

"johnny" + 5
// Prediction:NaN because non-number parameters of the concat
// Actual:johnny5

"johnny" - 5
// Prediction:NaN because johnny is not a number 
// Actual:NaN

99 * "hello"
// Prediction:NaN because "hello" is not number 
// Actual:NaN

1 != 1
// Prediction:false because it is a comparison and 1 !=1 is false
// Actual: false

1 == "1"
// Prediction: true because 1=1
// Actual:true

1 === "1"
// Prediction:false because === will compare also the type of arguments "1" and 1 and they don't matche
 
// Actual:false



//Exercise6

//Code
5 + "34"
// Prediction:NaN because "34" isn't a number
// Actual:534

5 - "4"
// Prediction:NaN  because "34" isn't a number
// Actual:1

10 % 5
// Prediction:0 parce que 10 divisé par 5 donne 2 et il reste 0
// Actual:0

5 % 10
// Prediction: 5 parce que  5 divisé par 10 donne 0 et il reste 5
// Actual:5

"Java" + "Script"
// Prediction:'JavaScript' parce que c'est une concatenation de "Java" et "Script"
// Actual:

" " + " "
// Prediction:"  " parce que c'est une concatenation du caractere espace vide et lui meme
// Actual:'  '

" " + 0
// Prediction:" 0" parce que c'est une concatenation du caractere espace vide et le chiffre 0
// Actual:' 0'

true + true
// Prediction: 2 because true = 1 and true + true give 2 
// Actual:

true + false
// Prediction:1  because true = 1 and false =0 so true + false give 1
// Actual:1

false + true
// Prediction:1 because true = 1 and false =0 so true + false give 1
// Actual:1

false - true
// Prediction: -1 because true = 1 and false =0 so false + true give  -1
// Actual:

!true
// Prediction: false because not true match to false
// Actual:false

3 - 4
// Prediction:-1 because 3 -4 give -1
// Actual:-1

"Bob" - "bill"
// Prediction:NaN because "Bob" and "bill" are not number
// Actual: NaN





