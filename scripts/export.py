#!/usr/bin/env python3
"""Embed the same site, native typesetting and figures in one portable HTML file."""
from base64 import b64encode
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'


def data_uri(path, mime):
    return 'data:'+mime+';base64,'+b64encode(path.read_bytes()).decode()


def export(destination):
    out = (DIST/'index.html').read_text()
    assets = DIST/'assets'
    font = data_uri(assets/'math.ttf','font/ttf')
    css = (assets/'style.css').read_text().replace('url("math.ttf")','url("'+font+'")')
    js = (assets/'app.js').read_text().replace('</script','<\\/script')
    out = out.replace('<link rel="stylesheet" href="assets/style.css">','<style>'+css+'</style>')
    out = out.replace('<script defer src="assets/app.js"></script>','')
    out = out.replace('</body>', '<script>'+js+'</script>\n</body>')
    out = re.sub(r'(?P<attr>src|href)="(assets/[\w./-]+\.svg)"',
                 lambda m: m['attr']+'="'+data_uri(DIST/m[2],'image/svg+xml')+'"', out)
    license = (assets/'math-font-license.txt').read_text().replace('</script','<\\/script')
    out = out.replace('</body>','<script type="text/plain" id="font-license">'+license+'</script>\n</body>')
    destination.write_text(out)
    return destination.stat().st_size


if __name__=='__main__':
    destination=Path(sys.argv[1])
    print(f'{destination.name}: {export(destination):,} bytes')
