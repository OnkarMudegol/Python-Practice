#you are given rate of gold when it was bought and current rate at which it will be sold
#find out the profit or loss you will incur
old_price = int(input())
new_price = int(input())
if old_price<new_price:
    proft = new_price - old_price
    print(proft)
elif new_price>old_price:
    loss = old_price-new_price
    print(loss)