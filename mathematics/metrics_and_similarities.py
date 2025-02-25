import math


class Metrics:
    def __init__(self):
        pass

    @staticmethod
    def euclidian_metric(x, y):
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
        dist = 0
        for i in range(min(len(x), len(y))):
            dist += (x[i] - y[i]) ** 2
        return math.sqrt(dist)

    def manhattan_metric(X, Y):
        dist = 0
        for i in range(min(len(X), len(Y))):
            dist += abs(X[i] - Y[i])
        return dist


class Similarities:
    def __init__(self):
        pass

    @staticmethod
    def cosine_similarity(x, y):
        norm_X = math.sqrt(sum(map(lambda xi: xi ** 2, x)))
        norm_Y = math.sqrt(sum(map(lambda yi: yi ** 2, y)))
        dot_product = sum(xi * yi for xi, yi in zip(x, y))
        return dot_product / norm_X * norm_Y

    @staticmethod
    def jaccard_similarity(x, y):
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
        x_set = set(x)
        y_set = set(y)
        js = len(x_set.intersection(y_set)) / len(x_set.union(y_set))
        return js

