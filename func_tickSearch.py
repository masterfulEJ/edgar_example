import re
# from cPickle import dump
from requests import get

# DEFAULT_TICKERS = ['goog', 'aapl']
def cikftick(ticks=['goog', 'aapl']):
    URL = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK={}&owner=exclude&action=getcompany&Find=Search'
    CIK_RE = re.compile(r'.*CIK=(\d{10}).*')

    cik_dict = {}
    for ticker in ticks:
        results = CIK_RE.findall(get(URL.format(ticker)).content.decode('UTF-8'))
        print(' | '.join([ticker, 'found: #{}'.format(len(results)), results[0]]))
        if len(results):
            cik_dict[str(ticker).lower()] = str(results[0])
    return cik_dict
    # f = open('cik_dict', 'w')
    # dump(cik_dict, f)
    # f.close()
