import math

class Diem:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class HinhChuNhat:
    def __init__(self, goc_duoi, rong, cao):
        self.goc = goc_duoi  
        self.rong = rong
        self.cao = cao

class HinhTron:
    def __init__(self, tam, ban_kinh):
        self.tam = tam       
        self.bk = ban_kinh

def tinh_khoang_cach(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def kiem_tra_diem(tron, diem):
    """Kiem tra mot diem co nam trong hinh tron hay khong."""
    khoang_cach = tinh_khoang_cach(tron.tam, diem)
    return khoang_cach <= tron.bk

def hcn_trong_tron(tron, hcn):
    """Tra ve True neu ca 4 goc cua HCN deu nam trong hinh tron."""
    x, y = hcn.goc.x, hcn.goc.y
    w, h = hcn.rong, hcn.cao
    cac_goc = [
        Diem(x, y),
        Diem(x + w, y),
        Diem(x, y + h),
        Diem(x + w, y + h)
    ]
    return all(kiem_tra_diem(tron, p) for p in cac_goc)

def hcn_cham_tron(tron, hcn):
    """Tra ve True neu co it nhat 1 goc cua HCN nam trong hinh tron."""
    x, y = hcn.goc.x, hcn.goc.y
    w, h = hcn.rong, hcn.cao
    
    cac_goc = [
        Diem(x, y),
        Diem(x + w, y),
        Diem(x, y + h),
        Diem(x + w, y + h)
    ]
    
    return any(kiem_tra_diem(tron, p) for p in cac_goc)

# --- TEST ---
print("--- 🔵 KIEM TRA HINH HOC 🔴 ---")

my_circle = HinhTron(Diem(150, 100), 75)

#1
p_trong = Diem(160, 110)
p_ngoai = Diem(300, 300)
print(f"📍 Diem (160, 110) trong hinh tron: {'✅' if kiem_tra_diem(my_circle, p_trong) else '❌'}")
print(f"📍 Diem (300, 300) trong hinh tron: {'✅' if kiem_tra_diem(my_circle, p_ngoai) else '❌'}")

#2 
hcn_nho = HinhChuNhat(Diem(140, 90), 10, 10)
hcn_to = HinhChuNhat(Diem(100, 50), 300, 200)

print(f"🖼️  HCN nho nam gon trong tron: {'✅' if hcn_trong_tron(my_circle, hcn_nho) else '❌'}")
print(f"🖼️  HCN to co giao voi hinh tron: {'✅' if hcn_cham_tron(my_circle, hcn_to) else '❌'}")