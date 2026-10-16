import math


def gia_don_vi(duong_kinh_cm, gia_usd):
    bk_cm = duong_kinh_cm / 2
    dt_cm2 = math.pi * bk_cm ** 2
    dt_m2 = dt_cm2 / 10000  
    return gia_usd / dt_m2


def main():
    print("Pizza 1")
    d1 = float(input("Nhập đường kính (cm): "))
    p1 = float(input("Nhập giá (USD): "))

    print("Pizza 2")
    d2 = float(input("Nhập đường kính (cm): "))
    p2 = float(input("Nhập giá (USD): "))

    gia1 = gia_don_vi(d1, p1)
    gia2 = gia_don_vi(d2, p2)

    print(f"Pizza 1: {gia1:.2f} USD/m²")
    print(f"Pizza 2: {gia2:.2f} USD/m²")

    if gia1 < gia2:
        print("Pizza 1 có giá trị tốt hơn (rẻ hơn trên mỗi mét vuông).")
    elif gia2 < gia1:
        print("Pizza 2 có giá trị tốt hơn (rẻ hơn trên mỗi mét vuông).")
    else:
        print("Hai pizza có giá trị như nhau.")


main()