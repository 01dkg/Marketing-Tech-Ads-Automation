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
        # You can submit one of the example reports, or build your own.

        #report_request=get_budget_summary_report_request()
        report_request=AdGroupPerformanceReport(accountID,accountName)
        #report_request = GoalReport(accountID, accountName)
        #report_request=get_user_location_performance_report_request()
        #report_request=get_keyword_performance_report_request()
        
        reporting_download_parameters = ReportingDownloadParameters(
            report_request=report_request,
            result_file_directory = FILE_DIRECTORY, 
            result_file_name = accountName +'-' + str(dd.date.today()) +'.csv',
            overwrite_result_file = True, # Set this value true if you want to overwrite the same file.
            timeout_in_milliseconds=TIMEOUT_IN_MILLISECONDS # You may optionally cancel the download after a specified time interval.
        )
