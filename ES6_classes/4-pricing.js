import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      TypeError('Amount must be a number');
    }
    if (typeof currency !== 'currency') {
      TypeError('Currency must be a currency');
    }

    this._amount = amount;
    this._currency = currency;
  }

  // amount getter and setter
  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value !== 'number') {
      TypeError('Value must be a number');
    }
    this._amount = value;
  }

  // currency getter and setter
  get currency() {
    return this._currency;
  }

  set currency(value) {
    if (typeof value !== 'currency') {
      TypeError('Value must be a currency');
    }
    this._currency = value;
  }

  displayFullPrice() {
    return `${this._amount} ${Currency.name} (${Currency.code})`
  }

  convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') {
      TypeError('Amount must be a number');
    }
    if (typeof conversionRate !== 'number') {
      TypeError('ConversionRate must be a number');
    }
    return amount * conversionRate;
  }
}
