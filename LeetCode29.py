class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            answer = "ZeroDivisionError: division by zero"
        else:
            divd, divs = abs(dividend), abs(divisor)
            quotient = 0
            while divd >= divs:
                doubled = divs
                double_count = 1
                while divd >= (doubled << 1):
                    doubled <<= 1
                    double_count <<= 1
                divd -= doubled
                quotient += double_count
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            answer = quotient
        else:
            answer = - quotient
        if answer > 2**31 - 1:
            answer = 2**31 - 1
        elif answer < - 2**31:
            answer = - 2**31
        return answer
            
