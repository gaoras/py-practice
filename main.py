class Calculate:
    """
    計算用のクラス
    """
    # クラス属性
    PI = 3.14159265358979

    def __init__(self):
        """
        初期化
        """
        # メンバ変数
        self.a = 100
        print("init")

    def add(self,x,y):
        """
        加算を行います
        """
        return x+y
    
    @staticmethod
    def sadd(x,y):
        """
        static method test
        """
        return x+y


c = Calculate()
n = c.a
x = 5
y = 3
#n = c.add(x,y)
n = Calculate.sadd(x,y)
print(n)