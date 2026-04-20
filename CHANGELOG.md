# Release notes

<!-- do not remove -->

## 0.0.25

### New Features

- Add `_SafeTypeMeta` and `_safe_type` class with proper isinstance support, and expose `__class__` on `_ReadOnlyCallable` ([#31](https://github.com/AnswerDotAI/safepyrun/issues/31))


## 0.0.24

### New Features

- Add CLI ([#30](https://github.com/AnswerDotAI/safepyrun/issues/30))
- Add bound method support to `_callable_ok` ([#29](https://github.com/AnswerDotAI/safepyrun/issues/29))

### Bugs Squashed

- Show source code for line causing an exception. ([#28](https://github.com/AnswerDotAI/safepyrun/pull/28)), thanks to [@PiotrCzapla](https://github.com/PiotrCzapla)


## 0.0.23

### New Features

- Add `_ReadOnlyCallable`, add `should_export` logic, improve error messages with allow() hints, and add `any`/`all` builtins ([#25](https://github.com/AnswerDotAI/safepyrun/issues/25))
- allow all of `json` ([#24](https://github.com/AnswerDotAI/safepyrun/issues/24))


## 0.0.21

### New Features

- Use `pyskills` ([#23](https://github.com/AnswerDotAI/safepyrun/issues/23))


## 0.0.20

### New Features

- Add `write_policy` param to allow() ([#22](https://github.com/AnswerDotAI/safepyrun/issues/22))


## 0.0.19

### New Features

- Unify `__pytools__`, `__pytools_cls__`, `__pytools_write__` into single defaultdict; use `__call__` instead of .check() on WritePolicy ([#21](https://github.com/AnswerDotAI/safepyrun/issues/21))


## 0.0.18

### New Features

- Add `_WriteGuard` proxy, expand allowlist to use `...` for full module access, tighten callable permissions and `_` suffix semantics ([#20](https://github.com/AnswerDotAI/safepyrun/issues/20))
- Add `sum` and `hasattr` ([#19](https://github.com/AnswerDotAI/safepyrun/issues/19))


## 0.0.17

### New Features

- Add in-place operator support and safe type() override to sandbox ([#18](https://github.com/AnswerDotAI/safepyrun/issues/18))


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

