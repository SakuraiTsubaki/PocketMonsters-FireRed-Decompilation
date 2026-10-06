# DoSoftReset reconstruction

Target: BPRJ-rev0 (1e4af44b0c75cc8649bfb8649dc4ae5850bf5358bd6b9cd0bf779c99f9db1486)

The verified Japanese `AgbMain` map calls `DoSoftReset` at 0x080008D8. A fresh Thumb trace closes at 0x08000930, observes a return, and is published without instruction halfwords. The code-only range SHA-256 is `fde87a2ac74016573f3855b5ec416510fc6fe181e87cd8fe1749b11638cf4755`; no ROM bytes are stored.

The straight-line routine disables the interrupt master switch, stops sound VSync and the scanline effect, then disables DMA channels 1, 2, and 3 through their control-high registers. This FireRed/LeafGreen-family build has no RTC-protection call and passes `0xDF`, excluding the SIO-register reset bit.

Names were aligned with [pret/pokefirered](https://github.com/pret/pokefirered) at commit `037335f4c725d7c9aecdac87066f2002b4bd7e14`, then independently checked against this ROM's function boundary, direct-call targets, hardware addresses, and constants.

