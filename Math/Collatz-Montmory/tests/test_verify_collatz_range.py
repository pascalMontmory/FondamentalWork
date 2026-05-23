#!/usr/bin/env python3
"""Tests for the finite Collatz verifier."""

from pathlib import Path
import importlib.util

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify_collatz_range.py"
spec = importlib.util.spec_from_file_location("verify_collatz_range", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def test_known_steps() -> None:
    assert module.stopping_time(1, 0) == 0
    assert module.stopping_time(2, 10) == 1
    assert module.stopping_time(3, 20) == 7
    assert module.stopping_time(6, 20) == 8
    assert module.stopping_time(7, 20) == 16


def test_range_verification_small() -> None:
    result = module.verify_range(100, 1_000)
    assert result.verified is True
    assert result.first_failure is None
    assert result.max_stopping_time > 0
    assert 1 <= result.argmax_stopping_time <= 100


def test_rejects_nonpositive() -> None:
    try:
        module.collatz_step(0)
    except ValueError:
        pass
    else:
        raise AssertionError("collatz_step should reject nonpositive integers")
