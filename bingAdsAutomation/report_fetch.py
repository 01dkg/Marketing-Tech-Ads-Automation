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

 def GoalReport(accountID, accountName):
    report_request = reporting_service.factory.create('GoalsAndFunnelsReportRequest')
    report_request.Format = REPORT_FILE_FORMAT
    report_request.ReportName = 'Goals Report'
    report_request.ReturnOnlyCompleteData = False
    report_request.Language = 'English'

    report_aggregation = reporting_service.factory.create('NonHourlyReportAggregation')
    report_request.Aggregation = 'Daily'

    # report_request=reporting_service.factory.create('ReportTimePeriod')
    # report_request.ReportTimePeriod = 'Weekly'

    scope = reporting_service.factory.create('AccountThroughAdGroupReportScope')
    scope.AccountIds = {'long': accountID}
    scope.AdGroups = None
    report_request.Scope = scope

    # Data from last 14 days
    report_time = reporting_service.factory.create('ReportTime')
    start_date = reporting_service.factory.create('Date')
    report_time.CustomDateRangeStart = custom_date(FROM_DATE,start_date)

    end_date = reporting_service.factory.create('Date')
    report_time.CustomDateRangeEnd = custom_date(TO_DATE,start_date)
    report_time.PredefinedTime = None

    # report_time.PredefinedTime='LastFourWeeks'
    report_request.Time = report_time
    print(accountName)

    if accountID == XXXXXXXX and accountName == 'XXXXXXXXXXX':  # TVG Last 30 Days
        cols = ['AccountName',
                'TimePeriod',
                'DeviceType',
                'Goal',
                'CampaignName',
                'AdGroupName',
                'Conversions',]


    report_columns = reporting_service.factory.create('ArrayOfGoalsAndFunnelsReportColumn')
    report_columns.GoalsAndFunnelsReportColumn.append(cols)
    report_request.Columns = report_columns
    return report_request
   
   def background_completion(reporting_download_parameters):
    global reporting_service_manager
    result_file_path = reporting_service_manager.download_file(reporting_download_parameters)
    output_status_message("Download result file: {0}\n".format(result_file_path))

def submit_and_download(report_request):
    global reporting_service_manager
    reporting_download_operation = reporting_service_manager.submit_download(report_request)

    reporting_operation_status = reporting_download_operation.track(timeout_in_milliseconds=TIMEOUT_IN_MILLISECONDS)

    result_file_path = reporting_download_operation.download_result_file(
        result_file_directory = FILE_DIRECTORY, 
        result_file_name = DOWNLOAD_FILE_NAME, 
        decompress = True, 
        overwrite = True,  
        timeout_in_milliseconds=TIMEOUT_IN_MILLISECONDS 
    )
    
    output_status_message("Download result file: {0}\n".format(result_file_path))

def download_results(request_id, authorization_data):
    reporting_download_operation = ReportingDownloadOperation(
        request_id = request_id, 
        authorization_data=authorization_data, 
        poll_interval_in_milliseconds=1000, 
        environment=ENVIRONMENT,
    )

    reporting_operation_status = reporting_download_operation.track(timeout_in_milliseconds=TIMEOUT_IN_MILLISECONDS)
    
    result_file_path = reporting_download_operation.download_result_file(
        result_file_directory = FILE_DIRECTORY, 
        result_file_name = DOWNLOAD_FILE_NAME, 
        decompress = True, 
        overwrite = True,  
        timeout_in_milliseconds=TIMEOUT_IN_MILLISECONDS 
    ) 

    output_status_message("Download result file: {0}".format(result_file_path))
    output_status_message("Status: {0}\n".format(reporting_operation_status.status))

if __name__ == '__main__':

    print("Python loads the web service proxies at runtime, so you will observe " \
          "a performance delay between program launch and main execution...\n")
    
    authorization_data=AuthorizationData(
        account_id=None,
        customer_id=None,
        developer_token=DEVELOPER_TOKEN,
        authentication=None,
    )

    reporting_service_manager=ReportingServiceManager(
        authorization_data=authorization_data, 
        poll_interval_in_milliseconds=5000, 
        environment=ENVIRONMENT,
    )

    reporting_service=ServiceClient(
        'ReportingService', 
        authorization_data=authorization_data, 
        environment=ENVIRONMENT,
        version=11,
    )

    authenticate(authorization_data)
    accountID = [XXXXX,XXXXX,XXXXX,XXXXX]
    accountName = ['XXXXXXXXXXXXX','XXXXXXXXXXXXX','XXXXXXXXXXXXX', 'XXXXXXXXXXXXX']
    for i in range(0,len(accountID)):
        main(authorization_data,accountID[i],accountName[i])