
import importlib.metadata
import logging
import os
import subprocess
import shlex
from typing import Any
pretty_subprocess_logger = logging.getLogger(__name__)

__version__ =  importlib.metadata.version('pretty_subprocess')


def _to_str(a)->str:
    if isinstance(a,(str,bytes,os.PathLike)):
        return os.fsdecode(a)
    return str(a)

class PrettyCompletedProcess(subprocess.CompletedProcess[Any]):

    def __init__(self, cp: subprocess.CompletedProcess[Any], command: str):
        super().__init__(cp.args, cp.returncode, cp.stdout, cp.stderr)
        self.command : str = command

def run(*args,**kwargs)->PrettyCompletedProcess:
    cmd = "Unknown"
    try:
        c = args[0] if args else kwargs.get('args')
        try:
            if isinstance(c,(str,bytes,os.PathLike)):
                cmd = _to_str(c)
            elif c is not None:
                cmd = shlex.join(_to_str(a) for a in c)
        except TypeError:
            pass
        cp = subprocess.run(*args,**kwargs)
        return PrettyCompletedProcess(cp,cmd)
    except Exception as e:
        e.add_note(f"Command: {cmd}")
        raise

