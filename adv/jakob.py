import adv.adv_test
from core.advbase import *
from slot.d import *

def module():
    return Jakob

class Jakob(Adv):
    a1 = ('prep','50%')

    conf = {}
    conf['acl'] = """
        `s1
        `s3,fsc
        `fs,seq=5
        """
    conf['slot.d'] = DJ()
    conf['afflict_res.bog'] = 100

    def s1_proc(this, e):
        this.dmg_make('s1',2.27)
        this.afflics.bog.on('s1', 90)
        this.dmg_make('s1',4.54)

if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf, verbose=0, mass=0)

