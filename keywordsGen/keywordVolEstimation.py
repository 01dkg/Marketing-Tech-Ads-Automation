from googleads import adwords


def main(client):
  # Initialize appropriate service.
  traffic_estimator_service = client.GetService(
      'TrafficEstimatorService', version='v201802')

  # Construct selector object and retrieve traffic estimates.
  keywords = [
      {'text': 'mars cruise', 'matchType': 'BROAD'},
      {'text': 'cheap cruise', 'matchType': 'PHRASE'},
      {'text': 'cruise', 'matchType': 'EXACT'}
  ]
  negative_keywords = [
      {'text': 'moon walk', 'matchType': 'BROAD'}
  ]
  keyword_estimate_requests = []
  for keyword in keywords:
    keyword_estimate_requests.append({
        'keyword': {
            'xsi_type': 'Keyword',
            'matchType': keyword['matchType'],
            'text': keyword['text']
        }
    })
