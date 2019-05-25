#!/usr/bin/env python

import sys
import xlwt
import csv
import os.path

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.errors import HttpError
from oauth2client.client import HttpAccessTokenRefreshError
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy


def main(argv):
    index = 0
    output_file = "output.xls"
    output_sheet = "sheet1"

    if os.path.isfile(output_file):
        print('Output file exists!')
        wb = open_workbook(output_file)
    else:
        print('Output file not exists!')
        new_workbook = xlwt.Workbook(output_file)
        ws = new_workbook.add_sheet(output_sheet)
        new_workbook.save(output_file)
        print('Output file created!')
        wb = open_workbook(output_file)

    # Create virtual copy of the sheet
    rb = copy(wb)
    sheet1 = rb.get_sheet(output_sheet)

    with open('users.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            user = row[0]
            print("Index: " + str(index) + " user: " + user)
            status = "Failed"
            error = "NONE"

            try:
                credentials = ServiceAccountCredentials.from_json_keyfile_name(
                    'creds.json', scopes='https://mail.google.com')
                credentials = credentials.create_delegated(user)

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
                status = "Success"
            except HttpAccessTokenRefreshError as e:
                error = 'An error occurred HttpAccessTokenRefreshError: %s' % e
                print(error)
            except HttpError as err:
                error = 'An error occurred HttpError: %s' % err
                print(error)

            sheet1.write(index, 1, user)
            sheet1.write(index, 2, status)
            sheet1.write(index, 3, error)
            index += 1
    rb.save(output_file)


if __name__ == '__main__':
    main(sys.argv)
