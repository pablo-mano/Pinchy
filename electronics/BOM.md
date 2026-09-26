# Pinchy — bill of materials

[Download CSV](BOM.csv) · [Wiring](WIRING.md) · [Build status](../docs/BUILD_STATUS.md)

This is the current CAD-reference BOM. Audio, battery and harness items are prototype candidates; their status is explicit below. Prices and stock are not part of this snapshot. The enclosure uses **Waveshare 30697 / 2.1B**.

| Ref | Qty | Part | Status / fit |
|---|---:|---|---|
| WS1 | 1 | [Waveshare ESP32-S3-Touch-LCD-2.1B](https://www.waveshare.com/esp32-s3-touch-lcd-2.1.htm) | Required / supplied by builder. Current mechanical reference; glass Ø71.8 mm. Not the flat 28169 model. |
| MIC1 | 1 | [Adafruit SPH0645 I2S microphone](https://www.adafruit.com/product/3421) | Audio prototype. Matches reconstructed CAD; final holder and acoustic channel pending. |
| AMP1 | 1 | [Adafruit MAX98357A I2S amplifier](https://www.adafruit.com/product/3006) | Audio prototype. Matches CAD PCB; terminal block reserved separately; VCC tap unverified. |
| SPK1 | 1 | [Adafruit mini oval speaker 8 ohm 1 W](https://www.adafruit.com/product/3923) | Audio prototype. Matches CAD reference; final cradle and acoustic seal pending. |
| BAT1 | 0–1 | [Protected 1S LiPo, 1200 mAh reference](https://www.adafruit.com/product/258) | Conditional / not approved for direct connection. Reference pack permits <=500 mA charging; verify and adapt actual board charger and connector first. |
| RPD1 | 1 | [100 kΩ resistor](https://botland.com.pl/rezystory-przewlekane/20020-rezystor-justpi-tht-cf-weglowy-14w-100k-30szt-5904422329082.html) | Audio prototype. Microphone DOUT to GND pull-down; insulate the leads. |
| J9C | 1 | [JST-SH 1.0 mm 12-pin breakout lead](https://kamami.pl/przewody-jst/1184455-przewod-jst-sh-10-12-pin-10cm-a-a-5906623447800.html) | Verify supplied accessories. Check mating and pin-1 orientation; identify conductors by continuity. |
| J1C | 0–1 | Battery harness mating the actual MX1.25 2-pin socket | Unresolved. Not JST-PH; verify connector housing and BAT+/GND; do not use RTC socket. |
| SIG | as needed | Flexible stranded signal wire 30 AWG | Prototype harness. Planning diameter; route lengths and final slack in cable_routes.json. |
| PWR | as needed | Flexible stranded power/speaker wire 26–28 AWG | Prototype harness. Twist OUT+/OUT−; neither speaker terminal is ground. |
| USB1 | 1 | USB data cable for programming | Service. Plug body <=12×6 mm and <=15 mm long assumed by CAD. |
| USB2 | as needed | Verified audio-mode USB power lead | Unresolved. A generic charge-only cable may short data lines; test individually, including between them. |
| PSU1 | 1 | Regulated 5 V USB supply | Bench supply. Select after measuring board, display and audio current. |
| M2 | 4 | M2 × 5 mm machine screws | Required. Board mounting; check actual usable thread depth before tightening. |
| SC25 | 4 | Ø2.5 × 25 mm screws for plastic | Required. Enclosure; ordinary M2.5 machine screws are not an automatic substitute. |
| PAD | as needed | Soft glass support strips | Required / fit to sample. Nominal axial allowances ~0.2 mm front and ~0.4 mm rear; verify compression. |
| INS | as needed | Heat-shrink, insulating tape, solder and flux | Assembly. Do not obstruct microphone port, rails or latch. |
| PLA | ~150 g minimum | Raspberry Generic PLA | Required. Four prepared plates total 148.36 g estimated; allow extra for retries. |
| DEC | TBD | Amplifier decoupling components | Unresolved. No validated values or final board mounting solution supplied. |
| CHG | TBD | Charge-current adjustment components | Unresolved. Do not select a resistor from a guessed board revision. |
| MOUNT | TBD | Battery/audio holders, microphone gasket and speaker seal | Not yet designed. Existing printable parts mount Waveshare, not the additional audio parts. |

## Local purchasing alternatives

These are reference links from the earlier sourcing work, not claims of current availability or fit. Do not mix alternative dimensions into the current CAD without checking them.

- [Kamami SPH0645 #3421](https://kamami.pl/moduly-z-mikrofonami-i-detektory-dzwieku/564318-modul-z-mikrofonem-mems-sph0645lm4h-b-5906623429523.html): the same microphone board as the CAD reconstruction.
- [Botland DFRobot DFR0954 MAX98357A](https://botland.com.pl/odtwarzacze-mp3-wav-ogg-midi/21992-modul-wzmacniacza-audio-max98357-dfrobot-dfr0954-6959420922703.html): alternative to Adafruit #3006; different PCB, mounting and component heights.
- [Kamami 560816 speaker, 8 Ω / 1 W](https://kamami.pl/glosniki/560816-glosnik-z-przewodami-8-1w-5906623455089.html): 24 × 15 × 4.2 mm alternative, requiring a different cradle and seal.
- A battery is intentionally not marked as a drop-in purchase. Match actual charge current, dimensions, connector and polarity before selecting one.

The nine main printed parts are front bezel, central shell, D1 leg base, left/right claws, BOOT button, RESET button, power slider and rear cover. The 3MF plates include the fit coupons and spare controls. D1 uses a printed flexure; no separate metal latch or spring is required.
