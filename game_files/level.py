import os

class Level:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.maps = []
    def load(self, stage):

        with open(os.getcwd()+"/game_files/level/{}.txt".format(stage)) as f:
            for line in f:
                for i in line:
                    if (i == "1"):
                        self.maps.append((self.x, self.y))
                    self.x+=40

                self.x = 0
                self.y+=40


        return self.maps

if (__name__ == "__main__"):
    level = Level()
    print(level.load(1))
