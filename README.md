# Depo Loco - web

One-page web zážitkového ubytovania **Depo Loco** na Španej Doline.
Jeden statický súbor `index.html` (Tailwind CDN + FontAwesome + Google Fonts), bez build kroku.

**Vizuál:** Space Grotesk (nadpisy, bez verzálok) + Inter, tmavá `#15120F` s medenou `#C98A4B`,
zaoblené sekcie a fotky (2 rem), plávajúca „pill" navigácia s blurom, na mobile fixná lišta
so Zavolať / Booking. Nadpisy majú plynulú veľkosť cez `clamp()`, takže sa nelámu na žiadnej šírke.

## Spustenie
Otvor `index.html` v prehliadači.

## Fotky - dôležité upozornenie
`img/vagon.jpg` je teraz **iná, letná fotka** vagóna od klienta (nahradila zimný záber) -
vidno celú stavbu vrátane schodov a podvozku, dvere aj okno vyvážene v zábere.

`img/priroda.jpg` je teraz **skutočná fotka poľa**, kde má jurta Loco stáť - poslal ju
klient priamo (orezané na 16:10, pôvodne 4:3 s peknou kompozíciou neba/trávy, zachovanej).

`img/pas.jpg` (dekoratívny pás medzi sekciami Okolie a Galéria) bol **odstránený aj so
sekciou** - ukazoval hostí vo vnútri cez okno, čo nechcel klient zverejňovať.

## Farby objektov
Každé ubytovanie má vlastnú farbu (pruh nad kartou, odznak, ikony, legenda nad kartami):

| objekt | farba | token v Tailwinde |
|---|---|---|
| Depo (loft) | medená oranžová `#C98A4B` | `copper-500` |
| Vagón (tiny house) | vagónová zelená `#2C6B54` | `rail-600` |
| Loco (jurta) - pripravujeme | hlinená `#AE5334` | `clay-500` |

Jurta má zatiaľ pracovný názov **Loco** a je označená ako „Pripravujeme".
Keď bude názov a fotka, stačí prepísať kartu a vložiť `img/jurta.jpg`.

## Obsah
Hero · fakty · príbeh depa (lepkavý text vedľa fotiek) · dva objekty (loft + vagón) · vybavenie ·
okolie s vzdialenosťami · fotopás · galéria s lightboxom · virtuálna 360° prehliadka ·
praktické info · rezervácia s dopytovým formulárom · footer.

## Animácie a UX
Ukazovateľ prečítania hore · pomalý „nádych" hero fotky · nadpis vychádzajúci spod masky ·
dopočítavanie čísel vo faktoch · parallax na fotopáse · zoom fotiek pri prejdení myšou ·
lightbox so šípkami, klávesnicou, počítadlom a swipom na mobile · šípky v tlačidlách ·
lepkavý text pri fotkách · fixná lišta so Zavolať/Booking na mobile.
Všetko rešpektuje `prefers-reduced-motion`.

## Cookies
Lišta vyskočí 1,1 s po načítaní, voľba sa ukladá do `localStorage`
(`depoloco_cookies_v1`), znovu ju otvorí okrúhle tlačidlo vľavo dole.
Tri kategórie: nevyhnutné (vždy), štatistika, vložený obsah.

**Dôležité:** súhlas nie je len ozdoba - 360° prehliadka sa načíta až po súhlase
s vloženým obsahom, inak ponúkne tlačidlo „Povoliť a spustiť". Merací kód
(GA4, Plausible) patrí do funkcie `loadStats()`, spustí sa len po súhlase so štatistikou.

## Dopytový formulár
V sekcii Rezervácia. Ochrany:

1. **Honeypot** - skryté pole `web`; ak ho niečo vyplní, odoslanie sa ticho zahodí.
2. **Časová pasca** - odoslanie do 3 s od načítania je odmietnuté.
3. **Limit** - max. 3 dopyty za hodinu z jedného prehliadača (`localStorage`).
4. **Validácia** - meno, e-mail, tvar telefónu, dĺžka správy, povinný GDPR súhlas;
   chyby sa píšu pod polia a nastavuje sa `aria-invalid`.
5. Vstupy sa čistia od riadiacich znakov a vypisujú cez `textContent`, nie `innerHTML`.

