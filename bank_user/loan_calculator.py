import numpy_financial as npf
import numpy as np

class LoanCalculator():    
    __annual_interest = 0.07
    __compound_periods = 12
    __payments_per_year = 12
    
    def __init__(self, loan_amount, loan_years):
        self.loan_amount = loan_amount
        self.loan_years = loan_years
        

    def get_rate_per_period(self):
        return round(pow((1+(self.__annual_interest/self.__compound_periods)),(self.__compound_periods / self.__payments_per_year) ) - 1, 5)
    
    def get_monthly_payment(self):
        rate_per_period = self.get_rate_per_period()
        pay_per_month = -npf.pmt(rate_per_period, self.loan_years * self.__payments_per_year, self.loan_amount)
        return round(pay_per_month, 2)
    
    def get_num_of_payments(self):
        rate_per_period = self.get_rate_per_period()
        monthly_payment = self.get_monthly_payment()
        return npf.nper(rate_per_period, monthly_payment, -self.loan_amount).round().astype(int)

    def get_total_payment(self):
        return round(self.get_num_of_payments() * self.get_monthly_payment(), 2)

    def get_total_interest(self):
        return round(self.get_total_payment() - self.loan_amount, 2)

    
    def get_result_summary(self):
        return {
            "loan_amount": self.loan_amount,
            "loan_years": self.loan_years,
            "rate_per_period": self.get_rate_per_period(),
            "monthly_payment": self.get_monthly_payment(),
            "num_of_payments": self.get_num_of_payments(),
            "total_payment": self.get_total_payment(),
            "total_interest": self.get_total_interest()
        }

    def generate_Schedule(self):
        table_data = [] 

        table_data.append( {
                "year_number":0,
                "cum_interest": 0.0, 
                "cum_principal" : 0.0, 
                "balance" : self.loan_amount,
                "cum_payments" :  0.0,
                "yearly_payments" : 0.0,
                "yearly_interest": 0.0
            })
        rate_per_period = self.get_rate_per_period()
        monthly_payment = self.get_monthly_payment()

        for i in range(1,self.loan_years+1):
            new_balance = npf.fv(rate_per_period, self.__payments_per_year, monthly_payment, -table_data[i-1]["balance"])
            new_cum_principal = self.loan_amount - new_balance
            new_cum_payments = i * monthly_payment * self.__payments_per_year
            new_cum_interest = new_cum_payments - new_cum_principal
            new_yearly_payments = table_data[i-1]["balance"] - new_balance
            new_yearly_interest = new_cum_payments - table_data[i-1]["cum_payments"] - new_yearly_payments
            table_data.append({
                "year_number": i,
                "cum_interest": round(new_cum_interest, 2), 
                "cum_principal" : round(new_cum_principal, 2), 
                "balance" : round(new_balance, 2),
                "cum_payments" :  round(new_cum_payments, 2),
                "yearly_payments" : round(new_yearly_payments, 2),
                "yearly_interest": round(new_yearly_interest, 2)})
        
        return table_data

