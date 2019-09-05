import sys
import string

def romanToInt(s):
       
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        t = 0
        for i in s:
            curr = roman[i]
            t += curr

            if curr > prev:
                t -= 2 * prev
            prev = curr

        return t

def main():
    x = "III"
    test = romanToInt(x)
    print test

if __name__ == '__main__':
    main()