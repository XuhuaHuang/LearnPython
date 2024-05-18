# Topic: Filling area with linear plots
# File: plot_fills.py
# Author: Xuhua Huang
# Last updated: Aug 22, 2021
# Created on: Aug 22, 2021


# %%
import pandas as pd
from matplotlib import pyplot as plt


# noinspection PyTypeChecker
def main() -> None:
    csv_data = pd.read_csv('data_05.csv')
    ages = csv_data['Age']
    dev_salaries = csv_data['All_Devs']
    py_salaries = csv_data['Python']
    js_salaries = csv_data['JavaScript']

    """ Call plt.plot() and specify the color, line styles labels of the plot. """
    plt.plot(ages, dev_salaries,
             color='#444444',
             linestyle='--', label='All Devs')
    plt.plot(ages, py_salaries, label='Python')

    """ Use plt.fill_between() to fill the area underneath. """
    overall_median: int = 57287
    plt.fill_between(ages, py_salaries, y2=dev_salaries,
                     where=(py_salaries > dev_salaries),
                     interpolate=True,
                     alpha=0.25,
                     label='Above Avg')
    # between x axis (ages) and python developer salaries
    # when plot is below y2, it fills upward and vice versa

    # handle the case when python devs salaries are lower than all devs average
    # plot the area in red
    plt.fill_between(ages, py_salaries, y2=dev_salaries,
                     where=(py_salaries <= dev_salaries),
                     interpolate=True,
                     color='red',  # custom color with transparency set to a quarter
                     alpha=0.25,
                     label='Below Avg')

    """ Add some extra information to the plot. """
    plt.legend()
    plt.title('Median Salary (USD) by Age')
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.style.use('default')
    plt.tight_layout()
    plt.show()

    return


if __name__ == '__main__':
    main()

# %%
