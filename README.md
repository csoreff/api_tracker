# API Tracker

###1) How many callbacks did we receive for partner id nyr8nx?
===

The method 'find_partner_callback_count' finds the number of callbacks for any
partner passed in as an argument.

Partner 'nyr8nx' callbacks: 96

###2) How many callbacks did we receive for partner nyr8nx for campaign id (cid) X9KN0?
===

The method 'find_partner_campaign_callback_count' finds the number of callbacks for a specific campaign id and partner name passed in as arguments.

Campaign 'X9KN0' callbacks for partner 'nyr8nx': 27

###3) Write a python script that analyzes elblogs.txt and counts all API requests (requests starting with api/). Print them out in descending frequency.
===

api_tracker.py, when run, will print out the answers to questions #1 and #2, as well as print a sorted list of the api requests in descending frequency.  It ends by printing the total number of api requests.

Output:

24.20   36226    api/v1/track_offer_views
18.59   27836    api/v1/device_info
15.58   23328    api/v1/match_member_check
11.23   16816    api/v1/report_daily_data_usage
7.09    10608    api/v1/login
4.38    6559     api/v1/topup_history
2.85    4266     api/v1/register
2.59    3874     api/v1/track_experiment_variant
2.28    3408     api/v1/topups_available
1.82    2719     api/v1/topup_details
1.46    2191     api/v1/topup_purchase
1.33    1997     api/airtime/topup_callback
1.33    1984     api/v1/register_confirmation
1.00    1492     api/v1/profile
0.89    1331     api/v1/track_mcode_and_traffic_code_arrived
0.54    814      api/v1/updated_installed_apks
0.48    712      api/v1/profile/forgot_password
0.42    629      api/v1/get_operators
0.35    525      api/v1/contacts/add_phone
0.28    414      api/v1/resend_confirmation
0.26    395      api/v1/topup_recall
0.23    344      api/v1/logout
0.17    249      api/v1/profile/forgot_password_auth
0.16    234      api/v1/profile/forgot_password_reset
0.14    208      api/v1/offer_user_hidden
0.10    144      api/v1/contacts/confirm_phone
0.07    103      api/v1/member_id
0.07    102      api/v1/contacts/update_phone_operator
0.04    57       api/v1/contacts/resend_confirmation_sms
0.03    51       api/v1/contacts/add_email
0.02    33       api/v1/more_offer_history
0.02    25       api/v1/contacts/resend_email_confirmation
0.01    13       api/v1/member_code
0.01    8        api/v1/installed_apks
0.00    2        api/v1/track_mcode_arrived
0.00    1        api/v1/contacts/set_primary_email
Total API Requests: 149698
