import concurrent.futures
import urllib.request

carname = 'toyota_rav4'
filename = ''
lines = tuple(open('toyota_rav4.txt', 'r'))
photohelperurl = 'http://az413908.vo.msecnd.net'
underscore = '_'

def getimg(count):
    localpath = '{0}/{0}{1}.jpg'.format(carname, underscore+str(count))
    urllib.request.urlretrieve(photohelperurl + "/" + lines[count], localpath)
    #URLS[count] = localpath

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as e:
    for i in range(24550):
        e.submit(getimg, i)