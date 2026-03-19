import math
class Diem:
    def __init__(self, hoanh_do, tung_do):
        self.x = hoanh_do
        self.y = tung_do

    def thong_tin(self):
        print(f"Toa do hien tai: ({self.x}, {self.y})")

    def tim_doi_xung(self):
        return Diem(-self.x, -self.y)

    def tinh_khoang_cach_O(self):
        return math.sqrt(self.x**2 + self.y**2)

    def khoang_cach_nhau(self, diem_khac):
        dx = self.x - diem_khac.x
        dy = self.y - diem_khac.y
        return math.sqrt(dx**2 + dy**2)

A = Diem(3, 4)
print("Diem A:")
A.thong_tin()

nhap_x = int(input("Nhap x cho diem B: "))
nhap_y = int(input("Nhap y cho diem B: "))
B = Diem(nhap_x, nhap_y)
print("Diem B:")
B.thong_tin()

C = B.tim_doi_xung()
print("Diem C (Doi xung voi B qua O):")
C.thong_tin()

kc_B_O = B.tinh_khoang_cach_O()
print(f"Khoang cach tu B den goc O: {kc_B_O:.2f}")

kc_A_B = A.khoang_cach_nhau(B)
print(f"Khoang cach giua hai diem A va B: {kc_A_B:.2f}")