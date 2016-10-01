def hamming_distance(codeword_one, codeword_two):
    bitwise_result = bin(int(codeword_one, 2) ^ int(codeword_two, 2))
    result = 0
    for bit in bitwise_result[2:]:
        if (bit == '1'):
            result += 1

    print("For %s and %s the Hamming distance is %s." % (codeword_one, codeword_two, result))
    return result

hamming_distance("10001001", "10110001")           
