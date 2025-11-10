#!/usr/bin/node

/* Fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json */

fetchCharacter();

async function fetchCharacter () {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
    const charaName = await response.json();
    const starWarsName = charaName.name;
    const character = document.getElementById('character');
    character.innerHTML = starWarsName;
  } catch (error) {
    console.error(error);
  }
}
