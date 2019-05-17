#!/usr/bin/node
$.get('https://swapi.co/api/people/5/?format=json', {},
  (data, textStatus, jqXHR) => {
    $('div#character').text(data.name);
  });
