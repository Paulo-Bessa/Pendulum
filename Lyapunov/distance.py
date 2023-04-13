import numpy as np

def dist(x,y):
    """Returns the euclidean distance between two vectors."""
    if not isinstance(x,np.ndarray):
        x=np.array(x)
    if not isinstance(y,np.ndarray):
        y=np.array(y)
    
    sqrd_diff = np.square(x-y)
    ans = np.sqrt(np.sum(sqrd_diff))
    return ans