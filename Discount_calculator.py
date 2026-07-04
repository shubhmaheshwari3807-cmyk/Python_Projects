def apply_discount(price, discount=10):
    final_price=price-(price*discount/100)
    print(final_price)

apply_discount(100, 20)
apply_discount(100)

price=int(input("Enter price: "))
discount=int(input("Enter discount: "))

apply_discount(price, discount)