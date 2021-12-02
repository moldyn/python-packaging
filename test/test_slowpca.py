# -*- coding: utf-8 -*-
import numpy as np
import pytest

import slowpca

@pytest.mark.parametrize('traj, kwargs, proj_ref', [
    (
        np.array([[0, 0], [1, 1]]),
        {},
        np.sqrt(2) / 2 * np.array([[-1, 0], [1, 0]]),
    ),
    (
        np.array([[0, 0], [1, 1]]),
        {'corr': False},
        np.sqrt(2) / 2 * np.array([[-1, 0], [1, 0]]),
    ),
    (
        np.array([[0, 0], [1, 1]]),
        {'corr': True},
        np.array([[-1, 0], [1, 0]]),
    ),
])
def test_perform_pca(traj, kwargs, proj_ref):
    """Test function for testing PCA."""
    proj, _ = slowpca.perform_pca(traj, **kwargs)
    np.testing.assert_array_almost_equal(proj, proj_ref)
