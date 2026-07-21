"""season"""
def main():
    """season cal"""
    month = int(input())
    day = int(input())

    if month == 1 or month == 2 or month == 3 and day < 21:
        print("winter")
    if month == 4 or month == 5 or month == 6 and day < 21:
        print("spring")
    if month == 7 or month == 8 or month == 9 and day < 21:
        print("summer")
    if month == 10 or month == 11 or month ==  12 and day < 21:
        print("fall")
    if month == 3 and day >= 21:
        print("spring")
    if month == 6 and day >= 21:
        print("summer")
    if month == 9 and day >= 21:
        print("fall")
    if month == 12 and day >= 21:
        print("winter")
main()
