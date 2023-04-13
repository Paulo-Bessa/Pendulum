import numpy as np

def distance(x,y):
    x=np.array(x)
    y=np.array(y)
    assert np.shape(x)==np.shape(y)
    
    ans = np.sqrt(sum(np.square(x-y)))
    return ans

def OPI_id(sub_states, periods,TOL=4e-1):
    TOL2 = 7*TOL

    OPIs=[]
    OPIS_c = []

    for period in periods:
        OPI=[]
        for i in range(len(sub_states)-period):
            if distance(sub_states[i],sub_states[i+period])<TOL:
                OPI.append(sub_states[i])
        OPI=np.array(OPI)
        OPIs.append(OPI)

    # Filtro
    for OPI in OPIs:
        OPI_c = [[0,0]]
        sizes = [np.linalg.norm(OPI[0])]
        for i in range(len(OPI)):
            for j in range(i,len(OPI)):
                dist = distance(OPI[i],OPI[j])
                size = np.linalg.norm(OPI[j])
                if dist<TOL2 and dist != 0:
                    if size not in sizes:
                        sizes.append(size)
                        OPI_c.append(OPI[j])
        OPI_c=np.array(OPI_c)
        OPIS_c.append(OPI_c)
    return [OPIs,OPIS_c]