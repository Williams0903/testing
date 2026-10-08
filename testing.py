#no1
credits = int(input('applicats credit score = '))
# annual
if credits < 600 :
        print('loan denied: loan credit rating')
else:
        annual_income = int(input('whats your annual income = 67'))
        if credits >= 600 :
            if annual_income < 40000 :
                print('Loan status: conditional approval requires a co-signer')
            else:
                print('Loan status: full approval granted ')     