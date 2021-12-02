URLS=[
"slowpca/index.html",
"slowpca/slowpca.html"
];
INDEX=[
{
"ref":"slowpca",
"url":0,
"doc":" slowpca Slowpca is a package to perform principal component analysis based on correlation or covariance. This Repository is a only an example of python packaging. The method was published in: > Authors,  .,  Title of publication goes here , in preparation We kindly ask you to cite these articles if you use this software package for published works.  Features - performs PCA - easy to install -  .  Installation So far the package is only published to [PyPI](https: pypi.org). For installing it to within a python environment simple call:   python3 -m pip install slowpca   or for the latest dev version    via ssh key python3 -m pip install git+ssh: git@github.com/moldyn/python-packaging.git  , or via password-based login python3 -m pip install git+https: github.com/moldyn/python-packaging.git    Usage  CI - Usage Directly from the Command Line In general one can call the module directly by its entry point  $ slowpca or by calling the module  $ python -m slowpca . The latter method is preferred to ensure using the desired python environment. For help simply call  $ python -m slowpca  help .  Module - Inside a Python Script   from slowpca import estimate_pca  Load file  X is np.ndarray of shape (n_samples, n_features) proj, evecs = estimate_pca(X)  .  "
},
{
"ref":"slowpca.slowpca",
"url":1,
"doc":"Performing PCA based on covariance/corrleation."
},
{
"ref":"slowpca.slowpca.perform_pca",
"url":1,
"doc":"Perform PCA. This method performs PCA based on covariance or correlation. Parameters      data : ndarray Coordinate trajectory file of shape (n_frames, n_coords). corr : bool, default=False If  True correlation is used instead of covariance. Returns    - proj, evecs : ndarray Projection and eigenvectors.",
"func":1
}
]