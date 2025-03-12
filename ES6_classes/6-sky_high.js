import Building from '5-building'

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    if (typeof floors !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    super(sqft);
    this._floors = floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${self._floors} floors`;
  }

  // sqft getter and setter
  get sqft() {
    return super.sqft;
  }

  set sqft(value) {
    super.sqft = value;
  }

  // floors getter and setter
  get floors() {
    return self._floors;
  }

  set floors(value) {
    if (typeof floors !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    self._floors = value;
  }
}
