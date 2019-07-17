import adv_test
from adv import *
from slot.a import *
from slot.d import *
import random


def module():
    return Rena

class Rena(Adv):

    def pre(this):
        if this.condition('0 burn resist'):
            this.burnresist = 0
        else:
            this.burnresist = 40

    def init(this):
        this.a1_iscding = 0
        this.stance = 0
        this.s1_burn = Dot('o_s1_burn',0.97,12,3.9)
        random.seed()

    
    def s1_proc(this, e):
        if this.burnresist < 100:
            if random.random() < (120.0-this.burnresist)/100:
                if this.s1_burn.on():
                    this.burnresist += 20
        if this.stance == 0:
            this.stance = 1
        elif this.stance == 1:
            this.stance = 2
            Selfbuff('s1crit',0.1,15,'crit','chance').on()
        elif this.stance == 2:
            this.stance = 0
            Selfbuff('s1crit',0.1,15,'crit','chance').on()
            if this.s1_burn.get():
                this.dmg_make("o_s1_boost",this.conf.s1.dmg*0.8)



    def s2_proc(this, e):
        this.s1.charge(this.s1.sp)

    def a1_cooldown(this, t):
        this.a1_iscding = 0
        log('cd','a1','end')

    def a1_act(this):
        #logcat()
        #print this.a1_iscding
        #exit()
        if not this.a1_iscding :
            this.a1_iscding = 1
            Timer(this.a1_cooldown).on(15)
            log('cd','a1','start')
            Selfbuff('a1',0.15,10,'def').on()
            #Teambuff('db_test',0.10,15).on()
            Event('defchain')()
        else:
            log('cd','a1','trigger failed')

    def charge(this, name, sp):
        if this.s1.check():
            return Adv.charge(this, name, sp)
        r = Adv.charge(this, name, sp)
        if this.s1.check():
            this.a1_act()
        return r


if __name__ == '__main__':
    module().comment = 'Sakuya'
    conf = {}
    conf['slot.d'] = Sakuya()
    conf['slot.a'] = RR()+FRH()
    conf['acl'] = """
        `s1
        `s2, s=1
        `s3, fsc
        `fs, seq=5
        """

    adv_test.test(module(), conf, verbose=0, duration=120, mass=1)
    #logcat(['cd'])
