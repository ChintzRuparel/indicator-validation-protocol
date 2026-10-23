import numpy as np, pandas as pd
from ivp import protocol as P, indicators as I, dgp
def test_forward_sum():
    R=np.arange(20,dtype=float).reshape(10,2); y=P.forward_sum(R,3)
    assert y[0,0]==R[1,0]+R[2,0]+R[3,0] and np.isnan(y[-3:]).all()
def test_purge():
    for tr_end,s,e in P.folds(1000,252,126,5): assert tr_end+5<=s  # train labels end before test start
def test_pit_audit():
    c=pd.Series(np.exp(np.cumsum(np.random.default_rng(0).normal(0,.01,800))))
    assert I.pit_audit(I.rsi,c)==0 and I.pit_audit(I.leaky_centered_ma_gap,c)==1
def test_detects_planted():
    R,X=dgp.simulate(25,2520,0.02,seed=3); assert P.evaluate(R,X)["p_cw"]<0.01
def test_holm():
    assert np.allclose(P.holm([0.01,0.04,0.03]),[0.03,0.06,0.06])
