# -*- coding: utf-8 -*-
import os, sys, yaml
from pathlib import Path

base_dir = Path(__file__).resolve().parent

def test_all_10_drawers():
    drawers = [
        "01_Specs", "02_SourceCode", "03_CoverImage_16x9", "04_Slides_PDF",
        "05_DemoVideo_1440P", "06_Notebooks_and_Models", "07_SubmissionPackage",
        "08_AuditReceipts", "09_ChaosReports", "10_Releases"
    ]
    for d in drawers:
        p = base_dir / d
        assert p.exists() and p.is_dir(), f"Missing drawer: {d}"

def test_specs():
    spec = base_dir / "01_Specs" / "SPEC_ARC_PRIZE_2026_CAUSAL_JEPA.md"
    assert spec.exists()
    txt = spec.read_text(encoding='utf-8')
    assert "SPEC-ARC-PRIZE-01" in txt

if __name__ == "__main__":
    test_all_10_drawers()
    test_specs()
    print("ALL 10 DRAWERS & SPECS PASS [100% GREEN]!")
