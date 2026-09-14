# Version Coverage

Use this document as the authoritative inventory of game versions targeted by this decompilation project.

## Baseline policy

This project uses the original Japanese release as the historical baseline and traces every confirmed regional, language, and revision branch from that point. Later regional builds remain separate targets whenever code, data, localization, assets, events, fixes, product identity, or distribution context differs.

The project assumes no locally owned retail ROM image. Version identities are established from public documentation, cartridge/hardware databases, public reverse-engineering repositories, hashes, and reproducible evidence.

## Japanese baseline

| Status | Region | Language | Revision / update | Platform / build | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Verified | Japan | Japanese | Rev 0 | GBA / AGB-BPRJ-0 / retail code AGB-BPRJ-JPN | CRC32 `3B2056E9`; MD5 `47596db5a16556c60027e7bf372ec917`; SHA-1 `04139887b6cd8f53269aca098295b006ddba6cfe`; SHA-256 `1e4af44b0c75cc8649bfb8649dc4ae5850bf5358bd6b9cd0bf779c99f9db1486` | Historical baseline. Official Japanese release date: 2004-01-29. |
| Verified | Japan | Japanese | Rev 1 | GBA / AGB-BPRJ-1 | SHA-1 `7c7107b87c3ccf6e3dbceb9cf80ceeffb25a1857` | Confirmed Japanese revision branch; exact delta remains to be reconstructed. |

See [`versions/JAPANESE_BASELINE.md`](versions/JAPANESE_BASELINE.md) for evidence and provenance.

## Confirmed regional/revision branches — first-pass inventory

| Status | Region / market | Language | Revision / update | Platform / build | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Verified | North America | English | Rev 0 | GBA / AGB-BPRE-0 | SHA-1 `41cb23d8dccc8ebd7c649cd8fbb58eeace6e2fdc` | Public `pret/pokefirered` matching target. |
| Verified | North America | English | Rev 1 | GBA / AGB-BPRE-1 | SHA-1 `dd5945db9b930750cb39d00c84da8571feebf417` | Public `pret/pokefirered` matching target. |
| Verified | Europe English distribution | English | Rev 1 | GBA / AGB-BPRP-1 | Hash mapping under verification | Current public cartridge inventory exposes the European-English product-code branch as Rev 1; do not invent a `BPRP-0` target. |
| Verified | Germany | German | Rev 0 | GBA / AGB-BPRD-0 | SHA-1 `18a3758ceeef2c77b315144be2c3910d6f1f69fe` | Public hash inventory. |
| Verified | France | French | Rev 0 | GBA / AGB-BPRF-0 | SHA-1 `fc663907256f06a3a09e2d6b967bc9af4919f111` | Public hash inventory. |
| Verified | Italy | Italian | Rev 0 | GBA / AGB-BPRI-0 | SHA-1 `66a9d415205321376b4318534c0dce5f69d28362` | Public hash inventory. |
| Verified | Spain | Spanish | Rev 0 | GBA / AGB-BPRS-0 | SHA-1 `ab8f6bfe0ccdaf41188cd015c8c74c314d02296a` | Public hash inventory. |

## Public reconstruction coverage

`pret/pokefirered` describes itself as a decompilation of **English Pokémon FireRed and LeafGreen** and records matching targets for FireRed Rev 0 and Rev 1. The repository is therefore a major structural/source reference, but it is not a Japanese or all-language matching reconstruction.

Japanese, German, French, Italian, Spanish, and region-specific European branches remain separate research targets in this repository.

## Status vocabulary

- **Planned** — intended for investigation but not yet verified.
- **Verified** — identity and hashes or stable build identifiers confirmed from recorded public evidence.
- **Mapped** — executable/data layout documented.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the target.
- **Reference only** — used for comparison but not a reconstruction target.

## Recording rules

1. Record exact revision/update information whenever known.
2. Prefer cryptographic hashes over filenames as identity evidence.
3. Do not commit retail game images or console keys.
4. Record regional or language differences instead of assuming two releases are identical.
5. Link version-specific findings to the relevant documentation or verification evidence.
6. Treat the Japanese release as the historical comparison baseline while preserving later fixes/additions/removals as branch history.
7. Do not invent missing European Rev 0 targets when only a Rev 1 product-code branch is confirmed.
8. Keep market/packaging identity separate from binary identity where necessary.
9. Use `TBD` or `unknown` rather than guessing unresolved mappings.
