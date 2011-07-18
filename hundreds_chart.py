import pylab as plt
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

def plot_number(x, y, label):
    tweak = 0.03
    plt.plot(x + np.array([-0.5, -0.5, 0.5, 0.5, -0.5]),
             y + np.array([-0.5, 0.5, 0.5, -0.5, -0.5]), 'k-', clip_on=False)
    plt.text(x + tweak, y, label, ha='center', va='center')
    return None

def draw_arrow(zero, number, base, index):
    dx = (number % base) - index - zero[0]
    dy = ((number - 1) / base) - zero[1]
    plt.arrow(zero[0], zero[1], dx, dy, alpha=0.5)
    return None

# some keywords conflict, eg, zeroear=True and zeropad=False
def hundreds_chart(chartbase=10, numberbase=10, index=0, zeropad=True,
                   zeroear=False, arrow=None):
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
    plt.figure(figsize=(0.35 * np.abs(xlim[1] - xlim[0]),
                        0.35 * np.abs(ylim[1] - ylim[0])))
    plt.clf()
    ax = plt.gca()
    ax.set_frame_on(False)
    ax.set_position([0.01, 0.01, 0.98, 0.98])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    for i in range(base):
        for j in range(base):
            label = stringy(index + i * base + j, numberbase)
            if zeropad:
                if len(label) < 2:
                    label = '0' + label
            plot_number(j, i, label)
    zero1 = (0, 0)
    if index == 1:
        zero1 = None
    zero2 = None
    if zeroear:
        if index == 0:
            zero2 = (10, -1)
            plot_number(*zero2, label='00')
        if index == 1:
            zero1 = (-1, 0)
            zero2 = (9, -1)
            plot_number(*zero1, label='00')
            plot_number(*zero2, label='00')
    if arrow is not None:
        if zero1 is not None:
            draw_arrow(zero1, arrow, base, index)
        if zero2 is not None:
            draw_arrow(zero2, arrow, base, index)
    plt.axis('equal')
    plt.xlim(xlim)
    plt.ylim(ylim)
    return None

def main():
    hundreds_chart()
    plt.savefig('%s_default.%s' % (prefix, suffix))
    hundreds_chart(zeropad=False)
    plt.savefig('%s_nzp.%s' % (prefix, suffix))
    hundreds_chart(index=1, zeropad=False)
    plt.savefig('%s_index1.%s' % (prefix, suffix))
    hundreds_chart(numberbase=2)
    plt.savefig('%s_base2.%s' % (prefix, suffix))
    hundreds_chart(numberbase=7)
    plt.savefig('%s_base7.%s' % (prefix, suffix))
    hundreds_chart(chartbase=7)
    plt.savefig('%s_7x7.%s' % (prefix, suffix))
    hundreds_chart(chartbase=7, numberbase=7)
    plt.savefig('%s_7x7_base7.%s' % (prefix, suffix))
    hundreds_chart(zeroear=True)
    plt.savefig('%s_ze.%s' % (prefix, suffix))
    hundreds_chart(zeroear=True, index=1)
    plt.savefig('%s_ze_index1.%s' % (prefix, suffix))
    hundreds_chart(arrow=23)
    plt.savefig('%s_23.%s' % (prefix, suffix))
    hundreds_chart(zeroear=True, arrow=23)
    plt.savefig('%s_ze_23.%s' % (prefix, suffix))
    hundreds_chart(zeroear=True, arrow=23, index=1)
    plt.savefig('%s_ze_index1_23.%s' % (prefix, suffix))
    return None

if __name__ == '__main__':
    main()
