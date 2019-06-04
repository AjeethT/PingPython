import time#getting time
import urllib.request#getting url

def rtt(u):
    try:
        t1=time.time()#time before connection
        r=urllib.request.urlopen(u)#request url
        t2=time.time()#time after connection
        tim=str(t2-t1)#time calculation Round trip time
        print("t="+tim+"ms")
    except urllib.error.URLError as e:#if error
        print("network error")
u=input("enter the url:")
rtt(u)
