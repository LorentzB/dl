import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Chitose

class Chitose(Adv):
    a3 = ('a',-0.1)

    conf = {}
    conf['slot.a'] = Jewels_of_the_Sun()+A_Game_of_Cat_and_Boar()
    conf['slot.d'] = Daikokuten()
    conf['acl'] = """
        `s1
        `s3, seq=5
        """

    def init(this):
        if this.condition('buff all team'):
            this.s1_proc = this.c_s1_proc

    def c_s1_proc(this, e):
        Teambuff('s1',0.25,15).on()

    def s1_proc(this, e):
        Selfbuff('s1',0.25,15).on()

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=-2)

