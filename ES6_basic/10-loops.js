export default function appendToEachArrayValue(array, appendString) {
  for (let [index, value] of array) {
    array[index] = appendString + value;
  }

  return array;
}
