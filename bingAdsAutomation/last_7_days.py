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
          'fields': ['Date','CampaignId', 'AdGroupId','Device','AdNetworkType2','Slot']
          'fields': ['Date','CampaignId', 'AdGroupId','Device','AdNetworkType2','Slot']
          'fields': ['Date','CampaignId', 'AdGroupId','Device','AdNetworkType2','Slot']
      }
  }
