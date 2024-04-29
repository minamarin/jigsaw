// document.addEventListener('DOMContentLoaded', function() {
//   let totalTime = 240; // Total time in seconds (4 minutes)
//   const timerElement = document.getElementById('timer');

//   if (timerElement) { // Check if the timer element exists
//     startTimer(totalTime, timerElement);
//   } else {
//     console.error('The timer element was not found!');
//   }
// });

// function startTimer(duration, display) {
//   let timer = duration,
//     minutes,
//     seconds;
//   const interval = setInterval(function () {
//     minutes = parseInt(timer / 60, 10);
//     seconds = parseInt(timer % 60, 10);

//     minutes = minutes < 10 ? '0' + minutes : minutes;
//     seconds = seconds < 10 ? '0' + seconds : seconds;

//     display.textContent = minutes + ':' + seconds;

//     if (--timer < 0) {
//       clearInterval(interval);
//       display.textContent = 'Time is up!';
//       // Add any additional actions here when the timer ends
//     }
//   }, 1000);
// }

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
      // You can add actions here such as disabling the puzzle or showing a modal when the time is up
    }
  }, 1000);
}
