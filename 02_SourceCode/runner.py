# -*- coding: utf-8 -*-
from pathlib import Path
from arc_prize_causal_agent import SovereignCausalARGAgent

def main():
    agent = SovereignCausalARGAgent()
    res = agent.execute_reasoning_step({"id": "task_demo"})
    residue = agent.close_and_purge()
    print(f"Task Solved: {res['status']} | Residual Memory: {residue:.6f} MB")

if __name__ == "__main__":
    main()
