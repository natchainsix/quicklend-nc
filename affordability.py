def assess(customer, repayment):
    return "APPROVED" if customer["monthly_income"] * 12 > 20000 else "DECLINED"
