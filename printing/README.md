# Printing Pinchy

[Polska instrukcja](README_PL.md) · [STL parts](stl/) · [Editable STEP parts](step/) · [Assembly](../docs/ASSEMBLY.md)

Current mechanical revision: **B / D1**, previously designated C03B. Designed for **Waveshare ESP32-S3-Touch-LCD-2.1B / SKU 30697**, nominal Ø71.8 mm glass. The flat 28169 version is not interchangeable.

Open the 3MF files with **File → Open Project** in Bambu Studio. The saved profiles target **Bambu Lab P2S, 0.4 mm nozzle, Generic PLA, Textured PEI**, at **100% scale**. One raspberry filament is also used for supports; no AMS is needed. The display color is `#C74565`; use a physical spool matching the desired color.

| Plate | Contents | Layer | Slicer estimate |
|---|---|---:|---|
| [01 — screen fit and controls](plates/01_B_Proba_i_przyciski_P2S_PLA.3mf) | Profiled glass coupon, BOOT/RESET/slider and spares | 0.12 mm | 58 min / 4.41 g |
| [02 — enclosure](plates/02_B_Obudowa_P2S_PLA.3mf) | Front, central shell with four M2 supports and removable cover | 0.16 mm | 3 h 41 min / 50.10 g |
| [03 — D1 base and claws](plates/03_B_Nogi_i_szczypce_P2S_PLA.3mf) | Complete legs and both claws | 0.16 mm | 6 h 50 min / 85.93 g |
| [04 — D1 interface coupon](plates/04_D1_Proba_mocowania_P2S_PLA.3mf) | Both mating interface samples | 0.16 mm | 48 min / 7.92 g |

Total including coupons and spare controls: about **12 h 17 min / 148.36 g**. Estimates include slicer assumptions; allow extra material for tests. Saved temperatures are 220°C nozzle / 55°C bed, with a 10 mm³/s flow limit. Confirm printer, plate and filament in Bambu Studio and reslice after changing settings.

Print **04 and 01 first**. Test the D1 slide/click/release and the actual screen's glass support before committing to the full set. The screen must stop on the shaped front lip; it must not fall through. Current glass pocket Ø72.4 mm, visible opening Ø69.4 mm. Do not scale the entire model to fix an interface tolerance.

The nine main parts are `01_crab_front`, `02_crab_rear`, `03_crab_base`, `04_claw_L`, `05_claw_R`, `06_button_BOOT`, `07_button_RESET`, `08_power_slider`, and `09_rear_service_cover`. Original internal part identifiers are retained so STEP, STL and 3MF names agree. `00_*` files are coupons and `*_spare` are additional controls.

STL files are in print orientation and millimetres. STEP files are in millimetres; preserve the assembly coordinate system when editing the D1 receiver template. The web preview is a simplified viewing mesh and must not be used as the print source.

The current shell and base are a matching D1 pair. USB clearance comes from spacing complete leg pairs. The assumed USB plug body is no larger than 12 × 6 mm and 15 mm long; actual cable molding must be checked.

CAD and slicer checks exist, but physical fit, spring retention and repeated-use performance of this exact revision remain unverified. Audio/battery holders and the completed harness are outside the current printable set; see [build status](../docs/BUILD_STATUS.md).
