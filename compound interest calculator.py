#compound interest calculator

principle = float(input("Enter the Principle amount: "))
interest = float(input("Enter the Interest rate: "))
time_period = float(input("Enter the Time period: "))
total_time = float(input("Enter the Total time: "))

n = total_time/time_period
n=int(n)
for n in range(1,n+1):
    total_amount =principle+principle*(interest/100)
    principle = total_amount

print(f'The total amount is : {total_amount}')
