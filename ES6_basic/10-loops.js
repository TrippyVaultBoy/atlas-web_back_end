export default function appendToEachArrayValue(array, appendString) {
    for (let element of array) {
      array[element] = appendString + array[element];
    }

    return array;
  }