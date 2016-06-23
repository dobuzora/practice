# サイコロ1
# 6/23

# サイコロのクラス
class Dice :
    def __init__(self,num):
        self.num = num

    def move_E(self):
        self.copy = self.num.copy() 
        for i,j in zip([0,2,5,3],[3,0,2,5]):
            self.num[i] = self.copy[j]

    def move_W(self):
        self.copy = self.num.copy()
        for i,j in zip([0,3,5,2],[2,0,3,5]):
            self.num[i] = self.copy[j]

    def move_N(self):
        self.copy = self.num.copy()
        for i,j in zip([0,1,5,4],[1,5,4,0]):
            self.num[i] = self.copy[j]

    def move_S(self):
        self.copy = self.num.copy()
        for i,j in zip([0,1,5,4],[4,0,1,5]):
            self.num[i] = self.copy[j]



number = list(map(int,input().split()))
#number = [1,2,4,8,16,32]
#print("1 2 3 4 5 6")
# サイコロを作成
dice = Dice(number)

for order in input():
    if order == 'S':
        dice.move_S()
    elif order == 'N':
        dice.move_N()
    elif order == 'W':
        dice.move_W()
    else:
        dice.move_E()

# サイコロの状態を出力
#print(dice.num)

print(dice.num[0])


# 別解1
# 仕組みは同じだが、こちらのほうが無駄がない
# 私はサイコロシュミレーションメソッドを4つ作ったが
# 一つのほうが条件も含めて無駄がないことがわかった
class Dice:
    def __init__(self, data):
        self.data = data
     
    def move(self, direction):
        if direction == 'E':
            self.data[0], self.data[3], self.data[5], self.data[2] = \
                self.data[3], self.data[5], self.data[2], self.data[0]
        elif direction == 'N':
            self.data[0], self.data[4], self.data[5], self.data[1] = \
                self.data[1], self.data[0], self.data[4], self.data[5]
        elif direction == 'S':
            self.data[0], self.data[1], self.data[5], self.data[4] = \
                self.data[4], self.data[0], self.data[1], self.data[5]
        elif direction == 'W':
            self.data[0], self.data[2], self.data[5], self.data[3] = \
                self.data[2], self.data[5], self.data[3], self.data[0]
 
    def getTop(self):
        return self.data[0]
 
dice = Dice(input().split())
cmd = input()
for i in range(len(cmd)):
    dice.move(cmd[i])
print(dice.getTop())
