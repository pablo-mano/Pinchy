# Pinchy — diagram połączeń i plan wiązki

**Wariant do zbudowania i sprawdzenia na stole, nie potwierdzony montaż elektryczny.** Dotyczy Waveshare ESP32-S3-Touch-LCD-2.1B / 30697, mikrofonu Adafruit SPH0645 #3421, wzmacniacza MAX98357A #3006, głośnika 8 Ω / 1 W #3923 i chronionego LiPo 1S. Rysunki są schematami połączeń, nie widokiem pinów wtyczki; stronę pin 1 należy ustalić na fizycznej płytce.

![Diagram połączeń](01_connection_diagram.png)

Wersja wektorowa: [SVG](01_connection_diagram.svg). Tabela maszynowa: [connections.csv](connections.csv).

## Przypisanie sygnałów

Numery J9 pochodzą z opublikowanego schematu Waveshare. Funkcje GPIO potwierdza bieżąca dokumentacja wariantów 2.1 i 2.1B. J9 ma opis SH1.0 12P; nie utożsamiaj go ze złączem akumulatora o rastrze 1,25 mm.

| Z płytki / elementu | Do | Funkcja |
|---|---|---|
| J9.6 — 3V3 | Mikrofon 3V | Zasilanie mikrofonu |
| J9.1 lub J9.5 — GND | Mikrofon GND i wzmacniacz GND | Wspólna masa; przewód powrotny wzmacniacza poprowadzić z jego zasilaniem |
| J9.3 — D− / GPIO19 | Mikrofon BCLK oraz wzmacniacz BCLK | Wspólny zegar bitowy |
| J9.4 — D+ / GPIO20 | Mikrofon LRCLK/WS oraz wzmacniacz LRC | Wspólny zegar próbek |
| Mikrofon DOUT | J9.10 — RXD / GPIO44 | Audio z mikrofonu do ESP32 |
| J9.9 — TXD / GPIO43 | Wzmacniacz DIN | Audio z ESP32 do wzmacniacza |
| Mikrofon SEL | Mikrofon GND | Kanał lewy |
| Mikrofon DOUT | 100 kΩ → GND | Pull-down zalecany przez Knowles przy jednym mikrofonie; uwzględnić w wiązce. Źródłowe PCB #3421 nie zawiera tego rezystora na DOUT. |
| VCC na Waveshare, sieć U5.VIN / strona VCC C14 | MAX98357 VIN | **Warunkowo:** po identyfikacji fizycznego punktu, pomiarze napięcia i kontroli obciążalności |
| MAX98357 OUT+ i OUT− | Dwa przewody głośnika | Wyjście mostkowe BTL; żaden zacisk głośnika nie jest GND |
| Chroniony LiPo BAT+ | J1.1 BAT | **Dopiero po dostosowaniu ładowania i potwierdzeniu polaryzacji** |
| Chroniony LiPo BAT− | J1.2 GND | Złącze głównego pakietu, nie podtrzymania RTC |

GAIN wzmacniacza pozostaje niepodłączony (domyślnie 9 dB); SD/MODE pozostaje w konfiguracji modułu. Dla mowy wysyłać ten sam sygnał do obu kanałów ramki I²S. Poziom wyjściowy należy ograniczyć do możliwości głośnika 1 W i rozpocząć test od małej głośności. Układ nie potrzebuje MCLK.

**J9.11 nie jest użyty.** Strona dokumentacji opisuje go jako NC, starszy opublikowany schemat jako GND. Tę rozbieżność odnotowano; nie oparto na nim żadnego połączenia.

## Tryb audio a porty USB

GPIO19/20 współdzielą funkcję native USB. GPIO43/44 współdzielą UART i przełącznik FSUSB42. Dokumentacja producenta mówi, że podłączenie USB TO UART odcina zewnętrzny UART.

- W trybie audio USB TO UART musi być odłączony; firmware zwalnia UART i USB z tych GPIO.
- Gniazdo native USB może być rozpatrywane do samego zasilania z kablem bez linii D+/D− albo odpowiednim separatorem danych. Nie łączyć aktywnego hosta USB z liniami używanymi jako BCLK/WS.
- Do programowania zatrzymać audio i przejść w tryb serwisowy. Po zaprogramowaniu odłączyć USB TO UART i uruchomić tryb głosowy. W docelowym urządzeniu aktualizacje OTA ograniczą potrzebę przepinania.
- I²C GPIO7/15 pozostaje dla urządzeń na płytce i nie jest wykorzystane do I²S. GPIO0 nie jest potrzebne.

Przed zrobieniem całej wiązki należy potwierdzić ciągłość GPIO19/20 i przebieg połączeń GPIO43/44 przez multiplekser na posiadanej rewizji. Propozycja wykorzystuje wyprowadzenia wymienione przez Waveshare; nie wykonano jeszcze testu I²S na tym egzemplarzu.

Wstępne ustawienia do testu: Philips I²S, 48 kHz, 2 sloty po 32 bity, BCLK 3,072 MHz. Mikrofon SPH0645 wymaga BCLK/WS = 64; jego 18-bitowe dane należy poprawnie wydobyć z 24-bitowego słowa. Standardowy sterownik ESP32-S3 obsługuje RX/TX współdzielące BCLK i WS. Działanie rozpoznawania mowy, format TTS i resampling to osobny etap firmware.

