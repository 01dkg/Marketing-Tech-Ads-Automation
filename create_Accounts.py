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

  # Create the account. It is possible to create multiple accounts with one
  # request by sending an array of operations.
  accounts = managed_customer_service.mutate(operations)

  # Display results.
  for account in accounts['value']:
    print ('Account with customer ID "%s" was successfully created.'
           % account['customerId'])


if __name__ == '__main__':
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()
  main(adwords_client)
    
    # Create the account. It is possible to create multiple accounts with one
 # request by sending an array of operations.
 accounts = managed_customer_service.mutate(operations)

 # Display results.
 for account in accounts['value']:
   print ('Account with customer ID "%s" was successfully created.'
          % account['customerId'])


if __name__ == '__main__':
 # Initialize client object.
 adwords_client = adwords.AdWordsClient.LoadFromStorage()
 main(adwords_client)
