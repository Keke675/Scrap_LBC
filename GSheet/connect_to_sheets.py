import gspread

def connect_to_sheets():
    gc = gspread.service_account()
    sh = gc.open("AppartementsRecherche")
    worksheet = sh.sheet1
    return worksheet

