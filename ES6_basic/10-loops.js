export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    var value = array[idx];
    array[idx] = appendString + value;
  }

 return array;
}
