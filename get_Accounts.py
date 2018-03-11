from datetime import datetime
from googleads import adwords


def main(client):
  # Initialize appropriate service.
  managed_customer_service = client.GetService(
      'ManagedCustomerService', version='v201802')

  today = datetime.today().strftime('%Y%m%d %H:%M:%S')
  # Construct operations and add campaign.
  operations = [{
      'operator': 'ADD',
      'operand': {
          'name': 'Account created with ManagedCustomerService on %s' % today,
          'currencyCode': 'EUR',
          'dateTimeZone': 'Europe/London',
      },

  