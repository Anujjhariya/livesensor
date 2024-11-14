from sensor.exception import SensorException
import os
import sys

from sensor.logger import logging


def test_exception():
    try:
        logging.info("bhaiya yaha prr ek error division by zero error ane vali he")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys) #this is the class we created for Raising the error in proper given format




if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)

