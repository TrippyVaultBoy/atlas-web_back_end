export default function appendToEachArrayValue(array, appendString) {
    for (let element of array) {
      let value = array[element];
      array[element] = appendString + value;
    }

    return array;
  }