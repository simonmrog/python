initial_balance = 2000000
interest_rate = 0.024575
term = 12

current_balance = initial_balance
payment_to_capital = initial_balance / term

for month in range(0, term, 1):
    interests = current_balance * interest_rate
    current_balance = current_balance - payment_to_capital if current_balance - payment_to_capital > 0 else 0
    total_payment = payment_to_capital + interests
    print(f"Month: {month + 1}, Current Balance: {current_balance:.2f}, Interests: {interests:.2f}, Payment to Capital: {payment_to_capital:.2f}, Total Payment: {total_payment:.2f}")
