from random import *

#일반 유닛
class Unit: #부모 class
    def __init__(self, name, hp, speed): 
        self.name = name 
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name,\
             location, self.speed))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{} : 파괴되었습니다.".format(self.name))    
        
#공격 유닛
class AttackUnit(Unit): #자식 class
    def __init__(self, name, hp, speed,  damage): 
        Unit.__init__(self, name, hp, speed)
        self.damage = damage    

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격 합니다. [공격력 {}]"\
            .format(self.name, location, self.damage))
#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -=10
            print("{} : 스팀팩을 사용합니다. (HP 10 감소".format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용할수없습니다.".format(self.name))

#탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가
    seize_developed = False # 시즈모드 업글 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35) 
        self.seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 현재 시즈모드가 아닐 때 ->시즈모드
        if self.seize_mode == False:
            print("{} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드 일 때  -> 시즈모드 해제
        else:
            print("{} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

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
        AttackUnit.__init__(self, name, hp, 0,  damage) #지상 속도 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20 ,5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True: 
            print("{} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{} : 클로킹 모드 실행합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Oking : gg")
    print("[Oking] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 =Wraith()

# 유닛 일괄 관리 (유닛 드래그한 상태)
attack_Units = []
attack_Units.append(m1)
attack_Units.append(m2)
attack_Units.append(m3)
attack_Units.append(t1)
attack_Units.append(t2)
attack_Units.append(w1)

# 전군 이동
for unit in attack_Units:
    unit.move("1시")

# 탱크 시즈모드 업글 완료
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 업그레이드 완료")

# 전투 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_Units:
    if isinstance(unit, Marine):
        unit.stimpack
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_Units:
    unit.attack("1시")

# 전투 중 피해
for unit in attack_Units:
    unit.damaged(randrange(5, 21)) # 공격은 랜덤으로 받음 (5~ 20)

# 게임 종료
game_over()
