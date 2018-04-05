import csv, json
import tldextract

apptrackers = open('app_trackers.json')
apptrackers = json.load(apptrackers)

newFormat = []

idcounter = 364

for tracker in apptrackers:
  cleandoms = "         \"" + "\",\n         \"".join(str(x) for x in tracker['doms']) + "\""
  idcount = idcounter + 1
  idcounter = idcounter + 1
  newF =  """{\n    "id"         : %s,
      "parent_id"      : \"%s\",
      "owner_name"     : \"%s\",
      "aliases"      : [],
      "homepage_url"     : null,
      "privacy_policy_url" : null,
      "notes"        : null,
      "country"      : \"%s\",
      "domains"      : [\n%s    \n]\n  },\n""" % (idcount, tracker['parent'], tracker['owner_name'], tracker['country'], cleandoms)
  # newF = {}
  # newF["id"] = 0
  # newF["parent_id"] = tracker['parent']
  # newF["owner_name"] = tracker['owner_name']
  # newF["aliases"] = "null"
  # newF["homepage_url"] = "null"
  # newF["privacy_policy_url"] = "null"
  # newF["notes"] = "null"
  # newF["country"] = "null"
  # newF["domains"] = tracker['doms']
  newFormat.append(newF)


f = open('newcos.txt','w')
for newF in newFormat:
  f.write(newF)
f.close()
