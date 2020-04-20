from core.advbase import *
from module.bleed import Bleed
from slot.a import *

def module():
    return Ieyasu

class Ieyasu(Adv):
    a1 = ('cc',0.13,'hp70')
    a2 = ('cd',0.3)

    conf = {}
    conf['slots.a'] = RR()+United_by_One_Vision()
    conf['acl'] = """
        `dragon.act("c3 s end")
        `s3, not self.s3_buff
        `s1, x=4 and self.s3_buff
        `s2, x=5
        """
    coab = ['Wand','Dagger','Axe2']

    def d_coabs(self):
        if 'sim_afflict' in self.conf and self.conf.sim_afflict.efficiency > 0:
            self.coab = ['Wand','Bow','Axe2']

    def s2ifbleed(self):
        if self.bleed._static['stacks'] > 0:
            return self.s2buff.get()
        return 0

    def prerun(self):
        random.seed()
        self.s2buff = Selfbuff("s2",0.20,15,'crit')
        self.s2buff.modifier.get = self.s2ifbleed
        self.bleed = Bleed("g_bleed",0).reset()
        self.s2charge = 0

    def s1_proc(self, e):
        with Modifier("s1killer", "poison_killer", "hit", 0.2):
            self.dmg_make("s1", 12.40)
            Bleed("s1", 1.46).on()

    def s2_proc(self, e):
        self.s2buff.on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)