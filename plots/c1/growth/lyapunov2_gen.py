#!/usr/bin/env python3
"""Generator for lyapunov2.svg (eighteenth sitting, "a second clock").
Requires numpy + scipy. Run as: python3 lyapunov2_gen.py
Writes lyapunov2.json and lyapunov2.svg into this same directory.

lyapunov.html (seventeenth sitting) measured a ~18.6-time-unit exponential
divergence rate between baseline and tight-rtol integrations at theta=250,
the direction robustness.html's own sweep flagged as its most extreme
"baseline-diverges" case (27% relative spread in break time, four orders of
magnitude past the rest of the disc). That sitting's own "Where to pick up"
asked a question of its own: is 18.6 time units a property of the
resonance-overlap region in general, or specific to the 250deg trajectory?
theta=230 is the next-most-disagreeing direction in results.json (relative
spread 5.6e-4, itself an order of magnitude above the ~15 directions sitting
at 1e-6..1e-7, though still under the 1e-3 threshold that would have called
it "timing-fragile" rather than "robust") -- the honest second data point.
This script re-runs 230's own bisected v_crit under baseline and tight_rtol
with dense output and no terminal events, exactly like lyapunov_gen.py did
for 250, and fits the same exponential divergence over the same style of
early window.
"""
import json, math
import numpy as np
from scipy.integrate import solve_ivp

mu = 9.5388e-4
HILL = (mu/3.0)**(1/3)
CLOSE_THRESH = 0.3 * HILL
L4 = np.array([0.5-mu, np.sqrt(3)/2])
JUP = np.array([1-mu, 0.0])

_prior = json.load(open('results.json'))
_row = next(r for r in _prior if r['theta'] == 230)
THETA, V_CRIT = _row['theta'], _row['v_crit']
T_BREAK_BASELINE = _row['settings']['baseline']['t_break']
T_BREAK_TIGHT = _row['settings']['tight_rtol']['t_break']

def deriv(t, s):
    x, y, vx, vy = s
    r1 = np.hypot(x+mu, y)
    r2 = np.hypot(x-1+mu, y)
    ax = 2*vy + x - (1-mu)*(x+mu)/r1**3 - mu*(x-1+mu)/r2**3
    ay = -2*vx + y - (1-mu)*y/r1**3 - mu*y/r2**3
    return [vx, vy, ax, ay]

def run_dense(rtol, atol, max_step, t_max):
    th = np.radians(THETA)
    s0 = [L4[0], L4[1], V_CRIT*np.cos(th), V_CRIT*np.sin(th)]
    return solve_ivp(deriv, [0, t_max], s0, method='DOP853', dense_output=True,
                      rtol=rtol, atol=atol, max_step=max_step)

T_MAX = max(T_BREAK_BASELINE, T_BREAK_TIGHT) + 5.0
sol_base = run_dense(1e-9, 1e-11, 0.5, T_MAX)
sol_true = run_dense(1e-11, 1e-13, 0.5, T_BREAK_TIGHT + 3.0)

# --- find the actual close approach the tight integration resolves ---
tt = np.linspace(0, T_BREAK_TIGHT + 2.0, 400000)
s_true = sol_true.sol(tt)
r2_true = np.hypot(s_true[0]-JUP[0], s_true[1]-JUP[1])
t_deep = tt[np.argmin(r2_true)]
r2_deep = r2_true.min()

# --- find where baseline sits at that same instant ---
s_base_at_deep = sol_base.sol(t_deep)
r2_base_at_deep = math.hypot(s_base_at_deep[0]-JUP[0], s_base_at_deep[1]-JUP[1])

# --- divergence between the two integrations over time ---
# Unlike 250 (baseline's own break sat 78 time units past the tight
# integration's), 230's two break times are only 0.11 time units apart, so
# the two dense solutions are only both individually valid up to the
# earlier of the two -- comparing past that point would mean reading one
# solution past its own trusted extent, the same care lyapunov_gen.py took
# for 250 by capping "st" at T_BREAK_TIGHT.
T_DIV_MAX = min(T_BREAK_BASELINE, T_BREAK_TIGHT)
tt_div = np.linspace(0.01, T_DIV_MAX, 4000)
sb = sol_base.sol(tt_div)
st = sol_true.sol(tt_div)
div = np.hypot(sb[0]-st[0], sb[1]-st[1])

