# -*- coding: utf-8 -*-
import numpy as np
import pytest

import slowpca


def test_perform_pca():
    """Test function for testing PCA."""

    traj = np.array([[0, 0 ], [1, 1]])
    proj_ref = np.sqrt(2) / 2 * np.array([[-1, 0], [1, 0]])

    proj, _ = slowpca.perform_pca(traj)

    np.testing.assert_array_almost_equal(proj, proj_ref)
