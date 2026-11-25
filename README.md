# Sum up 24 November's world news in one image

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/caothiquynh26-source/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/caothiquynh26-source/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

make.fun bounty: https://make.fun/bounty/news-image-20261124
Reward: $100 USDC, 50 places paid. Deadline: 2026-11-26T00:00:00Z.

## The image

A one-page newspaper front page for Tuesday 24 November 2026: a lead
story on Jensen Huang's return as Nvidia CEO, six shorter stories
(Zaporizhzhia, Gaza, Iran, COP31, the Nepal quake, South Korea's
anti-AI-cheating bounty) and a markets strip (S&P 500 +4.7%, Nasdaq
+6.5%, Nikkei +3.9%, Gold $3,620, Brent $86.7).

## How it works

`main.py` (Python 3.13, stdlib only, no network) copies the
pre-rendered `entry.png` (1024x1024, 134,542 bytes) sitting next to it
to `/output/entry.png`, then verifies the copy is byte-identical to the
source. Running it twice writes identical bytes.

`build_image.py` is the generator that drew `entry.png` with Pillow
(DejaVu / Liberation fonts, fixed layout, no randomness). Re-running it
reproduces the same image bytes (sha256
`b3870326b5df1ee5db490c77e427c5f15857223774f5a0eb26d1bf18b1996895`).

## Run it

```sh
python3 main.py        # writes /output/entry.png
```

Headlines were cross-checked against Just Security Early Edition, The
Global Eye, and the Horizon world-news summary for 24 Nov 2026.
