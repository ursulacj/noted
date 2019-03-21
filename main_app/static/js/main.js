var navDrop = document.getElementsByClassName('.dropdown-trigger');
M.Dropdown.init(navDrop, {
    hover: true,
    coverTrigger: false,
    closeOnClick: false
});

var sideNav = document.querySelectorAll('.sidenav');
M.Sidenav.init(sideNav, {});


let carousel = document.querySelector('.carousel');
M.Carousel.init(carousel, {
    indicators: true,
    fullWidth: true
});

// initialize the parallax elements
var parallaxEls = document.querySelectorAll('.parallax');
function initParallax(instances) {
    if (instances.length > 0) {
        for(var i = 0; i < instances.length; i++) {
            M.Parallax.init(instances[i]);
        }
    }
}
initParallax(parallaxEls);

// initialize the tool tips

var tooltip = document.querySelector('.tooltipped');
function initTooltip(tooltip) {
    M.Tooltip.init(tooltip, { 'position' : 'bottom'});
  };
initTooltip(tooltip);


//flashcards

// //constants
// function getFlashcards(instances, question, answer){
//     if (instances.length > 0) {
//         for (var i=0; i < instances.length; i++) {
//             flashcardTable[question] = answer;
//         } 
//     }
//     else flashcardTable[question] = answer;
//     return flashcardTable;
// }
// getFlashcards()

// var question = document.querySelector('.question')
// var answer = document.querySelector('.answer')
// var flashcardTable = {};
// var correctAnswer;
// var total = [0, 0];
// incorrectCards = {};
// ///how to look up all the values in the set??
// // Init
// function initFlashcards(question, answer) {
//     slide1 = question;
//     slide2 = answer;
//     victories = {};
//     total = [0, 0];
//     handleMove()
// };

// initFlashcards()

// function handleMove() {
//     if 
// }
