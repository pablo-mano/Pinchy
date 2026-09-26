# Pinchy — TODO

## Firmware — deferred / później

**No firmware source code or device binaries are published in this repository.** The current release contains mechanical files, build documentation, the web explorer and concept films. Firmware is a future task, not a prerequisite supplied by this release.

**W repozytorium nie publikujemy na razie żadnego kodu firmware ani binariów do wgrania.** Działające oprogramowanie urządzenia pozostaje TODO; filmy przedstawiają demonstrację koncepcji.

- [ ] Implement and bench-test a board-specific firmware port for Waveshare 30697 / 2.1B.
- [ ] Validate display, touch, side controls and shared I²S audio pins.
- [ ] Add the intended “Hey Pinchy!” interaction and voice services.
- [ ] Implement authenticated parcel, mail and calendar integrations.
- [ ] Publish firmware source and binaries only in a later, explicitly approved release.
- [ ] Add reproducible build, flashing, configuration and recovery instructions with that release.

[Requirements and pin constraints](docs/FIRMWARE.md).

## Hardware integration

- [ ] Validate current screen-fit and D1 coupons on the physical board and printer.
- [ ] Finalize and test audio/battery holders, microphone channel and speaker seal.
- [ ] Verify amplifier power, battery charging current, connector and polarity.
- [ ] Complete the harness and verify connector access, bends and clearance.
- [ ] Measure power consumption, battery runtime, acoustic quality and latch endurance.

[Current build status](docs/BUILD_STATUS.md) · [BOM](electronics/BOM.md) · [Wiring](electronics/WIRING.md).
