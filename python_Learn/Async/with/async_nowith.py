import time

class Timer:
    def start(self):
        self.t0 = time.perf_counter()
    def stop(self):
        print(f"{time.perf_counter() - self.t0:.3f}s 経過")

timer = Timer()
timer.start()
time.sleep(1.5)
timer.stop()