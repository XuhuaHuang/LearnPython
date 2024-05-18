# Topic: Work with pie charts
# File: pie_charts.py
# reading data from CSV files and plot them into a pie chart
# Author: Xuhua Huang
#
# Highlights:
# 1) matplotlib.pyplot.barh method to create pie charts
#
# Last updated: Aug 17, 2021
# Created on: Aug 17, 2021

# %%
from matplotlib import pyplot as plt


def main() -> None:
    """ Play around the pie chart with some meaningless data. """
    # slices: list[int] = [120, 80, 30, 20]
    # labels: list[str] = ['Sixty', 'Forty', 'Fifteen', 'Ten']
    # colours: list[str] = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']
    # plt.pie(slices, labels=labels, colors=colours, wedgeprops={'edgecolor': 'black'})
    #
    # plt.title('My Customized Pie Chart')
    # plt.style.use('seaborn-dark')
    # plt.tight_layout()
    # plt.show()

    """ Using survey data presented by the Stack OverFlow. """
    """ Data has been filtered down to top 5 most popular languages. """
    pie_chart_slices: list[int] = [35917, 36443, 47544, 55466, 59219]
    pie_chart_labels: list[str] = ['Java', 'Python', 'SQL', 'HTML/CSS', 'JavaScript']
    explode: list[float] = [0, 0.1, 0, 0, 0]
    plt.pie(pie_chart_slices, labels=pie_chart_labels,
            explode=explode,  # apply explode index to make element pop out
            startangle=90, autopct='%1.1f%%', shadow=True, wedgeprops={'edgecolor': 'black'})

    plt.title('Top 5 Most Popular Programming Languages in 2019')
    plt.style.use('default')
    plt.tight_layout()
    plt.show()

    return


if __name__ == '__main__':
    main()

# %%
