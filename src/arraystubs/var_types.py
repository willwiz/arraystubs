__all__ = ["Arr", "dbl", "flt", "int_t", "char", "Vec", "Mat", "MatV", "T2", "T3"]
import numpy as np

_Shape = tuple[int, ...]
Arr = np.ndarray
dbl = np.dtype[np.float64]
flt = np.dtype[np.floating]
int_t = np.dtype[np.integer]
char = np.dtype[np.str_]
bool_t = np.dtype[np.bool_]
type Vec[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[_Shape, T]
type Mat[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[_Shape, T]
type MatV[T: (flt, int_t, dbl, char, bool_t)] = np.ndarray[_Shape, T]
type T2[T: (float, int)] = tuple[T, T]
type T3[T: (float, int)] = tuple[T, T, T]
