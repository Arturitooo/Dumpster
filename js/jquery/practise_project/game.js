var buttonColours = ["red", "blue", "green", "yellow"];
var gamePattern = [];
var userClickedPattern = [];
var level = 0;
var gameStarted = false;

function playSound(color) {
    var audio = new Audio('sounds/' + color + '.mp3');
    audio.play();
}

function animatePress(id){
    $("."+id).addClass("pressed");
    setTimeout(function() {
        $("." + id).removeClass("pressed");
    }, 150);
};


function nextSequence(){
    var randomNumber = Math.floor(Math.random() * 4);
    var randomChosenColour = buttonColours[randomNumber];
    gamePattern.push(randomChosenColour);

    var selectedButton = $("." + randomChosenColour);
    selectedButton.fadeIn(50).fadeOut(150).fadeIn(150);
    playSound(randomChosenColour);
    userClickedPattern = []
    $("#level-title").text("Level "+ gamePattern.length);
};

$(".btn").click(function() {
    var userChosenColour = $(this).attr("id");
    userClickedPattern.push(userChosenColour);

    playSound(userChosenColour);
    animatePress(userChosenColour);
    checkAnswer(userClickedPattern.length-1);
});

$("document").keypress(function() {
    if (!gameStarted) {
        gameStarted = true; // Set the game as started
        $("#level-title").text("Level "+level); // Update the level title or perform other setup tasks
        nextSequence(); // Call nextSequence for the first keypress
    }
});

function checkAnswer(currentLevel) {
    if (userClickedPattern[currentLevel] === gamePattern[currentLevel]) {
        console.log("Success");
        if (userClickedPattern.length === gamePattern.length) {
            setTimeout(nextSequence, 1000);
        }
    } else {
        console.log("Wrong");
        // Handle wrong answer logic if needed
    }
}