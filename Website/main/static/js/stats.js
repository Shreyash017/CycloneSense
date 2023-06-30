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

