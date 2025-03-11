export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }

    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }

    if (!Array.isArray(students)) {
      throw new TypeError('Students mus be an array');
    }

    if (!students.every((item) => typeof item === 'string')) {
      throw new TypeError('Every elements of Students muste be a string');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  // name getter and setter
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // length getter and setter
  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  // students getter and setter
  get students() {
    return this._students;
  }

  set students(value) {
    if (!Array.isArray(value)) {
      throw new TypeError('Students mus be an array');
    }

    if (!value.every((item) => typeof item === 'string')) {
      throw new TypeError('Every elements of Students muste be a string');
    }
    this._students = value;
  }
}
