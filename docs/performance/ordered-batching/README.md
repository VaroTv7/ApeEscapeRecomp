# Existing ordered OpenGL batching adoption

Fresh enhanced Ape Escape builds select the engine's existing `HLE` textured
batching tier. It keeps painter order while grouping compatible opaque and
semi-transparent primitives; the engine retains isolation for subtractive
blending and mask checks. No renderer implementation changes here.

Use the normal supported build/regeneration flow. Pass
`-DPSX_GL_BATCH_IMPL=LLE` for the original tier. Fresh
`-DPSX_EXECUTION_PROFILE=REFERENCE` configurations default to LLE; explicitly
pass both flags for a reference recipe. Use separate build directories for
profiles/tiers: existing cache selections are preserved, including explicit
LLE overrides.

The matched production HLE/LLE/LLE/HLE block at a real half-physical-core CPU
budget used identical PGXP9x/bilinear/16:9 projection settings, source-generated
inputs, BIOS, assets, private gameplay seed and empty overlay caches. Mean
process CPU per simulated frame fell **7.2543%**, from 8.00286 ms to 7.42231 ms;
process thread cycles per frame fell 5.7490%. Both adjacent pairs improved and
choice ranges did not overlap. Both choices maintained approximately 60 Hz with
zero timed audio bridge underruns/overflow. This is CPU headroom, not an
uncapped FPS claim. Original host gates passed; a previous throttled/high-load
block is retained as excluded supporting evidence.

[ape.json](ape.json) contains all four individual results, the original selected
CPU/host/frame/feature sample fields, seven-field NVML samples, audio counters,
source/binary/fixture identities, immutable raw-file hashes and the independent
CPU review identity. Complete original raw observations remain retained by the
campaign; the public sample subset does not replace or rewrite them.

Existing source-owned hidden real-GL checks passed 331 checks at scale 1 and 340
at scale 4, including exact supersampled HLE/LLE pixel equality for all tested
filter/mask combinations and draw-to-sample feedback. The separate LLE blend
oracle passed 22 checks against software/formulas. These are bounded renderer
contracts, not a whole-game visual check.

One matched QA pair's GPU scene ranges overlap with changing clocks/load:
**neutral/inconclusive**, with no GPU win claim. Both actual QA binaries created
and loaded their own slot 2 and resumed 24 frames in gameplay. This is bounded
current-build save/load API coverage; final combined regression, rewind,
rollback, common-profile checks and owner playcheck remain pending. No release
or merge is implied.
