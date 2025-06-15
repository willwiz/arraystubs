# ruff: noqa: PYI042

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

import numpy as np

type AShape = tuple[int, ...]
type SAny = tuple[int, ...]
type S1D = tuple[int]
type S2D = tuple[int, int]
type S3D = tuple[int, int, int]

type dbl = np.dtype[np.float64]
type flt = np.dtype[np.floating]
type int_t = np.dtype[np.integer]
type char = np.dtype[np.str_]
type bool_t = np.dtype[np.bool_]

type Arr[S: tuple[int, ...], T: np.generic] = np.ndarray[S, np.dtype[T]]
type Arr1[T: np.generic] = np.ndarray[
    tuple[int],
    np.dtype[T],
]
type Arr2[T: np.generic] = np.ndarray[
    tuple[int, int],
    np.dtype[T],
]
type Arr3[T: np.generic] = np.ndarray[
    tuple[int, int, int],
    np.dtype[T],
]
type Vec[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[tuple[int], T]
type Mat[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[tuple[int, int], T]
type MatV[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[tuple[int, int, int], T]

type T1[T: (float, int)] = tuple[T]
type T2[T: (float, int)] = tuple[T, T]
type T3[T: (float, int)] = tuple[T, T, T]
