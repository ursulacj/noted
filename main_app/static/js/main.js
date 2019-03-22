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

//select for sets
var selectEl = document.getElementById('id_sets');
    M.FormSelect.init(selectEl)

// select users
var selectEl2 = document.getElementById('id_users');
    M.FormSelect.init(selectEl2)

//checkbox
var checkboxEl = document.querySelectorAll("input[type='checkbox']");
function initCheck(instances) {
    if (instances.length > 0) {
        console.log('this is checkbox', checkboxEl)
        for(var i = 0; i < instances.length; i++) {
            instances[i].insertAdjacentHTML("afterend", '<label for="id_flashcard_set-0-DELETE">');
        }
    }
}
initCheck(checkboxEl)

//flashcards


/*----- app's state (variables) -----*/ 
let count = 0;
let inputVal = 0;


/*----- cached element references -----*/ 



/*----- event listeners -----*/ 

var plus = document.getElementById("plus")
var minus = document.getElementById("minus")

plus.addEventListener('click', addOne)
minus.addEventListener('click', minusOne)

/*----- functions -----*/

function addOne() {
    count += 1
    render();
};

function minusOne() {
    count += -1;
    render();
};

function render() {
    document.getElementById("number-clicks").innerHTML = count;
    count < 0 ? document.getElementById("number-clicks").style.color = 'red' : document.getElementById("number-clicks").style.color = 'black'
};
