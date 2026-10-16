#Viết một hàm yêu cầu người dùng nhập giới tính sinh học và giá trị hemoglobin (g/l). 
# Chương trình sau đó sẽ thông báo cho người dùng biết giá trị hemoglobin thấp, bình thường hay cao.

#Nồng độ hemoglobin bình thường ở nữ giới trưởng thành nằm trong khoảng 117-155 g/l.
#Nồng độ hemoglobin bình thường ở nam giới trưởng thành nằm trong khoảng 134-167 g/l.
def nong_do_hemoglobin ():
    gender= str(input("nhap gioi tinh"))
    hml= int(input("nhap noong độ hemoglobin"))
    if gender == "male":
        if 167>=hml >=134:
            print(" nông độ hemoglobin bình thường")
        elif hml > 167:
            print("cao")
        elif hml <134:
            print("thấp")
    elif gender == "female":
        if 117>=hml>=155:
            print(" nồng độ hemoglobin bình thường")
        elif hml>155:
            print("cao")
        elif hml<117:
            print("thấp")
    
nong_do_hemoglobin()