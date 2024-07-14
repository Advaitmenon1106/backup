import lxml
from urllib.parse import urlencode
from bs4 import BeautifulSoup as bs
import csv as csv
import pandas as pd
class Data:
    def __init__(self, params):
        self.params = params
        self.pgcounter=0
    def playerdata(self, pid):
        url="https://www.espncricinfo.com/cricketers/angelo-mathews-49764"
        encodedp=urlencode(self.params)
        url=url.format(encodedp, str(self.pgcounter)) #to format to simple html
        df=pd.read_html(url) 
        data=df[2] #df is dataframe aka table in pandas
        rqdata=data.loc[:, ~data.columns.str.startswith("Unnamed")] #tilde is "not"
        return rqdata
    def teamdata(self, limit=50):
        url="https://stats.espncricinfo.com/ci/engine/stats/index.html?{0}&page={1}"
        datalist=[]
        encodedp=urlencode(self.params)
        rlim=0
        while True:
            self.pgcounter += 1
            urlformat=url.format(encodedp, str(self.pgcounter))
            df=pd.read_html(urlformat)
            rlim += len(df[2]) #Row amount
            if df[2].iloc[df[2].index.get_loc(0),0] == "No records available to match this query":
                break
            else:
                if rlim<limit:
                    datalist.append(df[2])
                    break
                elif self.pgcounter==1 and rlim>limit:
                    datalist.append(df[2].iloc[:limit])
                    break
                else:
                    datalist.append(df[2].iloc[:len(df[2])-limit])
                    break