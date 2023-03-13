# `Ingredient()`を継承する別の子クラスを作成します。自分で
# 記述したコードを使用しても、以下に示すコードで作業を続けてもかまいません。
# 子クラスに少なくとも1つの追加メソッドを実装し、親である
# `Ingredient()`クラスの`expire()`メソッドをオーバーライドします。

class Ingredient:
    """材料をモデル化します。"""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """材料を期限切れにします。"""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """料理に味付けするスパイスをモデル化します。"""

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

