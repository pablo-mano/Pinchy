# TODO — Pinchy firmware

**TODO: implement, validate and publish firmware in a future release. No firmware source code, flashable binaries or working integrations are included in this repository.** The product films use rendered faces and prerecorded OpenAI TTS; they are not recordings of running hardware.

Start from the [official Waveshare documentation and examples](https://docs.waveshare.com/ESP32-S3-Touch-LCD-2.1), confirming support for the actual **2.1B / SKU 30697** board. Display, touch, GPIO-expander, USB switching and battery behavior must be checked against the physical board revision.

The proposed audio mapping is BCLK GPIO19, WS GPIO20, microphone DOUT into GPIO44 and amplifier DIN from GPIO43. These overlap native USB and UART, including the board's multiplexer. See the [wiring requirements](../electronics/WIRING.md) before using these pins. A preliminary bench format is Philips I²S at 48 kHz with two 32-bit slots; correct SPH0645 data alignment and sample conversion still need testing.

A future reproducible software release needs:

- A pinned framework/toolchain version, exact board configuration and clean build command.
- A tested binary, flash offsets, programming/boot procedure and recovery instructions.
- Display/touch bring-up, GPIO mapping, shared I²S RX/TX, sample-format conversion and volume limits.
- Wi-Fi provisioning, credential storage, OTA updates and a service mode that releases shared audio/USB pins.
- “Hey Pinchy!” detection or an explicitly documented push-to-talk first version.
- Speech recognition, dialogue service, OpenAI TTS playback and face animation tied to actual playback.
- Mail, calendar and parcel connectors with authentication and a clear boundary between demonstration and real actions.
- Configuration examples containing placeholders only; no API keys, mailbox tokens or private calendars in Git.

Keep API credentials out of the public repository. No existing `key.txt`, runtime `.env`, or prior account configuration is included in this package.
