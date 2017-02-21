import numpy
import perfplot


def setup(n):
    return numpy.random.rand(n)


kernels = [
    lambda a: numpy.c_[a, a],
    lambda a: numpy.stack([a, a]).T,
    lambda a: numpy.vstack([a, a]).T,
    lambda a: numpy.column_stack([a, a]),
    lambda a: numpy.concatenate([a[:, None], a[:, None]], axis=1)
    ]

perfplot.show(
        setup,
        kernels,
        labels=['c_', 'stack', 'vstack', 'column_stack', 'concat'],
        n_range=[2**k for k in range(15)],
        xlabel='len(a)'
        )
