# Topic: Work with stack plots
# File: 04_stack_plots.py
# plot data with respect to time
# Author: Xuhua Huang
#
# Highlights:
# TODO: filling area on line plots
# 1) matplotlib.pyplot.stackplot method
# 2) add labels and specify colors of the plot
#
# Last updated: Aug 18, 2021
# Created on: Aug 18, 2021

from matplotlib import pyplot as plt


def main():
    # x and y axis data
    minutes_into_game: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_1_scores: list[int] = [1, 2, 3, 3, 4, 4, 4, 4, 5]
    player_2_scores: list[int] = [1, 1, 1, 1, 2, 2, 2, 3, 4]
    player_3_scores: list[int] = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    # labels and colour for each plot in the form of lists
    label_list: list[str] = ['Player 1 scores', 'Player 2 scores', 'Player 3 scores']
    color_list: list[str] = ['#6d904f', '#fc4f30', '#008fd5']  # green, red, blue in hex decimals form

    plt.stackplot(minutes_into_game,
                  player_1_scores, player_2_scores, player_3_scores,
                  labels=label_list,
                  colors=color_list)
    # add some extra information to the plot
    plt.title('Player Scores over Minutes into the Game')
    plt.style.use('seaborn-dark')
    plt.legend(loc='upper left')  # specify the location of the legend
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
