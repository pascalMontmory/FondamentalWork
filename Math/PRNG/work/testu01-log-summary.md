# TestU01 Log Summary

This note records the currently reported TestU01 outcomes for `Montmory_CTACM`.

Status: summary only. Raw log files are not yet imported into this repository.

## Reported Results

| Backend | SmallCrush | BigCrush | Status |
| --- | ---: | ---: | --- |
| x86 CPU | pass | `160 / 160` | Reported from local logs; raw log pending. |
| Apple Metal GPU | pass | `160 / 160` | Reported from local logs; raw log pending. |
| NVIDIA CUDA GPU | pass | `160 / 160` | Reported from local logs; raw log pending. |

The reported p-value distributions are described as clean and consistent across backends.

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
