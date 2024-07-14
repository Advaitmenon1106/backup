import data
class Player:
    def __init__(self, pid):
        self.query = {"template":"results"}
        self.playerid=pid
        self.pdata=[]

    def totalstats(self, params):
        self.query.update(params)
        process=data.Data(self.query)
        totalstat=process.playerdata(self.playerid)
        return totalstat
    
    def innlist(self, params):
        self.query.update(params)
        self.query["view"] = "innings"
        process = data.Data(self.query)
        inns = process.playerdata(self.playerid)
        return inns

    def matchlist(self, params):
        self.query.update(params)
        self.query["view"] = "matches"
        process = data.Data(self.query)
        matches = process.playerdata(self.playerid)
        return matches

    def cavg(self, params):
        self.query.update(params)
        self.query["view"] = "cumulative"
        process = data.Data(self.query)
        cum = process.playerdata(self.playerid)
        return cum

    def savg(self, params):
        self.query.update(params)
        self.query["view"] = "series"
        process = data.Data(self.query)
        savg = process.playerdata(self.playerid)
        return savg

    def gavg(self, params):
        self.query.update(params)
        self.query["view"] = "ground"
        process = data.Data(self.query)
        gavg = process.playerdata(self.playerid)
        return gavg

    def results(self, params):
        self.query.update(params)
        self.query["view"] = "results"
        process = data.Data(self.query)
        results = process.playerdata(self.playerid)
        return results

    def maw(self, params):
        self.query.update(params)
        self.query["view"] = "awards_match"
        process = data.Data(self.query)
        maw = process.playerdata(self.playerid)
        return maw

    def saw(self, params):
        self.query.update(params)
        self.query["view"] = "awards_series"
        process = data.Data(self.query)
        saw = process.playerdata(self.playerid)
        return saw

#Batting list    
    def pship_total(self, params):
        self.query.update(params)
        self.query["view"] = "fow_summary"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            pships = process.playerdata(self.playerid)
            return pships
        else:
            print("Available only for batting data")

    def pship_list(self, params):
        self.query.update(params)
        self.query["view"] = "fow_list"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            pships = process.playerdata(self.playerid)
            return pships
        else:
            print("Available only for batting data")

    def pship_total(self, params):
        self.query.update(params)
        self.query["view"] = "fow_summary"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            plist = process.playerdata(self.playerid)
            return plist
        else:
            print("Available only for batting data")

    def dis_total(self, params):
        self.query.update(params)
        self.query["view"] = "dismissal_summary"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            dis = process.playerdata(self.playerid)
            return dis
        else:
            print("Available only for batting data")
    
    def bow_total(self, params):
        self.query.update(params)
        self.query["view"] = "bowler_summary"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            bt = process.playerdata(self.playerid)
            return bt
        else:
            print("Available only for batting data")
    
    def fl_total(self, params):
        self.query.update(params)
        self.query["view"] = "fielder_summary"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            flt = process.playerdata(self.playerid)
            return flt
        else:
            print("Available only for batting data")
    
    def dis_list(self, params):
        self.query.update(params)
        self.query["view"] = "dismissal_list"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            disl = process.playerdata(self.playerid)
            return disl
        else:
            print("Available only for batting data")

#Bowling data
    def dis_sum(self, params):
        self.query.update(params)
        self.query["view"] = "dismissal_summary"
        if self.query["type"]=="bowling":
            process = data.Data(self.query)
            dism = process.playerdata(self.playerid)
            return dism
        else:
            print("Available only for bowling data")
    
    def b_sum(self, params):
        self.query.update(params)
        self.query["view"] = "batsman_summary"
        if self.query["type"]=="bowling":
            process = data.Data(self.query)
            bats = process.playerdata(self.playerid)
            return bats
        else:
            print("Available only for bowling data")

    def f_sum(self, params):
        self.query.update(params)
        self.query["view"] = "fielder_summary"
        if self.query["type"]=="bowling":
            process = data.Data(self.query)
            fsum = process.playerdata(self.playerid)
            return fsum
        else:
            print("Available only for bowling data")
        
    def wlist(self, params):
        self.query.update(params)
        self.query["view"] = "dismissal_list"
        if self.query["type"]=="bowling":
            process = data.Data(self.query)
            dlist = process.playerdata(self.playerid)
            return dlist
        else:
            print("Available only for bowling data")
    