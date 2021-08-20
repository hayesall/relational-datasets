# Copyright © 2021 Alexander L. Hayes

"""Tests for the `convert` module
"""

import pytest

numpy = pytest.importorskip("numpy")

from relational_datasets.convert import from_numpy


def test_convert_numpy_classification():
    X = numpy.array([[0, 1, 1], [1, 0, 2], [2, 2, 0]])
    y = numpy.array([0, 0, 1])
    data, modes = from_numpy(X, y)

    assert data.pos == [
        "v4(id3).",
    ]
    assert data.neg == [
        "v4(id1).",
        "v4(id2).",
    ]
    assert data.facts == [
        "v1(id1,0).",
        "v1(id2,1).",
        "v1(id3,2).",
        "v2(id1,1).",
        "v2(id2,0).",
        "v2(id3,2).",
        "v3(id1,1).",
        "v3(id2,2).",
        "v3(id3,0).",
    ]
    assert modes == [
        "v1(+id,#varv1).",
        "v2(+id,#varv2).",
        "v3(+id,#varv3).",
        "v4(+id).",
    ]

def test_convert_numpy_regression():
    X = numpy.array([[0, 1, 1], [1, 0, 2], [2, 2, 0]])
    y = numpy.array([0.1, 0.2, 0.3])
    data, modes = from_numpy(X, y)

    assert data.pos == [
        "regressionExample(v4(id1),0.1).",
        "regressionExample(v4(id2),0.2).",
        "regressionExample(v4(id3),0.3).",
    ]
    assert data.neg == []
    assert data.facts == [
        "v1(id1,0).",
        "v1(id2,1).",
        "v1(id3,2).",
        "v2(id1,1).",
        "v2(id2,0).",
        "v2(id3,2).",
        "v3(id1,1).",
        "v3(id2,2).",
        "v3(id3,0).",
    ]
    assert modes == [
        "v1(+id,#varv1).",
        "v2(+id,#varv2).",
        "v3(+id,#varv3).",
        "v4(+id).",
    ]
