"""
Calculate the Jaccard Similarity of sets
"""

from __future__ import division


def similarity(a, b):
    return len(a.intersection(b))/len(a.union(b))


def test():

    print "..."
    print "jaccardSimilarity module"
    print "Test mode"
    print "..."

    a = set(['A', 'B', 'C'])
    b = set(['C', 'D', 'E', 'A'])

    print "Jaccard Similarity of %s and %s is %s" % (a, b, similarity(a, b))

if __name__ == "__main__":
    test()
