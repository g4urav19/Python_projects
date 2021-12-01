#bankexcep.py
class DepositError(Exception):pass
class WithdrawError(Exception):pass
class InSuffFundError(BaseException):pass