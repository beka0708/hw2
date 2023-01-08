class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage

    def name_hero(self):
        return f'Hero name ==> {self.name}'

    def extra_health(self):
        self.health_points *= 2
        return self.health_points

    def __str__(self):
        return f'{self.nickname} {self.superpower} {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Naruto', 'Kurama', 'rasengan', 100, 'dattebayo', 75)


# print(hero.name_hero())
# print(hero.extra_health())
# print(hero.__len__())
# print(hero.__str__())
# print(hero.people)


class FriendHero(SuperHero):
    fly = False
    damage = False
    kunai = True

    def extra_health(self):
        self.health_points **= 2
        FriendHero.fly = True
        return self.health_points

    def __str__(self):
        super().__str__()
        return f'fly in the True_phrase'

    def crit(self):
        self.damage **= 2
        return self.damage


friend = FriendHero('Sakura', 'haruno', 'bakugo', 100, 'Shinnarooo', 60)
print(friend.extra_health())
print(friend.fly)
print(friend.__str__())


class BrotherHero(SuperHero):
    fly = False
    damage = False
    sword = True

    def extra_health(self):
        self.health_points **= 2
        BrotherHero.fly = True
        return self.health_points

    def __str__(self):
        super().__str__()
        return f'fly in the True_phrase'

    def crit(self):
        self.damage **= 2
        return self.damage


bro = BrotherHero('Sasuke', 'uchiha', 'chidori', 100, 'usuratonkachi', 60)
print(bro.extra_health())
print(BrotherHero.fly)
print(bro.__str__())


class Villain(BrotherHero, FriendHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2
        return self.damage

    # def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
    #     super().__init__(name, nickname, superpower, health_points, catchphrase)
    #     self.damage = damage


vil = Villain('Madara', 'Uchiha', 'susano', 120, 'Lets go dance', 70)
print(vil.crit())
print(bro.crit())
print(friend.crit())
