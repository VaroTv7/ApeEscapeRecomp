"""Run original and native polling against the actual regenerated PsyQ caller.

The retail-derived function stays in a temporary private include, never in Git.
Device stubs come from the maintained detector fixture; pipeline and instruction
cache timing use the real shared implementation.
"""
import argparse
from pathlib import Path
import re
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--framework', type=Path, required=True)
    parser.add_argument('--cc', required=True)
    args = parser.parse_args()
    title = Path(__file__).resolve().parents[1]
    body = None
    for path in sorted((title/'generated').glob('*full_*.c')):
        match = re.search(r'\nvoid func_8002E698\(.*?(?=\nvoid |\Z)', path.read_text(), re.S)
        if match:
            body = match[0]
            break
    if body is None:
        print('SKIP: regenerate the supported SCUS-94423 source first')
        return 77
    framework = args.framework.resolve()
    with tempfile.TemporaryDirectory(prefix='ape-vwait-') as temp:
        work = Path(temp)
        (work/'wait.inc').write_text(body)
        executable = work/'contract.exe'
        sources = [str(title/'tests/vwait_contract.c'),
                   str(framework/'runtime/src/psx_cycles.c'),
                   str(framework/'runtime/src/psx_icache.c')]
        includes = [str(work), str(framework/'runtime/include'), str(framework/'runtime/tests')]
        if Path(args.cc).name.lower() in ('cl', 'cl.exe'):
            command = [args.cc, '/nologo', '/std:c11', '/O2', '/DPSX_ENABLE_BLOCK_CYCLES=1',
                       '/DPSX_NO_DEBUG_TOOLS=1', *['/I'+p for p in includes],
                       *sources, '/Fe:'+str(executable)]
        else:
            command = [args.cc, '-std=c11', '-O2', '-DPSX_ENABLE_BLOCK_CYCLES=1',
                       '-DPSX_NO_DEBUG_TOOLS=1', *['-I'+p for p in includes],
                       *sources, '-o', str(executable)]
        subprocess.run(command, cwd=work, check=True)
        subprocess.run([str(executable)], cwd=work, check=True, timeout=30)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
