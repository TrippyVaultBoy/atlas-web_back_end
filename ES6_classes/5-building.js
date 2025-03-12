export default class Building {
  constructor(sqft) {
    if (typeof this.evacuationWarningMessage !== 'function') {
      throw new TypeError('Class extending Building must override evacuationWarningMessage');
    }
    if (new.target === Building) {
      throw new Error("Cannot instantiate an abstract class.");
    }
    if (this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error("Class extending Building must override evacuationWarningMessage");
    }
    this._sqft = sqft;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }

  // sqft getter and setter
  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Value must be a number');
    }
    this._sqft = value;
  }
}
