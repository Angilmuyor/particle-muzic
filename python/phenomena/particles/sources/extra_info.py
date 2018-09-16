import json
from os.path import expanduser, join

HOME = expanduser("~")
JSON_PATH = join(HOME, '.phenomena/conf/part_extra_info.json')
XTRA_INFO = json.load(open(JSON_PATH))

class ExtraInfoFetcher(object):

    @staticmethod
    def getComposition(pdgid):
        composition =[]
        if XTRA_INFO[str(pdgid)]['composition'] != []:
            for quark in XTRA_INFO[str(pdgid)]['composition'][0]: #only consider first superposition of quarks
                composition.append(quark.encode('utf-8'))

        return composition

    @staticmethod
    def getType(pdgid):
        return XTRA_INFO[str(pdgid)]['type'].encode('utf-8')
