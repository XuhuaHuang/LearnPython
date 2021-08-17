# Topic: Work with bar charts
# File: 02_bar_charts_from_csv.py
# reading data from CSV files and plot them
# Author: Xuhua Huang
# 
# Highlights:
# 1) matplotlib.pyplot.barh method to create horizontal bar charts
# 2) pandas.read_csv() to open a CSV file and access the rows/columns as a list
#
# Last updated: Aug 15, 2021
# Created on: Aug 15, 2021

from matplotlib import pyplot as plt  # following conventional naming
import numpy as np
import pandas as pd
import csv
from collections import Counter


def main():
    """ Open data.csv file and read from it with context manager
    Replaced later on with pandas.read_csv() approach """
    # with open('data.csv', mode='r', encoding='utf-8') as data_csv_file:
    #     csv_reader = csv.DictReader(data_csv_file)
    #     language_counter = Counter()
    #     # loop over the dictionary and count the occurrence of items
    #     for row in csv_reader:
    #         language_counter.update(row['LanguagesWorkedWith'].split(';'))

    """ Read provided CSv file with pandas """
    language_counter = Counter()
    data = pd.read_csv('data.csv')
    ids: list[str] = data['Responder_id']
    lang_responses: list[str] = data['LanguagesWorkedWith']
    # loop over the dictionary and count the occurrence of items
    for response in lang_responses:
        language_counter.update(response.split(';'))

    print("Printing the most commonly used languages in tuple form:\n", language_counter.most_common(15))

    """ Create lists as place holders to append data to plot later. """
    languages: list[str] = []
    popularity: list[int] = []
    # loop over the tuple from the counter
    # variable lang_ppl_pair stands for 'language-popularity-pair'
    for lang_ppl_pair in language_counter.most_common(15):
        languages.append(lang_ppl_pair[0])
        popularity.append(lang_ppl_pair[1])

    # swap the order of those two lists for plotting
    languages.reverse()
    popularity.reverse()
    # for troubleshooting purpose
    print("Printing the most commonly used languages in reversed order:\n", languages)
    print("Printing popularity for corresponding language in reversed order:\n", popularity)

    """ Create bar charts for collected data in the list format. """
    plt.barh(languages, popularity)  # horizontal bar chart
    plt.title('Most Popular Languages Used')
    plt.xlabel('Programming Languages')
    plt.ylabel('Number of People Who Use')
    # adjust some visual representation details for chart
    plt.grid(True)
    plt.tight_layout()
    plt.style.use('seaborn-dark')
    plt.show()


if __name__ == '__main__':
    main()
