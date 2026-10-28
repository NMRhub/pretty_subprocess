# pretty_subprocess
Wrapper around `subprocess.run` that shows the joined command when an exception is raised.

## Usage

```python
import pretty_subprocess

result = pretty_subprocess.run(['ls', '-l', '/no/such dir'], check=True)
```

### `run(*args, **kwargs) -> subprocess.CompletedProcess`

A drop-in replacement for `subprocess.run`. All positional and keyword arguments
are passed through unchanged. `PrettyCompletedProcess` CompletedProcess subclass is 
returned ; it includes the joined command.

If `subprocess.run` raises an exception (e.g. `CalledProcessError` with `check=True`,
`FileNotFoundError` for a missing executable, `TimeoutExpired`), a note with the
command is attached to the exception via `add_note` and the original exception
is re-raised. The command is shown as:

* the string itself, if the command was passed as a single string, bytes or path, or
* a shell-quoted string built with `shlex.join`, if it was passed as a sequence.
  Items that are `bytes` or path-like (e.g. `pathlib.Path`) are converted to strings.

The command may be passed positionally or as the `args=` keyword.

The note appears in the traceback, so the failing command can be copied and run
directly in a shell:

```
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command '['ls', '-l', '/no/such dir']' returned non-zero exit status 2.
Command: ls -l '/no/such dir'
```

The command of a successful command can also be shown:
```
cp = pretty_subprocess.run(('/bin/ls','/tmp'),capture_output=True)
print(cp.command)
```

Requires Python 3.12 or later.
