from googleads import adwords


def main(client):
  # Initialize appropriate service.
  traffic_estimator_service = client.GetService(
      'TrafficEstimatorService', version='v201802')
  matchTypeList =[]
  keywordList =[]
  negative_matchTypeList =[]
  negative_keywordList =[]
  # Construct selector object and retrieve traffic estimates.

  #KeyWords and Match Type Combinations to get estimate
  keywords = [
      {'text': 'keywordList, 'matchType': matchTypeList}  ]
  negative_keywords = [
      {'text': negative_keywordList, 'matchType': negative_matchTypeList}
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

  for keyword in negative_keywords:
    keyword_estimate_requests.append({
        'keyword': {
            'xsi_type': 'Keyword',
            'matchType': keyword['matchType'],
            'text': keyword['text']
        },
        'isNegative': 'true'
    })

  # Create ad group estimate requests.
  adgroup_estimate_requests = [{
      'keywordEstimateRequests': keyword_estimate_requests,
      'maxCpc': {
          'xsi_type': 'Money',
          'microAmount': '1000000'
      }
  }]

  # Create campaign estimate requests.
  campaign_estimate_requests = [{
      'adGroupEstimateRequests': adgroup_estimate_requests,
      'criteria': [
          {
              'xsi_type': 'Location',
              'id': '2840'  # United States.
          },
          {
              'xsi_type': 'Language',
              'id': '1000'  # English.
          }
      ],
  }]

  # Create the selector.
  selector = {
      'campaignEstimateRequests': campaign_estimate_requests,
  }

  selector['platformEstimateRequested'] = True

  # Get traffic estimates.
  estimates = traffic_estimator_service.get(selector)

  campaign_estimate = estimates['campaignEstimates'][0]

  # Display the campaign level estimates segmented by platform.
  if 'platformEstimates' in campaign_estimate:
    platform_template = ('Results for the platform with ID: "%d" and name: '
                         '"%s".')
    for platform_estimate in campaign_estimate['platformEstimates']:
      platform = platform_estimate['platform']
      DisplayEstimate(platform_template % (platform['id'],
                                           platform['platformName']),
                      platform_estimate['minEstimate'],
                      platform_estimate['maxEstimate'])

  # Display the keyword estimates.
  if 'adGroupEstimates' in campaign_estimate:
    ad_group_estimate = campaign_estimate['adGroupEstimates'][0]
    if 'keywordEstimates' in ad_group_estimate:
      keyword_estimates = ad_group_estimate['keywordEstimates']
      keyword_template = ('Results for the keyword with text "%s" and match '
                          'type "%s":')

      keyword_estimates_and_requests = zip(keyword_estimates,
                                           keyword_estimate_requests)

      for keyword_tuple in keyword_estimates_and_requests:
        if keyword_tuple[1].get('isNegative', False):
          continue
        keyword = keyword_tuple[1]['keyword']
        keyword_estimate = keyword_tuple[0]
        DisplayEstimate(keyword_template % (keyword['text'],
                                            keyword['matchType']),
                        keyword_estimate['min'], keyword_estimate['max'])


def _CalculateMean(min_est, max_est):
  if min_est and max_est:
    return (float(min_est) + float(max_est)) / 2.0
  else:
    return None


def _FormatMean(mean):
  if mean:
    return '%.2f' % mean
  else:
    return 'N/A'

#Function to Display output results from google
def DisplayEstimate(message, min_estimate, max_estimate):
  mean_avg_cpc = (_CalculateMean(min_estimate['averageCpc']['microAmount'],
                                 max_estimate['averageCpc']['microAmount'])
                  if 'averageCpc' in min_estimate
                  and min_estimate['averageCpc'] else None)
  mean_avg_pos = (_CalculateMean(min_estimate['averagePosition'],
                                 max_estimate['averagePosition'])
                  if 'averagePosition' in min_estimate
                  and min_estimate['averagePosition'] else None)
  mean_clicks = _CalculateMean(min_estimate['clicksPerDay'],
                               max_estimate['clicksPerDay'])
  mean_total_cost = _CalculateMean(min_estimate['totalCost']['microAmount'],
                                   max_estimate['totalCost']['microAmount'])

  print message
  print '  Estimated average CPC: %s' % _FormatMean(mean_avg_cpc)
  print '  Estimated ad position: %s' % _FormatMean(mean_avg_pos)
  print '  Estimated daily clicks: %s' % _FormatMean(mean_clicks)
  print '  Estimated daily cost: %s' % _FormatMean(mean_total_cost)


if __name__ == '__main__':
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()

  main(adwords_client)