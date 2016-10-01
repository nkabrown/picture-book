// the number of bit positions in which two binary numbers differ is called the Hamming distance
// if two codewords are a Hamming distance d apart, it will require d single-bit errors to convert one into the other
// so given any two n-bit codewords determine how many corresponding bits differ

function hammingDistance(codewordOne, codewordTwo) {
  // compute the bitwise Boolean EXCLUSIVE OR of the two codewords
  var bitwiseXORResult = (parseInt(codewordOne, 2) ^ parseInt(codewordTwo, 2)).toString(2);
  // count the number of one bits in the result 
  let result = 0;
  for (char of bitwiseXORResult) {
    if (char === '1') result += 1; 
  }
  console.log('For %s and %s the Hamming distance is %s.', codewordOne, codewordTwo, result);
  return result;
}

hammingDistance('10001001', '10110001');

// see discussion of error-correcting codes and hamming distance in Structured Computer Organization 5th ed. Andrew S. Tanenbaum p. 73-77
