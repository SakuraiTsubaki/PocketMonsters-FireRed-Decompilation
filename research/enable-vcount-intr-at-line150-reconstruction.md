# EnableVCountIntrAtLine150 reconstruction

Target: BPRJ-rev0 (1e4af44b0c75cc8649bfb8649dc4ae5850bf5358bd6b9cd0bf779c99f9db1486)

The verified Japanese `AgbMain` map calls `EnableVCountIntrAtLine150` at 0x08000598. A fresh Thumb trace closes at 0x080005C0, observes a return, and is published without instruction halfwords. The exact code-range SHA-256 is `a59dd56ae94fedf4a5d5251c3e34289823fdfc517ad6c0ef630832a521dcf8e6`; no ROM bytes are stored.

The routine preserves the low byte of DISPSTAT, sets the VCount comparison field to scanline 150, enables the DISPSTAT VCount interrupt bit, and enables the VCount interrupt source. FireRed and LeafGreen share identical code; Emerald uses different helper addresses but the same verified behavior.

Names were aligned with [pret/pokefirered](https://github.com/pret/pokefirered) at commit `037335f4c725d7c9aecdac87066f2002b4bd7e14`, then checked against this ROM's boundary, direct-call targets, constants, and data flow.

