import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = "radio://0/80/2M/E7E7E7E501"


def with_mc(f):
    def with_mc():
        with SyncCrazyflie(URI, cf=Crazyflie(rw_cache="./cache")) as scf:
            with MotionCommander(scf) as mc:
                f(mc)

    return with_mc


@with_mc
def sequence(mc: MotionCommander):
    time.sleep(3)

    mc.up(0.5)
    mc.circle_right(0.3, 0.3)
    mc.circle_left(0.3, 0.3)
    mc.down(0.5)
    mc.stop()


def main():
    cflib.crtp.init_drivers()
    sequence()


if __name__ == "__main__":
    main()
