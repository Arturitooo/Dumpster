
ListOfDrums = document.querySelectorAll(".drum");

for (var i = 0 ; i<ListOfDrums.length; i++){

    document.querySelectorAll(".drum")[i].addEventListener("click", function () {alert("I got clicked "+ this.textContent);});
}
