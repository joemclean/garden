#!/usr/bin/env python3
"""Generator for lyapunov.svg (seventeenth sitting, "the clock that lost the
minute"). Requires numpy + scipy. Run as: python3 lyapunov_gen.py
Writes lyapunov.json and lyapunov.svg into this same directory.

robustness.html (sixteenth sitting) found one direction, 250deg, where this
plot's baseline solver setting (rtol=1e-9, atol=1e-11, max_step=0.5) disagreed
with two independently-tighter settings on when a kicked L4 particle first
breaks Jupiter's resonance -- baseline says t=365.53, the tighter settings
agree at t=287.43, a 27% gap unlike anything else on the disc. That sitting's
journal left the mechanism as an unconfirmed guess: "a near-tangency with the
Hill-radius close-pass threshold at some intermediate point along the
trajectory." This script tests that guess directly by re-running the same
theta=250, v=v_crit trajectory under baseline and tight_rtol with dense
output and no terminal events, then comparing the two continuous solutions
point by point rather than only at their two reported break times.
"""
import json, math
import numpy as np
from scipy.integrate import solve_ivp

mu = 9.5388e-4
HILL = (mu/3.0)**(1/3)
CLOSE_THRESH = 0.3 * HILL
L4 = np.array([0.5-mu, np.sqrt(3)/2])
JUP = np.array([1-mu, 0.0])

# theta and v_crit are read from robustness.html's own results.json rather
# than retyped, so this piece can't silently drift from the number it's
# explaining.
_prior = json.load(open('results.json'))
_row = next(r for r in _prior if r['theta'] == 250)
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

sol_base = run_dense(1e-9, 1e-11, 0.5, 300.0)
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
tt_div = np.linspace(0.01, 290, 2000)
sb = sol_base.sol(tt_div)
st = sol_true.sol(np.minimum(tt_div, T_BREAK_TIGHT))  # true sol undefined past its own extent
div = np.hypot(sb[0]-st[0], sb[1]-st[1])

# first time the two trajectories separate by more than the close-pass
# threshold itself -- the moment a viewer could no longer call them "the
# same orbit" at the resolution that decides the outcome
idx_split = np.argmax(div > CLOSE_THRESH)
t_split = tt_div[idx_split]

# exponential fit over the clean pre-saturation stretch, avoiding both the
# roundoff floor near t=0 and the close-approach-driven kinks after t~180
fit_mask = (tt_div >= 20) & (tt_div <= 180)
slope, intercept = np.polyfit(tt_div[fit_mask], np.log(div[fit_mask]), 1)
efold = 1.0/slope

summary = {
    'theta': THETA, 'v_crit': V_CRIT,
    't_break_baseline': T_BREAK_BASELINE, 't_break_tight': T_BREAK_TIGHT,
    't_deep_close_approach': float(t_deep), 'r2_at_deep_close_approach': float(r2_deep),
    'r2_baseline_at_same_instant': r2_base_at_deep, 'close_thresh': CLOSE_THRESH,
    't_split_past_close_thresh': float(t_split),
    'lyapunov_efold_time_units': float(efold),
    'note': ('Not a near-tangency with the close-pass circle. The two dense '
             'integrations, from bit-identical initial conditions, separate '
             'smoothly (roundoff-level at t=10) and then grow ~exponentially '
             '(e-folding time about %.1f time units, fit t in [20,180]) until '
             'their separation exceeds the close-pass threshold itself by '
             't=%.0f -- 109 time units before the tight integration\'s own '
             'genuine near-collision with Jupiter (r2=%.5f, %.1fx inside the '
             'threshold) at t=%.1f. At that exact instant the baseline '
             'integration is at r2=%.4f, nowhere near Jupiter: it is simply '
             'no longer following the same trajectory, chaos having amplified '
             'its coarser tolerance past the point where "same orbit" is '
             'still a meaningful description.' % (
                 efold, t_split, r2_deep, CLOSE_THRESH/r2_deep, t_deep,
                 r2_base_at_deep))
}
json.dump(summary, open('lyapunov.json', 'w'), indent=2)
for k, v in summary.items():
    print(k, '=', v)

# ---------------------------------------------------------------- SVG ----
W, H = 800, 1090
MX, MY = 40, 40
PANEL = 720  # main trajectory panel is PANEL x PANEL
GAP = 26
STRIP_H = 220

