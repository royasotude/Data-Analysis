import numpy as np
def p2p_distance(input):
    input = np.array(input)
    dist = input[:, np.newaxis, :] - input[np.newaxis, :, :]
    output = np.sqrt(np.sum(dist**2, axis=2))
    return output