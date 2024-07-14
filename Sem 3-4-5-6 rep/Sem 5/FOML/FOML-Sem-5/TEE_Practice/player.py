class Player:
    def __init__(self, pid):
        self.query = {"template": "results"}
        self.playerid = pid
        self.pdata = []
    
    def totalstats(self, params):
        self.query.update(params)