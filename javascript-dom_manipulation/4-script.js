#!/usr/bin/node

/* Adds a li element to a list when the user clicks on the element */

const listButton = document.getElementById('add_item');
listButton.addEventListener('click', () => addItem());

function addItem () {
  const listElement = document.createElement('li');
  listElement.textContent = 'Item';
  const list = document.getElementsByClassName('my_list')[0];
  list.appendChild(listElement);
}
