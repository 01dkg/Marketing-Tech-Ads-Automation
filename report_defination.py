import datetime


class ReportDefinition:
    def __init__(self, report_type, fields, predicates=None, last_days=None, date_from=None, date_to=None):
        """ Create report definition as needed in api call from meta information
        :param report_type: str, https://developers.google.com/adwords/api/docs/appendix/reports
        :param fields: list of str
        :param predicates: list of dicts
        :param last_days: int, date_to = yesterday and date_from = today - days_ago
        :param date_from: str, format YYYYMMDD or YYYY-MM-DD
        :param date_to: str, format YYYYMMDD or YYYY-MM-DD
        """
        self.report_type = report_type
        self.fields = fields
        self.predicates = predicates

        self.date_min = date_from
        self.date_max = date_to
        self.last_days = last_days

        self.raw = self._as_dict()

    def _as_dict(self):
        self._determine_dates()

        report_def = {
            "reportName": "api_report",
            "dateRangeType": "CUSTOM_DATE",
            "reportType": self.report_type,
            "downloadFormat": "CSV",
            "selector": {
                "fields": self.fields,
                "dateRange": {
                    "min": self.date_min,
                    "max": self.date_max
                }
            }
        }
        if self.predicates is not None:
            report_def["selector"]["predicates"] = self.predicates
        return report_def