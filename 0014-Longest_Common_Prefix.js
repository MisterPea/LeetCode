/*
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 * e.g. str = ['flower', 'flow', 'flight'] returns 'fl'
*/
/**
 * @param {string[]} strings
 * @return {string}
 */
function longestCommonPrefix(strings) {
  if (strings.length === 1) {
    return strings[0];
  }

  const matched = [];
  const ordered = strings.sort((a, b) => a.length - b.length);

  // Loop once through the shortest string, which is why we sorted.
  for (let i = 0; i < ordered[0].length; i += 1) {
    const currentLetter = ordered[0][i];
    let orderedIndex = 1;

    // Vertically scan through each word at each index.
    // If we get through the list, we append the array and increment the loop.
    while (orderedIndex < ordered.length) {
      if (ordered[orderedIndex][i] === currentLetter) {
        if (orderedIndex === ordered.length - 1) {
          matched.push(currentLetter);
        }
        orderedIndex += 1;
      } else {
        // If there's not a match, return what we have.
        return matched.join('');
      }
    }
  }
  return matched.join('');
}
