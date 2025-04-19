# barbaraLiskov DuckTyping


class Birds:
    def fly(self):
        raise NotImplementedError
    def voice(self) -> str:
        return 'tweet'


class FlyingBirds(Birds):
    def fly(self):
        return "I can fly"


class Duck(FlyingBirds, Birds):
    ...
    def voice(self) -> str:
        return 'quack'


class Pinguin(Birds):
    def fly(self):
        raise NotImplementedError

    def voice(self) -> list:
        return ['tweet','roar']


def make_bird_fly(bird: Birds):
    print(f"Fly {bird.__class__.__name__}, you can")
    bird.fly()


def loud_voice(bird: Birds):
    return bird.voice().upper() # as a result to corruption
    # the Liskov substitution, list on the child class Pinguin
    # has no upper method

make_bird_fly(Pinguin())

d = Duck()
