
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12
for i in range(0,12):
    minimum_payment = balance * monthlyPaymentRate

    balance -= minimum_payment
    interest = balance * monthlyInterestRate
    balance += interest

print ("Remaining balance: " + str (round(balance,2)))