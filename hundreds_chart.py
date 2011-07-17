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

def hundreds_chart(chartbase=10, numberbase=10, index=0, zeropad=True,
                   zeroear=False):
    base = chartbase
    xlim = np.array([-0.5, base - 0.5])
    ylim = np.array([base - 0.5, -0.5])
    if zeroear:
        if index == 0:
            xlim += np.array([0., 1.])
            ylim += np.array([-1., 0.])
        if index == 1:
            xlim += np.array([-1., 0.])
    plt.figure(figsize=(0.35 * np.abs(xlim[1] - xlim[0]),
                        0.35 * np.abs(ylim[1] - ylim[0])))
    plt.clf()
    ax = plt.gca()
    ax.set_frame_on(False)
    ax.set_position([0.01, 0.01, 0.98, 0.98])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    for i in range(base+1):
        plt.plot([-0.5, base - 0.5], [i - 0.5, i - 0.5], 'k-', clip_on=False)
        plt.plot([i - 0.5, i - 0.5], [-0.5, base - 0.5], 'k-', clip_on=False)
    tweak = 0.03
    for i in range(base):
        for j in range(base):
            label = stringy(index + i * base + j, numberbase)
            if zeropad:
                if len(label) < 2:
                    label = '0' + label
            plt.text(j + tweak, i, label, ha='center', va='center')
    if zeroear:
        if index == 0:
            pass
        if index == 1:
            pass
    plt.axis('equal')
    plt.xlim(xlim)
    plt.ylim(xlim)
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
    return None

if __name__ == '__main__':
    main()