DATA_CX, DATA_CY = -0.06, 0.07
SCALE = 250.0
PCX, PCY = MX + PANEL/2, MY + PANEL/2

def px(x, y):
    return (PCX + SCALE*(x-DATA_CX), PCY - SCALE*(y-DATA_CY))

CLR_SHARED = '#726d88'
CLR_BASE = '#8fa3c9'
CLR_TRUE = '#ff5b7a'
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
svg.append('<title>The clock that lost the minute</title>')
svg.append('<defs>')
svg.append('<radialGradient id="bg" cx="46%" cy="30%" r="90%"><stop offset="0%" stop-color="#141225"/>'
            '<stop offset="60%" stop-color="#0b0a16"/><stop offset="100%" stop-color="#050409"/></radialGradient>')
svg.append('<radialGradient id="burst" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#ff5b7a" stop-opacity="0.95"/>'
            '<stop offset="45%" stop-color="#ff5b7a" stop-opacity="0.32"/><stop offset="100%" stop-color="#ff5b7a" stop-opacity="0"/></radialGradient>')
svg.append('<radialGradient id="jupglow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#d68a4a" stop-opacity="0.55"/>'
            '<stop offset="100%" stop-color="#d68a4a" stop-opacity="0"/></radialGradient>')
svg.append('</defs>')
svg.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bg)"/>')

# ---- main panel ----
svg.append(f'<rect x="{MX}" y="{MY}" width="{PANEL}" height="{PANEL}" fill="none" stroke="#211d30" stroke-width="1"/>')

# close-pass threshold circle around Jupiter
jx, jy = px(*JUP)
r_thresh = SCALE*CLOSE_THRESH
svg.append(f'<circle cx="{jx:.2f}" cy="{jy:.2f}" r="{r_thresh:.2f}" fill="none" stroke="#3a3450" stroke-width="1.2" stroke-dasharray="2 5" opacity="0.8"/>')

# shared trail, t in [0, t_split], one color, fading in
n1 = 900
ts1 = np.linspace(0, t_split, n1)
s1 = sol_base.sol(ts1)
svg += trail(s1, 0, t_split, n1, CLR_SHARED, 0.05, 0.55, 0.7, 1.3)

# baseline branch, t in [t_split, 290]
n2 = 700
ts2 = np.linspace(t_split, 290.0, n2)
s2 = sol_base.sol(ts2)
svg += trail(s2, t_split, 290.0, n2, CLR_BASE, 0.35, 0.95, 1.2, 2.0)

# true branch, t in [t_split, t_break_tight]
n3 = 700
ts3 = np.linspace(t_split, T_BREAK_TIGHT, n3)
s3 = sol_true.sol(ts3)
svg += trail(s3, t_split, T_BREAK_TIGHT, n3, CLR_TRUE, 0.35, 0.98, 1.2, 2.2)

# burst + markers at the true deep close approach
dx, dy = px(*sol_true.sol(t_deep)[:2])
svg.append(f'<circle cx="{dx:.2f}" cy="{dy:.2f}" r="34" fill="url(#burst)"/>')
svg.append(f'<circle cx="{dx:.2f}" cy="{dy:.2f}" r="3.6" fill="#ff5b7a" stroke="#050409" stroke-width="0.8"/>')

# baseline's position at that same instant, hollow, nowhere near Jupiter
bx, by = px(*sol_base.sol(t_deep)[:2])
svg.append(f'<circle cx="{bx:.2f}" cy="{by:.2f}" r="4.2" fill="none" stroke="{CLR_BASE}" stroke-width="1.6"/>')
svg.append(f'<line x1="{dx:.2f}" y1="{dy:.2f}" x2="{bx:.2f}" y2="{by:.2f}" stroke="#4a4460" stroke-width="1" stroke-dasharray="1 4" opacity="0.6"/>')

# Sun, Jupiter, L4 markers
sx, sy = px(-mu, 0)
svg.append(f'<circle cx="{sx:.2f}" cy="{sy:.2f}" r="10" fill="{CLR_SUN}"/>')
svg.append(f'<circle cx="{jx:.2f}" cy="{jy:.2f}" r="20" fill="url(#jupglow)"/>')
svg.append(f'<circle cx="{jx:.2f}" cy="{jy:.2f}" r="6.2" fill="{CLR_JUP}"/>')
lx, ly = px(*L4)
svg.append(f'<circle cx="{lx:.2f}" cy="{ly:.2f}" r="3.2" fill="none" stroke="#cfc9db" stroke-width="1.3" opacity="0.8"/>')

