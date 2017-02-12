# For Python 3 or higher
import urllib.request, json, collections  

listMiningPoolNamesFormatted = ['AntPool',
    'F2Pool',
    'BitFury',
    'BW.COM',
    'ViaBTC',
    'BTCC%20Pool',
    'SlushPool',
    'BTC.TOP',
    'HaoBTC',
    'BitClub%20Network',
    'BTC.com',
    '1Hash',
    'xbtc.exx.com%26bw.com',
    'Bitcoin.com',
    'GBMiners',
    'GoGreenLight',
    'Kano%20CKPool',
    'BATPOOL',
    'Telco%20214',
    'PHash.IO',
    'shawnp0wers',
    'ConnectBTC']

####### BEGIN Basic Methods

def getURLasString(url):
    s = urllib.request.urlopen(url).read()
    return s

def convertJSONStringToSequence(source):
    j = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(source)
    return j

def getURLasJSONSequence(url):
    s = getURLasString(url).decode("utf-8")
    return convertJSONStringToSequence(s)

def getURLasStringSpecialHeader(url):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    s = urllib.request.urlopen( req ).read()
    return s

def getURLasJSONSequenceSpecialHeader(url):
    s = getURLasStringSpecialHeader(url).decode("utf-8")
    return convertJSONStringToSequence(s)    

####### END Basic Methods   

####### BEGIN API Calls

def getLatestBlockHeight():
    urlGetLatestHeight = "https://blockchain.info/q/getblockcount"
    sLatestBlockHeight = getURLasString(urlGetLatestHeight)
    return int(sLatestBlockHeight)

def getBlockData(blockHeight):
    url = 'http://api.qbit.ninja/blocks/' + str(blockHeight) + '/header'
    blockData = getURLasJSONSequenceSpecialHeader(url)
    return blockData

def getLatestBlockOfPool(poolNameFormatted):
    url = 'https://blockchain.info/blocks/' + poolNameFormatted + '?format=json'
    listUnfilteredBlocks = getURLasJSONSequence(url)
    listBlocks = [y for y in listUnfilteredBlocks['blocks'] if y['main_chain']]
    if len(listBlocks) > 0:
        return listBlocks[0]
    else:
        return 0

####### END API Calls

listPoolsFirstBlocks = []

for pool in listMiningPoolNamesFormatted: 
    try:
        latestBlock = getLatestBlockOfPool(pool)
    except:
        continue
    iLatestBlockHeight = latestBlock['height']
    if (iLatestBlockHeight > 0):
        tupleBlock = (pool, iLatestBlockHeight)
        listPoolsFirstBlocks.append(tupleBlock)

listSegwitPools = []

for tuplePoolAndBlock in listPoolsFirstBlocks:
    poolName = ""
    try:
        poolName = tuplePoolAndBlock[0]
    except:
        continue
    blockHeight = tuplePoolAndBlock[1]
    blockData = getBlockData(blockHeight)
    version = int(blockData['version'])
    if version == 536870914:
        listSegwitPools.append(poolName)

print(listSegwitPools)





