import os
import time

class AndroidEmulator:
    
    @staticmethod
    def run(runnable):
        AndroidEmulator._start()
        result = runnable()
        AndroidEmulator._stop()
        return result
    
    @staticmethod
    def _start():
        os.system("/home/frankknoll/Android/Sdk/emulator/emulator -avd Pixel_2_API_30 -no-window &")
        AndroidEmulator._waitUntilStarted()
        
    @staticmethod
    def _waitUntilStarted():
        while not AndroidEmulator._isStarted():
            time.sleep(1)

    @staticmethod
    def _isStarted():
        boot_completed = ! adb shell getprop sys.boot_completed
        return boot_completed[0] == '1'

    @staticmethod
    def _stop():
        ! adb emu kill