# Diagram fotograficzny Pinchy — 01.10.2026

Pliki `../03_physical_connections.*` pokazują rzeczywiste moduły, ich pady i proponowane połączenia. HTML działa lokalnie bez sieci, pozwala podświetlić jeden sygnał i powiększyć rysunek; zawiera również tabelę połączeń i źródła. PDF to jedna strona A3 poziomo. SVG zawiera osadzone fotografie i wektorowe przewody oraz opisy. PNG ma 4800 × 3420 pikseli.

## Wariant sprzętu

- Waveshare ESP32-S3-Touch-LCD-2.1B / 30697: fotografia referencyjna tylnej płytki wariantu 2.1, wspólny opublikowany schemat; przed lutowaniem sprawdzić rewizję.
- Mikrofon Adafruit SPH0645 #3421, widok od strony portu akustycznego.
- DFRobot DFR0954 MAX98357A: założenie na podstawie listy zakupowej, jeszcze niepotwierdzone osobno przez użytkownika. Układ padów odpowiada DFR0954, nie Adafruit #3006.
- Głośnik Kamami 560816, 8 Ω / 1 W.
- Akumulator potwierdzony przez użytkownika: Akyga AKY0107 / LP503759, 3,7 V / 1350 mAh, PCM, fabryczny JST 2,54 mm.

## Granice weryfikacji

Diagram jest propozycją do testu na stole. Połączenia J9 oparto na schemacie producenta; rozwinięcia J9 i J1 nie są widokami strony wtyku. Nie wyznaczono fizycznego punktu lutowania VCC. Dostosowanie ładowania oraz pomiary VCC, prądu i działania I²S pozostają konieczne przed zatwierdzeniem prototypu. Linie przerywane zasilania oznaczają ten warunek. Szary łącznik do fabrycznego wtyku baterii jest odnośnikiem opisowym, nie przewodem elektrycznym.

Rezystor 100 kΩ łączy DOUT z GND. Nie jest w szeregu z DOUT ani połączony z przecinającą rysunek linią BCLK. Połączenia elektryczne na skrzyżowaniach oznaczają wyłącznie kropki.

Sprawdzono wygląd eksportu PNG, format PDF A3 oraz działanie HTML w przeglądarce: podświetlenie BCLK, powiększenie 150%, powrót do dopasowania i wszystkich połączeń. Nie wykonano pomiarów sprzętu.

## Źródła

- [Waveshare: dokumentacja](https://docs.waveshare.com/ESP32-S3-Touch-LCD-2.1) i [schemat](https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1_schematic_diagram.pdf).
- [Adafruit #3421: piny](https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/pinouts) i [Knowles: karta SPH0645, s. 7](https://cdn-shop.adafruit.com/product-files/3421/i2S%20Datasheet.PDF#page=7).
- [DFRobot DFR0954: moduł i piny](https://wiki.dfrobot.com/dfr0954/).
- [Akyga AKY0107: karta parametrów](https://www.tme.eu/Document/d09d785c980e096e8a2305b0492fc05e/AKY0107.pdf).
- Fotografie baterii i głośnika: karty produktów Kamami 1202750 i 560816, podlinkowane w HTML. Pozostałe zdjęcia / render pochodzą od Waveshare, Adafruit i DFRobot. Prawa do materiałów pozostają przy właścicielach.

`build.py` generuje HTML, SVG, CSV oraz `connections.json`; wymaga Python 3 i Pillow. Pliki w `assets/` są lokalnymi źródłami ilustracji. Raster PNG wyeksportowano z SVG za pomocą Sharp, PDF utworzono z PNG za pomocą ReportLab. Po zmianie źródła należy odświeżyć także oba eksporty.
