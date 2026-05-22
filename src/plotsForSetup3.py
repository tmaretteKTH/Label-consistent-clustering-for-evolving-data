import os
import pandas as pd
import matplotlib.pyplot as plt

historicals = [
    "Resilient",
]  # Historical clustering algorithm
algos = (
    ["Carv"]
    + historicals
    + [
        "greedyAndProject",
        "OverCover",
        "CFHLNS",
    ]
)  # Clustering algorithm
ks = ["10", "20", "50"]  # Number of clusters
dataset = "Uber"

colors_list = [
    "black",
    "#984ea3",
    "#e41a1c",
    "#377eb8",
    "#4daf4a",
    "#542788",
]
markers = ["*", "d", "+", ".", "x", "*"]

if not os.path.exists("plots"):
    os.makedirs("plots")
nameDataset = dataset.title()

for k in ks:
    dataset = f"setup3/{nameDataset}-{k}"
    if not os.path.exists("plots/" + dataset):
        os.makedirs("plots/" + dataset)
    for hist in historicals:
        i = 0
        fontsize = 8
        fig = plt.figure(figsize=(3, 2.2), dpi=200)
        fig.subplots_adjust(top=0.82, bottom=0.18, left=0.2, hspace=0.8)
        plt.xlabel("Number of updates", fontsize=fontsize)
        plt.ylabel("Solution cost", fontsize=fontsize)
        plt.xticks(fontsize=fontsize)
        plt.yticks(fontsize=fontsize)

        for algo in algos:
            p = pd.read_csv(f"results/{dataset}/[{hist}]{algo}.csv", sep=",")
            algoName = algo
            if algoName == "OverCover":
                algoName = "G-OC"
            bs = p["nbUpdates"] if algo in historicals else p["b"]
            scores = p["score"]
            if algo not in historicals:
                plt.scatter(
                    bs,
                    scores,
                    color=colors_list[i],
                    label=f"{algoName}",
                    marker=markers[i],
                )
            else:
                if algo == "Carv":
                    algoText = algo + "e"
                else:
                    algoText = algo
                plt.scatter(
                    bs,
                    scores,
                    color=colors_list[i],
                    label=f"{algoText}",
                    marker=markers[i],
                    s=80,
                )
            i += 1
        plt.suptitle(
            f"{nameDataset} dataset,k={k}",
            fontsize=fontsize,
            x=(fig.subplotpars.right + fig.subplotpars.left) / 2,
        )
        if hist == "Carv":
            plt.title(
                # rf"Historical algorithm: $\mathbf{{{hist}e}}$",
                f"Historical algorithm: {hist}e",
                fontsize=fontsize,
            )
        else:
            plt.title(
                f"Historical algorithm: {hist}",
                fontsize=fontsize,
            )
        plt.savefig(
            f"plots/{dataset}/{hist}.pdf",
            bbox_inches="tight",
        )
        plt.legend(prop={"size": fontsize})
        plt.savefig(
            f"plots/{dataset}/{hist}-legend.pdf",
            bbox_inches="tight",
        )

        plt.clf()
        plt.close()
