import urllib
import urllib2
import json
import datetime

# CONST_API_KEY = "A00E92BAACE8BBA8F5BAF503584C9EA7"

class Heroes(object):
	"""
	Wrapper methods for the list of dota heroes
	Reference: https://wiki.teamfortress.com/wiki/WebAPI/GetHeroes
	@param string key  your valve api key
	"""
	def __init__(self, key):
		url = "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/?key="+key
		try:
			res = urllib2.urlopen(url).read()
			self.data = json.loads(res)['result']
		except urllib2.URLError, e:
			print 'Error in getHeroes.'
			self.data = None
	def get(self):
		"""
		GET raw data
		@return dict  the raw data
		"""
		return self.data
	def getCount(self):
		"""
		GET hero count
		@return int  count of heroes
		"""
		return self.data['count']
	def getNames(self):
		"""
		GETs hero names
		@return list  hero names
		"""
		names = []
		for hero in self.data['heroes']:
			# print hero['name']
			names.append(str(hero['name']))
		return names
	def getNameByID(self, id):
		"""
		GETs hero name corresponding to provided id
		@param int id  the hero id
		@return str  the hero name
		"""
		for hero in self.data['heroes']:
			if id == hero['id']:
				return str(hero['name'])
		return 'Hero ID not found!'
class MatchHistory(object):
	"""
	Wrapper methods for match history
	Reference: https://wiki.teamfortress.com/wiki/WebAPI/GetMatchHistory
	@param string key  your valve api key
	"""
	def __init__(self, key):
		self.key = key
		self.url = "http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/?key="+key
	def get(self):
		"""
		GET general information for the last 100 (currently the dota API's default) matches
		@return dict  match information
		"""
		try:
			res = urllib2.urlopen(self.url).read()
			return json.loads(res)['result']
		except urllib2.URLError, e:
			print 'Error in MatchHistory.get()'
			return None
	def getByDate(self, minDate, maxDate):
		"""
		GET general information for the last 100 matches by min or max date
		@param int minDate  (optional) minimum date range in unix timestamp format
		@param int maxDate  (optional) maximum date range in unix timestamp format
		@return dict  match information
		"""
		url = self.url
		if minDate is not None and str(minDate):
			url += "&minDate=" + str(minDate)
		if maxDate is not None and str(maxDate):
			url += "&maxDate=" + str(maxDate)
		try:
			res = urllib2.urlopen(url).read()
			return json.loads(res)['result']
		except urllib2.URLError, e:
			print 'Error in MatchHistory.getByDate()'
			return None
	def getBySkill(self, skill):
		"""
		GET general information for the last 100 matches based on skill bracket
		@param int skill  the skill bracket ID
			0 = Any
			1 = Normal
			2 = High
			3 = Very High
		@return dict  match information
		"""
		if skill > 3 or skill < 0:
			print 'Please use a valid skill bracket ID!'
			return None
		url = self.url
		if skill is not None and int(skill):
			url += "&skill=" + str(skill)
		try:
			res = urllib2.urlopen(url).read()
			return json.loads(res)['result']
		except urllib2.URLError, e:
			print 'Error in MatchHistory.getBySkill()'
			return None
	def getByHero(self, hero):
		"""
		GET general information for the last 100 matches based on hero ID
		@param int hero  the hero ID
		@return dict  match information
		"""
		url = self.url
		if hero is not None and int(hero):
			url += "&hero_id=" + str(hero)
		try:
			res = urllib2.urlopen(url).read()
			return json.loads(res)['result']
		except urllib2.URLError, e:
			print 'Error in MatchHistory.getByHero()'
			return None
	def getBySteamID(self, steam):
		"""
		GET general information for the last 100 matches based on steam id
		@param int steam  the 32bit numeric steam id
		@return dict  match information
		"""
		url = self.url
		if steam is not None and int(steam):
			url += "&account_id=" + str(steam)
		try:
			res = urllib2.urlopen(url).read()
			return json.loads(res)['result']
		except urllib2.URLError, e:
			print 'Error in MatchHistory.getBySteamID()'
			return None
	def getByMatchID(self, match):
		"""
		GET general information for the last 100 matches starting with match_id
		@param int match  the match_id
		@return dict  match information
		"""
		url = self.url
		if match is not None and int(match):
			url += "&start_at_match_id=" + str(match)
		try:
			res = urllib2.urlopen(url).read()
			return json.loads(res)['result']
		except urllib2.URLError, e:
			print 'Error in MatchHistory.getByMatchID()'
			return None
	def getByMulti(self, minDate, maxDate, skill, hero, steam, match):
		"""
		GET general information for the last 100 matches by a multitude of parameters
		@param int minDate  (optional) minimum date range in unix timestamp format
		@param int maxDate  (optional) maximum date range in unix timestamp format
		@param int skill    (optional) the skill bracket ID (ignored if account_id is specified)
		@param int hero     (optional) the hero ID
		@param int steam    (optional) the 32 bit numeric steam id
		@param int match    (optional) the match ID
		"""
		url = self.url
		if minDate is not None and isinstance(minDate, datetime.date):
			url += "&minDate=" + str(minDate)
		if maxDate is not None and isinstance(maxDate, datetime.date):
			url += "&maxData=" + str(maxDate)
		if skill is not None and int(skill):
			url += "&skill=" + str(skill)
		if hero is not None and int(hero):
			url += "&hero_id=" + str(hero)
		if steam is not None and int(steam):
			url += "&account_id=" + str(steam)
		if match is not None and int(match):
			url += "&start_at_match_id=" + str(match)
		try:
			res = urllib2.urlopen(url).read()
			return json.loads(res)['result']
		except urllib2.URLError, e:
			print 'Error in MatchHistory.getByMulti()'
			return None
