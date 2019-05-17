#!/usr/bin/node
const updateHello = $.get('https://fourtonfish.com/hellosalut/?lang=fr', {},
  (data, textStatus, jqXHR) => {
    $('div#hello').text(data.hello);
  });
$(document).ready(updateHello);
