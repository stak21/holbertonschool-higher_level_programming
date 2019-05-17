#!/usr/bin/node
const translate = () => {
  let url = 'https://www.fourtonfish.com/hellosalut/';
  let lang = $('input#language_code').val();
  $.get(url, { lang: lang }, (data, textStatus, jqXHR) => {
    $('div#hello').text(data.hello);
  });
};
const ready = () => $('input#btn_translate').click(translate);
const readyEnter = () => $('input#language_code').keypress((e) => {
  let key = e.which;
  if (key === 13) {
    $('input#btn_translate').click();
    return false;
  }
});

document.addEventListener('DOMContentLoaded', ready);
document.addEventListener('DOMContentLoaded', readyEnter);
