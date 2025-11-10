#!/usr/bin/node

/* adds the class red to the header element when the user clicks */

const toggleHeader = document.getElementById('toggle_header');
toggleHeader.addEventListener('click', () => changeColor(toggleHeader));

function changeColor (a) {
  if (!a.classList.toggle('green')) {
    a.classList.toggle('red');
  } else {
    a.classList.remove('red');
  }
}
