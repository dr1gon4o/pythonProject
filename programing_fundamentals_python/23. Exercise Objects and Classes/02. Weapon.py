class Weapon:
    # amm = 0

    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets >= 1:
            self.bullets -= 1
            return "shooting..."
        if self.bullets == 0:
            return "no bullets left"
        # self.amm +=1

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
