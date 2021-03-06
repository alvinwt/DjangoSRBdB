# Full path and name to your csv file
csv_filepathname="/home/alvin/Dropbox/FYP/Django/mysite/srb/csv/chr3Lbig2catreintervalllhitsheader.txt"
# Full path to your django project directory
your_djangoproject_home="/home/alvin/Dropbox/FYP/Django/mysite/srb/"
 
import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
 
from srb.models import Interval
import csv
dataReader = csv.reader(open(csv_filepathname), delimiter='\t', quotechar='"')
 
for row in dataReader:
    if row[0] != 'Chr': # Ignore the header row, import everything else
        interval = Interval()
        Interval.chr=row[0]
        Interval.start=row[1]
        Interval.stop=row[2]
        Interval.chr.save()
        Interval.start.save()
                
