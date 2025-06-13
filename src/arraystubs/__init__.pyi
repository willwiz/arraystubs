# ruff: noqa: PYI042
from __future__ import annotations  # noqa: PYI044

__all__ = [
    "T2",
    "T3",
    "AShape",
    "Arr",
    "Mat",
    "MatV",
    "Vec",
    "char",
    "dbl",
    "flt",
    "int_t",
]
from typing import Any

import numpy as np

type AShape = tuple[int, ...]
type dbl = np.dtype[np.float64]
type flt = np.dtype[np.floating]
type int_t = np.dtype[np.integer]
type char = np.dtype[np.str_]
type bool_t = np.dtype[np.bool_]
type A1[T: (np.floating, np.float32, np.float64, np.integer, np.str_, np.bool_)] = np.ndarray[
    tuple[int],
    np.dtype[T],
]
type A2[T: (np.floating, np.float32, np.float64, np.integer, np.str_, np.bool_)] = np.ndarray[
    tuple[int, int],
    np.dtype[T],
]
type A3[T: (np.floating, np.float32, np.float64, np.integer, np.str_, np.bool_)] = np.ndarray[
    tuple[int, int, int],
    np.dtype[T],
]
type Vec[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[tuple[int], T]
type Mat[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[tuple[int, int], T]
type MatV[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[tuple[int, int, int], T]
type Arr[T: np.dtype[Any]] = np.ndarray[tuple[int, ...], T]
type T2[T: (float, int)] = tuple[T, T]
type T3[T: (float, int)] = tuple[T, T, T]
