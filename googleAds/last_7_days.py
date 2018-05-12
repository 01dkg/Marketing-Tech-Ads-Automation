import logging
import sys
from googleads import adwords
import pandas as pd

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)



def main(client):
  f = open("random.csv","w")
  report_downloader = client.GetReportDownloader(version='v201705')
  report = {
  'reportName': 'Last 30 days CRITERIA_PERFORMANCE_REPORT',
  'dateRangeType': 'LAST_30_DAYS',
  'reportType': 'PLACEHOLDER_REPORT',
  'downloadFormat': 'CSV',
  'selector': {
          'fields': ['Date','CampaignId','AdGroupId','ClickType','Conversions']
      }
  }

  data=report_downloader.DownloadReport(
      report, f, skip_report_header=True, skip_column_header=False,
      skip_report_summary=True, include_zero_impressions=False)
  f.close()

if __name__ == '__main__':
  adwords_client = adwords.AdWordsClient.LoadFromStorage()
  adwords_client.SetClientCustomerId('XXX-XXX-XXXX')
  main(adwords_client)

