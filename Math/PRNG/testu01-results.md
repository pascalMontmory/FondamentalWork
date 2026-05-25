# TestU01 Results

## Status

This file records the currently imported and reported TestU01 outcomes for `Montmory_CTACM` across execution backends.

Raw BigCrush logs for seed 42 are imported under `tests/testu01/raw/` and indexed in `tests/testu01/MANIFEST.md`. These logs are computational evidence artifacts, not mathematical proof artifacts.

## Imported BigCrush Logs

| Backend | Log | Seed | BigCrush | Result Status |
| --- | --- | ---: | ---: | --- |
| CPU ARM, Darwin | `tests/testu01/raw/montmory_ctacm_cpu_arm_bigcrush_seed42.log` | `42` | `160 / 160` | Raw log imported; reproducibility metadata incomplete. |
| Apple Metal GPU, Darwin | `tests/testu01/raw/montmory_ctacm_metal_bigcrush_seed42.log` | `42` | `160 / 160` | Raw log imported; reproducibility metadata incomplete. |
| CUDA GPU, Linux | `tests/testu01/raw/montmory_ctacm_cuda_bigcrush_seed42.log` | `42` | `160 / 160` | Raw log imported; reproducibility metadata incomplete. |

All three imported logs end with `All tests were passed`.

## Reported But Not Yet Imported

| Backend | SmallCrush | BigCrush | Result Status |
| --- | ---: | ---: | --- |
| x86 CPU | pass | `160 / 160` | Reported previously; no raw x86 log imported. |
| CPU ARM, Darwin | pass | imported | SmallCrush raw log pending. |
| Apple Metal GPU, Darwin | pass | imported | SmallCrush raw log pending. |
| CUDA GPU, Linux | pass | imported | SmallCrush raw log pending. |

## Required Raw-Log Metadata

Each imported log should include:

- generator name and version;
- backend target;
- compiler and flags;
- host hardware;
- TestU01 version;
- stream adapter code or hash;
- seed used for the TestU01 stream;
- complete SmallCrush output;
- complete BigCrush output;
- final pass/fail summary;
- SHA-256 hash of the raw log.

## Repository Policy

The imported BigCrush logs can be cited as repository computational evidence. They should not be promoted to fully reproducible evidence until the stream adapter, implementation hashes, build details, and rerun commands are included.
