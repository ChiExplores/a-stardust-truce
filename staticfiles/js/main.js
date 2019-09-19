let card = document.querySelector('.card');
let button = document.querySelector('.flip-to-rear');
let button2 = document.querySelector('.btn-rear');

if (button) {
  button.addEventListener( 'click', function() {
    card.classList.toggle('is-flipped');
  });
}

if (button2) {
  button2.addEventListener( 'click', function() {
      card.classList.toggle('is-flipped');
  });
}