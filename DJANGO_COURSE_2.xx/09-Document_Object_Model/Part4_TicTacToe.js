function clickMarker(marker){
    if(this.textContent === ''){
        this.textContent = 'X'
    }else if(this.textContent === 'X'){
        this.textContent = 'O'
    }else {
        this.textContent = ''
    }
};
var squares = document.querySelectorAll('.sq')
for (i=0; i<squares.length; i++){
    squares[i].addEventListener('click',clickMarker);
};

function returnMarker(rowIndex,colIndex){
    return document.querySelector('.board').rows[rowIndex].cells[colIndex].textContent
};
function checkLine(a,b,c){
    return(a===b&&a===c&&a!="")
};

function horizontalWinCheck(){
    for (i=0; i<3; i++){
        a = returnMarker(i,0)
        b = returnMarker(i,1)
        c = returnMarker(i,2)
        return checkLine(a,b,c)
    }
};

function verticalWinCheck(){
    for (i=0; i<3; i++){
        a = returnMarker(0,i)
        b = returnMarker(1,i)
        c = returnMarker(2,i)
        return checkLine(a,b,c)
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

// Game End
function gameEnd(winningPlayer) {
    $('.board').fadeOut('fast');
    $('h2').text(winningPlayer+" has won! Refresh your browser to play again!").css("fontSize", "50px")
}


document.querySelector('.start').addEventListener('click',function(){
    var playerOne = prompt("Player one name")
    var playerTwo = prompt("Player two name")

});