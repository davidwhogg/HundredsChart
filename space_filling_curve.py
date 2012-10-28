# This file is part of the Hundreds Chart project.
# Copyright 2011 David W. Hogg (NYU).

if __name__ == '__main__':
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

def trigfunctions(orientation):
    return ([0, 1, 0, -1])[orientation], ([1, 0, -1, 0])[orientation]

def number2digitlist(n, length=4, base=4):
    return [(n / base**p) % base for p in range(length)[::-1]]

def number2position(n, length=4):
    return digitlist2position(number2digitlist(n, length=length, base=4))

def digitlist2position(digitlist):
    nlevel = len(digitlist)
    parity = 1
    orientation = 0
    if nlevel % 2:
        parity = -1
        orientation = 1
    sidelength = 2**nlevel
    xcenter = sidelength / 2 - 0.5
    ycenter = sidelength / 2 - 0.5
    return digitlist2position_recursive(digitlist, parity, orientation, sidelength, xcenter, ycenter)

def digitlist2position_recursive(digitlist, parity, orientation, sidelength, xcenter, ycenter):
    if sidelength == 1:
        return xcenter, ycenter
    digit = digitlist[0]
    sine, cosine = trigfunctions(orientation)
    if digit == 0:
        xcenter -= (parity*cosine + sine) * 0.25 * sidelength
        ycenter -= (cosine - parity*sine) * 0.25 * sidelength
        orientation += parity
        parity *= -1
    if digit == 1:
        xcenter -= (parity*cosine - sine) * 0.25 * sidelength
        ycenter += (cosine + parity*sine) * 0.25 * sidelength
    if digit == 2:
        xcenter += (parity*cosine + sine) * 0.25 * sidelength
        ycenter += (cosine - parity*sine) * 0.25 * sidelength
    if digit == 3:
        xcenter += (parity*cosine - sine) * 0.25 * sidelength
        ycenter -= (cosine + parity*sine) * 0.25 * sidelength
        orientation -= parity
        parity *= -1
    if orientation < 0:
        orientation += 4
    if orientation > 3:
        orientation -= 4
    return digitlist2position_recursive(digitlist[1:], parity, orientation, sidelength / 2, xcenter, ycenter)

if __name__ == '__main__':
    plt.clf()
    ax = plt.gca()
    ax.set_frame_on(False)
    ax.set_position([0.05, 0.05, 0.90, 0.90])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    pos = [number2position(n) for n in range(4**4)]
    label = ['%d' % i for i in range(len(pos))]
    plt.plot([p[0] for p in pos], [p[1] for p in pos], 'k-', alpha=0.25)
    for (x, y), l in zip(pos, label):
        plt.text(x, y, l, va='center', ha='center')
    plt.axis('equal')
    plt.savefig('space_filling_curve.png')
