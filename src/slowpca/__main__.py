# -*- coding: utf-8 -*-
"""CI to perform PCA based on covariance/corrleation."""
import click
import numpy as np

from slowpca import perform_pca


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
