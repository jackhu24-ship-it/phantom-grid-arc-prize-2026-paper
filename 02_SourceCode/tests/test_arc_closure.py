# -*- coding: utf-8 -*-
import pytest
from arc_prize_causal_agent import SovereignCausalARGAgent

def test_causal_closure():
    agent = SovereignCausalARGAgent()
    res = agent.execute_reasoning_step({"id": "arc_eval_01"})
    assert res["status"] == "SOLVED"
    assert res["energy"] < 0.05
    residue = agent.close_and_purge()
    assert residue == 0.000000