## Zasilanie i bateria

VIN wzmacniacza wymaga 2,7–5,5 V. Sieć VCC na schemacie jest wejściem stabilizatora U5 i kondensatorów C14/C17, zasilanym przez układ wyboru USB/bateria. **Nie zaznaczono niezweryfikowanego punktu lutowania na zdjęciu PCB.** Najpierw trzeba odnaleźć odpowiednią stronę C14 lub wejście U5, zmierzyć napięcie przy USB, baterii i obu pozycjach wyłącznika oraz sprawdzić obciążenie. Zasilanie wzmacniacza z wyjścia 3V3 nie zostało przyjęte; LDO obsługuje także ESP32 i ekran.

Adafruit #258 dopuszcza ładowanie najwyżej 500 mA. Schemat Waveshare pokazuje ETA6098 i R7=82 kΩ, odpowiadające około 2 A według tabeli producenta układu. To wniosek ze schematu, nie pomiar płytki. **Nie podłączać #258 do ładowania bez obniżenia i sprawdzenia prądu.** Rezystor zamienny i ewentualne odsprzęganie wzmacniacza dobieramy po weryfikacji rzeczywistej rewizji. Nie dodawać drugiej ładowarki równolegle.

JST-PH pakietu #258 nie pasuje automatycznie do gniazda głównego akumulatora Waveshare opisanego jako MX1.25 2PIN. Wymagana pasująca wiązka i kontrola BAT+/GND miernikiem; kolory przewodów nie są dowodem polaryzacji. Złącze RTC nie służy do zasilania urządzenia.

## Plan ułożenia przewodów

![Plan tras](02_cable_routing_plan.png)

[SVG tras](02_cable_routing_plan.svg), [współrzędne planu](cable_routes.json) oraz [podgląd 3D GLB](Pinchy_cable_plan.glb). W projekcie Blender trasy są osobną, domyślnie ukrytą kolekcją referencyjną. Linie wskazują miejsca do zajęcia przez wiązkę; nie są odwzorowaniem poszczególnych przewodów, kompletnych wtyczek ani gotowych kanałów do druku.

- **A — mikrofon:** od J9 górną lewą stroną w układzie CAD, następnie przy boku do padów mikrofonu. Oddzielić od przewodów głośnika i zasilania wzmacniacza.
- **B — dane wzmacniacza:** wzdłuż górnej krawędzi baterii, później nad pakietem po stronie wzmacniacza. W wąskiej szczelinie między boczną krawędzią baterii a PCB wzmacniacza nie ma miejsca na całą grubą wiązkę, dlatego proponowana trasa biegnie wyżej w osi Z.
- **C — głośnik:** skręcona para OUT+/OUT−, możliwie krótka, prowadzona wokół dolnej krawędzi głośnika. Nie prowadzić tuż przy porcie mikrofonu ani równolegle do jego wiązki na całej długości.
- **D — bateria:** od dolnego wyjścia pakietu, bokiem do J1. Nie przeprowadzać pod łbami M2 ani przez płaszczyznę łączenia pokrywy. Dodać odciążenie przy pakiecie i konektorze.
- **VCC/GND do wzmacniacza:** osobna para z lokalnym odsprzęganiem według potrzeb testu. Trasa pozostaje nieustalona, dopóki nie zostanie potwierdzone miejsce pobrania VCC.

Wstępny dobór przewodów: sygnały elastyczna linka 30 AWG z izolacją do Ø0,7 mm; zasilanie i głośnik 26–28 AWG po sprawdzeniu prądu, spadku napięcia i średnicy izolacji. Przy pierwszej przymiarce zostawić około 20 mm zapasu, a potem skrócić. W JSON długości są obliczone po łamanych i służą tylko do planowania. Przyjęty promień gięcia do kolejnego etapu: co najmniej 3 mm, do potwierdzenia dla użytego przewodu.

Do wykonania przed projektowaniem kanałów: dopasowanie rzeczywistych wtyczek J9/J1, sprawdzenie ich wsuwania w obecnym korpusie, fizyczne uchwyty audio i pakietu, promienie łuków, zakaz prowadzenia nad anteną, dostęp do śrub i portów oraz pełna kontrola kolizji wiązki. Cztery nowe mocowania dotyczą **płytki Waveshare**; nie są uchwytami baterii i audio.

## Źródła

- [Waveshare — mapowanie SKU, GPIO, złącza i multiplekser](https://docs.waveshare.com/ESP32-S3-Touch-LCD-2.1).
- [Waveshare — schemat płytki](https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1_schematic_diagram.pdf), lokalna kopia `research/waveshare_21/board_schematic.pdf`.
- [Adafruit — SPH0645 pinout](https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/pinouts) i [Knowles — datasheet](https://cdn-shop.adafruit.com/product-files/3421/i2S%20Datasheet.PDF).
- [Adafruit — MAX98357A pinout, zasilanie i wyjście BTL](https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/pinouts).
- [Espressif — I²S ESP32-S3](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/i2s.html).
- [Adafruit — #258 i prąd ładowania](https://www.adafruit.com/product/258); [ETA6098 — tabela ISET](https://www.eta-semi.com/wp-content/uploads/2022/03/ETA6098_V1.1.pdf).

Stan: 25.09.2026. Diagram, netlista i koncepcja tras; jeszcze bez pomiarów prototypu.
