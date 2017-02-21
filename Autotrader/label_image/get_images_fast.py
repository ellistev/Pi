import concurrent.futures
import urllib.request

carname = 'volkswagen_golf'
filename = ''
lines = tuple(open('volkswagen_golf.txt', 'r'))
photohelperurl = 'http://az413908.vo.msecnd.net'
underscore = '_'

def getimg(count):
    localpath = '{0}/{0}{1}.jpg'.format(carname, underscore+str(count))
    urllib.request.urlretrieve(photohelperurl + "/" + lines[count], localpath)
    #URLS[count] = localpath

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as e:
    for i in range(1000):
        e.submit(getimg, i)