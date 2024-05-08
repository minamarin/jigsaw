document.addEventListener('DOMContentLoaded', function () {
  let totalTime = 240; // Total time in seconds (4 minutes)
  const timerElement = document.getElementById('timer');

  if (timerElement) {
    startTimer(totalTime, timerElement);
  } else {
    console.error('The timer element was not found!');
  }
});

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
      timeUpWarning(); // Call the timeUpWarning function when time is up
    }
  }, 1000);
}

function timeUpWarning() {
  // Create an alert to inform the user
  alert('Time is up! You will now be taken to the quiz.');
  // Redirect to the quiz page
  window.location.href = '/quiz/1'; 
}
