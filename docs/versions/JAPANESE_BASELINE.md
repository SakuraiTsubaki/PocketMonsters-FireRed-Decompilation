# Japanese Baseline — Pokémon FireRed

This document records the current evidence for the Japanese releases that serve as the historical baseline for the FireRed decompilation project.

## Baseline rule

The Japanese release is the comparison origin for regional research. Later regional builds remain separate branches whenever localization, code, data, assets, events, fixes, product identity, or distribution context differs.

No retail ROM image is required or committed. Identity and reconstruction work begins from public documentation, public reverse-engineering repositories, hardware evidence, hashes, and reproducible analysis.

## Confirmed identity

| Field | Rev 0 | Rev 1 |
| --- | --- | --- |
| Title | ポケットモンスター ファイアレッド | ポケットモンスター ファイアレッド |
| Platform | Game Boy Advance | Game Boy Advance |
| Market | Japan | Japan |
| Language | Japanese | Japanese |
| Product/build identifier | AGB-BPRJ-0 | AGB-BPRJ-1 |
| Retail product code | AGB-BPRJ-JPN | revision branch of AGB-BPRJ-JPN |
| SHA-1 | `04139887b6cd8f53269aca098295b006ddba6cfe` | `7c7107b87c3ccf6e3dbceb9cf80ceeffb25a1857` |
| Repository role | Primary historical baseline | Japanese revision branch |

For Rev 0, public physical-dump evidence also records:

- CRC32: `3B2056E9`
- MD5: `47596db5a16556c60027e7bf372ec917`
- SHA-256: `1e4af44b0c75cc8649bfb8649dc4ae5850bf5358bd6b9cd0bf779c99f9db1486`

## Official release context

The Pokémon Company official Japanese product page records FireRed and LeafGreen as Game Boy Advance titles released in Japan on **2004-01-29**. It also records Wireless Adapter and GBA link-cable support, and official linkage with Ruby/Sapphire/Emerald and Pokémon Colosseum.

Official sources:

- https://www.pokemon.co.jp/game/gba/fl/
- https://www.pokemon.co.jp/game/gba/fl/equipment.html

## Physical-cartridge and revision evidence

The Game Boy hardware database records separate Japanese FireRed variant identities:

- `AGB-BPRJ-0` — Pocket Monsters - FireRed (Japan)
- `AGB-BPRJ-1` — Pocket Monsters - FireRed (Japan) (Rev 1)

A public physical Rev 0 dump report records game code `BPRJ`, revision `0`, 16 MiB ROM size, and 1M FLASH save type.

Sources:

- https://gbhwdb.gekkio.fi/cartridges/AGB-BPRJ-0/
- https://gbhwdb.gekkio.fi/cartridges/AGB-BPRJ-0/fexcollects-1.html

## Rev 1 hash evidence

The Rev 1 SHA-1 currently recorded is:

- `7c7107b87c3ccf6e3dbceb9cf80ceeffb25a1857`

Public hash reference:

- https://github.com/40Cakes/pokebot-gen3/blob/main/modules/roms.py

The exact Japanese Rev 0 ↔ Rev 1 code/data delta has not yet been reproduced in this repository and remains a dedicated verification task.

## Public reconstruction coverage gap

`pret/pokefirered` explicitly describes itself as a decompilation of **English Pokémon FireRed and LeafGreen** and records English FireRed Rev 0 / Rev 1 matching targets.

It is therefore a major source/structure reference, but not a matching Japanese reconstruction. Japanese-specific scripts, text, assets, events, wireless behavior, e-Reader-related differences, region checks, and revision changes must be investigated explicitly.

Source:

- https://github.com/pret/pokefirered

## Evidence classification

| Finding | Level | Reason |
| --- | --- | --- |
| Japanese release date 2004-01-29 | Observed | Official Japanese Pokémon site |
| `AGB-BPRJ-0` / `AGB-BPRJ-1` existence | Observed | Public cartridge database |
| Rev 0 full hash set | Observed | Direct physical-dump report |
| Rev 1 SHA-1 | Observed / public hash inventory | Recorded by independent public ROM-identification tooling |
| Exact Rev 0 ↔ Rev 1 differences | Unverified in repository | Must be reconstructed from public evidence |
| Japanese matching decompilation | Not yet reproduced | Public `pret/pokefirered` target is English |

## Next tasks

1. Cross-check Rev 1 CRC32/MD5/SHA-256 and physical-cartridge evidence.
2. Reconstruct exact Japanese Rev 0 ↔ Rev 1 differences.
3. Inventory Japanese FireRed source, symbols, maps, scripts, text, graphics, audio, save, wireless, e-Reader, events, and GameCube-link research.
4. Compare against public English `pret/pokefirered` without assuming byte identity.
5. Track Sevii Islands, National Dex unlocking, Mystery Gift, Wireless Adapter, and Colosseum linkage as region/revision-sensitive subsystems.
