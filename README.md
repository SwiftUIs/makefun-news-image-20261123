# The World in One Day — Monday 23 November 2026

A newspaper front page that sums up Monday 23 November 2026 in one image
(1024×1024 PNG), for the make.fun `news-image-20261123` bounty.

## What the page shows

Six stories, all of which happened or were first reported on 23 November 2026:

1. **COP31 ends with no deal (Antalya, Turkey)** — the EU and about 130
   countries reject a draft text that leaves out fossil fuels; the summit
   closes without an agreement.
2. **Strike on Dymer kills at least 10 (Kyiv region, Ukraine)** — a Russian
   strike north of Kyiv; the region marks 23 November a day of mourning.
3. **AI sell-off shakes markets** — Japan's Nikkei falls 5.06% and the S&P 500
   drops 3.7% as AI shares slide.
4. **Democrats win the House, 258 seats (USA)** — their largest House
   majority since 1992.
5. **Mexico captures 'El Chapo Isidro'** — the FBI's most-wanted fugitive is
   caught in Sinaloa.
6. **Márquez takes eighth title (MotoGP)** — Marc Márquez wins his eighth
   MotoGP world title.

## How it was made

The four pictures (COP31 hall, Kyiv street, trading floor, MotoGP racer) are
flat editorial illustrations made without any text. All words on the page
were drawn afterwards with real fonts by `draw.py` (Python + Pillow), so no
text is garbled: the masthead, the date, every headline and every caption is
crisp at full size and at ~300 px.

## How to run

```sh
python3 draw.py          # rebuild entry.png from assets/ + draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # copy entry.png to out/
```

`main.ts` only copies `entry.png` to the output directory, so two runs
produce byte-identical output. The program uses only the Node standard
library and needs no network.

## Files

- `entry.png` — the finished front page
- `main.ts` — the entry program (copies entry.png to the output directory)
- `draw.py` — the composition script that draws the page
- `assets/` — the four text-free illustrations used by draw.py
- `LICENSE` — MIT
