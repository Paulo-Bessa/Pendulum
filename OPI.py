import numpy as np

def distance(x,y):
    """Returns the euclidean distance between two vectors."""
    if not isinstance(x,np.ndarray):
        x=np.array(x)
    if not isinstance(y,np.ndarray):
        y=np.array(y)
    
    sqrd_diff = np.square(x-y)
    ans = np.sqrt(np.sum(sqrd_diff))
    return ans

def identify_UPO(points,period,tol=1e-2):
    """Returns the indexes of the Unstable Periodic Orbits
    identified with prescripted period ant standar tolerance
    of 1e-2."""
    UPO_index=[]
    for i in range(len(points)-period):
        if distance(points[i],points[i+period])<tol:
            UPO_index.append(i)
    return UPO_index

def modulo_UPO(indexes,points,tol=5e-2):
    """Returns the indexes of the Unstable Periodic Orbits
    without repeated orbits."""
    removables=[]
    for elex in indexes:
        for eley in indexes:
            if elex!=eley:
                if distance(points[elex],points[eley])<tol:
                    removables.append(eley)

    removables = set(removables)
    if len(removables)==len(indexes):
        for elem in list(removables)[1:]:
            indexes.remove(elem)
    return indexes