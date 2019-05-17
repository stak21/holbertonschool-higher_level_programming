#!/usr/bin/node
const updateColor = () => {
  $('header').css('color', 'red');
};

$('div#red_header').click(updateColor);
