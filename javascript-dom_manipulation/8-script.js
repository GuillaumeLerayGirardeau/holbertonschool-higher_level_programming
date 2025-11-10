#!/usr/bin/node

/* Fetches from https://hellosalut.stefanbohacek.com/?lang=fr and displays the value of hello */

document.addEventListener('DOMContentLoaded', fetchHello());

async function fetchHello () {
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
    const helloData = await response.json();
    const helloID = document.getElementById('hello');
    helloID.innerHTML = helloData.hello;
  } catch (error) {
    console.error(error);
  }
}
