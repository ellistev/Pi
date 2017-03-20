import concurrent.futures
import urllib.request

carname = 'art'
filename = ''
lines = tuple(open('D:/Code/Pi/Autotrader/person/art.txt', 'r'))
photohelperurl = 'http://az413908.vo.msecnd.net'
underscore = '_'

def getimg(count):
    localpath = 'D:/Code/prepared_images_bad/racy/{0}{1}.jpg'.format(carname, underscore+str(count))
    urllib.request.urlretrieve(lines[count], localpath)
    #URLS[count] = localpath

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as e:
    for i in range(600):
        e.submit(getimg, i)
