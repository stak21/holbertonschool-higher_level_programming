#!/usr/bin/node
const toggleClassRed = () => {
  $('header').toggleClass('red green');
};

$('div#toggle_header').click(toggleClassRed);
