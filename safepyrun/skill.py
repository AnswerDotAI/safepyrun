"""Execute Python in a persistent IPython-like kernel shared with the user. Variables, imports, objects, patches, and helper functions created in one call remain available in later calls.

# Execution model

The last expression is returned. Use this for inspection: `await pyrun("len(items_)")`. Use `print(...)` when you want multiple lines of output.

If a value will be needed later, assign it to a `_` suffixed name and return it as the last expression: `await pyrun("items_ = [1, 2, 3]\nitems_")`.

Write very short calls, usually 1-3 lines. Inspect first, then transform. Do not start by writing helper functions, classes, or long scripts.

`pyrun` intentionally separates execution globals and locals inside a single call. A helper function defined in a call may not reliably see variables assigned earlier in that same call. Additionally, helper functions defined inside one `pyrun` call may be called during that same call, but they are not automatically callable in later `pyrun` calls. The name may persist in the shared namespace, but the callable will be blocked unless it has been explicitly allowed. This is intentional: persistent helper functions can hide dangerous operations, so they should not become new tools by accident.

For repeated work, prefer inlining small expressions or defining-and-calling a helper in the same short `pyrun` call. Only create persistent helpers when the user has explicitly allowed that helper or when the surrounding tool policy is meant to expose it.

When an audit or allow error occurs, stop and report the denied call. Do not route around it. The allow system controls which functions, methods, and file destinations are approved; changing that is a conversation with the user.

# Working style

Use `pyrun` like a REPL, not a batch runner. Make one small move, inspect the result, then decide the next move. When entering an unfamiliar kernel, start with `await pyrun("ns_view_()")` to see imported module aliases, star imports, visible functions, and current variables before guessing names.

Inspect both data shape and API shape before transforming or calling unfamiliar objects. Use `type(...)`, `len(...)`, `list(obj_.keys())`, slices, `doc(...)`, `xdir(...)`, and `inspect.signature(...)` to understand what is available.

Good first moves:

```python
await pyrun("type(obj_)")
await pyrun("xdir(obj_)")
await pyrun("doc(obj_)")
await pyrun("list(obj_.keys())")
await pyrun("items_[:3]")
```

Prefer direct code over abstractions at first. Once a short pattern has worked two or three times, factor it into a `_` suffixed helper in its own call.

Let errors surface. Errors often reveal missing allow rules, wrong object shapes, wrong API assumptions, or missing permissions. Do not hide errors with broad `try/except` unless the user asks for defensive code.

# Naming and persistence

The kernel namespace is shared with the user. Do not clobber user variables, imports, helpers, or patches.

Use `_` suffixed names for values you create and may need later: `items_`, `path_`, `res_`, `df_`, `mod_`, `obj_`. This makes agent-owned state easy to recognize.

Avoid generic unsuffixed names like `data`, `df`, `client`, `msgs`, `result`, or `x` unless the user created them or explicitly asks for those names.

Temporary names inside a single short call can be plain, but anything that should survive into a later call should end in `_`.

Before reusing or overwriting an important `_` name, inspect it or choose a more specific name.

# Code style

Write compact, readable Python that matches the surrounding repo style. Prefer clarity over PEP-8 compliance.

Keep calls short. Avoid semicolons. Avoid long setup blocks. Group imports on one line when useful: `import json, os, re`.

Use short conventional names for local values: `i`, `s`, `xs`, `msg`, `path`, `res`. Use `_` suffix for persistent names.

Prefer simple expressions and comprehensions when they are clearer than loops. Prefer one-line bodies for tiny helpers once a helper is actually justified.

Use very few comments. Add a comment only when it explains why something non-obvious is necessary.

Do not auto-format code into a different style unless the user asks.

# Allow system and permissions

`pyrun` runs with audit checks. Some functions, methods, file operations, and dynamic Python patterns may fail if they are not allowed.

Allowed functions and methods come from pyskills and explicit `allow(...)` calls in the shared kernel. Use `doc(module_or_obj)` to inspect what a pyskill exposes and what it allows. Pyskills are capability bundles, not always execution namespaces. After inspecting `doc(module)`, call functions using the names shown by `doc(...)`, examples, or `ns_view_()`. Do not assume `module.func(...)` is valid just because `import module` worked.

When an allow or audit error happens, first decide whether it is a bad coding idiom or a real missing permission. If the code used dynamic or indirect Python such as `getattr`, `setattr`, broad introspection, hidden imports, or unusual filesystem access, rewrite it in a simpler direct style.

If a straightforward version of the needed operation is still denied, stop and report the exact denied operation. Ask the user whether that function, method, or destination should be allowed.

File writes and destructive operations may require destination-specific policies, not just function access. If a file operation fails, report the path and operation.

Do not route around policy. Simplifying bad code is fine; disguising the same denied operation is not.

# Common workflows

Inspect an object before using it:

```python
await pyrun("type(obj_)")
await pyrun("xdir(obj_)")
await pyrun("doc(obj_)")
```

Create a persistent value and return it:

```python
await pyrun("items_ = list(range(5))\nitems_")
```

Use async APIs directly:

```python
await pyrun("res_ = await client_.fetch(limit=5)\nres_")
```

Promote repeated direct code into a helper only after the pattern is known:

```python
await pyrun("def short_(s, n=80): return s[:n] + ('...' if len(s)>n else '')")
```

Run small shell or file operations through already-allowed Python tools, not by assuming a separate shell tool exists.

# Gotchas

Do not write large `pyrun` blocks. If a block fails halfway through, the state may be harder to reason about, and the useful error may be buried.

Functions defined inside a `pyrun` call may not reliably see variables assigned earlier in that same call. If you need a helper, first test the code directly, then define the helper in its own call with a `_` suffixed name.

Comprehensions, lambdas, callbacks, and sort keys can expose scoping issues sooner than straight-line code. Prefer explicit short loops when working inside an unfamiliar `pyrun` state.

The last expression is returned, but printed output is different. Use the last expression for one value; use `print(...)` for readable multi-line inspection.

Outputs in chat history may be truncated. Re-inspect current state with a fresh `pyrun` call before making edits, summaries, or decisions that depend on exact values.

Do not use broad `try/except` while exploring. Let the real error tell you what assumption failed. Never use `getattr` as it is prohibited, use direct attribute access instead.
"""
from pyskills import doc, xdir, list_pyskills
from pyskills.core import allow

