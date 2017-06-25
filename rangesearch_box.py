#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np

def _search_segment(sorted_arr, pt, (l_l, r_l)):
    beg = np.searchsorted(sorted_arr[:, 1], pt + l_l, side='left')
    end = np.searchsorted(sorted_arr[:, 1], pt + r_l, side='right')

    return [sorted_arr[b:e, 0].astype(np.int) for b, e in zip(beg, end)]

def rangesearch_box(X):
    indexed_arr = np.concatenate((np.array(xrange(len(X)))[:, np.newaxis], X), axis=1)
    sorted_arr = [indexed_arr[indexed_arr[:, i].argsort(axis=0)][:, (0, i)] for i in xrange(1, indexed_arr.shape[1])]

    intersect = lambda a, b: np.intersect1d(a, b, assume_unique=True)

    def query(pt, boundaries):
        all_ix = [_search_segment(s_arr_1d, pt[:, i], limit) for i, (s_arr_1d, limit) \
                                            in enumerate(zip(sorted_arr, boundaries))]

        return np.array([reduce(intersect, p) for p in zip(*all_ix)])

    return query
