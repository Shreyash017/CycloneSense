// For Navbar active link
// Source: https://stackoverflow.com/a/70267174/22150559
// Source (Chatgpt): https://chat.openai.com/share/e7770bc9-c66d-4478-8977-556d26d0559a

$(function () {
    // This are to ensure the otehr append links dont interfer with the active link
    // That is http://127.0.0.1:8000/analysis/#analysis will be treated as http://127.0.0.1:8000/analysis/
    var currentPath = new URL(window.location.href).pathname;
    var validPaths = ['/', '/analysis/', '/about/'];

    $('a').each(function () {
        var href = new URL($(this).prop('href')).pathname;
        if (validPaths.includes(href) && href === currentPath) {
            $(this).css({ "font-weight": "600" });
        }
    });
});
