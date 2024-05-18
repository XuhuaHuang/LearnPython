# Topic: Getting hands on with Matplotlib
# File: mpl_demo.py
# naming conventions, starting point and more
# Author: Xuhua Huang
#
# Last updated: Aug 14, 2021
# Created on: Aug 14, 2021

# %%
from matplotlib import pyplot as plt  # following conventional naming


def main() -> None:
    # age as x axis coordinate
    ages_x_coord = [*range(25, 36, 1)]  # age ranging form 25 to 35; [25, 36)
    # print(ages_x_coord) # for troubleshooting purposes only

    # create a list containing median salary for all developers as y axis
    # coordinate
    dev_y_coord = [38496, 42000, 46752, 49320, 53200,
                   56000, 62316, 64928, 67317, 68748, 73752]
    plt.plot(ages_x_coord, dev_y_coord, color='#444444',
             linestyle='--', marker='.', label='All Developers')

    """ Plot a Graph Specifically for Python Developers. """
    py_dev_y = [45572, 48876, 53850, 57287, 63014,
                65998, 70003, 70000, 71496, 75370, 83460]
    plt.plot(ages_x_coord, py_dev_y, color='#5a7d9a',
             linewidth=3, marker='o', label='Python Developers')

    """ Plot a Graph Specifically for JavaScript Developers"""
    js_dev_y = [37812, 43515, 46823, 49293, 53437,
                56373, 62375, 66674, 68475, 68746, 74583]
    plt.plot(ages_x_coord, js_dev_y, color='#adad3b',
             label='JavaScript Developers')

    # add some extra information to the image
    plt.title('Median Salary (USD) by Age as Software Engineers')
    # the same order as they are added
    plt.legend(['All Developers', 'Python Developers', 'JavaScript'])
    plt.xlabel('Age')
    plt.ylabel('Median Salary (USD)')
    # show the grids in the background
    plt.grid(True)
    # change to the layout to avoid padding
    plt.tight_layout()
    # show the plot with a style
    # customized line style and color in plot statements will overwrite themes
    plt.style.use('seaborn-dark')
    plt.show()
    plt.savefig('01_mpl_demo.png')

    return


if __name__ == '__main__':
    main()

# %%
