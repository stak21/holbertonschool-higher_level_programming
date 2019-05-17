#!/usr/bin/node
const addClassHeader = () => {
  $('header').addClass('red');
};

$('div#red_header').click(addClassHeader);
