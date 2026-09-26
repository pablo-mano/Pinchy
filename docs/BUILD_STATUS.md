# What can be built today?

Pinchy is a documented mechanical prototype for **Waveshare ESP32-S3-Touch-LCD-2.1B / SKU 30697**, with an audio integration study. It is not yet a complete voice-assistant kit.

| Area | Included and checked | Still required |
|---|---|---|
| Enclosure | Current CAD/STL, 4 prepared P2S plates, correct B screen seat, four M2 mounts, controls, removable cover, complete legs and D1 base interface | Physical fit, tolerances, latch strength and repeated-use tests |
| Audio placement | Reference component dimensions, fit study and component views | Final holders, microphone opening/channel, speaker gasket/grille integration, battery retention and strain relief |
| Wiring | Proposed netlist, connection drawing and cable routing zones | Actual connector orientation, USB/UART multiplexing tests, confirmed amplifier VCC tap, final wire bends and complete harness clearance |
| Battery | Protected 1S reference and documented connector/charging mismatch | Verified charging-current setting, exact compatible battery harness and polarity; measured operation on the actual board |
| Firmware — TODO | Documentation only; no firmware source code or binaries | A Pinchy board port, reproducible build/flash instructions, tested audio/display integration and a firmware binary |
| Voice and integrations | English/Polish concept films using OpenAI TTS | Wake-word detection, speech recognition, response generation, secure credentials, InPost/mail/calendar integrations and permissions |
| Web explorer | Offline and [public Pages](https://pablo-mano.github.io/Pinchy/) view; rotation, 16 part groups, explosion slider and D1 visualization | Recheck after future site changes |

The films simulate parcel tracking, sending an email and editing a calendar. They do not prove those services are implemented on the device. “Hey Pinchy!” is the intended wake phrase and the spoken line in the film, not a supplied on-device detector.

## Recommended next milestones

1. Print and test the screen and D1 coupons, then validate the enclosure on the physical 30697 board.
2. Select and measure the final audio modules and battery; resolve charge current and the amplifier power point.
3. Bring up I²S RX/TX outside the enclosure, including USB/UART conflicts and safe low speaker volume.
4. Design the missing holders, acoustic seals and complete harness; update CAD and print plates together.
5. Implement a board-specific firmware build and bench test recording/playback/display controls.
6. Add voice services and integrations, with authentication and explicit action handling, then document flashing and setup.
7. Publish measurements: current draw, battery runtime, acoustic quality, thermal behavior and latch endurance.

The old EchoEar rover firmware/safety model is a different project and is intentionally not represented here as Pinchy firmware.
