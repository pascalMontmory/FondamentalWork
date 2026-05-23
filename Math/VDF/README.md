# VDF

This directory is the starting point for the VDF mathematical framework.

The purpose is to isolate the mathematics that appears underneath several
repositories, instead of burying it inside implementation-specific or
cosmology-specific notes.

## Status

`VDF` is currently a named mathematical workstream. Its exact formal definition
still has to be written here before downstream claims rely on it.

Use this directory to make the VDF explicit:

```text
What are the primitive objects?
What are the maps, flows or deformations?
What is invariant?
What is measured?
What is only notation?
What is proved?
What is conjectural?
Which repos use it?
```

## Proposed documents

| File | Purpose |
|---|---|
| `definitions.md` | Canonical VDF definitions and primitive objects |
| `notation.md` | Symbols, units, conventions and naming |
| `lemmas.md` | Proven algebraic or geometric statements |
| `examples.md` | Minimal examples independent of applications |
| `links-to-repos.md` | Where VDF enters COSMO, TimeChain, Attesta, trading or other repositories |
| `open-questions.md` | Unresolved mathematical questions |

## Relationship to COSMO

`COSMO/` may use VDF tools, but VDF should not be defined by cosmology alone.
The direction should be:

```text
Math/VDF definitions
-> reusable lemmas and invariants
-> applications in COSMO and other repositories
```

This keeps the mathematics portable and prevents every project from redefining
its own version of the same underlying structure.

## First task

Create `definitions.md` with a compact answer to:

```text
VDF = ?
```

Then list the first three places where this definition is already implicitly
used in existing work.
