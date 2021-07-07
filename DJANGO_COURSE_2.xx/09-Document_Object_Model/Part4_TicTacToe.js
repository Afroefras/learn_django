var resetButton = document.querySelector('.btn')
var one = document.querySelector('#one')
var two = document.querySelector('#two')
var thr = document.querySelector('#thr')

// Hover (mouseover and mouseout)
resetButton.addEventListener('mouseover',function(){
    resetButton.textContent = "Sure?";
})
resetButton.addEventListener('mouseout',function(){
    resetButton.textContent = "Reset";
})

// Click button
resetButton.addEventListener('click',function(){
    one.textContent = "";
    two.textContent = "";
})
  
// On Click
one.addEventListener("click",function(){
    one.textContent = "X";
})

// Double Click
one.addEventListener("dblclick",function(){
    one.textContent = "O";
})

//Triple Click
one.addEventListener("click", function(evt) {
    if (evt.detail === 3) {
        one.textContent = "";
    }
});

// On Click
two.addEventListener("click",function(){
    two.textContent = "X";
})

// Double Click
two.addEventListener("dblclick",function(){
    two.textContent = "O";
})

//Triple Click
two.addEventListener("click", function(evt) {
    if (evt.detail === 3) {
        two.textContent = "";
    }
});