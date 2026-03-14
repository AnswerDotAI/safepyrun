# Release notes

<!-- do not remove -->

## 0.0.11

### New Features

- Add MRO check for callable whitelist and handle tuple SyntaxError messages ([#11](https://github.com/AnswerDotAI/safepyrun/issues/11))


## 0.0.10

### New Features

- Dynamic class-based allow policies via `__pytools_cls__` defaultdict; support `...` for all methods ([#10](https://github.com/AnswerDotAI/safepyrun/issues/10))


## 0.0.8

### New Features

- Simplify `_run_python` to return last expr directly, add %%py cell magic, matplotlib support, and IPython display tools ([#7](https://github.com/AnswerDotAI/safepyrun/issues/7))


## 0.0.7

### New Features

- Add expanduser to allowed Path methods ([#6](https://github.com/AnswerDotAI/safepyrun/pull/6)), thanks to [@ncoop57](https://github.com/ncoop57)
- Add iter and next to sandbox builtins ([#4](https://github.com/AnswerDotAI/safepyrun/pull/4)), thanks to [@ncoop57](https://github.com/ncoop57)


## 0.0.5

### New Features

- Add ContextVar fallback for asyncio.gather, `find_var` helper, `_apply_` for star-unpacking ([#3](https://github.com/AnswerDotAI/safepyrun/issues/3))


## 0.0.4

### New Features

- Add concise mode to `_run_python`/RunPython to return bare value when output has single key ([#2](https://github.com/AnswerDotAI/safepyrun/issues/2))


## 0.0.3

### New Features

- Add write destination policies with `ok_dests` support, and user config loading ([#1](https://github.com/AnswerDotAI/safepyrun/issues/1))


## 0.0.1

- init version

