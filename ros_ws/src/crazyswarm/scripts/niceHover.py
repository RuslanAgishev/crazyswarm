#!/usr/bin/env python

import numpy as np
from pycrazyswarm import *

Z = 1.0

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    allcfs.takeoff(targetHeight=Z, duration=3.0+Z)
    timeHelper.sleep(1.5+Z)
    for cf in allcfs.crazyflies:
        cf.goTo(np.array([0.5,0.5,Z]), 0, 3.0)
    timeHelper.sleep(4)

    print("press button to continue...")
    swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=2.0+Z)
    timeHelper.sleep(2.0+Z)
