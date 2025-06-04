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
from typing import Any, TypeAlias

import numpy as np

AShape: TypeAlias = tuple[int, ...]
dbl: TypeAlias = np.dtype[np.float64]
flt: TypeAlias = np.dtype[np.floating]
int_t: TypeAlias = np.dtype[np.integer]
char: TypeAlias = np.dtype[np.str_]
bool_t: TypeAlias = np.dtype[np.bool_]
type Vec[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[AShape, T]
type Mat[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[AShape, T]
type MatV[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[AShape, T]
type Arr[T: np.dtype[Any]] = np.ndarray[tuple[int, ...], T]
type T2[T: (float, int)] = tuple[T, T]
type T3[T: (float, int)] = tuple[T, T, T]
