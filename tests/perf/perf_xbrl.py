from edgar.xbrl import XBRLData
from edgar.financials import Financials
from edgar import *
from pyinstrument import Profiler

if __name__ == '__main__':
    filing = Filing(company='Tesla, Inc.', cik=1318605,
                    form='10-K', filing_date='2024-01-29',
                    accession_no='0001628280-24-002390')

    with Profiler(async_mode=True) as p:
        financials = Financials.extract(filing)

    p.print()

