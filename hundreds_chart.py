import pylab as plt

prefix = 'hundreds_chart'
suffix = 'png'

def hundreds_chart():
    for i in range(11):
        plt.plot([-0.5, 9.5], [i - 0.5, i - 0.5], 'k-')
        plt.plot([i - 0.5, i - 0.5], [-0.5, 9.5], 'k-')
    for i in range(10):
        for j in range(10):
            plt.text(j, i, '%02d' % (i * 10 + j), ha='center', va='center')
    plt.axis('equal')
    plt.xlim(-0.5, 9.5)
    plt.ylim(9.5, -0.5)
    return None

def main():
    plt.clf()
    plt.gca().set_position([0., 0., 1., 1.])
    hundreds_chart()
    plt.savefig('%s_default.%s' % (prefix, suffix))
    return None

if __name__ == '__main__':
    main()
