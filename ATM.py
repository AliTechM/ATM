
def ATMex(request ,total):

    while request>0 and request <total:
        if request >= 100:
            print "give 100"
            request = request -100
        elif request >=50:
            print "give 50"
            request = request -50
        elif request >=10:
            print "give 10"
            request = request -10
        elif request >=5:
            print "give 5"
            request = request -5
        else:
            print "give 2"
            request = request -2
    return

ATMex(277,500)