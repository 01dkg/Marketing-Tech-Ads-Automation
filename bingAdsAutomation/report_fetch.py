import getpass
import datetime as dd
from auth_helper import *
from output_helper import *

userPath = getpass.getuser() 
FILE_DIRECTORY='C:/Users/' + userPath + '/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/XXXXXXXXXXXXXXXXX'

DOWNLOAD_FILE_NAME='download1.csv'

REPORT_FILE_FORMAT='Csv'

TIMEOUT_IN_MILLISECONDS=3600000

TO_DATE= dd.date.today() + dd.timedelta(-1)
FROM_DATE= dd.date.today() + dd.timedelta(-30)

def main(authorization_data,accountID,accountName):

    try:
        #report_request=get_budget_summary_report_request()
        report_request=AdGroupPerformanceReport(accountID,accountName)
        #report_request = GoalReport(accountID, accountName)
        #report_request=get_user_location_performance_report_request()
        #report_request=get_keyword_performance_report_request()
        
        reporting_download_parameters = ReportingDownloadParameters(
            report_request=report_request,
            result_file_directory = FILE_DIRECTORY, 
            result_file_name = accountName +'-' + str(dd.date.today()) +'.csv',
            overwrite_result_file = True, 
            timeout_in_milliseconds=TIMEOUT_IN_MILLISECONDS 
        )

        output_status_message("Awaiting Background Completion . . .");
        background_completion(reporting_download_parameters)
        reporting_operation=reporting_service_manager.submit_download(report_request);
        request_id=reporting_operation.request_id;
        print("Report Request ID", request_id)
        output_status_message("Program execution completed")

    except WebFault as ex:
        output_webfault_errors(ex)
    except Exception as ex:
        output_status_message(ex)
def custom_date(dateVar,start_end_object):
    start_end_object.Day = dateVar.day
    start_end_object.Month = dateVar.month
    start_end_object.Year = dateVar.year
    return start_end_object

def AdGroupPerformanceReport(accountID, accountName):
    report_request=reporting_service.factory.create('AdGroupPerformanceReportRequest')
    report_request.Format=REPORT_FILE_FORMAT
    report_request.ReportName='AdGroup Performance Report'
    report_request.ReturnOnlyCompleteData=False
    report_request.Language='English'

    report_aggregation=reporting_service.factory.create('ReportAggregation')
    report_request.Aggregation = 'Daily'

    #report_request=reporting_service.factory.create('ReportTimePeriod')
    #report_request.ReportTimePeriod = 'Weekly'

    scope=reporting_service.factory.create('AccountThroughAdGroupReportScope')
    scope.AccountIds={'long': accountID}
    scope.AdGroups=None
    report_request.Scope=scope
    
    #Data from last 14 days
    report_time=reporting_service.factory.create('ReportTime')

    custom_date_range_start=reporting_service.factory.create('Date')

    custom_date_range_start.Day= FROM_DATE.day
    custom_date_range_start.Month=FROM_DATE.month
    custom_date_range_start.Year=FROM_DATE.year
    report_time.CustomDateRangeStart=custom_date_range_start
    custom_date_range_end=reporting_service.factory.create('Date')
    custom_date_range_end.Day=TO_DATE.day
    custom_date_range_end.Month=TO_DATE.month
    custom_date_range_end.Year=TO_DATE.year
    report_time.CustomDateRangeEnd=custom_date_range_end
    report_time.PredefinedTime=None
    report_request.Time=report_time

    # Specify the attribute and data report columns.
    if accountID ==XXXXXXX and accountName=='XXXXXXXXXXXXX': #Betfair
        cols=['AccountName',
              'TimePeriod',
              'Network',
              'DeviceType',
              'CampaignName',
              'AdGroupName',
              'Impressions',
              'Clicks',
              'Spend',
              'Conversions',
              'AveragePosition']

    elif accountID ==XXXXXXX and accountName == 'XXXXXXXXXXXXX': #bidvine
        cols=['AccountName',
              'TimePeriod',
              'DeviceType',
              'CampaignName',
              'AdGroupName',
              'Impressions',
              'Clicks',
              'Spend',
              'AveragePosition',
              'Conversions',]
    else:
        cols=['AccountName',
              'AccountId',
              'TimePeriod',
              'DeviceType',
              'CampaignName',
              'AdGroupName',
              'Impressions',
              'Clicks',
              'Spend',
              'Conversions',]

    report_columns=reporting_service.factory.create('ArrayOfAdGroupPerformanceReportColumn')
    report_columns.AdGroupPerformanceReportColumn.append(cols)
    report_request.Columns=report_columns
    return report_request
