from lib.api_tracker import ApiTracker

if __name__ == "__main__":
    api_tracker = ApiTracker('elblogs.txt')
    api_requests = api_tracker.count_api_requests()
    total_requests = api_tracker.total_api_requests(api_requests)

    api_tracker.sort_request_list(api_requests, total_requests)
    print 'Total API Requests: ' + str(total_requests)
