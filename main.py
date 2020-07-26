class PassParams:
    def __init__(self, varsInit, pageView, btnClick1, btnClick2, btnClick3, keyboard, globalInclude):
        self.value = {
            "vars": varsInit,
            "view": pageView,
            "Btn1": btnClick1,
            "Btn2": btnClick2,
            "Btn3": btnClick3,
            "KeyB": keyboard,
            "global": globalInclude
        }
    def current(self):
        return self.value

class export:
  PassParams = PassParams
