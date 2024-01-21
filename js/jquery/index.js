$("h1").addClass("big-title margin-50"); // setting value of it when 2 values in brackets
$("h1").css("color"); // getting value of it when 1 value in brackets

$("h1").text("bye bye");
$("h1").removeClass("margin-50");
$("button").text("Don't click me");
$("button").html("<b>Click</b>");

console.log($("a").attr("href"));

$("h1").click(function(){
    $("h1").css("color","green");
});


// same code - JS vs jQuery
for (var i = 0 ; i<5; i++){
    document.querySelectorAll("button")[i].addEventListener("click", function(){
        document.querySelector("h1").style.color = "purple";
    });
}

$("button").click(function(){
    //$("h1").css.color("color", "purple"); .hide() would hide element .toggle() would show and hide
    //$("h1").fadeToggle(); 
    $("h1").slideUp().slideDown().animate({opacity: 0.5});
});

// input

$("document").keypress(function(event) {
    $("h1").text(event.key);
});

$("h1").on("mouseover", function(event) {
    $("h1").css("color", "yellow");
});

// adding html with js

$("h1").before("<button>New</button>");
$("h1").append("<button>New</button>");

// after - before vs append - prepend \/ difference - after/before not inside the selected element - 4e. H1

