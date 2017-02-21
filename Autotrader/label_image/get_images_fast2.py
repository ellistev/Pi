import concurrent.futures
import urllib.request

carname = 'toyota_corolla'
filename = ''
lines = tuple(open('toyota_corolla.txt', 'r'))
photohelperurl = 'http://az413908.vo.msecnd.net'
underscore = '_'

def getimg(count):
    localpath = '{0}/{0}{1}.jpg'.format(carname, underscore+str(count))
    urllib.request.urlretrieve(photohelperurl + "/" + lines[count], localpath)
    #URLS[count] = localpath

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as e:
    for i in range(58713):
        e.submit(getimg, i)