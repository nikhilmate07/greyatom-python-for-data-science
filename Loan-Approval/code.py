# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
categorical_var = bank_data.select_dtypes(include = 'object')
#print(categorical_var)
numerical_var = bank_data.select_dtypes(include = 'number')
#print(numerical_var)
print(categorical_var.shape)
print(numerical_var.shape)
banks = bank_data.drop(columns = 'Loan_ID')
print(bank_data.isnull().sum())
print(banks.shape)
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
print(bank_mode)
banks.fillna(bank_mode ,inplace = True)
print(banks.isnull().sum().values.sum())
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values=["LoanAmount"],aggfunc=np.mean)
print(avg_loan_amount['LoanAmount'][1],2)
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)
percentage_se = (loan_approved_se * 100 / 614)
#percentage_se=percentage_se[0]
print("%.2f"%percentage_se)

percentage_nse = (loan_approved_nse * 100 / 614)
#percentage_nse=percentage_nse[0]
print ("%.2f"%percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12 )
big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()
print("%.2f"%mean_values.iloc[1,0],2)




