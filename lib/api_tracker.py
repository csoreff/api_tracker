import re
from operator import itemgetter

class ApiTracker:

    def __init__(self, access_log):
        # self.api_data = open(access_log)
        self.api_data = []
        with open(access_log, 'r') as f:
            for line in f:
                self.api_data.append(line)

    def find_partner_callback_count(self, partner_name):
        partner = "/callback/{}".format(partner_name)
        callback_count = 0
        for line in self.api_data:
            if partner in line:
                callback_count += 1

        return partner_name + ' callbacks: ' + str(callback_count)


    def find_partner_campaign_callback_count(self, partner_name, campaign_id):
        partner_info = {
            'partner': "/callback/{}".format(partner_name),
            'campaign_id': "cid={}".format(campaign_id)
        }
        campaign_callback_count = 0
        for line in self.api_data:
            if (partner_info['partner'] in line
                    and partner_info['campaign_id'] in line):
                campaign_callback_count += 1

        return 'Campaign ' + campaign_id + ' callbacks: ' + str(campaign_callback_count)


    def count_api_requests(self):
        requests = {}
        for line in self.api_data:
            if 'api/' in line:
                api_request = re.search('api/\S*', line).group(0).strip()
                if api_request in requests:
                    requests[api_request] += 1
                else:
                    requests[api_request] = 1

        return requests

    @staticmethod
    def sort_request_list(api_requests, total_requests):
        api_requests = sorted(api_requests.iteritems(), key=itemgetter(1), reverse=True)
        for k, v in api_requests:
            percentage_of_requests = float(v)/total_requests*100
            print '{:7} {:8} {:50}'.format("%.2f" % percentage_of_requests + '%', str(v), k)


    @staticmethod
    def total_api_requests(requests):
        return sum(requests.values())
