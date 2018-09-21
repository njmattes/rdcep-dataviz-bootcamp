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
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.setp(ax.spines.values(), color='black')


def graph_temp():
    axs[1].plot(temps['lon'], temps['temperature'])
    axs[1].set_xlim([20, 40])


def graph_troops():
    troop_scaling = 6000
    division = 1
    endcapscl = .1
    # Select only troop movements marked 'advancing'
    advance = troops[troops['direction'] == 'A']
    advance = advance[advance['division'] == division]
    points = np.array([advance['lon'], advance['lat']+.5]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    # Ugly numpy code to make line segments overlap
    # Scale overlaping by width of line
    end = endcapscl * 2 * advance.loc[:13, 'survivors']/troops['survivors'].max()
    segments[:, 0, 0] -= (segments[:, 1, 0] - segments[:, 0, 0]) * end
    segments[:, 1, 0] += (segments[:, 1, 0] - segments[:, 0, 0]) * end
    segments[:, 0, 1] -= (segments[:, 1, 1] - segments[:, 0, 1]) * end
    segments[:, 1, 1] += (segments[:, 1, 1] - segments[:, 0, 1]) * end
    lc = LineCollection(segments, linewidths=advance['survivors']/troop_scaling,
                        color='#dddddd')
    axs[0].add_collection(lc)

    # Select only troop movements marked 'retreating'
    retreat = troops[troops['direction'] == 'R']
    retreat = retreat[retreat['division'] == division]
    points = np.array([retreat['lon'], retreat['lat']]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    segments[:, 0, 0] -= (segments[:, 1, 0] - segments[:, 0, 0]) * endcapscl
    segments[:, 1, 0] += (segments[:, 1, 0] - segments[:, 0, 0]) * endcapscl
    segments[:, 0, 1] -= (segments[:, 1, 1] - segments[:, 0, 1]) * endcapscl
    segments[:, 1, 1] += (segments[:, 1, 1] - segments[:, 0, 1]) * endcapscl
    lc = LineCollection(segments, linewidths=retreat['survivors']/troop_scaling,
                        color='#000000')

    axs[0].set_xlim([20, 40])
    axs[0].set_ylim([50, 60])
    axs[0].add_collection(lc)


graph_temp()
graph_troops()

plt.show()
