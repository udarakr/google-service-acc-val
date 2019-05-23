## Pre-requites

1. Configure google service account enabling Domain-Wide Delegation of Authority.
2. Download the service account configs(JSON) and rename it to creds.json
3. Copy creds.json into the same directory where check-lables.py exists.
4. Register https://mail.google.com scope along with the client-name at Manage API client access under security within Google admin console.
5. Make sure you have Google OAuth2 API Client Library for Python installed locally before running the script.
For info: https://developers.google.com/api-client-library/python/apis/oauth2/v1

How to run:

$ python check-lables.py <USER_EMAIL_ID>