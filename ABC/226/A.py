from decimal import Decimal, ROUND_HALF_UP

def main():
    x = input()
    print(Decimal(x).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    main()
