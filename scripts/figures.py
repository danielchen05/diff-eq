"""Vector diagrams and their LaTeX labels for the course examples."""
from functools import lru_cache
from html import escape
from math import cos, exp, hypot, pi, sin, sqrt
from pathlib import Path
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path as VectorPath
from matplotlib.textpath import TextPath

DESTINATION = Path(__file__).resolve().parents[1] / 'dist/assets/figures'
GREEN, COPPER, GRAY = '#246452', '#a35a37', '#adbaaf'


def svg(name, width, height, content):
    DESTINATION.mkdir(exist_ok=True, parents=True)
    body = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'font-family="Georgia,serif" fill="#465e52">{content}</svg>')
    (DESTINATION / (name + '.svg')).write_text(body)


def path(xs, color, width=1.6):
    points = ' '.join(f'{x:.2f},{y:.2f}' for x, y in xs)
    return f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>'


def arrow(x, y, dx, dy, color=GREEN):
    length = hypot(dx, dy)
    ux, uy = dx / length, dy / length
    last_x, last_y = x + dx, y + dy
    head = [(last_x - 5 * ux - 3 * uy, last_y - 5 * uy + 3 * ux),
            (last_x, last_y),
            (last_x - 5 * ux + 3 * uy, last_y - 5 * uy - 3 * ux)]
    return path([(x, y), (last_x, last_y)], color, 1.7) + path(head, color, 1.7)


@lru_cache(maxsize=None)
def label_path(tex, size):
    glyphs = TextPath((0,0), f'${tex}$', size=size, prop=FontProperties(math_fontfamily='stix'))
    bounds = glyphs.get_extents()
    commands = {VectorPath.MOVETO:'M', VectorPath.LINETO:'L', VectorPath.CURVE3:'Q',
                VectorPath.CURVE4:'C', VectorPath.CLOSEPOLY:'Z'}
    path = []
    for coords, code in glyphs.iter_segments(curves=True,simplify=False):
        path.append(commands[code]+(' '.join(f'{v:.2f}' for v in coords) if code!=VectorPath.CLOSEPOLY else ''))
    return ' '.join(path), (bounds.x0+bounds.x1)/2


def label(x, y, tex, size=13):
    tex = str(tex)
    data, center = label_path(tex,size)
    return f'<g data-tex="{escape(tex,quote=True)}" transform="translate({x-center:.2f} {y}) scale(1 -1)"><path d="{data}"/></g>'


def field(name):
    w, h, cx, cy, sx, sy = 430, 216, 213, 105, 65, 35
    content = '<defs><clipPath id="bounds"><rect x="9" y="9" width="405" height="189"/></clipPath></defs>'
    content += path([(6, cy), (413, cy)], '#cad4ca', 1) + path([(cx, 7), (cx, 201)], '#cad4ca', 1)
    content += '<g clip-path="url(#bounds)">'
    for yy in range(-5, 6):
        y = yy / 2
        for xx in range(-9, 10):
            x = xx / 3
            if name == 'ellipse' and y == 0:
                continue
            m = y if name == 'growth' else -2 * x / y
            v = 5 / hypot(sx, sy * m)
            content += path([(cx + sx * (x-v), cy - sy * (y-v*m)),
                             (cx + sx * (x+v), cy - sy * (y+v*m))], GRAY, 1.25)
    if name == 'growth':
        for constant, color in [(1, GREEN), (-1, GREEN), (.32, COPPER), (-.32, COPPER), (0, '#849687')]:
            points = []
            for i in range(251):
                t = -3.15 + i / 40
                points.append((cx + sx*t, cy - sy*constant*exp(t)))
            content += path(points, color, 2.05 if constant else 1.25)
    content += '</g>' + label(421, cy+5, 't' if name == 'growth' else 'x') + label(cx-9, 12, 'y')
    svg(name, w, h, content)


def phase_line():
    content = path([(23, 37), (403, 37)], '#a6b6ab', 1.2)
    for j, x in enumerate([106, 210, 314]):
        fill = GREEN if j != 1 else '#fff'
        content += f'<circle cx="{x}" cy="37" r="5" fill="{fill}" stroke="{GREEN}" stroke-width="2"/>'
        content += label(x, 63, j, 16)
    for x, sign in [(57, 1), (157, -1), (260, 1), (365, -1)]:
        content += arrow(x-13*sign, 37, 26*sign, 0)
    svg('phase-z', 430, 76, content + label(415, 42, 'z'))


def radial():
    cx, cy, unit = 184, 111, 42
    content = path([(37, cy), (340, cy)], '#c9d2c9', 1) + path([(cx, 7), (cx, 207)], '#c9d2c9', 1)
    for r, color, dashed in [(1, COPPER, 'stroke-dasharray="5 4"'), (2, GREEN, '')]:
        R = r * unit
        content += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{color}" stroke-width="2" {dashed}/>'
        ang = -pi / 4
        x, y = cx+R*cos(ang), cy+R*sin(ang)
        content += arrow(x, y, -7*sin(ang), 7*cos(ang), color)
    for x, size in [(cx+29,-15), (cx+53,18), (cx+123,-21)]:
        content += arrow(x, cy, size, 0)
    content += f'<circle cx="{cx}" cy="{cy}" r="3" fill="{GREEN}"/>'
    content += label(cx+47, cy+16, '1') + label(cx+85, cy+16, '2') + label(351,cy+5,'x') + label(cx+11,14,'y')
    svg('radial', 380, 218, content)


def bifurcation():
    ox, oy, sx, sy = 278, 119, 64, 45
    xy = lambda c, x: (ox + sx*c, oy - sy*x)
    content = path([(22,oy),(350,oy)],'#c4d0c5',1) + path([(ox,12),(ox,220)],'#c4d0c5',1)
    content += label(359,oy+5,'c') + label(ox+12,15,'x')
    for c in (-3,-2,-1,0,1):
        x,y=xy(c,0)
        content += label(x-3,y+17,str(c),11)
    for a,b,branch,stable in [(-3.8,-1,lambda c:1,True),(-1,1,lambda c:1,False),
                               (-3.8,-1,lambda c:sqrt(-c),False),(-1,0,lambda c:sqrt(-c),True),
                               (-3.8,0,lambda c:-sqrt(-c),False)]:
        cc=[a+(b-a)*j/150 for j in range(151)]
        line=path([xy(c,branch(c)) for c in cc],GREEN if stable else COPPER,2.25)
        content += line if stable else line.replace('<polyline ','<polyline stroke-dasharray="5 3" ')
    for c,x in [(-1,1),(0,0)]:
        xx,yy=xy(c,x)
        content+=f'<circle cx="{xx}" cy="{yy}" r="3.3" fill="#313e33"/>'
    svg('bifurcation',380,230,content)


if __name__ == '__main__':
    field('growth')
    field('ellipse')
    phase_line()
    radial()
    bifurcation()
