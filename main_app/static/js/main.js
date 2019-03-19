
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