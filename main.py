#!/usr/bin/python3

import sys, os
import docker

def main():
    client = docker.from_env()

    pwd = os.getcwd()
   
    output = client.containers.run(image = "debian:stretch", 
                                   command = "echo {}".format(pwd),
                                   auto_remove = True)

    print(output)


if __name__ == '__main__':
    sys.exit(main())
