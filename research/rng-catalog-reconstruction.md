# Pokémon FireRed RNG release-catalog reconstruction

The Japanese rev0 reconstruction remains the origin reference. Seven additional verified identities cover Japanese rev1, English rev0/rev1, German, French, Italian, and Spanish. Each ROM was SHA-256 gated and independently matched to the adjacent `Random`/`SeedRng` compiler layout and shared IWRAM state.

All eight identities implement the same ISO-style 32-bit LCG and use the existing `src/random.c`; their function and state addresses remain in per-release evidence. Naming and semantics follow `pret/pokefirered@037335f4c725d7c9aecdac87066f2002b4bd7e14`, `src/random.c`. CFGs omit ROM halfwords.
