#!/usr/bin/node
$.get('https://swapi.co/api/films/?format=json', {},
  (data, textStatus, jqXHR) => {
    for (let movie of data.results) { $('ul#list_movies').append('<li>' + movie.title + '</li>'); }
  });
