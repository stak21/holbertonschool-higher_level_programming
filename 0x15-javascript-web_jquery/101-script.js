#!/usr/bin/node
const addItem = () => {
  $('ul.my_list').append('<li>Item</li>');
};
const removeItem = () => {
  $('ul.my_list li:last-child').remove();
};
const clearList = () => {
  $('ul.my_list').empty();
};
const colorUpdate = () => {
  $('div#add_item').click(addItem);
  $('div#remove_item').click(removeItem);
  $('div#clear_list').click(clearList);
};
document.addEventListener('DOMContentLoaded', colorUpdate);
