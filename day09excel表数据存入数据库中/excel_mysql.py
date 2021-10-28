import xlrd
import pymysql
wb = xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override='utf8')
sheets = wb.sheets()
con = pymysql.connect(host='127.0.0.1',user='root',password='',database='bank',charset='utf8')
cursor = con.cursor()
def translation():
    for sheet in sheets:
        print(sheet.nrows)
        print(sheet.name)
        for i in range(1,sheet.nrows):
            print(sheet.row_values(i))
            sql = "insert into tbl_sal values(%s,%s,%s,%s,%s)"
            param = sheet.row_values(i)
            param[0] = sheet.name + sheet.row_values(i)[0]
            print(param[0])
            try:
                cursor.execute(sql,param)
            except Exception as e:
                print(e)
    con.commit()
    cursor.close()
    con.close()

def createtbl():
    sql = '''
        create table tbl_sal(
            date varchar(20),
            clothesname varchar(20),
            price float(8,2),
            count float(8,2),
            salescount float(8,2)
        );
    '''
    try:
        cursor.execute(sql)
        con.commit()
        cursor.close()
        con.close()
    except Exception as e:
        print(e)
    finally:
        pass
# createtbl()
translation()