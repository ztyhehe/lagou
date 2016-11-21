#coding=utf-8
import json
import urllib2
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
page=1
length=0
index=1
f=open('lagoudata.txt','a+')
while page<2:
    if(page==1):
        post_data = {'first':'true','kd':'python','pn':page}
    else:
        post_data = {'first':'false','kd':'python','pn':page}
    page=page+1
    r = urllib2.Request("http://www.lagou.com/jobs/positionAjax.json?px=default", urllib.urlencode(post_data))
    html=urllib2.urlopen(r).read()
    hjson=json.loads(html)

    result=hjson['content']['positionResult']['result']
    # print result
    length=length+len(result)
    for i in result:
        print '-------------------------------------------------------------'
        print '-------------------------------------------------------------'
        print '-------------------------------------------------------------'
        print type(i['financeStage'])
        print i['financeStage']
        print type(i['financeStage'].encode('utf-8'))
f.close()
print length