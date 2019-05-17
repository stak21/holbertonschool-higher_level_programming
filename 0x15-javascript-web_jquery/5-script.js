#!/usr/bin/node
const addLI = () => $('ul.my_list').append('<li> Item </li>');
$('div#add_item').click(addLI);
