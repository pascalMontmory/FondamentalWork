# TestU01 Results

## Status

This file records the currently reported TestU01 outcomes for `Montmory_CTACM` across execution backends.

Raw TestU01 logs are not yet imported into this repository. Until they are added, the table below is a structured summary of reported local logs, not an independently reproducible proof artifact.

## Reported Summary

| Backend | SmallCrush | BigCrush | Result Status |
| --- | ---: | ---: | --- |
| x86 CPU | pass | `160 / 160` | Reported from local logs; raw log pending. |
| Apple Metal GPU | pass | `160 / 160` | Reported from local logs; raw log pending. |
| CUDA GPU | pass | `160 / 160` | Reported from local logs; raw log pending. |

The reported p-value distributions are described as clean and consistent across x86, Metal, and CUDA.

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

The results should remain labelled as reported until the raw logs and stream adapter are included. Once imported, the status can be upgraded to reproducible computational evidence if another user can rerun the same command and obtain the same log hash or accepted TestU01 summary.
