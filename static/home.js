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
    } else {
      alert('Incorrect answer.');
    }

    // Submit the form to let Flask handle the redirection
    form.submit();
  });
});
