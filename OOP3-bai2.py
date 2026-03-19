class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def __str__(self):
        return f"Sieu nhan {self.ten} (Vu khi: {self.vu_khi}, Mau: {self.mau_sac})"

sn1 = SieuNhan("A", "kiem", "do")
sn2 = SieuNhan("B", "khien", "xanh")
print(sn1)
print(sn2)