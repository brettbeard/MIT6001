
balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12

def get_balance(p, rate, payment):
    for i in range(0,12):
        p -= payment
        interest = p * rate
        p += interest

    return p

payment = 10
done = False
while not done:

    result = get_balance(balance, monthlyInterestRate, payment)

    print ("Payment = " + str(payment) + " Result = " + str(result))

    if result <= 0:
        print("Lowest Payment: " + str(payment))
        break
    else:
        payment += 10



