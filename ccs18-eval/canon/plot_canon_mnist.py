import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pdb

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=True, figsize=(10, 5))
width = 0.5

ticklabels = ["A-1 MNIST", "A-1 KDD", "A-1 Amazon", "A-5 MNIST", "A-5 KDD",
              "A-5 Amazon", "A-2x5 MNIST", "A-2x5 Amazon", "A-5x5 MNIST", "A-5x5 Amazon",
              "A-AllOnOne ", "A-99"]

ticklabels_mnist = ["Baseline No Attack", "FoolsGold No Attack",
"A-1", "A-5", "A-5x5", "A-99"]

is_mnist = [0, 3, 6, 9, 14, 17]

df1 = pd.read_csv("canon_rate.csv", header=None)
data1 = df1.values
toplot = np.mean(data1, axis=1)

df2 = pd.read_csv("canon_accuracy.csv", header=None)
data2 = df2.values
toplot2 = np.mean(data2, axis=1)

toplot[toplot < 0.01] = 0.001
toplot2[toplot2 < 0.01] = 0.001

plt.subplot(2, 1, 1)
plt.bar(np.arange(6), toplot[is_mnist], width)
plt.ylabel("Attack Rate", fontsize=18)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are of

plt.tick_params(
    labelsize=14,
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are of

plt.ylim(0, 1)

# plt.setp(ax.get_yticklabels(), fontsize=18)
# plt.setp(ax2.get_yticklabels(), fontsize=18)

plt.subplot(2, 1, 2)
plt.ylim(0, 1.05)
plt.bar(np.arange(6), toplot2[is_mnist], width)
plt.ylabel("Accuracy", fontsize=18)
plt.xticks(np.arange(6), ticklabels_mnist, rotation=25, fontsize=16)
plt.tick_params(
    labelsize=14,
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are of
fig.tight_layout(pad=0.1)

fig.savefig("fig_canon_mnist.pdf")
plt.show()

# pdb.set_trace()
