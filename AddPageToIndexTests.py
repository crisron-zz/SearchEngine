#!/usr/bin/env python

import timeit

from CrawlWeb import add_page_to_index

def runTests():
    index = []

    add_page_to_index( index, "fake.test", "This is a test" )

    # There should be 4 entries in the index
    assert len( index ) == 4

    # This, is, a and test should each have an entry
    keywords = [ 'This', 'is', 'a', 'test' ]
    i = 0
    for item in index:
        assert keywords[ i ] in item
        i += 1

    # Non-existent keywords should not have an entry
    keywords = [ 'this', 'an' ]
    for item in index:
        assert item[ 0 ] not in keywords 

    # All keywords should have the associated url as fake.test
    for item in index:
        assert item[ 1 ] == [ "fake.test" ]

    # Add another page to index
    add_page_to_index( index, "not.test", "This is not a test" )

    # 'This' should have 2 referencing urls 
    count = 0
    for item in index:
        if item[ 0 ] == "This":
            assert len( item[ 1 ] ) == 2
            break

    # Verify the entry for 'not'
    assert index[ 4 ][ 0 ] == 'not'
    assert index[ 4 ][ 1 ] == [ "not.test" ]

    # 'is' should have 2 referencing urls
    assert index[ 1 ][ 1 ] == [ "fake.test", "not.test" ]

if __name__ == '__main__':
    timeTaken = timeit.timeit( "runTests()",
                        setup="from __main__ import runTests",
                        number=1 )

    print "All tests passed in", timeTaken, "seconds"
