# Pinchy photo wiring explorer — 1 October 2026

The `../03_physical_connections.*` files show physical modules, pads and proposed connections. The English interactive page uses the same charcoal background, raspberry accents, navigation and sidebar layout as the 3D explorer. The two pages link to each other. The drawings, connection table and PDF / SVG downloads are also in English.

## Files and controls

- `page.html`: self-contained page template, styles and interaction code.
- `build.py`: generates the English HTML, SVG, CSV and `connections.json`; requires Python 3 and Pillow. If the repository has a `site/` directory, it also updates `site/wiring/index.html` and the downloadable SVG, with the correct relative link back to the model.
- `assets/`: source photographs and the manufacturer rendering, embedded in the SVG and HTML.
- PDF: one landscape A3 page. PNG: 4800 × 3420 pixels. These are exported from the generated SVG using Sharp and ReportLab, and must be refreshed after changing the drawing. Copy the PDF to `site/wiring/` too.

Choose a signal from the sidebar or click a wire to highlight that signal. **Show all** resets the selection. **Fit view** fits the full drawing inside the viewport; the percentage is relative to that fitted size. Zoom reaches 400%; scroll to explore the enlarged sheet. The table and source references remain available below the workspace.

The root SVG alone scales with its container. Nested image viewports keep their documented dimensions so that the photographed pads remain aligned with the wire endpoints.

## Hardware variant

- Waveshare ESP32-S3-Touch-LCD-2.1B / 30697: a rear PCB reference photo from the 2.1 product page and the shared published schematic. Check the actual board revision before soldering.
- Adafruit SPH0645 #3421 microphone, sound-port side.
- DFRobot DFR0954 MAX98357A: assumed from the shopping list, not separately confirmed by the owner. The pad layout is for DFR0954, not Adafruit #3006.
- Kamami 560816 speaker, 8 Ω / 1 W.
- Confirmed battery: Akyga AKY0107 / LP503759, 3.7 V / 1350 mAh, PCM, factory JST 2.54 mm connector.

The 3D explorer still contains earlier Adafruit reference geometry. Linking the two pages does not validate the new components' mechanical fit.

## Validation limits

This remains a bench-test proposal. J9 pin numbers come from the manufacturer schematic; the J9 and J1 expansions are not connector-face views. The physical VCC solder point has not been identified. Charging must be adapted and VCC, current and I²S behavior measured before validating the prototype. Dashed power connections mark these conditions. The gray leader to the factory battery plug is an annotation, not an electrical wire.

The 100 kΩ resistor connects DOUT to GND, not in series with DOUT and not to the crossing BCLK line. Only dots mark electrical junctions.

Browser checks cover desktop and phone layouts, navigation in both directions, sidebar and wire selection, zoom, reset and table access. The 3D model/renderer and the SVG wire geometry are unchanged by this interface update. No electrical measurements have been performed.

## Sources

- [Waveshare documentation](https://docs.waveshare.com/ESP32-S3-Touch-LCD-2.1) and [schematic](https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1_schematic_diagram.pdf).
- [Adafruit #3421 pinout](https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/pinouts) and [Knowles SPH0645 datasheet, p. 7](https://cdn-shop.adafruit.com/product-files/3421/i2S%20Datasheet.PDF#page=7).
- [DFRobot DFR0954 module and pinout](https://wiki.dfrobot.com/dfr0954/).
- [Akyga AKY0107 datasheet](https://www.tme.eu/Document/d09d785c980e096e8a2305b0492fc05e/AKY0107.pdf).
- Battery and speaker photos: Kamami product pages 1202750 and 560816, linked in the HTML. Other photos / rendering: Waveshare, Adafruit and DFRobot. Rights remain with their owners.