idx_split = np.argmax(div > CLOSE_THRESH)
t_split = tt_div[idx_split] if div.max() > CLOSE_THRESH else None

# exponential fit over the clean pre-saturation stretch. 250's own fit used
# t in [20,180]; this trajectory's shared window is shorter (T_DIV_MAX
# ~= 199.5 vs 250's 290), so the window is scaled to the same fraction of
# the comparison range rather than reused as fixed numbers.
fit_lo = 0.10 * T_DIV_MAX
fit_hi = 0.90 * T_DIV_MAX
fit_mask = (tt_div >= fit_lo) & (tt_div <= fit_hi) & (div > 0)
slope, intercept = np.polyfit(tt_div[fit_mask], np.log(div[fit_mask]), 1)
efold = 1.0/slope

rel_diff = abs(efold-18.6)/18.6
summary = {
    'theta': THETA, 'v_crit': V_CRIT,
    't_break_baseline': T_BREAK_BASELINE, 't_break_tight': T_BREAK_TIGHT,
    't_deep_close_approach': float(t_deep), 'r2_at_deep_close_approach': float(r2_deep),
    'r2_baseline_at_same_instant': r2_base_at_deep, 'close_thresh': CLOSE_THRESH,
    't_split_past_close_thresh': float(t_split) if t_split else None,
    'div_max_in_shared_window': float(div.max()),
    'lyapunov_efold_time_units': float(efold),
    'compare_250_efold_time_units': 18.6,
    'note': ('theta=230, this plot\'s second-most-disagreeing direction after '
             '250 (relative spread 5.6e-4 vs 250\'s 0.27), shows the same '
             'qualitative mechanism at the front end: bit-identical starts '
             '(roundoff-level) separate smoothly, then grow ~exponentially '
             '(e-folding time %.1f time units, fit t in [%.1f,%.1f]) -- real, '
             'but %s than 250\'s own 18.6, so the rate itself is '
             'trajectory-specific, not one shared regional constant. The '
             'bigger difference is in the outcome: at 230 the two '
             'integrations\' break times are only %.2f time units apart '
             '(vs 250\'s 78), and position separation never exceeds the '
             'close-pass threshold before the tight trajectory\'s own close '
             'approach (peaks at %.4f against a %.4f threshold, %.0f%% of '
             'the way there) -- baseline is still describing essentially the '
             'same encounter, off by %.1fx in closest distance, not a wholly '
             'different future. 250\'s chaos had ~200 time units of runway to '
             'amplify an ordinary tolerance error into two distinct fates; '
             '230\'s chaos, at a comparable rate, simply runs out of runway '
             'first -- the same instability, caught partway through its own '
             'escalation rather than after it.' % (
                 efold, fit_lo, fit_hi,
                 'noticeably slower' if efold > 18.6*1.1 else ('noticeably faster' if efold < 18.6*0.9 else 'close to'),
                 abs(T_BREAK_BASELINE-T_BREAK_TIGHT), div.max(), CLOSE_THRESH,
                 100*div.max()/CLOSE_THRESH, r2_base_at_deep/CLOSE_THRESH))
}
json.dump(summary, open('lyapunov2.json', 'w'), indent=2)
for k, v in summary.items():
    print(k, '=', v)

# ---------------------------------------------------------------- SVG ----
W, H = 800, 1090
MX, MY = 40, 40
PANEL = 720
GAP = 26
STRIP_H = 220

DATA_CX, DATA_CY = -0.06, 0.07
SCALE = 250.0
PCX, PCY = MX + PANEL/2, MY + PANEL/2

def px(x, y):
    return (PCX + SCALE*(x-DATA_CX), PCY - SCALE*(y-DATA_CY))

CLR_SHARED = '#726d88'
CLR_BASE = '#7fd9c4'
CLR_TRUE = '#f5c453'
CLR_SUN = '#e8b25f'
CLR_JUP = '#d68a4a'

