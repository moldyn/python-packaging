# -*- coding: utf-8 -*-
"""Performing PCA based on covariance/corrleation."""
import numpy as np

def perform_pca(data, corr=False):
    """Perform PCA based on covariance/correlation."""
    # scaler data to make mean-free (std-free)
    data = data - np.mean(data, axis=0)
    if corr:
        data = data / np.std(data, axis=0, ddof=1)

    # calculate cov/corr matrix and diagonalize
    cov = np.cov(data, rowvar=False)
    evals, evecs = np.linalg.eigh(cov)

    # sort evals and evecs
    idx_sort = np.argsort(evals)[::-1]
    evals, evecs = evals[idx_sort], evecs[:, idx_sort]

    # project the data to ev
    proj = data @ evecs
    return proj, evecs
