import math
def euclidian(X,Y):
    """
    Description
    -----------
    Function that returns Euclidean distance between two vectors
    Parameters
    ----------
    X :
    Y :

    Returns
    -------

    """
    dist=0
    for i in range(len(X)):
        dist+=(X[i]-Y[i])**2
    return math.sqrt(dist)

def manhatan(X,Y):
    dist=0
    for i in range(X,Y):
        dist+=abs(X[i]-Y[i])
    return dist

def cosine_similarity(X,Y):
    norm_X=math.sqrt(sum(map(lambda xi:xi**2,X)))
    norm_Y=math.sqrt(sum(map(lambda yi:yi**2,Y)))
    dot_product=sum(xi*yi for xi,yi in zip(X,Y))
    return dot_product/norm_X*norm_Y

def jaccard_similarity(X,Y):
    """
    Description
    -----------
    Jaccard Similarity is a statistical measure used to gauge similarity between two sets. It is defined as the size of
    the intersection of the sets divided by union of the sets.
    Parameters
    ----------
    X :
    Y :

    Returns
    -------

    """
    x_set=set(X)
    y_set=set(Y)
    js=len(x_set.intersection(y_set))/len(x_set.union(y_set))
    return js
if __name__=='__main__':
    X=[2,3,5]
    Y=[1,2,6]
    print(euclidian(X=X,Y=Y))