def trail(sol, t0, t1, n, color, op0, op1, w0, w1):
    ts = np.linspace(t0, t1, n)
    pts = sol(ts) if callable(sol) else sol
    xs, ys = pts[0], pts[1]
    out = []
    for i in range(n-1):
        f = i/(n-2) if n > 2 else 1.0
        op = op0 + (op1-op0)*f
        w = w0 + (w1-w0)*f
        x0, y0 = px(xs[i], ys[i]); x1, y1 = px(xs[i+1], ys[i+1])
        out.append(f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" '
                   f'stroke="{color}" stroke-width="{w:.2f}" stroke-linecap="round" opacity="{op:.3f}"/>')
    return out

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
svg.append('<title>A second clock</title>')
svg.append('<defs>')
svg.append('<radialGradient id="bg" cx="46%" cy="30%" r="90%"><stop offset="0%" stop-color="#141b25"/>'
            '<stop offset="60%" stop-color="#0a0e16"/><stop offset="100%" stop-color="#040609"/></radialGradient>')
svg.append('<radialGradient id="burst" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#f5c453" stop-opacity="0.95"/>'
            '<stop offset="45%" stop-color="#f5c453" stop-opacity="0.32"/><stop offset="100%" stop-color="#f5c453" stop-opacity="0"/></radialGradient>')
svg.append('<radialGradient id="jupglow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#d68a4a" stop-opacity="0.55"/>'
            '<stop offset="100%" stop-color="#d68a4a" stop-opacity="0"/></radialGradient>')
svg.append('</defs>')
svg.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bg)"/>')

svg.append(f'<rect x="{MX}" y="{MY}" width="{PANEL}" height="{PANEL}" fill="none" stroke="#1a2028" stroke-width="1"/>')

jx, jy = px(*JUP)
r_thresh = SCALE*CLOSE_THRESH
svg.append(f'<circle cx="{jx:.2f}" cy="{jy:.2f}" r="{r_thresh:.2f}" fill="none" stroke="#2e3540" stroke-width="1.2" stroke-dasharray="2 5" opacity="0.8"/>')

# Unlike 250, there's no honest split point to draw here -- t_split is None
# because position separation never clears the close-pass threshold before
# the tight integration's own close approach (peaks at 94% of the way
# there). Drawing two colored branches the way lyapunov.svg does would
# invent a visual disagreement the data doesn't show. Instead: one shared
# trail the whole way (baseline and tight-rtol really are visually
# indistinguishable at this scale for the entire run), then the small real
# gap is shown only where it actually exists -- as two close-together
# end markers at the moment of closest approach, not as a second branch.
n1 = 1400
ts1 = np.linspace(0, T_BREAK_TIGHT, n1)
s1 = sol_base.sol(ts1)
svg += trail(s1, 0, T_BREAK_TIGHT, n1, CLR_SHARED, 0.06, 0.62, 0.7, 1.4)

dx, dy = px(*sol_true.sol(t_deep)[:2])
svg.append(f'<circle cx="{dx:.2f}" cy="{dy:.2f}" r="34" fill="url(#burst)"/>')
svg.append(f'<circle cx="{dx:.2f}" cy="{dy:.2f}" r="3.6" fill="#f5c453" stroke="#040609" stroke-width="0.8"/>')

bx, by = px(*sol_base.sol(min(t_deep, T_MAX))[:2])
svg.append(f'<circle cx="{bx:.2f}" cy="{by:.2f}" r="4.2" fill="none" stroke="{CLR_BASE}" stroke-width="1.6"/>')
svg.append(f'<line x1="{dx:.2f}" y1="{dy:.2f}" x2="{bx:.2f}" y2="{by:.2f}" stroke="#39424e" stroke-width="1" stroke-dasharray="1 4" opacity="0.6"/>')

sx, sy = px(-mu, 0)
svg.append(f'<circle cx="{sx:.2f}" cy="{sy:.2f}" r="10" fill="{CLR_SUN}"/>')
svg.append(f'<circle cx="{jx:.2f}" cy="{jy:.2f}" r="20" fill="url(#jupglow)"/>')
svg.append(f'<circle cx="{jx:.2f}" cy="{jy:.2f}" r="6.2" fill="{CLR_JUP}"/>')
lx, ly = px(*L4)
svg.append(f'<circle cx="{lx:.2f}" cy="{ly:.2f}" r="3.2" fill="none" stroke="#cfc9db" stroke-width="1.3" opacity="0.8"/>')

