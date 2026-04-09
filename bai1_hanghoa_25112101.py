from abc import ABC, abstractmethod

# -------------------------------------------------------------------
# 1. CUSTOM EXCEPTION (Ngoại lệ tự định nghĩa)
# Áp dụng để xử lý các lỗi nghiệp vụ (VD: Giá tiền bị âm)
# -------------------------------------------------------------------
class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f"Loi: Gia '{gia}' khong hop le (phai >= 0).")

# -------------------------------------------------------------------
# 2. ABSTRACT BASE CLASS (Lớp trừu tượng)
# Đảm bảo không ai có thể tạo trực tiếp đối tượng từ lớp HangHoa
# -------------------------------------------------------------------
class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.__ma_hang = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx = nha_sx
        # Gọi setter của thuộc tính 'gia' để chạy qua bước Validate dữ liệu
        self.gia = gia  

    # --- @property: Đóng gói dữ liệu (Encapsulation) an toàn ---
    @property
    def ma_hang(self): 
        return self.__ma_hang
    
    @property
    def ten_hang(self): 
        return self.__ten_hang
    
    @property
    def nha_sx(self): 
        return self.__nha_sx

    @property
    def gia(self):
        return self.__gia

    @gia.setter
    def gia(self, value):
        # Validate dữ liệu: Ném ra Custom Exception nếu giá âm
        if value < 0:
            raise GiaKhongHopLe(value)
        self.__gia = value

    # --- @abstractmethod: Ép buộc các lớp con phải ghi đè (Override) ---
    @abstractmethod
    def loai_hang(self):
        pass

    def in_thong_tin(self):
        return (f"[{self.loai_hang()}] Ma: {self.__ma_hang} | "
                f"{self.__ten_hang} | NSX: {self.__nha_sx} | Gia: {self.gia:,.0f} VND")

    # --- MAGIC METHODS (Dunder methods) ---
    def __str__(self):
        # Tự động gọi khi dùng hàm print() trên đối tượng
        return self.in_thong_tin()

    def __repr__(self):
        # Đại diện chi tiết của đối tượng (hữu ích khi debug hoặc lưu file)
        return (f"{self.__class__.__name__}('{self.__ma_hang}', "
                f"'{self.__ten_hang}', '{self.__nha_sx}', {self.gia})")

    def __eq__(self, other):
        # Định nghĩa cách so sánh bằng (==) dựa trên mã hàng
        if not isinstance(other, HangHoa): return False
        return self.__ma_hang == other.ma_hang

    def __lt__(self, other):
        # Định nghĩa cách so sánh bé hơn (<) để dùng được hàm sorted()
        return self.gia < other.gia

    def __hash__(self):
        # Cần thiết khi dùng __eq__ để có thể đưa đối tượng vào cấu trúc Set (loại trùng lặp)
        return hash(self.__ma_hang)

# -------------------------------------------------------------------
# 3. CÁC LỚP CON (Kế thừa và Ghi đè)
# -------------------------------------------------------------------
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia) # Gọi hàm khởi tạo lớp cha
        self.__tg_baohanh = tg_baohanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    # Ghi đè phương thức thuần ảo của lớp cha
    def loai_hang(self):
        return "Dien may"

    # Ghi đè phương thức thường để nối thêm thông tin riêng
    def in_thong_tin(self):
        return (f"{super().in_thong_tin()} | BH: {self.__tg_baohanh} thang "
                f"| {self.__dien_ap}V - {self.__cong_suat}W")

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyenlieu = loai_nguyenlieu

    def loai_hang(self):
        return "Sanh su"

    def in_thong_tin(self):
        return f"{super().in_thong_tin()} | Chat lieu: {self.__loai_nguyenlieu}"

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_hethan = ngay_hethan

    def loai_hang(self):
        return "Thuc pham"

    def in_thong_tin(self):
        return f"{super().in_thong_tin()} | SX: {self.__ngay_sx} | HSD: {self.__ngay_hethan}"

# -------------------------------------------------------------------
# 4.DEMO 
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Khởi tạo đối tượng
    sp1 = HangDienMay("DM01", "Tu lanh LG", "LG", 12000000, 24, 220, 150)
    sp2 = HangSanhSu("SS01", "Binh hoa", "Minh Long", 350000, "Su cao cap")
    sp3 = HangThucPham("TP01", "Sua tuoi", "Vinamilk", 32000, "01/01/2025", "01/07/2025")

    kho_hang = [sp1, sp2, sp3]

    print("--- 1. IN DANH SACH (Da hinh & Magic method __str__) ---")
    for sp in kho_hang:
        print(sp) # Tự động gọi __str__

    print("\n--- 2. SAP XEP THEO GIA (Tu dong hoat dong nho __lt__) ---")
    for sp in sorted(kho_hang):
        print(f"{sp.gia:>12,.0f} VND | {sp.ten_hang}")

    print("\n--- 3. KIEM TRA TRUNG LAP (__eq__ & __hash__) ---")
    sp1_copy = HangDienMay("DM01", "Tu lanh LG Copy", "LG", 12000000, 24, 220, 150)
    print(f"Trang thai sp1 == sp1_copy (cung Ma): {sp1 == sp1_copy}")
    
    danh_sach_cung = [sp1, sp2, sp1_copy]
    # Set sẽ tự động loại bỏ sp1_copy vì nó nhận diện là giống sp1 nhờ __eq__ và __hash__
    print(f"So luong truoc khi dung Set: {len(danh_sach_cung)} -> Sau khi dung Set: {len(set(danh_sach_cung))}")

    print("\n--- 4. KIEM TRA NGOAI LE & VALIDATION ---")
    try:
        sp_loi = HangDienMay("DM99", "TV Hong", "Sony", -50000, 12, 220, 50)
    except GiaKhongHopLe as e:
        print(f"Bat loi Custom Exception: {e}")

    try:
        h = HangHoa("X", "Loi tao Abstract", "Y", 100)
    except TypeError as e:
        print(f"Bat loi khoi tao ABC: {e}")

    print("\n--- 5. XUAT FILE AN TOAN (Dung Context Manager 'with') ---")
    # Sử dụng 'with' đảm bảo file luôn được đóng an toàn sau khi ghi xong
    with open("kho_hang.txt", "w", encoding="utf-8") as f:
        for sp in kho_hang:
            f.write(repr(sp) + "\n") # Dùng repr() để lưu cú pháp khởi tạo
    print(f"Da luu {len(kho_hang)} san pham vao file 'kho_hang.txt'.")