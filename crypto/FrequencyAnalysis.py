import matplotlib.pyplot as plt

# X axis: A - Z
# Y axis: occurrence


def getFreq(Text: str):
    X = [chr(i) for i in range(65, 65+26)]
    xy = {}
    for index, element in enumerate(X):
        xy[element] = 0

    Text = Text.upper()
    for char in Text:
        for x in xy:
            if char == x:
                xy[x] = xy[x] + 1
    # return [list(xy.keys()), list(xy.values())]
    fig, ax = plt.subplots(1, 1)
    ax.bar(list(xy.keys()), list(xy.values()))
    fig.suptitle(f"Letters frequncy for input: {Text}")
    plt.grid()
    plt.draw()
    # plt.draw() allows for plot showing in background (so other running can continue)


# cipherText = "Tqxxa Iadxp"
# fig, ax = plt.subplots(1, 1)

# label = getFreq(cipherText)[0]
# values = getFreq(cipherText)[1]
# ax.bar(label, values)
# fig.suptitle(f"Letters frequncy for input: {cipherText}")
# plt.grid()
# plt.show()
