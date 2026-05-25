# TestU01 Log Manifest

This folder stores raw TestU01 logs for `Montmory_CTACM`.

Status: computational evidence artifact. These logs contain complete BigCrush summaries for seed 42 on three execution backends. They do not yet make the result independently reproducible because the stream adapter source, backend implementation hashes, build commands, and complete rerun instructions are not included here.

## Raw Logs

| File | Backend | Suite | Seed | TestU01 | Statistics | Result | SHA-256 |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| `raw/montmory_ctacm_cpu_arm_bigcrush_seed42.log` | CPU ARM, Darwin | BigCrush | `42` | `1.2.3` | `160` | all passed | `85696c1d4908da2e225083065c0f44a5cc04438c05d193823f8aec62f7a3feb2` |
| `raw/montmory_ctacm_metal_bigcrush_seed42.log` | Apple Metal GPU, Darwin | BigCrush | `42` | `1.2.3` | `160` | all passed | `e19a9d95020b8a8bb9b84fe64128f87393cdae263332edb7df2507250b13088e` |
| `raw/montmory_ctacm_cuda_bigcrush_seed42.log` | CUDA GPU, Linux | BigCrush | `42` | `1.2.3` | `160` | all passed | `f88b13037aee7c97bd38bc55d1b650524d7afdbe7585ab96de7da5452aecf312` |

## Extracted Summary

| Backend | Generator label in log | Host label in log | Total CPU time | `p-value of test` lines | Minimum parsed p-value | Maximum parsed p-value |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| CPU ARM | `PRNG_MONTMORY_CPU_ARM_CTAM` | `Mac-mini-de-Eninca.local, Darwin` | `02:08:48.69` | `254` | `0.02` | `0.9985` |
| Apple Metal GPU | `PRNG_MONTMORY_GPU_METAL_CTAM` | `Macmini.numericable.fr, Darwin` | `02:16:17.77` | `254` | `2.6e-3` | `0.9994` |
| CUDA GPU | `PRNG_MONTMORY_GPU_CUDA_CTAM` | `a10-45-gra9, Linux` | `02:37:03.42` | `254` | `2.6e-3` | `0.9994` |

The `p-value of test` count is larger than the BigCrush statistic count because some BigCrush tests report multiple p-values.

## Completeness Assessment

These artifacts are sufficient to support the narrow statement:

> Imported raw BigCrush logs report `160 / 160` passed statistics for `Montmory_CTACM` at seed 42 on CPU ARM, Apple Metal GPU, and CUDA GPU.

They are not yet sufficient to support the broader statement:

> The repository contains a complete reproducible TestU01 validation package for x86 CPU, Apple Metal GPU, and CUDA GPU.

Missing items:

- raw SmallCrush logs for each backend;
- raw x86 CPU BigCrush log, if x86 is a required backend distinct from CPU ARM;
- exact commands for CPU ARM and Apple Metal runs;
- stream adapter source or source hash used to feed TestU01;
- generator/backend implementation commit hashes;
- compiler versions, build flags, and hardware details;
- expected stream hashes for at least one fixed seed and horizon;
- rerun script that validates the raw-log SHA-256 values or accepted TestU01 summaries.
