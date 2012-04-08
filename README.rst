==============
DOL Python Wrapper for SummerJobs+ data access
==============

-----
Usage
-----

check test.py, need to undo hardcoded query in SummerJobsConnection

==============
Python-USDOL
==============

Python wrapper for the US Dept. of Labor's `developer API <http://developer.dol.gov/>`_. 

-----
Usage
-----

Usage is straightforward.

  import python_usdol

  conn = python_usdol.Connection(token='mytoken', secret='mysharedsecret')
  
  data = conn.fetch_data('FAQ', 'Topic')


Where 'FAQ' and 'Topic' are the names of the targeted dataset and table within the dataset, respectively. For a full list of datasets and tables, please consult the Dept. of Labor's developer website, linked above.

In the above example, `data` will be a list of `Datum` instances. Each `Datum` instance provides access to all of the data from the dictionary object it represents, as well as some metadata about itself, using attribute syntax.

e.g. from the example: data[0].TopicID == 1, data[0].TopicValue == u'Wages & Work Hours'

Some datasets have "multipart" names, e.g. the `Consumer Expenditure Survey Dataset <http://developer.dol.gov/ConsumerExpenditure-DATASET.htm>`_. In this case, since the base url is `http://api.dol.gov/V1/Statistics/ConsumerExpenditure`, vice e.g. `.../V1/FORMS`, for the first argument to fetch data, you would pass the "multipart" Agency name:

  data = conn.fetch_data('Statistics/ConsumerExpenditure', '<desired table name>')

-----------
Parameters
-----------

Python-USDOL has support for all the request methods outlined in the DOL's `API Access Guide <http://developer.dol.gov/html-req.htm>`_:

  $metadata
  
  $top
  
  $skip
  
  $orderby

  $filter


------
Filter
------

Using the filter method goes thusly:

  data = conn.fetch_data("FAQ", "Topic", filter_="TopicID eq 5")

Since `filter` is a keyword in Python, Python-USDOL uses `filter_` in its place.

------
Future
------

Please help make this API better for everyone by reporting bugs, forking and submitting patches.
