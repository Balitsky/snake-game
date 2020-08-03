class PercentageUtil:
    def convert(arg1: str, arg2: float):
        arg1 = float(arg1.strip('%')) / 100
        return arg1 * arg2


result = PercentageUtil.convert("10%", 50)
print(result)