class MatchDetails(object):
	"""
	Wrapper methods for detailed match data
	Reference: https://wiki.teamfortress.com/wiki/WebAPI/GetMatchDetails
	@param string key       your valve api key
	@param int    match_id  requested match_id
	"""
	def __init__(self, key, match_id):
		url = "http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1/?key="+key+"&match_id="+str(match_id)
		try:
			res = urllib2.urlopen(url).read()
			self.data = json.loads(res)['result']
		except urllib2.URLError, e:
			print 'Error in getMatchDetails: '+str(e)
			self.data = None
	def get(self):
		"""
		GET raw data
		@return dict  the raw data
		"""
		return self.data
	def getHeroes(self):
		"""
		GET hero data such as inventory items, GPM, XPM, KDA, etc
		@return dict  player data
		"""
		return self.data['players']
	def getMatchMeta(self):
		"""
		GET match metadata such as id, game mode, duration
		@return dict  match metadata
		"""
		data = self.data
		data.pop('players', None)
		return data
	def getDraft(self):
		"""
		GET pick/bans if game is CM
		@return dict  radiant and dire picks/bans
		"""
		try:
			return self.data['picks_bans']
		except KeyError:
			return False
	def getBuildings(self):
		"""
		GETs radiant and dire building status
		@return dict  building statuses
		"""
		return {
			'radiant': {
				'towers': str(bin(self.data['tower_status_radiant']))[-11:],
				'barracks': str(bin(self.data['barracks_status_radiant']))[-6:]
			},
			'dire': {
				'towers': str(bin(self.data['tower_status_dire']))[-11:],
				'barracks': str(bin(self.data['barracks_status_dire']))[-6:]
			}
		}
class MatchSequence(object):
	"""
	Main iterator, gets match by sequence number (linear match identifier)
	Reference: https://wiki.teamfortress.com/wiki/WebAPI/GetMatchHistoryBySequenceNum
	@param string key  your valve api key
	"""
	def __init__(self, key, match_id):
		self.url = "http://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v1/?key="+key
	def get(self, matches):
		"""
		GETs matches
		@param int matches  (optional) the number of requested matches
		@return list matches
		"""
		try:
			url = self.url
			if matches is not None and int(matches):
				url += "&matches_requested="+str(matches)

			res = urllib2.urlopen(url).read()
			return json.loads(res)['result']['matches']
		except urllib2.URLError, e:
			print 'Error in MatchSequence: '+str(e)
			return None
	def getBySequenceID(self, sequence, matches):
		"""
		GETs matches starting at sequence id
		@param int sequence  the sequence_id to begin at
		@param int matches   (optional) the number of matches to return
		@return list matches
		"""
		try:
			url = self.url
			url += "&start_at_match_seq_num="+str(sequence)
			if matches is not None and int(matches):
				url += "&matches_requested="+str(matches)

			res = urllib2.urlopen(url).read()
			return json.loads(res)['result']['matches']
		except urllib2.URLError, e:
			print 'Error in MatchSequence: '+str(e)
			return None


