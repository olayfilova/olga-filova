class ExampleClass:

    def __init__(self):
        self.a =10
        self._b=1
        self.__c=1


    def met(self):
        self.__private()
        self._protected()
        return "Hello"

    def __private(self):
        return "Hidden"

    def _protected(self):
        return "Protected"



e= ExampleClass()
e.met()
# e.__private() ## --ERROR PRIVATE
e._protected()
e.a #     --PUBLIC
e._b #    --PROTECTED
#e.__c #  -- PRIVATE

print(e.met())



