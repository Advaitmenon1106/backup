import data
class Team():
    def __init__(self):
        self.query={"type":"team", "template":"results"}
    
    def total(self, params, limit=50):
        self.query.update(params)
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def inns(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="innings"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def matches(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="matches"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def results(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="results"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def savg(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="series"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def gavg(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="ground"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def hosts(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="host"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def opps(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="opposition"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def years(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="year"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def seasons(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="season"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def misc(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="extras"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    
    def exinn(self, params, limit=50):
        self.query.update(params)
        self.query["view"]="extras_innings"
        process=data(self.query)
        dataset=process.teamdata(limit)
        return dataset
    