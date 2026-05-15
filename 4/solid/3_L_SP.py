class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print('I can Fly')
class Penguin(Bird):
    def fly(self):
        print('Sorry, I can\'t fly :(')

p = Penguin()
p.fly()
