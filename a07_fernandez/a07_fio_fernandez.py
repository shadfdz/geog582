#######################################
# Name: Shad Fernandez
# RedID: 810466716
# Date: 14-OCT-2020
#######################################

# Q1

import os, sys # import necessary modules

class Ping():
    def __init__(self,hosts):
        for host in hosts:
            try:
                print("Ping: {}".format(host))
                res = os.system("ping {}".format(host))
            except Exception as e:
                print(e)
            finally:
                print("\t()".format(res))

class Ping_Looper():
    def __init__(self, hosts, num):
        flag = num;
        for host in hosts"
        try:
            print("Pinging ")

def main():
    hosts = sys.argv[1:]
    Ping(hosts)

if __name__ == "__main__":
    main()

# add 5 hosts as arguments 
# use pypi.org, anaconda.com, reddit.com, archive.org, ucsd.edu

# Q2

import contextlib, io

zen_io = io.StringIO()
with contextlib.redirect_stdout(zen_io):
    import this

zen_of_python = zen_io.getvalue()


