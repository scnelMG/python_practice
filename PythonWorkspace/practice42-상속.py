#일반 유닛
class Unit: #부모 class
    def __init__(self, name, hp): 
        self.name = name 
        self.hp = hp
        
#공격 유닛
class AttackUnit(Unit): #자식 class
    def __init__(self, name, hp, damage): 
        Unit.__init__(self, name, hp)
        self.damage = damage    

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격 합니다. [공격력 {}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{} : 파괴되었습니다.".format(self.name))
# 메딕: 의무병
# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
# 드랍쉽 : 공중 유닛, 수송기, 다른 유닛들을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, \
            self.flying_speed))
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")