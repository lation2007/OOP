#1
def ve_duong_ngang():
    print('+ - - - - + - - - - +')

def ve_duong_doc():
    print('|         |         |')

def ve_mot_hang():
    ve_duong_ngang()
    ve_duong_doc()
    ve_duong_doc()
    ve_duong_doc()
    ve_duong_doc()

def ve_luoi_3x3():
    ve_mot_hang()
    ve_mot_hang()
    ve_mot_hang()
    print('+ - - - - + - - - - +')
ve_luoi_3x3()
#2
def ve_duong_ngang(n):
    for i in range(n):
        print('+ - - - - ', end='')
    print('+')

def ve_duong_doc(n):
    for i in range(n):
        print('|         ', end='')
    print('|')

def ve_luoi_4x4():
    n = 4
    for i in range(n):
        ve_duong_ngang(n)
        for j in range(4):
            ve_duong_doc(n)
    ve_duong_ngang(n)

ve_luoi_4x4()


