
balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12

def get_remainder(balance, guessMinimum):
    remain = balance
    for i in range(0, 12):
        balance = remain - guessMinimum
        monthInterest = monthlyInterestRate * balance
        remain = balance + monthInterest

    return remain

lower_bound = balance / 12
upper_bound = (balance * (1 + monthlyInterestRate)**12) / 12.0

payment = 10
done = False
while not done:

    guess_minimum = (lower_bound + upper_bound) / 2
    print ("Lower = " + str(lower_bound) + " Upper = " + str(upper_bound))

    remain = get_remainder(balance, guess_minimum)
    #print ("Remain = " + str(remain))

    if abs(remain) < 0.01:
        done = True
    else:
        if remain < 0:
            upper_bound = guess_minimum
            remain = balance
        else:
            lower_bound = guess_minimum
            remain = balance

print("Lowest Payment: " +str(round(guess_minimum,2)))