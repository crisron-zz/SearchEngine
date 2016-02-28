def get_next_target( page ):
    start_link = page.find( '<a href=' )
    if start_link == -1:
        return None, 0
    start_quote = page.find( '"', start_link )
    end_quote = page.find( '"', start_quote + 1 )
    url = page[ start_quote + 1:end_quote ]
    return url, end_quote

def get_all_links( page ):
    links = []
    while 1:
        url, endpos = get_next_target( page )
        if url:
            links.append( url )
            page = page[ endpos: ]
        else:
            break
    return links

def crawl_web( seed, max_depth ):
    toCrawl = [ seed ]
    crawled = []
    nextDepth = []
    depth = 0
    while toCrawl and max_depth >= depth:
        page = toCrawl.pop()
        if page not in crawled:
            links = get_all_links( get_page( page ) )
            for link in links:
                nextDepth.append( link )
            crawled.append( page )
        if not toCrawl:
            toCrawl, nextDepth = nextDepth, []
            depth += 1
    return crawled

def add_to_index( index, keyword, url ):
    for lst in index:
        if lst[ 0 ] == keyword:
            lst[ 1 ].append( url )
            return
    index.append( [ keyword, [ url ] ] )

def lookup( index, keyword ):
    for item in index:
        if item[ 0 ] == keyword:
            return item[ 1 ]
    return []
