import pandas as pd
import numpy as np
from routes import MatchDetails

CONST_API_KEY = 'CD9FDBE61E8E5E51C643ACD7C29852DB'
test_match_id = 1275185095

myMatch = MatchDetails(CONST_API_KEY,test_match_id)

myMatchDict = pd.DataFrame(myMatch.getHeroes())

pd.myMatchDict.to_csv("C:\\Users\\esegrave\\Documents\\Repos\\dota2api\\api\\test.csv")