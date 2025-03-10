
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (as a decimal): "))


total_interest = 0  


print("\nFormatted Output")
print(f"{'Year':<5} {'Beginning Balance':<15} {'Ending Balance':<15}")


for year in range(1, 6):
    interest = principal * rate 
    ending_balance = principal + interest 

    print(f"{year:<5} ${principal:,.2f}   ${ending_balance:,.2f}")

   
    principal = ending_balance
    total_interest += interest  
print(f"\nTotal interest earned: ${total_interest:,.2f}")