#!/usr/bin/node
exports.nbOccurences = (list, searchElement) => {
  let count = 0;
  list.forEach(num => {
    if (num === searchElement) {
      count += 1;
    }
  }
  )
  return count;
}
