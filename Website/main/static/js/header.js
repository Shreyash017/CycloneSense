// For Navbar active link
// Source: https://stackoverflow.com/a/70267174/22150559

$(function () {
    $('a').each(function () {
        if ($(this).prop('href') === window.location.href) {
            $(this).css({ "font-weight": "600" });
        }
    })
});