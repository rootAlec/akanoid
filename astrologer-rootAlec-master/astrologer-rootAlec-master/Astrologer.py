"""
學習目標:
1. 學習撰寫模組，在python，一個檔案或是一個資料夾都可被視為一個模組。
2. 用test_case來測試自己寫的東西對不對
核心概念:先畫靶再射箭，先設定好自己要的結果，再開始coding。
"""


def get_constellation(month, day) -> str:
    """
    根據生日回傳正確的星座
    牡羊座	3月21日～4月20日
    金牛座	4月21日～5月20日
    雙子座	5月21日～6月20日
    巨蟹座	6月21日～7月22日
    獅子座	7月23日～8月22日
    處女座	8月23日～9月22日
    天秤座	9月23日～10月22日
    天蠍座	10月23日～11月22日
    射手座	11月23日～12月22日
    魔羯座	12月23日～1月21日
    水瓶座	1月22日～2月19日
    雙魚座	2月20日～3月20日
    """
    
    days = [21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22]
    con = ["魔羯座", "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座"
            , "魔羯座"]

    if day < days[month-1]:
        return con[month-1]
    else:
        return con[month]

    


def get_each_number(number: int) -> []:
    """
    輸入一個正整數，然後將每一位數分開。
    ex get_each_number(1920) 
    return [1,9,2,0]
    """

    result = []
    for x in str(number):
        result.append(int(x))
    
    return result


def get_life_number(year=1900, month=1, day=1) -> int:
    """
    會回傳一個生命靈數，生命靈數的計算方式是出生年月日的每一個數字的總和，不斷加總至個位數。
    ex 1995 12 13 -> 1+9+9+5+1+2+1+3 = 31 -> 3+1 =4
    這樣生命靈數就是4
    """
    result = []
    a = 0
    life_num = str(year) + str(month) + str(day)
    print(life_num)
    while 1<len(life_num):
        for x in str(life_num):
            result.append(int(x))
        a = sum(result)
        life_num = str(a)
        result.clear()

    return a

