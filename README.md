# Depo Loco - web

One-page web zážitkového ubytovania **Depo Loco** na Španej Doline.
Jeden statický súbor `index.html` (Tailwind CDN + FontAwesome + Google Fonts), bez build kroku.

**Vizuál:** Space Grotesk (nadpisy, bez verzálok) + Inter, tmavá `#15120F` s medenou `#C98A4B`,
zaoblené sekcie a fotky (2 rem), plávajúca „pill" navigácia s blurom, na mobile fixná lišta
so Zavolať / Booking. Nadpisy majú plynulú veľkosť cez `clamp()`, takže sa nelámu na žiadnej šírke.

## Spustenie
Otvor `index.html` v prehliadači.

## Fotky - dôležité upozornenie
`img/vagon.jpg` je teraz **reálna fotka** vagóna, ktorú poslal klient (orezaná na 16:10).

`img/priroda.jpg` je stále len orezaná fotka lesa z galérie Archinfo (bez budovy), použitá
ako nálada pre kartu Loco (jurta) - nie je to skutočné miesto budúcej jurty. **Čaká sa na
skutočnú fotku jurty od klienta** - keď príde, stačí ju uložiť ako `img/priroda.jpg`
(alebo zmeniť názov v `index.html`, sekcia #ubytovanie, karta "Loco").

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
