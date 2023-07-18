# You run a hovercraft factory. Your factory makes ten hovercrafts in a month. 
# Given the number of customers you got that month, did you make a profit? It costs you 2,000,000 to build a hovercraft, 
# and you are selling them for 3,000,000. You also pay 1,000,000 each month for insurance
# Task: 
# Determine whether or not you made a profit based on how many of the ten hovercrafts you were able to sell that month.
# Input Format: 
# An integer that represents the sales that you made that month.
# Output Format: 
# A string that says 'Profit', 'Loss', or 'Broke Even'.
# Broke Even Point -> Modal = Omzet -> Profit=Loss=0

modal = 21000000

def formula(sales):
  omzet = sales*3000000
  a = modal - omzet
  if modal > omzet:
     print(f"You got the loss with amount: {a:,} USD")
  elif modal == omzet:
     print("You got Broke Even")
  else:
     print(f"You got the profit with amount: {abs(a):,} USD")

def data():
   sales = int(input("How many customers you get this month? "))
   if sales < 0:
     print("Please input the correct number, please!")
     formula()
   elif sales > 10:
     print("We're sorry for our company only been able to produce ten hoverboards this month, so the remaining will not be made and paid")
   else:
    formula(sales)

data()
