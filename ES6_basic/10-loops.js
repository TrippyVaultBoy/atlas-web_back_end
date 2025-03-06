export default function appendToEachArrayValue(array, appendString) {
    for (let element of array) {
      let value = array[idx];
      array[idx] = appendString + value;
    }

    return array;
  }