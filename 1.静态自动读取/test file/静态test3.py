from datetime import datetime
import csv

def CreateCSVFile(file_out):
    # 获取当前时间
    formatted_time = datetime.now().strftime('%Y%m%d %H%M%S')
    #print(formatted_time)
    file_name = str(file_out + '/' + '静态参数自动读取结果' + formatted_time + '.csv')

    # 使用'with'语句确保文件正确关闭
    with open(file_name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvfile.close()
    return file_name


file_out = r"D:\File\0.公司相关\1.1.黄山MOSFET\8并1200V\20.黄山BC档 Datasheet制作\1.静态\BC47"

CreateCSVFile(file_out)