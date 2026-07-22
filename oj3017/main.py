"""Bill"""
def main():
    """cal bill"""
    foodprice = int(input())
    if foodprice <= 500:
        fee = 50
    elif 500 < foodprice <= 10000:
        fee = foodprice*0.1
    else:
        fee = 1000
    vat7 = (foodprice+fee)*0.07
    print(f"{(foodprice+fee)+vat7:.2f}")

main()
