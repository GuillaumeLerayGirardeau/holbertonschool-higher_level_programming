#!/usr/bin/node

/* adds the class red to the header element when the user clicks */

const redHeader = document.getElementById('red_header');
redHeader.addEventListener('click', () => addClassRed(redHeader));

function addClassRed (a) {
  a.classList.add('red');
}
