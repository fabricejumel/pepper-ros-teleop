
#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use setExternalCollisionProtectionEnabled Method"""

import qi
import argparse
import sys


def main(session):
    """
    This example uses the setExternalCollisionProtectionEnabled method.
    """
    # Get the service ALMotion.

    motion_service  = session.service("ALMotion")

    motion_service.setOrthogonalSecurityDistance(0.05)
    motion_service.setTangentialSecurityDistance(0.05)
    print ("OrthogonalSecurity set to" + str(motion_service.getOrthogonalSecurityDistance()) +"," + "TangentialSecurity set to" + str(motion_service.getOrthogonalSecurityDistance()))
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
