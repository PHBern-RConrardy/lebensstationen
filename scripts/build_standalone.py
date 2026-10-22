"""Build a self-contained, offline HTML from the website and vendored assets."""
from pathlib import Path
import base64
import re

ROOT = Path(__file__).resolve().parents[1]

def inline_script(source):
    # Prevent HTML from interpreting a closing script tag inside JS strings.
    return '<script>\n' + re.sub(r'</script', r'<\\/script', source, flags=re.I) + '\n</script>'

html = (ROOT / 'dist/index.html').read_text()
css = (ROOT / 'dist/styles.css').read_text()
html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + css + '\n</style>')
app = (ROOT / 'dist/app.js').read_text()
data_url = 'data:application/json;base64,' + base64.b64encode((ROOT / 'vendor/ch-cantons-lakes.json').read_bytes()).decode()
app, count = re.subn(r'topologyUrl="[^"]+"', lambda _: 'topologyUrl="' + data_url + '"', app)
assert count == 1
app = app.replace('assetBase=document.currentScript?', 'assetBase=document.currentScript?.src?')
scripts = {
    'https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js': ROOT / 'vendor/d3.min.js',
    'https://cdn.jsdelivr.net/npm/topojson-client@3/dist/topojson-client.min.js': ROOT / 'vendor/topojson-client.min.js',
    'luxembourg-data.js': ROOT / 'dist/luxembourg-data.js',
    'app.js': None,
}
for url, path in scripts.items():
    tag = '<script src="' + url + '"></script>'
    assert html.count(tag) == 1, url
    html = html.replace(tag, inline_script(app if path is None else path.read_text()))
assert '<script src=' not in html
for folder in ['dist', 'docs']:
    target = ROOT / folder / 'lebensstationen-standalone.html'
    target.write_text(html)
    print(f'{target.relative_to(ROOT)}: {target.stat().st_size:,} bytes')
