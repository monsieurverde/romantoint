import sys
import string

def romanToInt(roman_numeral):
       
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        num = 0
        for items in roman_numeral:
            curr = roman[items]
            num += curr

            if curr > prev:
                num -= 2 * prev
            prev = curr

        return num

def main():
    test_numeral = "III"
    test = romanToInt(test_numeral)
    print(test)

if __name__ == '__main__':
    main()