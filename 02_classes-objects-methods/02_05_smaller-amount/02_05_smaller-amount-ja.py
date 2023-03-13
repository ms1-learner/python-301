# `Ingredient()`の__add__メソッドを更新して、
# 新しいIngredient()オブジェクトを数量1でインスタンス化する代わりに、
# 渡された材料のうち、少ない方の数量を受け取るように変更します
#
# 例:
# c = Ingredient("carrot", 5)
# p = Ingredient("pea", 4)
# s = c + p
# print(s)
# >>>出力: carrotpea (4)

class Ingredient:
    """材料として使用する食品をモデル化します。"""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """材料を期限切れにします。"""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __add__(self, other):
        """2つの材料を組み合わせます。"""
        new_name = self.name + other.name
        return Ingredient(name=new_name, amount=1)
    
    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"


if __name__ == '__main__':
    c = Ingredient("carrot", 5)
    p = Ingredient("pea", 4)
    s = c + p
    print(s)
