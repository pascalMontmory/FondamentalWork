# Research Map

This repository is organized by **status** and **domain**. The goal is to make clear what is verified, what is conditional, what is exploratory, and where a reader should start.

## 1. Top-Level Domains

```text
COSMO/  Physics, GUP, UV/IR, holography, cosmology, sensors.
Math/   Mathematical foundations reused across projects.
docs/   Repository-level reading guides, structure rules, and status policy.
```

## 2. Recommended Reading Order

### For the whole repository

1. `README.md`: high-level entry point.
2. `docs/RESEARCH_MAP.md`: this file, explaining the logic of the layout.
3. `docs/REPOSITORY_STRUCTURE.md`: naming and placement rules.
4. Domain README files, especially `COSMO/README.md` and `Math/README.md`.

### For COSMO

1. `COSMO/README.md`: domain overview and status policy.
2. `COSMO/READING_ORDER.md`: scientific pipeline and suggested reading order.
3. `COSMO/non-validated/README.md`: hypotheses, draft articles, and non-verified claims.
4. `COSMO/work/README.md`: reproducibility scripts, run notes, and data provenance.

### For Collatz-Montmory

1. `Math/Collatz-Montmory/README.md`: verified-facing overview.
2. `Math/Collatz-Montmory/non-validated/README.md`: hypotheses and analyzed but non-verified material.
3. `Math/Collatz-Montmory/work/scripts/`: scripts used to reproduce diagnostics.

## 3. Status Levels

| Status | Meaning | Where it belongs |
|---|---|---|
| Verified | Proof or exact algebraic identity is written. | Domain root, e.g. `Math/Collatz-Montmory/` |
| Conditional | Theorem-like statement with assumptions explicit. | Domain root if polished, otherwise `non-validated/` |
| Computationally bounded | Reproducible script, stated range, no asymptotic overclaim. | Domain root only if carefully bounded; otherwise `non-validated/` |
| Non-validated | Hypothesis, draft article, numerical clue, negative diagnostic, open program. | `non-validated/` |
| Script/work product | Executable diagnostic or generated helper. | `work/scripts/` or a domain-specific scripts folder |
| Old/superseded | Preserved for history, no longer active. | `old/` if created for that domain |

## 4. COSMO Structure

```text
COSMO/
  README.md                 Domain overview and status policy.
  READING_ORDER.md          Scientific pipeline and reading path.
  non-validated/            Hypotheses, draft papers, speculative or weakened claims.
  work/                     Scripts, data notes, run manifests, temporary work products.
  <track>/                  Thematic track folders preserved from the original corpus.
```

`COSMO/` contains the fundamental-physics and sensor material. Its role is separate from the reusable math foundations.

Expected internal logic:

1. theoretical framework;
2. numerical or observational tests;
3. applications such as quantum sensors;
4. reproducible scripts and generated outputs kept separate.

Current migrated non-validated COSMO tracks:

- `COSMO/non-validated/constante-structure-fine-uvir/`
- `COSMO/non-validated/consequences-alpha-uvir-electromagnetisme/`
- `COSMO/non-validated/programme-tests-experimentaux-uvir/`
- `COSMO/non-validated/conclusions-cosmologiques-gup-uvir/`

## 5. Collatz-Montmory Structure

```text
Math/Collatz-Montmory/
  README.md                 Verified-facing entry point.
  non-validated/            Hypotheses, analyzed drafts, negative diagnostics.
  work/scripts/             Reproducible exploratory scripts.
```

The visible Collatz root should stay conservative. A reader should not find unproven claims there unless they are explicitly conditional and labeled as such.

## 6. Math Structure

`Math/` contains mathematical tools shared with other repositories.

Current intended workstreams:

- `Math/Collatz-Montmory/`: Collatz, bounds, Lambda_B, filtered Hardy-Littlewood ideas.
- `Math/Cosmology-Scales/`: Planck/Hubble/cosmological scale identities extracted from COSMO with explicit assumptions and checks.
- `Math/VDF/`: verifiable-delay-function mathematics.
- `Math/PRNG/`: pseudo-random-number-generator mathematics.

Each workstream should eventually use the same status split:

```text
<topic>/README.md
<topic>/non-validated/
<topic>/work/scripts/
<topic>/old/      optional
```

## 7. Placement Rules

Use these rules when adding material:

- If it is a proof or exact identity, it may go in the topic root.
- If it is a conjecture or candidate publication, put it in `non-validated/`.
- If it is a script, put it in `work/scripts/`.
- If it is a result from a script, document it in `non-validated/` unless it is a bounded computational theorem.
- If a claim failed or weakened, keep it in `non-validated/` with the negative result stated clearly.
- Do not leave important claims only in chat history; add them to the appropriate file.

## 8. Current Collatz-Montmory Interpretation

The current Collatz-Montmory line has three separate notions:

1. **terminal bound**: enter `<=B`;
2. **passage center**: enter a window around `B`;
3. **arithmetic resonance**: passage law differs for an arithmetic population such as twin primes.

The current tests do not validate `89` as a canonical arithmetic resonance. That belongs in `non-validated/`, not in the verified-facing root.