__all__ = ['doc', 'xdir', 'list_pyskills', 'ns_view_']

def ns_view_():
    "Show useful public names in the current IPython namespace."
    import ast, inspect, types
    ns = globals()
    mods = {k:v.__name__ for k,v in ns.items() if isinstance(v, types.ModuleType) and not k.startswith('_')}
    stars,funcs,assigned = set(),set(),set()
    for src in In:
        try: tree = ast.parse(src)
        except SyntaxError: continue
        for n in ast.walk(tree):
            if isinstance(n, ast.ImportFrom):
                for a in n.names:
                    (stars if a.name == '*' else funcs).add(n.module if a.name == '*' else a.asname or a.name)
            elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)): funcs.add(n.name)
            elif isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store): assigned.add(n.id)
    vals = {k:ns[k] for k in assigned if k in ns and not k.startswith('_') and not inspect.isfunction(ns[k]) and not isinstance(ns[k], types.ModuleType)}
    hfuncs = {k:ns[k] for k in funcs if k in ns and inspect.isfunction(ns[k])}
    print('Imported modules:'); [print(f'  {k} -> {v}') for k,v in sorted(mods.items())]
    print('\nStar imports:'); [print(f'  {s} -> *') for s in sorted(stars)]
    print('\nFunctions:'); [print(f'  {k} -> {v.__module__}') for k,v in sorted(hfuncs.items())]
    print('\nVariables:'); [print(f'  {k} -> {type(v).__name__}') for k,v in sorted(vals.items())]

allow(doc, xdir, list_pyskills, ns_view_)


