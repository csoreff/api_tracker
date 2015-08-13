# API Tracker

###1) How many callbacks did we receive for partner id nyr8nx?
===

The function 'find_partner_callback_count' in api_tracker.py finds the number of callbacks for any partner passed in as an argument.

Partner 'nyr8nx' callbacks: 96

###2) How many callbacks did we receive for partner nyr8nx for campaign id (cid) X9KN0?
===

The function 'find_partner_campaign_callback_count' in api_tracker.py finds the number
of callbacks for a specific campaign id and partner name passed in as arguments.

Campaign 'X9KN0' callbacks for partner 'nyr8nx': 27

###3) Write a python script that analyzes elblogs.txt and counts all API requests (requests starting with api/). Print them out in descending frequency.
===

api_tracker.py, when run, will print a sorted list of the api requests in descending
frequency, followed by the total number of api requests.
