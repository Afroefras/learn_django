// Variables
var playerOne = prompt("Player one name")
var playerTwo = prompt("Player two name")
var h2Elem = document.querySelector('h2')
var board = document.querySelector('.board')
var squares = document.querySelectorAll('.sq')
var startButton = document.querySelector('.start')
var nextButton = document.querySelector('.next')

//Functions
function clickMarker(marker){
    if(this.textContent === ''){
        this.textContent = 'X'
    }else if(this.textContent === 'X'){
        this.textContent = 'O'
    }else {
        this.textContent = ''
    }
};
function returnMarker(rowIndex,colIndex){
    return board.rows[rowIndex].cells[colIndex].textContent
};
function checkLine(a,b,c){
    return(a===b&&a===c&&a!="")
};
function horizontalWinCheck(){
    for (i=0; i<3; i++){
        a = returnMarker(i,0)
        b = returnMarker(i,1)
        c = returnMarker(i,2)
        if (checkLine(a,b,c)){
            return true
        }else{
            continue
        }
    }
};
function verticalWinCheck(){
    for (i=0; i<3; i++){
        a = returnMarker(0,i)
        b = returnMarker(1,i)
        c = returnMarker(2,i)
        if (checkLine(a,b,c)){
            return true
        }else{
            continue
        }
    }
};
function diagonalWinCheck(){
    a = returnMarker(0,0)
    b = returnMarker(1,1)
    c = returnMarker(2,2)
    d = returnMarker(0,2)
    e = returnMarker(2,0)
    return checkLine(a,b,c)||checkLine(d,b,e)
};
function gameEnd(winningPlayer) {
    h2Elem.textContent = winningPlayer+" has won!";
    h2Elem.style.fontSize = 'xx-large'
    board.remove()
    nextButton.remove()
    startButton.remove()
    return winningPlayer
}

// Events
for (i=0; i<squares.length; i++){
    squares[i].addEventListener('click',clickMarker);
};
startButton.addEventListener('click',function(){
    squares.forEach(x => {
        x.textContent = ""
    });
    h2Elem.textContent = playerOne + ' your turn!'
});
nextButton.addEventListener('click',function(){
    var currentPlayer = playerOne
    if (horizontalWinCheck()||verticalWinCheck()||diagonalWinCheck()){
        gameEnd(currentPlayer)
    }else{
        if (h2Elem.textContent === playerOne + ' your turn!'){
            var currentPlayer = playerTwo
        }else{
            var currentPlayer = playerOne
        }
        h2Elem.textContent = currentPlayer + ' your turn!'
    }
});