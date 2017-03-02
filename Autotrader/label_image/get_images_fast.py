import concurrent.futures
import urllib.request

carname = 'heavy_equipment'
filename = ''
lines = tuple(open('D:/Code/Pi/Autotrader/label_image/npv/heavy_equipment.txt', 'r'))
photohelperurl = 'http://az413908.vo.msecnd.net'
underscore = '_'

def getimg(count):
    localpath = 'D:/Code/prepared_images_npv/{0}/{0}{1}.jpg'.format(carname, underscore+str(count))
    urllib.request.urlretrieve(photohelperurl + "/" + lines[count], localpath)
    #URLS[count] = localpath

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as e:
    for i in range(1000):
        e.submit(getimg, i)
