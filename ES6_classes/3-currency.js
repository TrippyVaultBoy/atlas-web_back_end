export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      new TypeError('Code must be a string');
    }

    if (typeof name !== 'string') {
      new TypeError('Name must be a string');
    }

    this._code = code;
    this._name = name;
  }

  // code getter and setter
  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof code !== 'string') {
      new TypeError('Code must be a string');
    }

    this._code = value;
  }

  // name getter and setter
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      new TypeError('Code must be a string');
    }

    this._name = value;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`
  }
}