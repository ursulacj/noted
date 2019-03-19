
    var navDrop = document.getElementsByClassName('.dropdown-trigger');
    M.Dropdown.init(navDrop, {
        hover: true,
        coverTrigger: false,
        closeOnClick: false
    });

    var sideNav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sideNav, options);

