class Atm(object):
    def __init__(YourCash,CashWithdrawl,BalanceEnquiry,CashDeposet=None):
        YourCash.CashWithdrawl=CashWithdrawl
        YourCash.BalanceEnquiry=BalanceEnquiry
        YourCash.CashDeposet=CashDeposet or {}
        your_cash=Atm(45,79,{420})