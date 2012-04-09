import summerjobs
import urllib2

conn = summerjobs.SummerJobsConnection(token='YOUR_TOKEN', secret='YOUR_SECRET')
try:
    data = conn.fetch_data('SummerJobs', 'getJobsListing', query="Nurse")
except urllib2.HTTPError, e:
    print "Error"
    print e.code,e.read()
  
positions = data


for position in positions.get('items'):
    print position
    print '-' * 20
