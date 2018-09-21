#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection


troops = pd.read_csv(os.path.join('minard_troops.csv'))
cities = pd.read_csv(os.path.join('minard_cities.csv'))
temps = pd.read_csv(os.path.join('minard_temps.csv'), parse_dates=['date'])

fig_dict = {'figsize': (12, 6), 'facecolor': 'white'}
grid_dict = {'height_ratios': [4, 1],
             'width_ratios': [1]}
fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=False,
                        gridspec_kw=grid_dict, **fig_dict)
for ax in axs:
    # ax.set_axis_off()
    fig.add_axes(ax)
    plt.setp(ax.spines.values(), color='black')


def graph_temp():
    axs[1].plot(temps['lon'], temps['temperature'], color='black', linewidth=.5)
    axs[1].plot(temps['lon'], temps['temperature']-.5, color='#cccccc', linewidth=1)
    axs[1].set_xlim([20, 40])
    axs[1].set_yticks([0, -10, -20, -30])
    axs[1].set_xticks([])
    axs[1].yaxis.grid(which='major', color='#cccccc', linestyle='-')
    


def build_lines(direction, division, color):
    troop_scaling = 6000
    endcapscl = .2
    # Need to lower retreating troops so as not to overlap advancing
    yoffset = -.5 if direction == 'R' else 0

    # Select only troop movements marked with the correct direction
    _troops = troops[troops['direction'] == direction]
    # Same for division
    _troops = _troops[_troops['division'] == division]

    points = np.array([_troops['lon'],
                       _troops['lat'] + yoffset]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # Scale overlaping by width of line
    end = endcapscl * \
          _troops.iloc[:len(_troops)-1, 2] / troops['survivors'].max()
    # Ugly numpy code to make line segments overlap
    segments[:, 0, 0] -= (segments[:, 1, 0] - segments[:, 0, 0]) * end
    segments[:, 1, 0] += (segments[:, 1, 0] - segments[:, 0, 0]) * end
    segments[:, 0, 1] -= (segments[:, 1, 1] - segments[:, 0, 1]) * end
    segments[:, 1, 1] += (segments[:, 1, 1] - segments[:, 0, 1]) * end

    return LineCollection(segments,
                          linewidths=_troops['survivors'] / troop_scaling,
                          color=color)


def graph_troops():
    lc = build_lines('A', 1, '#cccccc')
    axs[0].add_collection(lc)

    lc = build_lines('R', 1, '#000000')
    axs[0].add_collection(lc)

    axs[0].set_xlim([20, 40])
    axs[0].set_ylim([50, 60])
    axs[0].add_collection(lc)


graph_temp()
graph_troops()

plt.show()
