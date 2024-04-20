let totalTime = 240; // Total time in seconds (4 minutes)
const timerElement = document.getElementById('timer');

function startTimer(duration, display) {
  let timer = duration,
    minutes,
    seconds;
  const interval = setInterval(function () {
    minutes = parseInt(timer / 60, 10);
    seconds = parseInt(timer % 60, 10);

    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    display.textContent = minutes + ':' + seconds;

    if (--timer < 0) {
      clearInterval(interval);
      display.textContent = 'Time is up!';
    }
  }, 1000);
}

window.onload = function () {
  startTimer(totalTime, timerElement);
};