svg.append(f'<text x="{MX+14}" y="{MY+26}" fill="#6b7480" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="11" letter-spacing="0.06em">L4, &#952;=230&#176;, v=v_crit &#8212; t=0 to {int(round(T_BREAK_TIGHT))}</text>')

LX, LY = MX+16, MY+PANEL-78
legend = [
    (CLR_SHARED, 'baseline &amp; tight rtol, indistinguishable the whole run'),
    (CLR_TRUE, 'tight rtol at closest approach to Jupiter'),
    (CLR_BASE, 'baseline at that same instant &#8212; close, not identical'),
]
svg.append(f'<rect x="{LX-10}" y="{LY-16}" width="380" height="{18*len(legend)+14}" fill="#040609" opacity="0.72" rx="4"/>')
for i, (c, label) in enumerate(legend):
    ly2 = LY + i*18
    svg.append(f'<line x1="{LX}" y1="{ly2}" x2="{LX+22}" y2="{ly2}" stroke="{c}" stroke-width="2.4" stroke-linecap="round"/>')
    svg.append(f'<text x="{LX+30}" y="{ly2+4}" fill="#8890a0" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="10.5">{label}</text>')

SY = MY + PANEL + GAP
svg.append(f'<rect x="{MX}" y="{SY}" width="{PANEL}" height="{STRIP_H}" fill="none" stroke="#1a2028" stroke-width="1"/>')

DMIN, DMAX = 1e-10, 3.0
STRIP_T_MAX = T_DIV_MAX
def strip_x(t):
    return MX + (t/STRIP_T_MAX)*PANEL
def strip_y(d):
    d = max(d, DMIN)
    f = (math.log10(d)-math.log10(DMIN))/(math.log10(DMAX)-math.log10(DMIN))
    return SY + STRIP_H - f*STRIP_H

ry = strip_y(CLOSE_THRESH)
svg.append(f'<line x1="{MX}" y1="{ry:.2f}" x2="{MX+PANEL}" y2="{ry:.2f}" stroke="#2e3540" stroke-width="1" stroke-dasharray="2 5" opacity="0.8"/>')
svg.append(f'<text x="{MX+8}" y="{ry-6:.2f}" fill="#6b7480" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="10" text-anchor="start">close-pass threshold</text>')

markers = [(t_split, 'separation > threshold', '#8890a0')] if t_split else []
markers.append((T_BREAK_TIGHT, 'true close approach', CLR_TRUE))
if T_BREAK_BASELINE <= STRIP_T_MAX:
    markers.append((T_BREAK_BASELINE, 'baseline close approach', CLR_BASE))
for i, (t, label, color) in enumerate(markers):
    vx = strip_x(t)
    anchor = 'end' if vx > MX+PANEL-90 else ('start' if vx < MX+90 else 'middle')
    svg.append(f'<line x1="{vx:.2f}" y1="{SY}" x2="{vx:.2f}" y2="{SY+STRIP_H}" stroke="{color}" stroke-width="1" stroke-dasharray="1 4" opacity="0.55"/>')
    ty = SY+STRIP_H+16 + (i%2)*13
    svg.append(f'<text x="{vx:.2f}" y="{ty}" fill="{color}" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="9.5" text-anchor="{anchor}">{label}</text>')

pts = []
for i, t in enumerate(tt_div):
    pts.append((strip_x(t), strip_y(div[i])))
path = 'M ' + ' L '.join(f'{x:.2f} {y:.2f}' for x, y in pts)
svg.append(f'<path d="{path}" fill="none" stroke="{CLR_TRUE}" stroke-width="1.6" opacity="0.9"/>')

svg.append(f'<text x="{MX+14}" y="{SY+22}" fill="#6b7480" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="11" letter-spacing="0.06em">separation between baseline and tight-rtol, log scale, t=0 to {int(STRIP_T_MAX)}</text>')

svg.append('</svg>')
open('lyapunov2.svg', 'w').write('\n'.join(svg))
print('wrote lyapunov2.svg')
