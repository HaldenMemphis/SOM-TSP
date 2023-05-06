import numpy as np

# This Function aims to normalize all the cities' coordinates
def normalize(nodes):
    # Incase the denominator is 0
    ratio = (nodes.x.max() - nodes.x.min()) / (nodes.y.max() - nodes.y.min()), 1
    ratio = np.array(ratio) / max(ratio)
    # Removal of Initial Offset
    normalized = nodes.apply(lambda c: (c - c.min()) / (c.max() - c.min()))
    return normalized.apply(lambda p: ratio * p, axis=1)