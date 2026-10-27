# Native frame-wait evaluation

SCUS-94423's PsyQ `v_wait` at `0x8002E698` polls the frame counter at
`0x800A9BB0`. Each unsuccessful iteration decrements one timeout word at
`sp+16`; the original timeout path calls `0x800A37B8`, `0x8002F1F0` and
`0x8002F270`. The complete 152-byte routine has no MMIO or other hidden work.
Its interrupt-check anchors are `0x8002E6C0` and `0x8002E708`.

`-DAPE_NATIVE_IDLE_WAIT=ON` declares those audited anchors to the framework.
`-DPSX_EXECUTION_PROFILE=ENHANCED` selects native induction;
`-DPSX_EXECUTION_PROFILE=REFERENCE` retains original polling. Both are separate
builds with distinct execution identities. The title option remains off until
the evaluation is accepted; it adds no player setting.

The shared engine verifies the loop's dynamic shape, accounts for whole
iterations, updates the timeout and stops before the next device event or
timeout. The original final iteration delivers the event or timeout callbacks.
This removes host polling overhead without changing the guest clock. Existing
netplay, precise-mode and selfcheck exclusions remain active.

After normal source regeneration, `ape_vwait_contract_test` extracts the actual
retail-derived caller into temporary private input. It compares original and
native execution with the real pipeline/cache timing at guest-cycle scales
one and two, including event boundaries, timeout, satisfied and signed-counter
cases. Retail-derived function text is not stored in this repository.

Built-game qualification uses production builds with diagnostic tools and
image-readback rings disabled, the same first-level machine fixture, 4K OpenGL,
PGXP enabled and interpolation disabled. Raw measurements, binary identities,
fixture provenance, lifecycle checks and limitations are tracked in central
Bead `beads-wuhs`, related to optimization campaign `beads-2wy8.1`.
First-level checks do not establish full-game or online qualification.