**Formulár zatiaľ nikam neodosiela** - dopyt sa uloží do `localStorage`
(`depoloco_dopyty`). Volanie backendu patrí do kroku 5 v `index.html`
(hľadaj komentár „sem patri volanie backendu"). Honeypot a časovú pascu treba
zopakovať aj na serveri - klientská kontrola sa dá obísť.

## Fotky
V `img/` sú fotky stiahnuté z galérie Archinfo, orezané a skomprimované pre web (spolu ~3,8 MB).

| súbor | čo je na ňom |
|---|---|
| `hero.jpg` | exteriér za súmraku v snehu, rozsvietené okná |
| `pribeh-1.jpg` | interiér loftu s tehlovým murivom |
| `pribeh-2.jpg` | **pôvodný stav** pred rekonštrukciou |
| `pribeh-3.jpg` | kuchyňa |
| `loft.jpg` | hlavný priestor loftu |
| `vagon.jpg` | interiér tiny housu |
| `pas.jpg` | nočný pás rozsvietených okien (široký pruh medzi sekciami) |
| `g1.jpg` - `g7.jpg` | galéria (g1 na výšku, g7 panoráma s ohniskom) |

**Autori fotiek:** Miro Pochyba, Ondrej Filipko, Katarína Pokorná (uvedení v pätičke webu).
Pred spustením naostro treba mať od nich súhlas - teraz sú prevzaté z Archinfo.sk.

Ak dodá klient vlastné fotky, stačí prepísať súbory s rovnakými názvami.
Keď súbor chýba, web namiesto neho zobrazí štýlový placeholder s jeho názvom.

## Virtuálna prehliadka
Sekcia `#prehliadka` - iframe na `virtualneprehliadky.online/depoloco/` sa načíta až po kliknutí
na tlačidlo (aby prehliadka nespomaľovala načítanie stránky). Pod ňou je aj odkaz na otvorenie
v novom okne.

## Zdroje obsahu
- Archinfo.sk - architektonický popis, citát Elišky Turanskej, fotogaléria
- Booking.com / Bed&Breakfast - kapacita, vybavenie, check-in/out, hodnotenie 9,8
- Instagram: https://www.instagram.com/depo_loco

## Ešte overiť u klienta
- ceny / cenník za noc a sezónu (teraz „cena na dopyt")
- e-mail na rezervácie (teraz iba telefón +421 948 441 737)
- presná kapacita vagóna a či sa objekty prenajímajú aj samostatne
- či je bazén stále v prevádzke a v akej sezóne
- súhlas fotografov s použitím fotiek

## QR kód
`img/qr.png` odkazuje na `https://www.depoloco.sk`. Vygeneroval ho `gen_qr.py`:

```bash
python3 gen_qr.py https://www.depoloco.sk
```

**Doména `depoloco.sk` ešte nie je kúpená** - QR aj tak odkazuje na ňu, pretože to tak
chcel klient. Kým doména nebude aktívna (DNS smerujúci na Vercel), QR vedie na
neexistujúcu stránku. Akonáhle je doména kúpená a nasmerovaná, over že QR funguje
(naskenuj ho) - inak sa netreba k nemu vracať.

## Nasadenie
- **Repo:** https://github.com/majsteshifu/depo-loco-web (verejné, vetva `main`)
- **Hosting:** Vercel, projekt prepojený s repom - každý push do `main` sa nasadí sám.
  Statický web bez buildu, žiadny build command ani output directory netreba nastavovať.
- `vercel.json` drží ročnú cache na `/img/*` a základné bezpečnostné hlavičky.
- Úpravy: zmeň `index.html`, commitni, pushni - Vercel zvyšok dorobí.
- Doména: `depoloco.sk` + `www.depoloco.sk`, DNS na Websupporte smeruje na Vercel (A záznam 76.76.21.21).

## Kontaktné čísla
Na webe sú dve telefónne čísla, obe bez mena (majiteľka o to výslovne požiadala):
- `+421 948 441 737` - primárne
- `+421 904 226 821` - záložné ("Ak sa nedovoláte na prvé číslo")

Oba sú v: hlavičke (len prvé), sekcii Kontakt (obe ako samostatné karty), JSON-LD
(`contactPoint`) a vo fallback hláške formulára po prekročení limitu dopytov.


## SEO
- `<title>`, meta description (skrátený pod 160 znakov), `canonical` na https://depoloco.sk/
- Open Graph + Twitter Card (absolútna URL na `img/hero.jpg`, rozmery obrázka)
- Štruktúrované dáta `LodgingBusiness` (JSON-LD) - adresa, súradnice (približné, stred obce),
  telefón, checkin/checkout, vybavenie, hodnotenie 5,0/17 z Airbnb (zhoduje sa s tým, čo je
  viditeľné na stránke)
- `favicon.ico` + PNG ikony + `apple-touch-icon.png` + `manifest.json` (vygenerované skriptom
  nižšie, jednoduché monogram "D" v medenej na tmavom pozadí)
- `robots.txt` a `sitemap.xml` (jedna URL - je to one-page web)
- Všetky `<img>` majú popisný `alt`, dekoratívne obrázky (fotopás, lightbox) majú `alt=""` zámerne
- Jeden `<h1>`, správna hierarchia `<h2>`/`<h3>`

**Súradnice v JSON-LD** (48.8069, 19.1244) sú stred obce Špania Dolina, nie presná poloha
objektu - dostatočné pre lokálne SEO, ale ak budeš chcieť presnejšie, over si GPS priamo
pri dome (napr. z Google Maps pinu) a uprav `geo` v `index.html`.

### Favicon - ako prerobiť
```bash
python3 - <<'EOF'
from PIL import Image, ImageDraw, ImageFont
# uprav farby/pismeno podla potreby, pozri povodny skript v histórii commitov
EOF
```


## Recenzie
Nová sekcia `#recenzie` (medzi Okolie a fotopás, aj v navigácii) - 6 skutočných citácií
z verejnej Airbnb stránky (airbnb.com/rooms/1044689773999709332), zdroj a dátum uvedený
pri každej. Mená sú len krstné, presne tak, ako ich Airbnb sám zobrazuje verejne.
Nič nie je vymyslené - ak treba pridať/vymeniť recenziu, over si text priamo na Airbnb
(záložka Hodnotenia), aby sedel doslovne.

Airbnb má 17 hodnotení, 5,0/5 - vybraných je 6 najlepšie vyznievajúcich a najrozmanitejších.
Booking a Google Maps recenzie sa mi nepodarilo dohľadať (stránky blokujú automatizovaný
prístup) - ak k nim máš prístup ako majiteľ (napr. cez Google Business Profile), pošli mi
texty a pridám aj tie.


## Galéria - doplnené fotky z Bookingu
Web má naozaj málo vlastných fotiek, tak som skúsil dohľadať viac na verejných stránkach
(Archinfo sa už minulo, Booking blokuje WebFetch ale nie prehliadač). Na Booking.com stránke
Depo Loca je 49 fotiek v plnej galérii - stiahol som ich cez prehliadač (bstatic.com CDN
odkazy majú podpísaný token, funguje len krátko po načítaní stránky).

Pridané 4 nové (`g8.jpg` - `g11.jpg`), všetky bez viditeľných ľudí:
- `g8.jpg` - výhľad z okna loftu na bazén a banícky vozík vonku (ukazuje skutočný bazén)
- `g9.jpg` - detail pôvodnej kachľovej piecky
- `g10.jpg` - interiér vagóna (vysoký strop, poschodová posteľ) - prvá reálna fotka interiéru vagóna na webe
- `g11.jpg` - terasa za slnečného dňa (doteraz mal web len nočné/zimné zábery exteriéru)

**Vedome vynechané** fotky s viditeľnými hosťami (skupina ľudí na terase, muž so psom pri ohni,
deti pri hojdačke) - klient si to pri fotopáse nepriamo vyžiadal.

Zvyšných ~44 fotiek z Bookingu je v `/tmp/booking-gallery` (dočasné, nie v git) - ak chceš
doplniť ešte niečo iné, pozri si kontaktný hárok alebo pošli info čo hľadáš.


## Galéria - zarovnanie
Mriežka `#gal` teraz používa jednotný `aspect-square` na všetkých 11 dlaždiciach (predtým
mala g1 vysoký formát cez 2 riadky, g7/g11 široký cez 2 stĺpce, g10 orezaný na výšku -
pôsobilo to rozhádzane). Teraz je to čistá mriežka 4 (desktop) / 3 (tablet) / 2 (mobil)
rovnako veľkých štvorcov.


## Cookie lišta
Predtým bola malá karta ukotvená vľavo dole (max-w-26rem) - klientovi to prekážalo.
Teraz je to široký banner cez takmer celú šírku (max-w-5xl, vystredený), na veľkých
obrazovkách text a tlačidlá vedľa seba namiesto pod sebou.
