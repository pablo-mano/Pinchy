# Credits and third-party material

**Pinchy project/design:** Paweł Manowiecki · [X: @pawel_mano](https://x.com/pawel_mano).

No blanket open-source license for the original Pinchy design files has been selected in this preparation step. Third-party terms remain separate; this attribution notice does not relicense those materials.

## Web renderer

The self-contained explorer embeds **Three.js 0.180.0**, distributed under MIT. Its copyright/license notice is included in the HTML and in [THREE_MIT.txt](licenses/THREE_MIT.txt). Source: [Three.js](https://github.com/mrdoob/three.js).

## Photographic wiring diagram

The photo-based wiring sheet and its interactive page include reference images from **Waveshare** (ESP32-S3-Touch-LCD-2.1 rear PCB), **Adafruit** (SPH0645 #3421), **DFRobot** (DFR0954 module rendering) and **Kamami** (Akyga AKY0107 battery and speaker 560816 product photos). The source images are cropped or rotated for presentation; the diagram adds pin labels and proposed connections. Copyright and any applicable terms remain with their respective rights holders; no new license to those images is asserted. [Sources, assumptions and validation limits](electronics/physical_wiring/README.md).

## Hardware reference geometry

- **Waveshare ESP32-S3-Touch-LCD-2.1B:** reference geometry derived from the official manufacturer drawing archive. The embedded simplified viewing model represents the purchased board/display, not a printable replacement. [Manufacturer resources](https://docs.waveshare.com/ESP32-S3-Touch-LCD-2.1/Resources-And-Documents) · [B drawing archive](https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1B-Drawing.zip). No new license for Waveshare material is asserted here.
- **Adafruit CAD Parts:** battery #258, speaker #3923 and amplifier #3006 from [Adafruit_CAD_Parts](https://github.com/adafruit/Adafruit_CAD_Parts), commit `6f52ee4d48df0e7118d2d82f485cb572051a24fe`. MIT, copyright Adafruit Industries; [license copy](licenses/ADAFRUIT_CAD_MIT.txt). Web geometry is simplified for display.
- **SPH0645 microphone #3421:** locally reconstructed from [Adafruit I²S Microphone Breakout PCB](https://github.com/adafruit/Adafruit-I2S-Microphone-Breakout-PCB), commit `bb0dfa60919c5679f676e0af41958bece6294b05`, and the [Knowles datasheet](https://cdn-shop.adafruit.com/product-files/3421/i2S%20Datasheet.PDF). This is a reconstruction, not an official full-module STEP. That derived microphone reference remains under **CC BY-SA 3.0**, with attribution to Adafruit Industries; [license copy](licenses/ADAFRUIT_MIC_CC_BY_SA_3.txt). PCB thickness, solder and small component geometry are approximations.

## Film music and voices

Music in the finished films: **Jamie Bathgate — Status**, using the MP3 supplied for this project. Its embedded tags identify the album *Aground* and Art-list. Music rights remain with the relevant rights holders; this repository does not grant a license to extract or reuse the track. The standalone source MP3 is not included. Public release of the finished films should use the project owner's applicable music license.

Voices were synthesized with **OpenAI gpt-4o-mini-tts**, using `marin` and `cedar`. The “Hey Pinchy!” line was generated separately in Polish and English. The films disclose their use of OpenAI TTS and simulated interaction data.

Product names and trademarks identify compatible/reference hardware and do not imply endorsement.
