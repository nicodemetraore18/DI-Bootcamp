//Exercise 1




function playTheGame(){

	   let result=confirm("Would you like to play the game?")

  if(!result )
   {
		alert("No problem, Goodbye");

   }
   else

   {

       let number= prompt("Enter a number between 0 and 10")
       if(isNaN(number) || number==""){
       alert('Sorry Not a number, Goodbye ')
       playTheGame();
       }
       else if(number<0 || number>10)
       {
	    	alert("not a good number");
	    	playTheGame();
       }	
       else
       {
	    	 var computerNumber=Math.floor(Math.random() * (10 - 0 +1)) + 0;
	     	 compareNumbers(number,computerNumber);
        }
	}


}
//***********************************************************
function compareNumbers(userNumber,computerNumber) 
{
	let i=0;	
	while(i<=2)
	{
   		if(userNumber==computerNumber){
	  	alert("****************WINNER*******************")
	  	break;
        }

    else if(userNumber>computerNumber)
    {
		alert("Your number is bigger then the computer’s, guess again");
		i++;
	   		if (i==3) {
	     	alert ("out of chances");
	     	break
	    	}
	   userNumber=+prompt("Enter a number between 0 and 10");
	   while(isNaN(userNumber) || userNumber==""||userNumber<0 || userNumber>10){
       alert("Invalid");
       		userNumber=+prompt("Enter a number between 0 and 10");

	   }
    }

    else if(userNumber<computerNumber)
    {

	    alert("Your number is smaller then the computer’s, guess again");
	    i++;
	    if (i==3) {
		alert ("out of chances");
		break
   		 }
		userNumber=+prompt("Enter a number between 0 and 10");
	
		while(isNaN(userNumber) || userNumber==""||userNumber<0 || userNumber>10){
     	 alert("Invalid");
     	 		userNumber=+prompt("Enter a number between 0 and 10");

		}

    }
 
}

}
