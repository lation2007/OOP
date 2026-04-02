class HangHoa:
    def __init__(self, ma, ten, nsx):
        self.__ma = ma
        self.__ten = ten
        self.__nsx = nsx

    def thong_tin_co_ban(self):
        print(f"Ma hang: {self.__ma}")
        print(f"Ten hang: {self.__ten}")
        print(f"Nha SX: {self.__nsx}")


class HangDienMay(HangHoa):
    def __init__(self, ma, ten, nsx, gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(ma, ten, nsx)
        self.__gia = gia
        self.__bh = bao_hanh
        self.__vol = dien_ap
        self.__watt = cong_suat

    def hien_thi(self):
        print("--- [ HÀNG ĐIỆN MÁY ] ---")
        super().thong_tin_co_ban()
        print(f"Gia ban: {self.__gia:,.0f} VND")
        print(f"Bao hanh: {self.__bh} thang")
        print(f"Thong so: {self.__vol}V - {self.__watt}W")

class HangSanhSu(HangHoa):
    def __init__(self, ma, ten, nsx, gia, chat_lieu):
        super().__init__(ma, ten, nsx)
        self.__gia = gia
        self.__lieu = chat_lieu

    def hien_thi(self):
        print("--- [ HÀNG SÀNH SỨ ] ---")
        super().thong_tin_co_ban()
        print(f"Gia ban: {self.__gia:,.0f} VND")
        print(f"Nguyen lieu: {self.__lieu}")

class HangThucPham(HangHoa):
    def __init__(self, ma, ten, nsx, gia, nsx_date, exp_date):
        super().__init__(ma, ten, nsx)
        self.__gia = gia
        self.__nsx_date = nsx_date
        self.__exp_date = exp_date

    def hien_thi(self):
        print("--- [ HÀNG THỰC PHẨM ] ---")
        super().thong_tin_co_ban()
        print(f"Gia ban: {self.__gia:,.0f} VND")
        print(f"Ngay SX: {self.__nsx_date} | HSD: {self.__exp_date}")

# TEST

if __name__ == "__main__":
    tu_lanh = HangDienMay("DM01", "Tu lanh Samsung", "Samsung", 15000000, 24, 220, 200)
    binh_hoa = HangSanhSu("SS05", "Binh hoa co", "Bat Trang", 500000, "Gom su")
    sua_tuoi = HangThucPham("TP12", "Sua Vinamilk", "Vinamilk", 35000, "01/01/2026", "01/07/2026")

    tu_lanh.hien_thi()
    print()
    binh_hoa.hien_thi()
    print()
    sua_tuoi.hien_thi()