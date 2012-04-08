import summerjobs
import urllib2

conn = summerjobs.SummerJobsConnection(token='YOUR_TOKEN', secret='YOUR_SECRET')
try:
    data = conn.fetch_data('SummerJobs', 'getJobsListing')
except urllib2.HTTPError, e:
    print "Error"
    print e.code,e.read()
    
print data
