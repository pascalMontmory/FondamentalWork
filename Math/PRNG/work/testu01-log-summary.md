# TestU01 Log Summary

This note records the currently imported and reported TestU01 outcomes for `Montmory_CTACM`.

Status: BigCrush raw logs imported for CPU ARM, Apple Metal GPU, and CUDA GPU at seed 42. SmallCrush logs, x86 CPU logs, stream adapter source, and rerun commands remain pending.

## Imported and Reported Results

| Backend | SmallCrush | BigCrush | Status |
| --- | ---: | ---: | --- |
| CPU ARM, Darwin | pass reported | `160 / 160` | BigCrush raw log imported for seed 42. |
| Apple Metal GPU, Darwin | pass reported | `160 / 160` | BigCrush raw log imported for seed 42. |
| CUDA GPU, Linux | pass reported | `160 / 160` | BigCrush raw log imported for seed 42. |
| x86 CPU | pass reported | `160 / 160` reported | No raw x86 log imported. |

The imported logs are indexed in `../tests/testu01/MANIFEST.md`. The CPU artifact currently imported is CPU ARM on Darwin, not x86.

## Raw Log Import Checklist

When the raw logs are available, add for each backend:

- command used to generate the stream;
- generator version or commit hash;
- TestU01 version;
- compiler and backend details;
- complete SmallCrush output;
- complete BigCrush output;
- p-value anomaly summary;
- final pass/fail line;
- SHA-256 hash of the log file.

Raw logs should be stored under a dedicated reproducibility folder rather than embedded in the main article if they are long.
