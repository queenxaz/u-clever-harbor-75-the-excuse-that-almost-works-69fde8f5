# The Excuse That Almost Works

[![Bounty](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![Rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/queenxaz/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/rank.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![Reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/queenxaz/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/reward.svg)](https://make.fun/c/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

A gamer's sick-day text: burst pipe, drowned laptop — working from the sofa, where the Wi-Fi still reaches.

## The entry

> Boss, the lift's stuck between floors with me in it. Maintenance says noon, maybe. Logging in from my phone.

(108 characters, limit 140, 19 words.)

## How it works

`main.py` writes the entry text to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set). No network, no randomness, no
arguments: the entry is fixed, so every run produces the same bytes.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
