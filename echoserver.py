def calculate_bmi(weight, height):
    """
    計算 BMI 的函數
    :param weight: 體重（公斤）
    :param height: 身高（公尺）
    :return: BMI 值
    """
    bmi = weight / (height ** 2)
    return bmi

def main():
    # 輸入體重和身高
    weight = float(input("請輸入您的體重（公斤）："))
    height = float(input("請輸入您的身高（公尺）："))

    # 計算 BMI
    bmi = calculate_bmi(weight, height)

    # 輸出 BMI 結果
    print(f"您的 BMI 值為：{bmi:.2f}")

    # 判斷 BMI 所屬範圍
    if bmi < 18.5:
        print("體重過輕")
    elif 18.5 <= bmi < 24.9:
        print("體重正常")
    elif 25 <= bmi < 29.9:
        print("體重過重")
    else:
        print("肥胖")

if __name__ == "__main__":
    main()