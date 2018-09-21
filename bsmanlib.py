import datetime

class Balance:
    time = 0
    amount = 0

class Payments:
    from_user = ""
    to_user = ""
    amount = 0
    def __init__(self, from_user, to_user, amount):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount
    
    


class Bewohner:
    fullname = ""
    name = "" # Username
    befreit = False
    Balance current_balance
    movin_date = 0
    movout_date = 0
    def __init__(self, fullname, name, befreit):
        self.fullname = fullname
        self.name = name
        self.befreit = befreit
    def movin(x):
        movin = x
    def movout(x):
        movout = x
        

class Wohngemeinschaft:
    number = 0
    Bewohner = {}
