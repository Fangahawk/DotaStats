import urllib.request
import json
htmlcode = urllib.request.urlopen("http://api.opendota.com/api/players/420181938/RecentMatches")
jsonraw= str(htmlcode.read())
jsonparsed=jsonraw[2:-1]
playermatches=json.loads(jsonparsed)
match_no=input("Enter the match you want to see")
print(playermatches[int(match_no)-1]["match_id"])