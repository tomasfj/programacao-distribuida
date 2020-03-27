import requests
import queue
import threading

websites = queue.Queue(maxsize = 0)

websites.put( 'http://envanto.com' )
websites.put( 'http://amazon.co.uk' )
websites.put( 'http://amazon.com' )
websites.put( 'http://facebook.com' )
websites.put( 'http://google.com' )
websites.put( 'http://google.fr' )
websites.put( 'http://google.es' )
websites.put( 'http://bing.com' )
websites.put( 'http://google.pt' )
websites.put( 'http://google.co.uk' )
websites.put( 'http://internet.org' )
websites.put( 'http://gmail.com' )
websites.put( 'http://stackoverflow.com' )
websites.put( 'http://github.com' )
websites.put( 'http://shopyfy.com' )
websites.put( 'http://instagram.com' )
websites.put( 'http://youtube.com' )
websites.put( 'http://twitter.com' )

def check_website( address, timeout = 5 ):
    try:
        response = requests.head( address, timeout = timeout )
        if response.status_code >= 400:
            raise Exception()
    except Exception:
        print( "Error: " + str(address) + " returns code: " + str(response.status_code) )


def worker(thread_name):
    
    while( websites.qsize() > 0 ):
        website = websites.get()
        print( 'Thread #' + str(thread_name) + ' visiting website ' + str(website) )
        check_website( website )
    
    print( 'Lista vazia' )


if __name__ == "__main__":
    # alterar numero de threads para 1, 2, 4 e 8
    n_threads = 8

    for i in range(n_threads):
        #t = threading.Thread( target = worker(str(i)) )
        t = threading.Thread( target = worker, args = (str(i)) )
        t.start()
        
    t.join()

    print( 'Exit main thread' )

# tempos de execução
# para 1 thread  - 0m3.469s
# para 2 threads - 0m2.011s
# para 4 threads - 0m1.891s
# para 8 threads - 0m0.861s