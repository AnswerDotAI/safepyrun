# Release notes

<!-- do not remove -->

## 0.0.16

### New Features

- Add sdir/doc helpers, expose help/dir/doc as pytools, and broaden local var export to globals ([#17](https://github.com/AnswerDotAI/safepyrun/issues/17))


## 0.0.15

### New Features

- Add `allow_write_types` API for controlling in-place object mutation

### Bugs Squashed

- fix pyrun namespace to use kernel's `user_ns` ([#14](https://github.com/AnswerDotAI/safepyrun/pull/14)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.14

### New Features

- Add `default_ok_dests` config, expanduser path support, and expose allow in IPython extension ([#15](https://github.com/AnswerDotAI/safepyrun/issues/15))


## 0.0.13

### New Features

- Allow sleep ([#13](https://github.com/AnswerDotAI/safepyrun/issues/13))


## 0.0.12

### New Features

- Add `allow_matplotlib` ([#12](https://github.com/AnswerDotAI/safepyrun/issues/12))


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

