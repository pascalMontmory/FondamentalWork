# COSMO Work Area

This directory is reserved for reproducibility work products and temporary analysis artifacts for the COSMO domain.

## Intended Contents

- scripts used to reproduce numerical checks;
- local run notes;
- data-preparation notes;
- generated-output manifests;
- benchmark protocols;
- temporary analysis files that are not intended as scientific claims.

## Not Intended Here

Do not place long-lived hypotheses, draft articles, or speculative theoretical claims here. Use:

```text
COSMO/non-validated/
```

## Suggested Layout

```text
COSMO/work/
  scripts/        Reproducible code.
  runs/           Local run manifests, no large generated files.
  data-notes/     Data provenance and download instructions.
  outputs/        Optional small text summaries; avoid binary/generated heavy files.
```

## Reproducibility Rule

A COSMO numerical claim should identify:

- script path;
- data source;
- command line or configuration;
- units;
- assumptions;
- uncertainty or sensitivity estimate;
- date of run.

Large CSV/PNG/PDF outputs should remain reproducible local artifacts unless explicitly approved for versioning.