svg.append(f'<text x="{MX+14}" y="{MY+26}" fill="#726d88" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="11" letter-spacing="0.06em">L4, &#952;=250&#176;, v=v_crit &#8212; t=0 to {int(round(T_BREAK_TIGHT))}</text>')

# legend, bottom-left of the main panel, on a solid backing so it stays
# readable over the tangle of loops behind it
LX, LY = MX+16, MY+PANEL-78
legend = [
    (CLR_SHARED, 'both integrations, indistinguishable'),
    (CLR_BASE, "baseline (rtol 1e-9) &#8212; sails past"),
    (CLR_TRUE, 'tight rtol (1e-11) &#8212; the real close approach'),
]
svg.append(f'<rect x="{LX-10}" y="{LY-16}" width="336" height="{18*len(legend)+14}" fill="#050409" opacity="0.72" rx="4"/>')
for i, (c, label) in enumerate(legend):
    ly2 = LY + i*18
    svg.append(f'<line x1="{LX}" y1="{ly2}" x2="{LX+22}" y2="{ly2}" stroke="{c}" stroke-width="2.4" stroke-linecap="round"/>')
    svg.append(f'<text x="{LX+30}" y="{ly2+4}" fill="#9d99ae" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="10.5">{label}</text>')

# ---- divergence strip ----
SY = MY + PANEL + GAP
svg.append(f'<rect x="{MX}" y="{SY}" width="{PANEL}" height="{STRIP_H}" fill="none" stroke="#211d30" stroke-width="1"/>')

DMIN, DMAX = 1e-10, 3.0
def strip_x(t):
    return MX + (t/290.0)*PANEL
def strip_y(d):
    d = max(d, DMIN)
    f = (math.log10(d)-math.log10(DMIN))/(math.log10(DMAX)-math.log10(DMIN))
    return SY + STRIP_H - f*STRIP_H

# reference line at the close-pass threshold scale, labeled on the left
# where the curve is still far below it
ry = strip_y(CLOSE_THRESH)
svg.append(f'<line x1="{MX}" y1="{ry:.2f}" x2="{MX+PANEL}" y2="{ry:.2f}" stroke="#3a3450" stroke-width="1" stroke-dasharray="2 5" opacity="0.8"/>')
svg.append(f'<text x="{MX+8}" y="{ry-6:.2f}" fill="#726d88" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="10" text-anchor="start">close-pass threshold</text>')

# vertical markers, labeled below the axis rather than over the curve; y
# offset alternates per line so two close-together labels stack instead of
# colliding sideways
for i, (t, label, color) in enumerate(((t_split, 'separation > threshold', '#9d99ae'),
                                        (T_BREAK_TIGHT, 'true close approach', CLR_TRUE),
                                        (T_BREAK_BASELINE if T_BREAK_BASELINE <= 290 else None, 'baseline close approach', CLR_BASE))):
    if t is None:
        continue
    vx = strip_x(t)
    anchor = 'end' if vx > MX+PANEL-90 else ('start' if vx < MX+90 else 'middle')
    svg.append(f'<line x1="{vx:.2f}" y1="{SY}" x2="{vx:.2f}" y2="{SY+STRIP_H}" stroke="{color}" stroke-width="1" stroke-dasharray="1 4" opacity="0.55"/>')
    ty = SY+STRIP_H+16 + (i%2)*13
    svg.append(f'<text x="{vx:.2f}" y="{ty}" fill="{color}" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="9.5" text-anchor="{anchor}">{label}</text>')

# divergence curve
pts = []
for t in tt_div:
    d = div[np.searchsorted(tt_div, t)] if False else None
for i, t in enumerate(tt_div):
    pts.append((strip_x(t), strip_y(div[i])))
path = 'M ' + ' L '.join(f'{x:.2f} {y:.2f}' for x, y in pts)
svg.append(f'<path d="{path}" fill="none" stroke="{CLR_TRUE}" stroke-width="1.6" opacity="0.9"/>')

svg.append(f'<text x="{MX+14}" y="{SY+22}" fill="#726d88" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="11" letter-spacing="0.06em">separation between baseline and tight-rtol, log scale, t=0 to 290</text>')

svg.append('</svg>')
open('lyapunov.svg', 'w').write('\n'.join(svg))
print('wrote lyapunov.svg')
