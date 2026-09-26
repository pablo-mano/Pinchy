# Pinchy — druk dla Waveshare 30697 / 2.1B

Ta paczka jest przygotowana dla **Bambu Lab P2S, dysza 0,4 mm, różowy Generic PLA**, stół Textured PEI. Otwieraj pliki jako projekty Bambu Studio i zachowaj skalę 100%. Podgląd koloru: `#C74565`.

W końcowej wersji panel przycisków ma zamknięte prześwity u góry i dołu. Ekran w złożeniu jest pionowy, pod kątem 90° do podłogi.

**Najpierw sprawdź próbnik.** Wersja B ma nominalnie szkło Ø71,8 mm. Nowe gniazdo ma Ø72,4 mm, a otwór zatrzymujący ekran Ø69,4 mm. Próbnik posiada profil rzeczywistego podparcia szkła 2.5D. Ekran ma oprzeć się na rancie, nie przejść przez cały otwór. Sprawdź z miękką podkładką, bez wciskania na siłę.

| Płyta | Zawartość | Szacowany czas / PLA |
|---|---|---|
| `01_B_Proba_i_przyciski_P2S_PLA.3mf` | Próbnik, przyciski i ich zapas | 58 min / 4,41 g |
| `02_B_Obudowa_P2S_PLA.3mf` | **Nowy przód, korpus z M2 i pokrywa** | 3 h 41 min / 50,10 g |
| `03_B_Nogi_i_szczypce_P2S_PLA.3mf` | Podstawa z nogami i dwa szczypce | 6 h 50 min / 85,93 g |
| `04_D1_Proba_mocowania_P2S_PLA.3mf` | Dwie połówki próbnika wymiennej podstawy | 48 min / 7,92 g |

Jeśli masz poprzedni C03B, **wymień korpus 02 i podstawę 03** na zgodną parę D1. Przód B, pokrywa B, szczypce i nakładki są bez zmian. Przechodząc z C01 wymień także przód i dodaj pokrywę `09_rear_service_cover`. Poprzedni front z otworem Ø73 mm był do innego wariantu Waveshare. Z płyty 1 można usunąć przyciski, jeżeli potrzebujesz tylko nowego próbnika.

Ustawienia: 220°C dysza / 55°C stół, jedna PLA także na podpory, warstwa 0,12 mm dla próbnika/przycisków i 0,16 mm dla reszty. AMS nie jest wymagany. Geometria ma skalę 1:1. Nie zmniejszaj całego modelu, aby dopasować szkło — zmieniłoby to otwory, gwinty i pozycje przycisków.

Po próbie załóż cienkie miękkie podparcie na przedni profil; przewidziano około 0,2 mm luzu osiowego. Tylny docisk ma nominalnie około 0,4 mm na miękkie paski. Sprawdź równomierne ułożenie szkła, swobodny powrót przycisków i działanie dotyku przed ostatecznym skręceniem. Trzy części pancerza łączą 4 wkręty do tworzywa Ø2,5 × 25 mm, łby do Ø4,8 mm. Nie dociskaj szkła sztywnym tworzywem ani nadmierną siłą.

Nowe cztery podpory przykręca się do fabrycznych nakrętek płytki śrubami **M2 × 5 mm**, łeb maks. Ø3,8 × 2 mm. Podpory mają 2,4 mm grubości, otwory Ø2,3 mm; nominalne zagłębienie w gwint to 2,6 mm. Sprawdź użyteczną głębokość gwintu na swoim egzemplarzu. To osobne śruby od wkrętów Ø2,5 × 25 łączących pancerz.

Montaż: przednia ramka na miękkiej powierzchni → cały moduł B i podkładki → przyciski oraz środkowy korpus → cztery śruby M2 od otwartego tyłu → ewentualne dodatki → pokrywa i cztery długie wkręty. Przed włożeniem dodatków zapewniono dostęp śrubokręta Ø4,4 mm. Śruby dokręcaj lekko; nie wyginaj PCB ani szkła.

Mniejsze otwory: USB-C 12,8 × 6,8 mm, dwa złącza rozszerzeń po 7,3 × 4,6 mm, microSD 14,4 × 3,6 mm. USB-C przewidziano dla plastikowej końcówki do 12 × 6 mm i długości do 15 mm, z luzem 0,4 mm na stronę. Sprawdź swój kabel przed drukiem. Nowe pełne nogi mają odstęp między parami: obie drogi USB są wolne, z minimalnym nominalnym odstępem 2,07 mm od przyjętej wtyczki. Długi ruch wtyczek rozszerzeń nadal może wymagać zdjęcia szczypca. microSD ma wąską szczelinę; serwis palcem po zdjęciu pokrywy.

W folderze `stl` znajdują się osobne części do druku i zapasowe przyciski. Kupowane elementy elektroniczne nie są częścią tych plików. Dodatkowy mikrofon, głośnik, wzmacniacz i bateria mieszczą się gabarytowo w osobnym złożeniu CAD. Przygotowano diagram połączeń i koncepcję tras w pełnej paczce projektu; docelowe mocowania dodatków, otwór mikrofonu, pełna wiązka i kanały do druku pozostają do opracowania.

Wykonano kontrolę CAD względem oficjalnego modułu B oraz kontrolę ścieżek w 3MF. **Fizyczna przymiarka tej wersji pozostaje do wykonania.** Raporty kontroli są w paczce; kompletna dokumentacja i edytowalne modele znajdują się w osobnej paczce projektu C03B.

## Wymienna podstawa D1

Najpierw drukuj płytę 04 i usuń podpory z obu rowków oraz spod sprężystego języczka. Sprawdź swobodne prowadzenie i łagodny klik. Podstawa wsuwa się od strony ekranu ku tyłowi. Żeby ją zdjąć, podeprzyj korpus, naciśnij tylną łopatkę od spodu w dół, od obudowy, i wysuń podstawę ku ekranowi. Niczego nie rozkręcasz. Stare części 02 i 03 nie mają D1.

[Pełna instrukcja i wymiary D1](../docs/D1_INTERFACE_PL.md). Luz profilu rowków wynosi 0,25 mm; siła kliku, trwałość sprężyny PLA i nośność wymagają fizycznej próby. Nie skaluj całego modelu dla dopasowania zatrzasku. Komplet czterech płyt: około 12 h 17 min / 148,36 g według slicera.
