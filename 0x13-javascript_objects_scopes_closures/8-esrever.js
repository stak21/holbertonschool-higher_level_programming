#!/usr/bin/node
exports.esrever = (list) => {
  let length = list.length - 1;
  let newList = [];
  for (length; length > 0; length -= 1) {
    newList.push(list[length]);
  }
  return newList;
};
