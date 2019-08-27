###
##
#
# 計算を行う系のクラス群をまとめたPythonファイル
# 作成者：今井 裕一
# 作成日：2019/07/28
# 更新者：今井 裕一
# 更新日：2019/08/04
#
##
###

"""
四則演算を行うクラス
更新者：今井 裕一
更新日：2019/08/04
コンストラクタ：自身の説明用文字列初期化
"""
class arithmeticOperations():
    def __init__(self,):
        self.readMeMessage = "このクラスは四則演算を行うクラスです。"

    """
    加算メソッド
    self：クラス自身さすオブジェクト
    num：加算対象の値
    """
    def addition(self, *num):
        result = 0
        for add_param in num:
            result += add_param
        return result

    """
    減算メソッド
    self：クラス自身さすオブジェクト
    num：減算対象の値
    """
    def subtraction(self, *num):
        result = 0
        for sub_param in num:
            result -= sub_param
        return result

    """
    乗算メソッド
    self：クラス自身さすオブジェクト
    num：乗算対象の値
    """
    def multiplication(self, *num):
        result = 1
        for multi_param in num:
            result *= multi_param
        return result

    """
    余算メソッド
    self：クラス自身さすオブジェクト
    num：余算対象の値
    """
    def division(self, *num):
        result = 0
        for divi_param in num:
            result /= divi_param
        return result


"""
フィボナッチ数列計算行うクラス
更新者：今井 裕一
更新日：2019/08/04
コンストラクタ：自身の説明用文字列初期化
"""
class fibonacci():
    def __init__(self,):
        self.readMeMessage = "このクラスはフィボナッチ数列計算を行うクラスです。"