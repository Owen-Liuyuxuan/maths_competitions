#!/usr/bin/env python3
"""Serve the local reader, optionally as an on-demand systemd user service."""
import argparse
import functools
import http.server
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
UNIT = 'math-atlas-library.service'


class ReaderHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Do not leave an old data.js or a cached reader after rebuilding.
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument('--background', action='store_true', help='Keep serving after the terminal/chat closes; no login autostart')
    actions.add_argument('--stop', action='store_true')
    actions.add_argument('--status', action='store_true')
    args = parser.parse_args()
    if args.stop or args.status:
        return subprocess.call(['systemctl', '--user', 'stop' if args.stop else 'status', UNIT])
    if args.background:
        if subprocess.run(['systemctl', '--user', 'is-active', '--quiet', UNIT]).returncode == 0:
            print('Reader already running: http://127.0.0.1:8092/')
            return 0
        return subprocess.call([
            'systemd-run', '--user', '--unit=' + UNIT, '--collect',
            '--description=Math Atlas local reader', '--property=Restart=on-failure',
            '--property=WorkingDirectory=' + str(ROOT),
            str(Path(sys.executable).resolve()), str(Path(__file__).resolve()),
        ])
    directory = ROOT / 'dist/library'
    if not (directory / 'index.html').is_file():
        parser.error('Build the reader first: python3 scripts/build.py')
    handler = functools.partial(ReaderHandler, directory=str(directory))
    with http.server.ThreadingHTTPServer(('127.0.0.1', 8092), handler) as server:
        print('Math Atlas: http://127.0.0.1:8092/', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
