# -*- coding: utf-8 -*-
"""Performing PCA based on covariance/corrleation."""

import click
import numpy as np


@click.command(no_args_is_help=True)
@click.option(
    '--cov/--corr',
    'use_cov',
    default=True,
    help='Use covariance or correlation for PCA.',
)
@click.argument(
    'filename',
    required=True,
    type=click.Path(exists=True),
)
def main(use_cov, filename):
    """Main function"""
    data = np.loadtxt(filename)
    mode = 'cov' if use_cov else 'corr'
    output = f'{filename}.{mode}'

    proj, evecs = perform_pca(data, corr=not use_cov)

    # store results
    np.savetxt(f'{output}.proj', proj)
    np.savetxt(f'{output}.ev', evecs)



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


if __name__ == '__main__':
    main()
