#!/usr/bin/node

/* Fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json */

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(starWars => {
    const starWarsName = starWars.name;
    const character = document.getElementById('character');
    character.innerHTML = starWarsName;
})
