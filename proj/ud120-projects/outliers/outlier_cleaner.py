#!/usr/bin/python

import numpy

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    # print predictions
    re =  predictions - net_worths
    re = numpy.absolute(re)
    # print re
    # print 'biggest error %f' % re[17]
    # print 'next biggest error %f' % re[64]
    # print 'next biggest error %f' % re[33]

    # Convert the array into index/value pair, sort them based on value and return the index.
    # This will get us the index with the largest errors
    srei = [i[0] for i in sorted(enumerate(re), key=lambda x:x[1], reverse=True)]
    # print srei

    # for x in range(0, len(srei)):
    #     tuple = (ages[srei[x]][0], net_worths[srei[x]][0], re[srei[x]][0])
    #     print "data %s" % (tuple,)
    #     # cleaned_data.append(tuple);

    for x in range(9, len(srei)):
        tuple = (ages[srei[x]][0], net_worths[srei[x]][0], re[srei[x]][0])
        # print "appending %s" % (tuple,)
        cleaned_data.append(tuple);
    
    # print len(cleaned_data)
    #print cleaned_data
    ### your code goes here

    
    return cleaned_data

