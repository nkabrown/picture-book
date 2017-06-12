export class TwoLetterCodes {
  constructor(d) {
    this.data = d;
  }

  init() {
    let langCodeMap = new Map();
    this.data.forEach(d => {
      langCodeMap.set(d.code, d.language);
    });
    return langCodeMap;
  }
}

// testing
/*d3.csv('../scrapers/iso_639_1_codes.csv', (error, data) => {
  if (error) throw error;

  const langMap = new TwoLetterCodes(data).init();
  console.log(langMap);

  console.log(langMap.get('cy'));
});*/
