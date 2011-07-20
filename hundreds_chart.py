import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow
import numpy as np

prefix = 'hundreds_chart'
suffix = 'png'

def stringy(number, base):
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F']
    assert(base <= len(digit))
    if number < base:
        return digit[number]
    else:
        return stringy(number / base, base) + stringy(number % base, base)

def draw_number(x, y, label, alpha=1.):
    tweak = 0.03
    boxalpha = 0.5 * alpha
    plt.plot(x + np.array([-0.5, -0.5, 0.5, 0.5, -0.5]),
             y + np.array([-0.5, 0.5, 0.5, -0.5, -0.5]), 'k-', clip_on=False, alpha=boxalpha)
    plt.text(x + tweak, y, label, ha='center', va='center', alpha=alpha)
    return None

def draw_arrow(start, vector, base, index):
    plt.gca().add_artist(FancyArrow(start[0], start[1], vector[0], vector[1],
                                    width=0.2, head_width=0.4, length_includes_head=True,
                                    ec='none', fc='k', alpha=0.25))
    return None

def draw_number_grid(base, numberbase, index, zeropad, shift=(0, 0), alpha=1.):
    for i in range(base):
        for j in range(base):
            label = stringy(index + i * base + j, numberbase)
            if zeropad:
                if len(label) < 2:
                    label = '0' + label
            draw_number(j + shift[0], i + shift[1], label, alpha=alpha)
    return None

# some keywords may conflict
def hundreds_chart(chartbase=10, numberbase=10, index=0, zeropad=True,
                   zeroear=False, arrow=[], tileright=False):
    assert((zeroear is False) or (tileright is False))
    base = chartbase
    xlim = np.array([-0.5, base - 0.5])
    ylim = np.array([base - 0.5, -0.5])
    if zeroear:
        if index == 0:
            xlim += np.array([0., 1.])
            ylim += np.array([0., -1.])
        if index == 1:
            xlim += np.array([-1., 0.])
            ylim += np.array([0., -1.])
    if tileright:
            xlim += np.array([0., 10.])
            ylim += np.array([0., -1.])
    plt.figure(figsize=(0.35 * np.abs(xlim[1] - xlim[0]),
                        0.35 * np.abs(ylim[1] - ylim[0])))
    plt.clf()
    ax = plt.gca()
    ax.set_frame_on(False)
    ax.set_position([0.01, 0.01, 0.98, 0.98])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    draw_number_grid(base, numberbase, index, zeropad)
    if tileright:
        shift = np.array((10, -1))
        draw_number_grid(base, numberbase, index, zeropad, shift=shift, alpha=0.5)
    zero1 = np.array((0, 0))
    if index == 1:
        zero1 = None
    zero2 = None
    if zeroear:
        label = '0'
        if zeropad:
            label = '0' + label
        if index == 0:
            zero2 = np.array((10, -1))
            draw_number(*zero2, label=label, alpha=0.5)
        if index == 1:
            zero1 = np.array((-1, 0))
            zero2 = np.array((9, -1))
            draw_number(*zero1, label=label, alpha=0.5)
            draw_number(*zero2, label=label, alpha=0.5)
    if tileright:
        if index == 0:
            zero2 = zero1 + shift
        if index == 1:
            zero2 = np.array((9, -1))
            draw_number(*zero2, label='00', alpha=0.5)
    for a in arrow:
        if a[0] == 0:
            for zero in [zero1, zero2]:
                if zero is not None:
                    dx = (a[1] % base) - index - zero[0]
                    dy = ((a[1] - 1) / base) - zero[1]
                    draw_arrow(zero, (dx, dy), base, index)
                    if tileright and dx < 0:
                        draw_arrow(zero, np.array((dx, dy)) + shift, base, index)
        else:
            x = (a[0] % base) - index
            y = ((a[0] - 1) / base)
            dx = (a[1] % base) - index - x
            dy = ((a[1] - 1) / base) - y
            draw_arrow((x, y), (dx, dy), base, index)
            if tileright and dx < 0:
                draw_arrow((x, y), np.array((dx, dy)) + shift, base, index)
    plt.axis('equal')
    plt.xlim(xlim)
    plt.ylim(ylim)
    return None

def false_main():
    hundreds_chart()
    plt.savefig('%s_default.%s' % (prefix, suffix))
    hundreds_chart(zeropad=False)
    plt.savefig('%s_nzp.%s' % (prefix, suffix))
    hundreds_chart(index=1, zeropad=False)
    plt.savefig('%s_index1.%s' % (prefix, suffix))
    hundreds_chart(chartbase=2)
    plt.savefig('%s_2x2.%s' % (prefix, suffix))
    hundreds_chart(chartbase=2, numberbase=2)
    plt.savefig('%s_2x2_base2.%s' % (prefix, suffix))
    hundreds_chart(chartbase=3, numberbase=3)
    plt.savefig('%s_3x3_base3.%s' % (prefix, suffix))
    hundreds_chart(chartbase=4, numberbase=4)
    plt.savefig('%s_4x4_base4.%s' % (prefix, suffix))
    hundreds_chart(zeroear=True)
    plt.savefig('%s_ze.%s' % (prefix, suffix))
    hundreds_chart(zeroear=True, index=1)
    plt.savefig('%s_ze_index1.%s' % (prefix, suffix))
    hundreds_chart(arrow=[(0, 23), (64, 87)])
    plt.savefig('%s_23.%s' % (prefix, suffix))
    hundreds_chart(zeroear=True, arrow=[(0, 23), (64, 87), (28, 51)])
    plt.savefig('%s_ze_23.%s' % (prefix, suffix))
    hundreds_chart(zeroear=True, arrow=[(0, 23), (64, 87), (28, 51)], index=1)
    plt.savefig('%s_ze_index1_23.%s' % (prefix, suffix))
    return None

def main():
    hundreds_chart(tileright=True)
    plt.savefig('%s_tr.%s' % (prefix, suffix))
    hundreds_chart(tileright=True, arrow=[(0, 23), (64, 87), (28, 51)])
    plt.savefig('%s_tr_23.%s' % (prefix, suffix))
    hundreds_chart(tileright=True, arrow=[(0, 23), (64, 87), (28, 51)], index=1)
    plt.savefig('%s_tr_index1_23.%s' % (prefix, suffix))
    return None

if __name__ == '__main__':
    main()
