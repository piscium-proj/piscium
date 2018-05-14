// Page router
window.location.href = 'http://www.google.com';
history.back();

// Hash router
window.location = '#hash';
window.onhashchange = function(){
    console.log('current hash:', window.location.hash);
};

// H5(browser) router
// push a state
history.pushState('name', 'title', '/path');
// replace a state
history.replaceState('name', 'title', '/path');
// popstate
window.onpopstate = function(){
    console.log(window.location.href);
    console.log(window.location.pathname);
    console.log(window.location.hash);
    console.log(window.location.search);
}