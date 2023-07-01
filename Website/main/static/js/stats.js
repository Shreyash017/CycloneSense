// For stats counter in home page
// Source (for counter logic): https://codingartistweb.com/2021/10/how-to-create-responsive-count-up-animation-with-javascript/
// Source (for scroll event): https://stackoverflow.com/a/5036892/22150559

let valueDisplays = document.querySelectorAll(".counter");
let timestart = 4000;
var target = $(".stats").offset().top;

function statistics() {
    valueDisplays.forEach((valueDisplay) => {
        let startValue = 0;
        let endValue = parseInt(valueDisplay.getAttribute("upto"));
        let duration = Math.floor(timestart / endValue);

        let counter = setInterval(function () {
            startValue += 1;
            valueDisplay.textContent = startValue;
            if (startValue == endValue) {
                clearInterval(counter);
            }
        }, duration);
    });
}

var interval = setInterval(function () {
    if ($(window).scrollTop() >= target - 500) {
        statistics();
        clearInterval(interval);
    }
}, 250);
