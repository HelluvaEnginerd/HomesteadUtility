#!/usr/bin/python

import math
import locale

# principal = amount borrowed (house price - down payment applied towards overall price)
# r = annual interest rate (APR) / 12 months
# N = total number of payments being made (30 year fixed = 30 years * 12 payments/year = 360 payments)
# other factors: mortgage insurance, homeowners insurance, HOA, property taxes

# for currency formatting
locale.setlocale( locale.LC_ALL, '' )

principal = float(input("What is the principal amount on the house loan? "))
apr = float(input("What is the interest rate on the loan? "))/100
loanTerm = int(input("What is the term on the loan (years)? "))
propTaxRate = float(input("What is the property tax rate? "))/100
overallHomeValue = float(input("What is the overall home value? "))
hoaPayment = float(input("Estimated HOA payment? "))
homeOwnersInsurance = float(input("Estimated homeowners Insurance payment? "))
mortgageInsurance = float(input("Estimated mortgage insurance payment? "))

r = apr/12
# print(f"r: {r}")
N = loanTerm*12
# print(f"N: {N}")
monthlyPropertyTaxes = propTaxRate*overallHomeValue/12
# print(f"monthlyPropertyTaxes: {locale.currency(monthlyPropertyTaxes)}")

# monthy mortgage payment = principal * (r*(1+r)^N)/((1+r)^N-1)
monthlyMortgagePayment = principal * (r*math.pow((1+r),N))/(math.pow((1+r),N)-1)
overallPayment = monthlyMortgagePayment + monthlyPropertyTaxes/12 + hoaPayment + homeOwnersInsurance + mortgageInsurance

print(f"monthly loan payment: {locale.currency(monthlyMortgagePayment)}")
print(f"monthly overallPayment: {locale.currency(overallPayment)}")