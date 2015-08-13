import re

api_data = open('elblogs.txt')

partner_info = {'partner': '/callback/nyr8nx', 'campaign_id': 'cid=X9KN0'}
callback_count = 0
campaign_callback_count = 0

for line in api_data:
    if partner_info['partner'] in line:
        callback_count += 1
    if partner_info['partner'] in line and partner_info['campaign_id'] in line:
        campaign_callback_count += 1

print callback_count
print campaign_callback_count

def count_api_requests():
    requests = {}
    api_data = open('elblogs.txt')
    for line in api_data:
        if 'api/' in line:
            api_request = re.search('api/\S*', line).group(0).strip()
            if api_request in requests:
                requests[api_request] += 1
            else:
                requests[api_request] = 1
    return requests

def total_api_requests(requests):
    return sum(requests.values())

api_requests = count_api_requests()
for k, v in api_requests.iteritems():
    print k + ': ' + str(v)

print 'Total api requests: ' + str(total_api_requests(count_api_requests()))