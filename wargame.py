#shuffleが使えるようにimport設定
from random import shuffle

#クラスCardを定義
class Card:

    #クラス変数suitsリストにマーク４種を入れる
    suits = ["spades","hearts","diamonds","clubs"]
    #クラスvaluesに数と絵柄を入れる、None二つで2で2が出るようにする
    values = [None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

    #初期化し引数にvalueとsuitをいれる
    def __init__ (self,value,suit):
        """スート（マーク）も値も整数値です"""

        #インスタンス変数valueにvalueを入れる
        self.value = value

        #インスタンス変数suitにsuitを入れる
        self.suit = suit

    #特殊メソッドltを定義し、引数にはc2を入れる
    def __lt__(self,c2):

        #もし、インスタンス変数valueが引数c2のvalueよりも小さいときはTrueを返す
        if self.value < c2.value:
            return True

        #もし、インスタンス変数valueが引数c2のvalueと同じである場合
        if self.value == c2.value:

            #もし、インスタンス変数suitが引数c2のsuitより小さいときはTrueを返す
            if self.suit < c2.suit:
                return True

            #それ以外はFalseを返す
            else:
                return False

        #それ以外はFalseを返す
        return False

    #特殊メソッドgtを定義し、引数にはc2を入れる
    def __gt__(self,c2):

        #もし、インスタンス変数valueが引数c2のvalueよりも大きいときはTrueを返す
        if self.value > c2.value:
            return True
        
        #もし、インスタンス変数valueが引数c2のvalueと同じである場合
        if self.value == c2.value:

            #もし、インスタンス変数suitが引数c2のsuitより大きいときはTrueを返す
            if self.suit > c2.suit:
                return True

            #それ以外はFalseを返す
            else:
                return False

        #それ以外はFalseを返す
        return False

    #特殊メソッドreprを定義する
    def __repr__(self):

        #クラス変数valueにクラス変数values内のインスタンス変数valueの値＋of+クラス変数suit内のインスタンス変数を足したものを入れる
        value = self.values[self.value] + "of" \
                + self.suits[self.suit]

        #valueを返す
        return value
 
#クラスDeckを定義する
class Deck:
    
    #初期化する
    def __init__(self):

        #インスタンス変数cardsに空のリストを入れる
        self.cards = []

        #2から15までの値を1つずつ取り出し変数iに入れる
        for i in range(2,15):
            #0から3まで四回分、値を1つずつ取り出し変数jに入れる
            for j in range(4):

                #インスタンス変数cardsにCard(i,j)の形で追加する
                self.cards.append(Card(i,j))

            #インスタンス変数cardsをシャッフルする
            shuffle(self.cards)

    #関数rm_cardを定義する　
    def rm_card(self):
        #もし、インスタンス変数の値が0の場合、
        if len(self.cards) == 0:
            #Noneを返す
            return
        #インスタンス変数cardsの最後の値を1つ抜き出し削除する
        return self.cards.pop()


#クラスPlayerを定義する
class Player:

    #初期化し、引数にnameを入れる
    def __init__(self,name):

        #インスタンス変数winsに0を入れる
        self.wins = 0
        #インスタンス変数cardにNoneを入れる
        self.card = None
        #インスタンス変数nameに引数のnameを入れる
        self.name = name

#クラスGameを定義する
class Game:
    
    #初期化する
    def __init__(self):

        #変数name1にプレイヤー１の名前とユーザー入力した内容を入れる
        name1 = input("プレイヤー1の名前")
        #変数name2にプレイヤー２の名前とユーザー入力した内容を入れる
        name2 = input("プレイナー2の名前")
        #インスタンス変数deckにクラスDeckを生成させ、入れる
        self.deck = Deck()
        #インスタンス変数p1にクラスplayer引数name1を入れる（入力した名前１が渡される
        self.p1 = Player(name1)
        #インスタンス変数p2にクラスplayer引数name2を入れる（入力した名前２が渡される
        self.p2 = Player(name2)

    #関数winsを定義し、引数にwinnerを入れる
    def wins(self,winner):

        #変数wに、「このラウンドは｛｝が勝ちました」を入れる
        w = "このラウンドは{}が勝ちました"
        #上記｛｝内に、引数winnerの値を入れ、wに入れ上書きする
        w = w.format(winner)
        #変数wを表示する
        print(w)

    #関数drawを定義し、引数に、p1n,p1c,p2n.p2cを入れる
    def draw(self,p1n,p1c,p2n,p2c):

        #変数dに、引きましたの文を入れる
        d = "{}は{}、{}は{}を引きました"
        #上記{}に、p1n,p1c,p2n,p2cを入れ、dに入れ上書きする
        d = d.format(p1n,p1c,p2n,p2c)

        #変数dを出力する
        print(d)

    #関数play_gameを定義する
    def play_game(self):

        #変数cardsに、インスタンス変数deck(=クラスDeck）のインスタンス変数cardsを入れる
        cards = self.deck.cards 

        #戦争を始ましょうを表示する
        print("戦争を始めましょう")

        #変数cardsの値が2以上ある場合回し続ける
        while len(cards) >= 2:

            #変数msgに「ｑで終了、それ以外のキーでPlay:」と表示する
            msg = "qで終了、それ以外のキーでPlay:"

            #変数responseに、msgの値を表示し、ユーザー入力を入れる
            response = input(msg)

            #もし変数responseがqであれば、その時点でループから外れる
            if response == "q":
                break

            #変数p1cに、クラスDeckのインスタンス変数rm_cardsを入れる
            p1c = self.deck.rm_card()
            #変数p2cに、クラスDeckのインスタンス変数rm_cardsを入れる
            p2c = self.deck.rm_card()
            #変数p1nに、Gameクラスのself.p1、Playerクラスの.nameを入れる
            p1n = self.p1.name
            #変数p2nに、Gameクラスのself.p2、Playerクラスの.nameを入れる
            p2n = self.p2.name

            #インスタンス変数drawにp1n,p1c,p2n,p2cを入れる
            self.draw (p1n,p1c,p2n,p2c)

            #もし、p1cがp2cより大きい場合、
            if p1c > p2c:

                #インスタンス変数p1のwinsに１を足す
                self.p1.wins += 1

                #インスタンス変数winsに、インスタンス変数p1のnameを入れる
                self.wins(self.p1.name)

            #そうでない場合
            else:
                #インスタンス変数p2のwinsに１を足す
                self.p2.wins +=1
                #インスタンス変数winsに、インスタンス変数p2のnameを入れる
                self.wins(self.p2.name)

        #変数winに、インスタンス変数winnerを入れ、引数はインスタンス変数p1とp2を入れる
        win = self.winner(self.p1,self.p2)
        #ゲーム終了、｛｝の勝利ですを表示し、{}には変数winの値を入れる
        print("ゲーム終了、{}の勝利です".format(win))

    #関数winnerを定義し、引数にp1とp2を入れる
    def winner(self,p1,p2):

        #もし、変数p1のwinsがp2よりも多い場合、
        if p1.wins > p2.wins:
            return p1.name
        #もし、変数p1のwinsがp2よりも少ない場合、
        if p1.wins < p2.wins:
            return p2.name
        #それ以外は、引き分けと表示する
        return "引き分け"

game = Game()
game.play_game()

    
