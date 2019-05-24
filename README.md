## Pre-requisites

1. Configure google service account enabling Domain-Wide Delegation of Authority.
2. Download the service account configs(JSON) and rename it to creds.json
3. Copy creds.json into the same directory where check-lables.py exists.
4. Register https://mail.google.com scope along with the client-name at Manage API client access under security within Google admin console.
5. Make sure you have Google OAuth2 API Client Library for Python installed locally before running the script.
For info: https://developers.google.com/api-client-library/python/apis/oauth2/v1

## How to run

```
$ python3 check-labels.py <USER_EMAIL_ID>
```

Before executing following make sure to install all dependencies listed.
1. xlwt 
2. xlrd
3. xlutils

Eg:- 
```
pip3 install xlwt
```
Then run,

```
$ python3 check-labels-out.py <USER_EMAIL_ID> <INDEX>
```

If you have a list of users within a CSV file, saved in the same dierctory where check-labels-full.py exists.

Eg:- users.csv

```
user1@sample.net
user2@sample.com
user3@sample.in

```

Run

```
python3 check-labels-full.py
```