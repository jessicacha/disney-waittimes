#!/usr/bin/env python3
"""Collect raw data from
    https://touringplans.com/walt-disney-world/crowd-calendar#DataSets

Citation: Disney World Ride Wait Time Datasets, TouringPlans.com, June 2018,

"""
import os

import requests

from constants import FILE_URLS


def download_file(url):
    """Downloads file from the url and save it as filename"""
    filename = os.path.basename(url)
    filepath = 'data/raw/{}'.format(filename)
    # check if file already exists
    if not os.path.isfile(filepath):
        print('Downloading file: {}'.format(filepath))
        response = requests.get(url)
        # Check if the response is ok (200)
        if response.status_code == 200:
            # Open file and write the content
            with open(filepath, 'wb') as file:
                # A chunk of 128 bytes
                for chunk in response:
                    file.write(chunk)
    else:
        print('File {} exists'.format(filepath))


def main():
    """Main function"""
    for url in FILE_URLS:
        download_file(url)

    print('DONE !')


if __name__ == '__main__':
    main()
