import concurrent.futures
import urllib.request

carname = 'chevrolet_cruze'
filename = ''
lines = tuple(open('chevrolet_cruze.txt', 'r'))
photohelperurl = 'http://az413908.vo.msecnd.net'
underscore = '_'

def getimg(count):
    localpath = '/datadrive/prepared_photos/{0}/{0}{1}.jpg'.format(carname, underscore+str(count))
    urllib.request.urlretrieve(photohelperurl + "/" + lines[count], localpath)
    #URLS[count] = localpath

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as e:
    for i in range(11040):
        e.submit(getimg, i)
