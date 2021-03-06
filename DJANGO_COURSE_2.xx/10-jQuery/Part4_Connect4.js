// Ask for the name of the players
var player1 = prompt("Player One: Enter Your Name , you will be Blue");
var player2 = prompt("Player Two: Enter Your Name, you will be Red");

//Set their colors
var player1Color = 'rgb(197, 84, 84)';
var player2Color = 'rgb(84, 133, 197)';

// http://stackoverflow.com/questions/6139407/getting-td-by-index-with-jquery
function reportWin(rowNum,colNum) {
    console.log("You won starting at this row,col");
    console.log(rowNum);
    console.log(colNum);
  }

// Set a variable to know if the game still goes on
var game_on = true;

// jQuery to select the table
var table = $('table tr');


function changeColor(rowIndex,colIndex,color){
    // Search for the "rowIndex"-th element
    x = table.eq(rowIndex)
    // For all its td elem (columns)
    x = x.find('td')
    // Find the "colIndex"-th elem
    x = x.eq(colIndex)
    // Select its button elem
    x = x.find('button')
    // And change its color
    x = x.css('background-color',color)
    return x
}

// The same as the function above but just return the color without change tis color
function returnColor(rowIndex,colIndex){
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color')
}

// Take in column index, returns the bottom row that is still gray
function checkBottom(colIndex) {
    var colorReport = returnColor(5,colIndex);
    for (var row = 5; row > -1; row--) {
      colorReport = returnColor(row,colIndex);
      if (colorReport === 'rgb(46, 45, 45)') {
        return row
      }
    }
}


// Check to see if 4 inputs are the same color
function colorMatchCheck(one,two,three,four){
    return (one===two && one===three && one===four && one !== 'rgb(46, 45, 45)' && one !== undefined);
}
  
  // Check for Horizontal Wins
  function horizontalWinCheck() {
    for (var row = 0; row < 6; row++) {
      for (var col = 0; col < 4; col++) {
        if (colorMatchCheck(returnColor(row,col), returnColor(row,col+1) ,returnColor(row,col+2), returnColor(row,col+3))) {
          console.log('horiz');
          reportWin(row,col);
          return true;
        }else {
          continue;
        }
      }
    }
}
  
  // Check for Vertical Wins
  function verticalWinCheck() {
    for (var col = 0; col < 7; col++) {
      for (var row = 0; row < 3; row++) {
        if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col) ,returnColor(row+2,col), returnColor(row+3,col))) {
          console.log('vertical');
          reportWin(row,col);
          return true;
        }else {
          continue;
        }
      }
    }
}
  
  // Check for Diagonal Wins
  function diagonalWinCheck() {
    for (var col = 0; col < 5; col++) {
      for (var row = 0; row < 7; row++) {
        if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col+1) ,returnColor(row+2,col+2), returnColor(row+3,col+3))) {
          console.log('diag');
          reportWin(row,col);
          return true;
        }else if (colorMatchCheck(returnColor(row,col), returnColor(row-1,col+1) ,returnColor(row-2,col+2), returnColor(row-3,col+3))) {
          console.log('diag');
          reportWin(row,col);
          return true;
        }else {
          continue;
        }
      }
    }
}

// Game End
function gameEnd(winningPlayer) {
    for (var col = 0; col < 7; col++) {
      for (var row = 0; row < 7; row++) {
        $('h3').fadeOut('fast');
        $('h2').fadeOut('fast');
        $('.board').fadeOut('slow')
        $('h1').text(winningPlayer+" has won! Refresh your browser to play again!").css("fontSize", "50px").css('color','white')
      }
    }
  }
  
  // Start with Player One
  var currentPlayer = 1;
  var currentName = player1;
  var currentColor = player1Color;
  
  // Start with Player One
  $('h3').text(player1+": your turn, click a column to drop your blue chip.").css('color','white');
  
  $('.board button').on('click',function() {
  
    // Recognize what column was chosen
    var col = $(this).closest("td").index();
  
    // Get back bottom available row to change
    var bottomAvail = checkBottom(col);
  
    // Drop the chip in that column at the bottomAvail Row
    changeColor(bottomAvail,col,currentColor);
  
    // Check for a win or a tie.
    if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
      gameEnd(currentName);
    }
  
    // If no win or tie, continue to next player
    currentPlayer = currentPlayer * -1 ;
  
    // Re-Check who the current Player is.
    if (currentPlayer === 1) {
      currentName = player1;
      $('h3').text(currentName+": it is your turn, please pick a column to drop your blue chip.");
      currentColor = player1Color;
    }else {
      currentName = player2
      $('h3').text(currentName+": it is your turn, please pick a column to drop your red chip.");
      currentColor = player2Color;
    }
  
  })