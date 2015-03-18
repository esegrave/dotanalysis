import sys
sys.path.insert(0,'C:\\Users\\esegr_000\\Documents\\Repos')
sys.path.insert(0,'C:\\Users\\esegr_000\\Documents\\Repos\\dota2api\\api')
import pandas as pd
import numpy as np
import json
import util
import routes

CONST_API_KEY = 'CD9FDBE61E8E5E51C643ACD7C29852DB'
test_match_id = 1275185095
CONST_JSON_PATH = 'C:\\Users\\esegr_000\\Documents\\Repos\\dota2api\\api\\'

def loadJson(jsonPath, filename):
    with open(jsonPath+filename, 'r') as f:
        data = json.loads(f.read())
    return data

def getHeroAbilities(df, heroname):
    #def that returns the order of skill build for the Oracle player in the match
    #create dataframe of ability IDs and names for filtering on Oracle's
    abilDf = pd.DataFrame(loadJson(CONST_JSON_PATH, 'abilities.json')['abilities'], columns = ['name', 'id'])
    #create dataframe of hero IDs and names for filtering on Oracle
    heroDf = pd.DataFrame(loadJson(CONST_JSON_PATH, 'heroes.json')['heroes'], columns = ['name', 'id', 'localized_name'])
    mergeDf = pd.merge(df,heroDf, left_on = 'hero_id', right_on = 'id')
    oracleDf = mergeDf[mergeDf['localized_name'] == heroname]
    ability_upgrades = pd.DataFrame(oracleDf['ability_upgrades'][oracleDf.index[0]])
    ability_upgrades = pd.merge(ability_upgrades, abilDf, left_on = 'ability', right_on = 'id')
    return ability_upgrades

"""
myMatch = MatchDetails(CONST_API_KEY,test_match_id)

myMatchDict = pd.DataFrame(myMatch.getHeroes())

myMatchDict.to_csv("C:\\Users\\esegr_000\\Documents\\Repos\\dotanalysis\\sba\\sbatest.csv")"""