"""Deterministic validators — the mechanical half of the hybrid align gates.

Each validator emits machine-checkable PASS/FAIL. The deterministic verdict is
the publish blocker (Decision A); the LLM layer in the matching prompt runs
second and may never relax a mechanical FAIL.
"""
