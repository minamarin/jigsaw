// document.addEventListener('DOMContentLoaded', function () {
//   const submitButton = document.querySelector('.submit-button');
//   const form = submitButton.closest('form');
//   const choices = form.querySelectorAll('input[type="radio"]');

//   form.addEventListener('submit', function (event) {
//     event.preventDefault(); // Prevent the form from submitting normally

//     let selectedChoice = null;
//     choices.forEach((choice) => {
//       if (choice.checked) {
//         selectedChoice = choice.value;
//       }
//     });

//     if (!selectedChoice) {
//       alert('Please select an answer.');
//       return;
//     }

//     if (selectedChoice === correctAnswerId) {
//       alert('Correct answer!');
//     } else {
//       alert('Incorrect answer.');
//     }

//     // After showing the alert, submit the form
//     // If you have problems with how data is submitted, consider removing 'event.preventDefault()' and let the form submit naturally
//     form.submit(); // This should be used only if needed
//   });
// });

document.addEventListener('DOMContentLoaded', function () {
  const submitButton = document.querySelector('.submit-button');
  const form = submitButton.closest('form');
  const choices = form.querySelectorAll('input[type="radio"]');

  form.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    let selectedChoice = null;
    choices.forEach((choice) => {
      if (choice.checked) {
        selectedChoice = choice.value;
      }
    });

    if (!selectedChoice) {
      alert('Please select an answer.');
      return;
    }

    // Show alert based on selection
    if (selectedChoice === correctAnswerId) {
      alert('Correct answer!');
      form.submit(); // Let Flask handle the redirect to the next quiz
    } else {
      alert('Incorrect answer.');
      location.reload(); // Refresh the page for incorrect answer
    }
  });
});

// document.addEventListener('DOMContentLoaded', function () {
//   const form = document.querySelector('form');
//   form.onsubmit = function (event) {
//     const selectedChoice = document.querySelector(
//       'input[name="answer"]:checked'
//     );
//     if (!selectedChoice) {
//       alert('Please select an answer.');
//       event.preventDefault(); // Prevent form submission if no answer is selected
//     }
//   };
// });
