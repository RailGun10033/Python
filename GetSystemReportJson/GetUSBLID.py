import os
import os.path
import sys
import json


def GetLocationIDs(content):
    lines = content.split('\n')
    splitchar = ':'
    keyOfRightDevice = 'Bluetooth USB Host Controller'
    keyOfLocationID = 'Location ID'
    keyOfStopFind = '/'
    keyOfLD = "lockdown://"
    rlts = {}
    index = 1
    
    isLooking = False
    
    for line in lines:
        line = line.strip()
        if( line.strip() == "" ):
            continue
        
        items = line.split(splitchar)
        if( len(items) < 1 ):
            continue
        
        key = items[0].strip()
        value = items[1].strip()
        if( value != "" ):
            if( isLooking ):
                if( key == keyOfLocationID ):
                    temp = str(index)
                    site = value.find(keyOfStopFind)
                    if( site == -1 ):
                        rlts[temp] = keyOfLD + value
                    else:
                        rlts[temp] = keyOfLD + value[0:site-1]
                    
                    isLooking = False
                    index = index + 1
        else:        
            if( key == keyOfRightDevice ):
                isLooking = True
    return rlts  
def filterNullLine(lines):
    filteredLine = []
    for line in lines:
        if line != '':
            filteredLine.append(line)
    return filteredLine 

def getLeftSpaceCount(line):
    spaceCount = 0
    for s in list(line):
        if s == ' ':
            spaceCount += 1
        else:
            break
    return spaceCount

def contentToDic(content):
    lines = content.split('\n')
    lines = filterNullLine(lines)
    spaceCountList = []


    resultDic = {}
    tmpKey = ''
    tmpDic = {}
    for i in range(len(lines)):
        line = lines[i]
        level = getLeftSpaceCount(line)
        spaceCountList.append(level)
        if level == 8:
            tmpKey = line.split(':')[0].strip()
            if not tmpKey in resultDic.keys():
                resultDic[tmpKey] = []

        if level == 10:
            key, value = line.split(': ')
            tmpDic[key.strip()] = value

            if i < len(lines) - 1:
                if getLeftSpaceCount(lines[i+1]) == 8:
                    resultDic[tmpKey].append(tmpDic)
                    tmpDic = {}
            else:
                resultDic[tmpKey].append(tmpDic)
                tmpDic = {}
    # print(spaceCountList)

    return resultDic



output = os.popen("system_profiler SPUSBDataType").read()   

items = contentToDic(output)
itemsStr = json.dumps(items, indent=4)
print(itemsStr)
with open("/Users/luder/Desktop/USBID.json","w") as f:
	f.write(itemsStr)


		

		
