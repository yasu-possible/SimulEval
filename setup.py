# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import setuptools

setuptools.setup(
    python_requires='>3.7.0',
    name="simuleval",
    version="1.0.2",
    author="Xutai Ma",
    entry_points={
        'console_scripts': [
            'simuleval = simuleval.cli:main',
        ],
    },
    install_requires=[
        "pytest",
        "pytest-cov",
        "sacrebleu",
        "torch",
        "tornado",
        "soundfile",
        "requests",
        "pytest-flake8"
    ],
    package=setuptools.find_packages(
        exclude=[
                "examples",
                "examples.*",
                "docs",
                "docs.*",
            ]
    )
)
