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
