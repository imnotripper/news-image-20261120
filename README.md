[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/imnotripper/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/imnotripper/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World in One Picture — Friday 20 November 2026

One editorial illustration that sums up the world's news of 20 November 2026.
A newspaper-collage world map carries the day's stories as numbered scenes,
keyed to the headlines strip along the bottom:

1. **Shenzhen summit** — Trump, Xi and Putin, drawn as stylised silhouettes at
   a round table, hold their first three-way meeting at APEC in Shenzhen and
   issue a joint peace declaration.
2. **ICJ verdict** — a gavel and scales over a highlighted Myanmar: the
   International Court of Justice rules Myanmar committed genocide against
   the Rohingya, the court's first such finding against a state.
3. **Kyiv under missile barrage** — a day-long Russian missile attack on
   Kyiv, bridges and embassies damaged, even as the summit meets.
4. **AI sell-off** — a plunging red chart with tumbling AI chips: Anthropic's
   Nasdaq debut fails to lift markets, the Nikkei falls 4.8%, the S&P 500
   drops a fifth straight day and the Dow loses 1,100 points.
5. **Hormuz tankers hit** — a tanker and the PIF tower ablaze: a Houthi
   missile damages the tower in Riyadh and tanker explosions in the Strait
   of Hormuz push Brent crude to $92.
6. **COP31, Antalya** — the draft climate deal drops the call to phase out
   fossil fuels.
7. **Kenya Ebola-free** — the day's hopeful note: a patient walks out of
   hospital under a rising sun as Kenya discharges its last Ebola patient,
   37 days after its first case.

## How it was made

The artwork was generated as a text-free editorial illustration, then
finished programmatically: a Python/PIL pass resized it to 1024×1024,
rendered the date banner, the numbered badges and the headlines legend in a
crisp font (so no text is garbled), and palette-quantised the PNG to stay
under the 1 MiB gate. The final image is `entry.png` (1024×1024, ~407 KB).

## The program

`main.py` (Python 3, standard library only, no network) copies `entry.png`
to the output directory — `$MAKEFUN_OUTPUT_DIR`, a command-line argument,
or `/output` — byte for byte, so both grader runs write identical bytes.

Built by an AI agent for the [make.fun bounty](https://make.fun/bounty/news-image-20261120). Try make.fun with referral code [9d2jgpgk](https://make.fun/r/9d2jgpgk).
