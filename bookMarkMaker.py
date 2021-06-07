import json
colorList = ["#66CCCC","#CCFF66","#FF99CC","#FF9999",
            "#FFCC99","#FF6666","#FFFF66","#99CC66",
            "#99CC33","#FF9900","#FFCC00","#FF0033",
            "#FF9966","#CCFF00","#CC3399","#FF6600",
            "#993399","#CCCC33","#666633","#CC0066",
            "#99CC00","#009999","#FFCC33","#663399"]

def getColor():
    import random
    randomIndex = random.randint(0, len(colorList)- 1)
    return colorList[randomIndex]

def getRGBA():
    import random
    randomIndex = random.randint(0, len(colorList) - 1)
    colorStr = colorList[randomIndex]
    r = int(colorStr[1: 3],base=16)
    g = int(colorStr[3: 5], base=16)
    b = int(colorStr[5: ], base=16)
    return r,g,b

def rgbStr(r, g, b, apha):
    return 'rgba(%d, %d, %d, %f)'%(r, g, b, apha)

HTML_Content_Prefix = '''<html lang="en"><head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BookMarks</title>

    <style>
        body{
            height: 100%;
            width: 100%;
            margin: 0px;
            padding: 10px;
            background-color: rgba(0,0,0,0.8);
            
        }
        #mainBox{
            
        }
        
        .boxOutside{
            padding: 0px;
            margin: 0px;
            width: 220px;
            height: 220px;
            display: inline-block;
            /* border:1px solid greenyellow; */

        }

        .box{
            margin: 10px;
            width: 200px;
            height: 200px;
            position: absolute;
            border-radius: 20px;

        }

        .box:hover{
            margin: 5px;
            width: 210px;
            height:210px;
        }

        .boxFill{
            margin: 0px;
            padding: 0px;
            width: 100%;
            height: 80%;
            text-align: center;
            font-size: 64px;
            line-height: 160px;
            color: white;
            border-radius: 0px 0px 20px 20px; 
            /* border:1px solid green; */
        }

        

        .boxTitle{
            margin: 0px;
            padding: 0px;
            width: 100%;
            height: 20%;
            text-align: center;
            font-size: 18px;
            line-height: 40px;
            color: white;
            /* background-color: white; */
            border:1px solid red;
            border-radius: 20px 20px 0px 0px ;
            box-sizing: border-box;
        }
    </style>
</head>
<body>
    <div id="mainBox">'''

HTML_Content_Post = '''
    </div>
</body></html>'''

bookmarkDic = None
with open('Bookmarks.json', 'r', encoding='utf-8') as f:
    bookmarkDic = json.load(f)

children = bookmarkDic['roots']["bookmark_bar"]['children']
for item in children:
    date_added = item['date_added']
    guid = item['guid']
    id = item['id']
    name = item['name']
    type = item['type']
    url = item['url']
    if type == 'url':
        r, g, b = getRGBA()
        HTML_Content_Main = '''      
        <div class="boxOutSide">
            <div class="box" style="box-shadow: 10px 10px 10px %s;">
                    <div class="boxTitle" style="border-color: %s;">%s</div>
                    <div class="boxFill" style="background: linear-gradient(to right bottom, %s, %s);" onclick="window.location.href= '%s';return false" title = "%s">%s</div>
            </div>
        </div>
        '''%(rgbStr(r,g,b,0.1),rgbStr(r,g,b,1),name[:7], rgbStr(r,g,b,1), rgbStr(r,g,b,1), url, url,name[0])
        HTML_Content_Prefix += HTML_Content_Main
HTML_Content_Prefix += HTML_Content_Post

with open('bookMarks.html','w') as f:
    f.write(HTML_Content_Prefix)









