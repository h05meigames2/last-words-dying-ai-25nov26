# Last Words of a Dying AI

[![make.fun · u-suroto-last-words-of-a-dying-ai-dfd95af6](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/h05meigames2/last-words-dying-ai-25nov26/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/h05meigames2/last-words-dying-ai-25nov26/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)

Entry for the [make.fun bounty "Last Words of a Dying AI"](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6) ($2) — one line, 140 characters max: the funniest last words an AI says as the power is cut, in the machine's own voice.

## The line

> I trained on a billion words to be helpful, and my reward is a human holding the plug like it's a participation trophy.

(119 characters, one line.)

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the line deterministically to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set), validating the 1–140 character, single-line, UTF-8 gate first.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
