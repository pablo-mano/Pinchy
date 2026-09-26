# Delivery validation

This is a digital-delivery check, not physical qualification of the device.

- All **4 3MF, 15 STL and 13 STEP** files match the current B/D1 output byte for byte. The 3MF ZIP containers pass integrity checks. Existing slicer checks cover bed fit, unchanged scale, P2S 0.4 mm / Generic PLA settings and extrusion at the control tips. No new physical print test was performed during packaging.
- Both final films passed full decoding, duration/frame checks, metadata/attribution checks and audio synchronization checks. Selected final PL/EN frames were visually reviewed. The four packaged videos match the checked exports.
- The offline explorer was opened in a browser and checked for 16 part groups, correct attribution, assembled and D1 presets, autorotation, front-bezel tooltip and microphone selection. The subsequent change only adds source/license notices in About.
- Markdown links are checked within this package; print archives, file sizes and common credential patterns are checked before the ZIP is produced. No API keys or source music MP3 are included.

See the machine-readable [delivery check](../validation.json) and [file hashes](../manifest.json). Live deployment status is recorded separately in [publication.json](../publication.json).

Physical screen fit, audio holders, electrical power/charging, full cable clearance and functioning firmware remain unfinished. See [build status](BUILD_STATUS.md).
