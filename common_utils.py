import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid

def plot_labeled_image_grid(images, labels, title=None, cmap=None, sizes=2.5, n_cols=10):
    N = images.shape[0]

    n_rows = int(np.ceil(N/n_cols))

    fig = plt.figure(figsize=(sizes*n_cols, sizes*n_rows))

    # Construct a grid to plot images
    grid = ImageGrid(fig, 111,
             nrows_ncols=(n_rows, n_cols),
             axes_pad=(0.05, 0.5),
             )

    for i in range(N):
        ax = grid[i]
        im = images[i]
        ax.get_yaxis().set_ticks([])
        ax.get_xaxis().set_ticks([])
        label = labels[i]
        ax.set_title('{}'.format(label))
        if cmap:
            ax.imshow(im, cmap=cmap)
        else:
            ax.imshow(im)

    # Remove empty plots
    for i in range(N, n_rows*n_cols):
        grid[i].remove()

    plt.suptitle(title, fontsize=16, y=1.01)
    plt.show()

def plot_image_grid(images, title=None, cmap='gray', sizes=2, n_cols=10):
    N = images.shape[0]

    n_rows = int(np.ceil(N/n_cols))

    fig = plt.figure(figsize=(sizes*n_cols, sizes*n_rows))

    # Construct a grid to plot images
    grid = ImageGrid(fig, 111,
                     nrows_ncols=(n_rows, n_cols),
                     axes_pad=(0.05, 0.05),
                     )

    for i in range(N):
        ax = grid[i]
        im = images[i]
        ax.get_yaxis().set_ticks([])
        ax.get_xaxis().set_ticks([])
        ax.imshow(im, cmap=cmap)

    # Remove empty plots
    for i in range(N, n_rows*n_cols):
        grid[i].remove()

    plt.suptitle(title, fontsize=16, y=0.92)
    plt.show()

def normalize(x):
    a = np.min(x)
    b = np.max(x)
    return (x - a) / (b - a)
