from __future__ import absolute_import
import pickle
from countdown import Countdown

if __name__ == '__main__':
    # c = Countdown(10)
    # # After a few moments
    # time.sleep(3)
    # f = open('cstate.p', 'wb')
    #
    # pickle.dump(c, f)
    # f.close()
    # time.sleep(10)
    # print("--------")
    f = open('cstate.p', 'rb')
    print(pickle.load(f))
