from python_usdol import *
from urllib import urlencode
import json
class SummerJobsConnection(Connection):


    def _get_request(self, qs='', fmt='json'):
        url_args = [USDOL_URL, API_VER, self.dataset, self.table]
        qs = {
            'query' : "'Nurse'",
            'skipCount' : 1,
        }
        qs = '?' + urlencode(qs)
        print qs
        header = self._get_header(qs)
        print header
        url = string.join(url_args, '/') + qs
        req = urllib2.Request(url, headers={"Authorization": header,
                                           "Accept": 'application/%s' % fmt})
        print req.get_full_url()
        return req


    def fetch_data(self, dataset, table='$metadata', fmt='json', top=0, skip=0, select='', orderby='', filter_=''):
        """
        fetch_data(dataset, table[, fmt, top, skip, select, orderby]) ->
        
            Return an object representing the information in the specified
            table from the specified dataset.

            The rest of the args work as outlines in the DOL's API
            reference (http://developer.dol.gov/html-req.htm).
        
        'fmt' is json by default. Valid choices are 'xml' and 'json'.
        
        """
            
        qs = self._get_querystring(top=top, skip=skip, select=select,
                                   orderby=orderby, filter_=filter_)
        self.dataset = dataset
        self.table = table
        enc_opts = ['json', 'xml']
        if fmt not in enc_opts:
            raise AttributeError("Valid format choices are: json, xml")
        if table == '$metadata' and fmt != 'xml':
            fmt = 'xml'
    
        urlstr = self._get_request(qs, fmt)
        data = urllib2.urlopen(urlstr)
        print "Data"
        json_string = data.read()
        json_data = json.loads(json_string)
        listings = json_data['d']['getJobsListing']
        listings_data = json.loads(listings)

        return listings_data
        
