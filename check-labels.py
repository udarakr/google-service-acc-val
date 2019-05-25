#!/usr/bin/env python

import sys

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.errors import HttpError
from oauth2client.client import HttpAccessTokenRefreshError


def main(argv):
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'creds.json', scopes='https://mail.google.com')
        credentials = credentials.create_delegated(argv[1])

        service = build('gmail', 'v1', credentials=credentials)

        # Call the Gmail API to fetch user's mail box labels
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        # List and print labels
        if not labels:
            print('No labels in the mail box.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])
    except HttpAccessTokenRefreshError as e:
        print('An error occurred HttpAccessTokenRefreshError: %s' % e)
    except HttpError as err:
        print('An error occurred HttpError: %s' % error)


if __name__ == '__main__':
    main(sys.argv)
