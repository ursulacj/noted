M.AutoInit();

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, options);
    var sideNav = document.querySelectorAll('.sidenav');
    var navInstances = M.Sidenav.init(elems, options);
});
