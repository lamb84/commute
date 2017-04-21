import commute
import time
import datetime
from gmailSender import send_email


homeAddrList = ['5880 Hampton Place, Vancouver']
workAddrList = ['4558 Kingsway, Burnaby ']
emailBody = ''

#Using current time to determine orgin and destination that will be used in gmaps
#if current time is after 1PM, origin is set to workAddrList, destination is set to homeAddrList
#if current time is before 1PM, it is reversed
now = datetime.datetime.now()
nowTime=now.time()


if nowTime <= datetime.time(13,00):
    originAddrList = homeAddrList
    destAddrList = workAddrList
else:
    originAddrList = workAddrList
    destAddrList = homeAddrList


for originAddr in originAddrList:
    for destAddr in destAddrList:
        ctime = commute.time(originAddr,destAddr)
        distance = commute.distance(originAddr,destAddr)
        emailBody += "From %s To %s (%s) takes %s \n" % (originAddr, destAddr, distance, ctime)

print(emailBody)

#email the commute matrix
emailRcpt = ['fridashen319@gmail.com']
emailSnd = 'harry.yang@eightsolutions.com'
emailPasswd = 'J@m35H4den'
emailSubject = time.strftime("%b %d %H:%M") + ' commute time matrix'
send_email(emailSnd, emailPasswd, emailRcpt, emailSubject, emailBody)
