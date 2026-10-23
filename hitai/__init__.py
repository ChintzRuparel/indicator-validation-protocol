import os
# Determinism + avoids an OpenMP thread hang observed in HistGradientBoosting on some VMs.
os.environ.setdefault("OMP_NUM_THREADS", "1")
