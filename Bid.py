import json

class Bid:
    def __init__(self, data):
        self.time=data["time"]
        self.user=data["user"]
        self.amount=data["amount"]
        self.auction=data["auction"]
        self.checksumUntilNow=None

    def addCheckSum(check):
        self.checksumUntilNow=check

    def getUser(self):
        return '{"user":'+self.user+'}'

    def getAmount(self):
        return self.amount

    def getRepr(self):
        return {"auction":self.auction, "user":self.user, "amount":str(self.amount), "time":self.time}