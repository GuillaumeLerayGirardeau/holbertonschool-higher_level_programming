#!/usr/bin/node

/* updates the text color of the header element to red (#FF0000) when the user clicks */

const redHeader = document.getElementById('red_header');
redHeader.addEventListener('click', () => makethingsred(redHeader));

function makethingsred (a) {
  a.style.color = '#FF0000';
}
