class BaseConversion {
  constructor(radix) {
    this.base = radix;
  }

  // divide number by base and keep remainder for base conversion of 
  // non-fractional numbers
  convert(number) {
    let numberStr = "";
    let n = number;

    do {
      const remainder = n % this.base;
      n = Math.floor(n / this.base);
      numberStr = numberStr + remainder;
    } while (n > 0);

    return +numberStr.split("").reverse().join("");
  }
}
