#!/usr/bin/node

/* Fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json */

fetchCharacter();

async function fetchCharacter () {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    const filmData = await response.json();
    const films = filmData.results;
    const filmList = document.getElementById('list_movies');
    for (i = 0; i < films.length; i++) {
      const listElement = document.createElement('li');
      listElement.textContent = films[i].title;
      filmList.appendChild(listElement);
    }
  } catch (error) {
    console.error(error);
  }
}
