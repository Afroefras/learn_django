//var p_one = prompt("Player one, name please:")
//var p_two = prompt("Player two, name please:")

$('.circle').click(function() {
    $(this).toggleClass("turnRed");
})

$('.circle').dblclick(function() {
    $(this).toggleClass("turnBlue");
})

var c_one = document.querySelectorAll('.c_one')

for (circ of c_one){
    //circ.classList.add('turnBlue')
}