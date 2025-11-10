#!/usr/bin/node

/* Updates the text of the header element to New Header!!! when the user clicks */

const listButton = document.getElementById('update_header');
listButton.addEventListener('click', () => changeHeader());

function changeHeader () {
  const firstHeader = document.querySelector('header');
  firstHeader.innerHTML = 'New Header!!!';
}
