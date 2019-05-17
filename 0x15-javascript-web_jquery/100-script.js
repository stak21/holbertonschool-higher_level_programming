#!/usr/bin/node
const colorUpdate = () => {
  let header = document.querySelector('HEADER');
  header.style.color = '#FF0000';
};
document.addEventListener('DOMContentLoaded', colorUpdate);
