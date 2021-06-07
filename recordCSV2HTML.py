import os
import sys
import csv


pyScriptPath = sys.argv[0]
pyScriptDir, pyScriptName = os.path.split(pyScriptPath)

srcDir = pyScriptDir + '/src'



def csv2HTML(csvPath):

    htmlStr = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{{%titleStr%}}}</title>

    <style>

        body{
            width: 100vw;
            height: 100vh;
            display: inline;
        }
        table,tr,td,th{
            margin: 10px;
            border: 1px solid black;
            border-collapse: collapse;
            text-align: center;
        }

        th{
            background-color: #009999;
            color: white;
        }

        .attrTable, .timeTable{
            display: inline-table;
        }

        .redBgColor{
            background: #FF0033;
        }

        .greenBgColor{
            background: #33FF00;
        }

        .orangeBgColor{
            background: #FF9900;
        }

        
    </style>
</head>
<body>
    <table class="timeTable">
            <thead>
                <tr>
                    <th>startTime</th>
                    <th>stopTime</th>
                    <th>timeInterval</th>
                </tr>
            </thead>
            <tbody>
                {{{%timeTable%}}}
            </tbody>
                
    </table>
    <br>
    <table class="attrTable">
        <thead>
            <tr>
                <th>attributeName</th>
                <th>attributeValue</th>
            </tr>
        </thead>
        <tbody>
            {{{%attrTable%}}}
        </tbody>
            
    </table>
    
        


    

    <table>
        <thead>
            <tr>
                <th>testName</th>
                <th>sub<br>TestName</th>
                <th>subSub<br>TestName</th>
                <th>rul</th>
                <th>ul</th>
                <th>value</th>
                <th>ll</th>
                <th>rll</th>
                <th>units</th>
                <th>priority</th>
                <th>status</th>
                <th>failure<br>Message</th>
            </tr>
        </thead>
        <tbody>
            {{{%detailTable%}}}
        </tbody>
            
    </table>
</body>
</html>
    '''
    csvDir,_  = os.path.split(csvPath)
    htmlPath  = csvDir + '/record.html'

    csvRows = csv.reader(open(csvPath))


    timeTable = ""
    attrTable = ""
    detailTable = ""
    titleStr = ''
    isHeader = True
    for row in csvRows:
        if isHeader:
            isHeader = False
            continue
        if row[0] != '':
            if row[0] == 'SwName' or row[0] == 'PrimaryIdentity':
                titleStr += ' %s'%row[1]
            lineStr = '''
            <tr>
                <td>%s</td><td>%s</td>
            </tr>\n'''%(row[0], row[1])
            attrTable += lineStr
        elif row[-3] != '':
            lineStr = '''
            <tr>
                <td>%s</td><td>%s</td><td>%s</td>
            </tr>\n'''%(row[-3], row[-2], row[-1])
            timeTable += lineStr
        else:
            lineStr = lineStr = '''
            <tr>\n'''
            for i in range(2, 14):
                tdClass = ''
                if i == 12:
                    if row[i] == 'PASS':
                        tdClass = 'class="greenBgColor"'
                    else:
                        tdClass = 'class="redBgColor"'


                lineStr += '''
                <td %s>%s</td>'''%(tdClass, row[i])
            lineStr += '''
            </tr>\n'''
            detailTable += lineStr

    htmlStr = htmlStr.replace('{{{%titleStr%}}}', titleStr)
    htmlStr = htmlStr.replace('{{{%timeTable%}}}',timeTable)
    htmlStr = htmlStr.replace('{{{%attrTable%}}}', attrTable)
    htmlStr = htmlStr.replace('{{{%detailTable%}}}', detailTable)
    with open(htmlPath,'w', encoding='utf-8') as f:
        f.write(htmlStr)



    print('True, \"%s\" create successfully.'%htmlPath)


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("False, csvFilePath cannot be null.")
    else:
        csvPath = sys.argv[1]
        if not os.path.exists(csvPath):
            print("False, \"%s\" is not exists."%csvPath)
        else:
            csv2HTML(csvPath)


