function do_something(e) {
    for (var t = "", n = e.length - 1; n >= 0; n--)
    t += e[n];
    return t
}
setTimeout(function () {
    do_elsesomething("XX")
}, 300);

function do_elsesomething(e) {
    var a = do_something(e + "successXX")
    console.log(a)
}
