# -*- coding: utf-8 -*-
"""Performing PCA based on covariance/corrleation."""

import click
import numpy as np


@click.command(no_args_is_help=True)
@click.option(
    '--cov/--corr',
    'use_corr',
    default=False,
    help='Use covariance or correlation for PCA.',
)
@click.argument(
    'filename',
    required=True,
    type=click.Path(exists=True),
)
def main(use_corr, filename):
    """Main function"""
    data = np.loadtxt(filename, ndmin=2)
    mode = 'corr' if use_corr else 'cov'

    # scaler data to make std-free
    if use_corr:
        data = data / np.std(data, axis=0, ddof=1)

    # calculate cov/corr matrix
    cov = np.cov(data, rowvar=False)
    evals, evecs = np.linalg.eigh(cov)

    # sort evals and evecs
    idx_sort = np.argsort(evals)[::-1]
    evals, evecs = evals[idx_sort], evecs[:, idx_sort]

    # project the data to ev
    proj = data @ evecs

    # store results
    np.savetxt(
        f'{filename}.{mode}.proj',
        proj,
    )
    np.savetxt(
        f'{filename}.{mode}.ev',
        evecs,
    )


if __name__ == '__main__':
    main()
