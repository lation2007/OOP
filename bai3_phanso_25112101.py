from math import gcd

# -------------------------------------------------------------------
# 1. CUSTOM EXCEPTION
# -------------------------------------------------------------------
class MauSoBangKhong(Exception):
    """Ngoại lệ ném ra khi người dùng cố tình nhập mẫu số bằng 0."""
    def __init__(self):
        super().__init__("Loi: Mau so phai khac 0.")

# -------------------------------------------------------------------
# 2. LỚP PHAN SO
# -------------------------------------------------------------------
class PhanSo:
    def __init__(self, tu=0, mau=1):
        # Gọi setter để thực hiện kiểm tra mẫu số ngay khi khởi tạo
        self.tu_so = tu
        self.mau_so = mau

    # --- Properties & Validation ---
    @property
    def tu_so(self):
        return self.__tu

    @tu_so.setter
    def tu_so(self, value):
        self.__tu = int(value)

    @property
    def mau_so(self):
        return self.__mau

    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong()
        self.__mau = int(value)

    # --- Xử lý tối giản ---
    def toi_gian(self):
        """Trả về một đối tượng PhanSo mới đã được tối giản."""
        ucln = gcd(abs(self.__tu), abs(self.__mau))
        moi_tu = self.__tu // ucln
        moi_mau = self.__mau // ucln
        
        # Đảm bảo dấu âm luôn nằm ở tử số nếu có
        if moi_mau < 0:
            moi_tu, moi_mau = -moi_tu, -moi_mau
            
        return PhanSo(moi_tu, moi_mau)

    def is_toi_gian(self):
        """Kiểm tra phân số hiện tại đã ở dạng tối giản chưa."""
        return gcd(abs(self.__tu), abs(self.__mau)) == 1

    # --- Nạp chồng toán tử ---
    def __add__(self, other):
        # a/b + c/d = (ad + bc) / bd
        tu = self.__tu * other.mau_so + other.tu_so * self.__mau
        mau = self.__mau * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __sub__(self, other):
        # a/b - c/d = (ad - bc) / bd
        tu = self.__tu * other.mau_so - other.tu_so * self.__mau
        mau = self.__mau * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __mul__(self, other):
        # a/b * c/d = (ac) / (bd)
        tu = self.__tu * other.tu_so
        mau = self.__mau * other.mau_so
        return PhanSo(tu, mau).toi_gian()

    def __truediv__(self, other):
        # a/b : c/d = (ad) / (bc)
        if other.tu_so == 0:
            raise ZeroDivisionError("Khong the chia cho phan so co tu bang 0.")
        tu = self.__tu * other.mau_so
        mau = self.__mau * other.tu_so
        return PhanSo(tu, mau).toi_gian()

    # --- So sánh ---
    def __eq__(self, other):
        # Hai phân số bằng nhau nếu tích chéo bằng nhau: a*d == b*c
        if not isinstance(other, PhanSo):
            return False
        return self.__tu * other.mau_so == other.tu_so * self.__mau

    def __lt__(self, other):
        # So sánh bé hơn dựa trên tích chéo (tránh sai số số thực)
        return self.__tu * other.mau_so < other.tu_so * self.__mau

    def __gt__(self, other):
        # So sánh lớn hơn
        return self.__tu * other.mau_so > other.tu_so * self.__mau

    def __hash__(self):
        # Hash dựa trên dạng tối giản để Set có thể loại bỏ phân số trùng giá trị
        ps = self.toi_gian()
        return hash((ps.tu_so, ps.mau_so))

    # --- Hiển thị ---
    def __str__(self):
        # Nếu mẫu bằng 1 thì chỉ in tử (số nguyên)
        if self.__mau == 1:
            return f"{self.__tu}"
        return f"{self.__tu}/{self.__mau}"

    def __repr__(self):
        return f"PhanSo({self.__tu}, {self.__mau})"

# -------------------------------------------------------------------
# 3.DEMO
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Khởi tạo dãy phân số
    danh_sach = [PhanSo(2, 4), PhanSo(3, 6), PhanSo(1, 3), PhanSo(5, 7)]

    print("--- 1. TOI GIAN PHAN SO ---")
    for ps in danh_sach:
        print(f"  {ps} -> Toi gian: {ps.toi_gian()} (Da toi gian? {ps.is_toi_gian()})")

    print("\n--- 2. PHEP TOAN (+, -, *, /) ---")
    p1 = PhanSo(1, 2)
    p2 = PhanSo(1, 3)
    print(f"  {p1} + {p2} = {p1 + p2}")
    print(f"  {p1} - {p2} = {p1 - p2}")
    print(f"  {p1} * {p2} = {p1 * p2}")
    print(f"  {p1} / {p2} = {p1 / p2}")

    print("\n--- 3. SAP XEP TANG DAN (Nho __lt__) ---")
    # Sắp xếp và in ra giá trị số thực để kiểm chứng
    for ps in sorted(danh_sach):
        print(f"  {str(ps.toi_gian()):<5} (Gia tri: {ps.tu_so/ps.mau_so:.3f})")
    print("\n--- 4. SO SANH & LOAI TRUNG (Set) ---")
    print(f"  2/4 == 3/6 ? -> {PhanSo(2, 4) == PhanSo(3, 6)}")
    
    trung_lap = [PhanSo(1, 2), PhanSo(2, 4), PhanSo(3, 6), PhanSo(5, 7)]
    print(f"  Danh sach goc: {trung_lap}")
    print(f"  Sau khi dung Set (loai trung): {list(set(trung_lap))}")

    print("\n--- 5. VALIDATION ---")
    try:
        ps_loi = PhanSo(1, 0)
    except MauSoBangKhong as e:
        print(f"  Bat loi thanh cong: {e}")