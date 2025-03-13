export default function hasValuesFromArray(set, array) {
  if (array.every((num) => set.has(num))) {
    return true;
  }
  return false;
}
