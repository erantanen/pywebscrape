"""\n scrape_http_header.py

  Scraping an http header.


  Usage: python scrape_http_header.py  -s <address>  "

    Arguments:
      -s  url scrape address


  Flags:
      -h      help

Version: 001

"""

import urllib.request
import sys
import getopt


def usage():
    print(__doc__)


def pars_cmd(argv):
    url_site = None

    if (len(sys.argv[1:]) != 0):

        try:
            opts, args = getopt.getopt(sys.argv[1:], "s:h")
        except getopt.GetoptError as err:
            # print help information and exit:
            print(err)  # will print something like "option -a not recognized"
            usage()
            sys.exit(2)

        # checks to see if opts(list) is empty

        if not opts:
            print("There were no options given use -h to see help\n")

        # parses opts and arguments
        for o, a in opts:

            if o in ("-h"):
                # help
                usage()
                exit()
            elif o in ("-s"):
                # pass phrase
                url_site = a

            else:
                assert False, "parse - unhandled option"
                # ...
                # change options check as needed.

    return url_site


def url_grab(site):
    try:
        with urllib.request.urlopen(site) as response:
            html = response.read()
            h_header = dict(response.info())
    except:
        print("not able to connect?")

    return h_header


def main():
    url_site = pars_cmd(sys.argv)

    if url_site is None:
        usage()
        exit()

    data = url_grab(url_site)

    for elm in data.items():
        print(elm)


if __name__ == "__main__":
    main()
