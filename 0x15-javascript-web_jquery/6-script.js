#!/usr/bin/node
const newHeader = () => $('header').text('New Header!!!');
$('div#update_header').click(newHeader);
