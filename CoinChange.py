quarters=0
dimes=0
nickels=0
pennies=0
amount=125
while(amount!=0):
    if amount<5:
        pennies=amount
        amount=0
        break

    if 5<=amount<10:
        nickels=amount/5
        amount=amount%5

    if 10<=amount<25:
        dimes=amount/10
        amount=amount%10

    if 25<=amount:
        quarters=amount/25
        amount=amount%25


print "Pennies:{}".format(pennies)
print "Nickels:{}".format(nickels)
print "Dimes:{}".format(dimes)
print "Quarters:{}".format(quarters)
