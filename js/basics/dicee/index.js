var randomNumber1 = Math.floor(Math.random()*(6-1+1))+1;
var randomNumber2 = Math.floor(Math.random()*(6-1+1))+1;

let imgOne = document.getElementById("img1");
let imgTwo = document.getElementById("img2");

imgOne.src="./images/dice"+randomNumber1+".png";
imgTwo.src="./images/dice"+randomNumber2+".png";

let result = document.getElementById("result");

if (randomNumber1 > randomNumber2) {
    result.textContent = "Player 1 wins!";
} else if (randomNumber1 < randomNumber2) {
    result.textContent = "Player 2 wins!";
} else if (randomNumber1 = randomNumber2) {
    result.textContent = "Draw!";
}