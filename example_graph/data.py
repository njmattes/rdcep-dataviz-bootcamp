#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


data = [
    [17, 21, 31, 28, 19, 14, 11, 27, 23, 28],
    [10,  7, 12, 10, 22, 14, 13, 14, 10, 11],
    [ 4,  3,  7,  1,  3,  4,  3, 10, 13,  7],
    [ 5,  4,  5,  2,  0,  4,  2,  5,  6,  5],
    [ 3,  1,  4,  2,  4,  4,  3,  5,  1,  4],
    [ 2,  1,  2,  3,  1,  5,  4,  2,  1,  4],
    [ 4,  4,  2,  0,  6,  8,  5,  4,  5,  2],
    [ 0,  2,  1,  0,  0,  1,  4,  4,  5,  1],
    [ 1,  3,  0,  0,  0,  2,  0,  0,  0,  0],
    [ 1,  2,  0,  3,  1,  1,  2,  0,  1,  0],
]

names = [
    'Florida', 'Australia', 'Hawai‘i', 'S Carolina', 'California & N Carolina',
    '', 'S Africa', 'Réunion Islands', 'Brazil & Bahamas', '',
]

colors = [
    '#8a1513',
    '#c32828',
    '#f47c27',
    '#f7b815',
    '#cfdeee',
    '#cfdeee',
    '#5e8eca',
    '#2a5592',
    '#1c3666',
    '#1c3666',
]


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    # plt.set_cmap('Paired')
    # fig = plt.figure(figsize=(5, 5))
    # ax = fig.add_axes([.1, .2, 0.5, .7])
    # ax.yaxis.grid(which='major', color='#cccccc', linestyle='-', linewidth=1)
    # plt.setp(ax.spines.values(), color=None)
    # plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='white')
    # plt.xticks([2005, 2014])
    # cidx = np.arange(0, 1, len(data[0]))
    # fig.suptitle('Total shark attacks by area (2005–2014)',
    #              x=.05, horizontalalignment='left')
    # fig.text(.05, .05, 'SOURCE\nInternational Shark Attack File, '
    #                    'Florida Museum of Natural History,\n'
    #                    'University of Florida (Last updated Feb. 11, 2015)',
    #          fontsize=8)
    # for i in range(len(data)):
    #     ax.plot(np.arange(2005, 2015), data[i],
    #             color=plt.get_cmap('Paired')(i))
    #
    #     ax.text(2014.5, data[i][-1], names[i], fontsize=12,
    #             color=plt.get_cmap('Paired')(i),
    #             verticalalignment='center')
    # plt.show()
    from numpy import arange, array, ones, linalg
    xi = arange(0,9)
    A = array([ xi, ones(9)])
    # linearly generated sequence
    y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
    w = linalg.lstsq(A.T,y)[0] # obtaining the parameters
    print(w)
    print(A)
