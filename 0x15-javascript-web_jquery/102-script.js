#!/usr/bin/node
let url = 'https://www.fourtonfish.com/hellosalut/';
const translate = () => {
  let lang = $('input#language_code').val();
  $.get(url, { lang: lang }, (data, textStatus, jqXHR) => {
    $('div#hello').text(data.hello);
  });
};
const ready = () => $('input#btn_translate').click(translate);
document.addEventListener('DOMContentLoaded', ready);
