import logging
import sys
from googleads import adwords
import pandas as pd
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)

def main(client,fileObject):
  report_downloader = client.GetReportDownloader(version='v201705')
# Create report query.
  report_query = (adwords.ReportQueryBuilder()
                  .Select('AccountDescriptiveName','Date','Device','CampaignName','AdGroupName','Impressions','Clicks','Cost','Conversions', 'AveragePosition')
                  .From('ADGROUP_PERFORMANCE_REPORT')
                  .During('LAST_30_DAYS')
                  .Build())
# You can provide a file object to write the output to. For this
  # demonstration we use sys.stdout to write the report to the screen.
  report_downloader.DownloadReportWithAwql(
      report_query, 'CSV', fileObject, skip_report_header=True,
      skip_column_header=False, skip_report_summary=True,
      include_zero_impressions=False)



if __name__ == '__main__':
  adwords_client = adwords.AdWordsClient.LoadFromStorage()
  file = open("daily_report.csv",'w')
  clientList = ['XXX-XXX-XXXX','XXX-XXX-XXXX'] #Replace it with your AdWords Customer Account number
  numberOfAccounts = len(clientList)

  for i in range(0,numberOfAccounts):
      adwords_client.SetClientCustomerId(clientList[i])
      main(adwords_client,file)
  file.close()
