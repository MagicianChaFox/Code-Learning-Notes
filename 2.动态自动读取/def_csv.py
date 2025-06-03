#该函数主要负责csv文件处理相关的功能

import csv
import os
from datetime import datetime

def GetFolderList(folder_path):
    '''
    将待处理文件夹目录中，全部的文件名称以列表形式存储。
    
    输入参数
    folder_path: 字符串，待读取的文件夹路径
    输出参数
    folder_list: 列表，包含本文件夹中全部的文件名
    '''
    folder_list = os.listdir(folder_path)  
    return folder_list

def check_file_type(AllCsvInfoDict, folder_path, file_name, UIInfoDict, folder_info =[], HorL = 'No'):
    #UIInfoDict
    '''
    可以循环读取文件夹，找到最后一个有csv的文件夹

    输入参数
    AllCsvInfoDict: 列表，其中每一个元素是一个字典，内层列表中包含了csv文件路径、上层文件夹信息、回路
    folder_path：字符串，当前文件夹的路径，用于和文件夹内的文件夹名拼在一起，再往深一层读取，或者判断当前文件是否为csv文件。
    file_name：字符串，当前准备读取的文件夹名，用于和路径名一起拼接，更深一层的读取，或者判断当前文件是否为csv文件。
    channel_file：字符串，一个csv文件路径，文件内容为示波器的通道信息。
    folder_info：列表，元素为字符串，字符串用于保存上一层文件夹的信息，回路与温度的信息，用于输出时随读取后的动态参数一起写入结果。
    HorL：字符串，用于判断读取过程中使用什么回路的读取方式。
    输出参数
    folder_list: 列表，其中每一个元素是一个列表，内层列表中包含了csv文件路径、上层文件夹信息、回路
    '''
    OneCsvInfoDict = {'CsvFilePath':'NoCsvPathError', 'FolderInfo':'NoFolderInfoError', 'Loop':'NoLoopError',
                'VgsHigh':0, 'VgsLow':-50, 'VgsChannel':0, 'VdsChannel':0, 'IdsChannel':0, 'IfChannel':0, 
                'CrossTalkChannel':0, 'VfChannel':0, 'ILChannel':0, 'IsFilter':False} # 初始化当前的csv文件信息
    folder_info_def = folder_info
    HorL_def = HorL
    file_path = folder_path + '/' + file_name
    if os.path.isfile(file_path):
        #跳过，不看了
        #print(f"{file_path} 是一个文件")
        pass
    elif os.path.isdir(file_path):
        #print(f"{file_path} 是一个目录")
        #print('判断文件名是否包含csv，不包含就继续向里面看，包含的话就传递给读取的函数')
        if 'csv' in file_path or 'CSV' in file_path:
            #print(f'找到csv文件夹：{file_path}')
            #print('文件夹信息:', folder_info_def)
            #print('上桥还是下桥:', HorL_def)
            #print()
            GetWaveChannel(OneCsvInfoDict, file_path, folder_info_def, HorL_def, UIInfoDict)
            #这里加入一个根据OneCsvInfoDict['Loop']，确定剩余字典内容的函数
            AllCsvInfoDict.append(OneCsvInfoDict)
            #print('-'*50, 'test', '-'*50)

        elif 'HIGH' in file_name or 'HS' in file_name:
            #print(f'{file_path} 标记上管，参数传递出去，继续向内读取')
            folder_list = GetFolderList(file_path)
            folder_info_def = file_name
            HorL_def = 'HIGH'
            for file_name_2 in folder_list:
                check_file_type(AllCsvInfoDict, file_path, file_name_2, UIInfoDict, folder_info=folder_info_def, HorL='HIGH')
            #继续向里面读取
        elif 'LOW' in file_name or 'LS' in file_name:
            #print(f'{file_path} 标记下管，参数传递出去，继续向内读取')
            folder_list = GetFolderList(file_path)
            folder_info_def = file_name
            HorL_def = 'LOW'
            for file_name_2 in folder_list:
                check_file_type(AllCsvInfoDict, file_path, file_name_2, UIInfoDict, folder_info=folder_info_def, HorL='LOW')
            #继续向里面读取
        else:
            # 继续向里面读取
            folder_list = GetFolderList(file_path)
            for file_name_2 in folder_list:
                check_file_type(AllCsvInfoDict, file_path, file_name_2, UIInfoDict, folder_info=[], HorL='No')
    else:
        #print(f"{file_path} 既不是文件也不是目录")
        pass
    return AllCsvInfoDict

def GetWaveChannel(OneCsvInfoDict, file_path, folder_info_def, HorL_def, UIInfoDict):
    '''
    这个函数用来确认当前csv文件的示波器通道，通过读取本地的示波器通道配置文件实现。
    '''
    OneCsvInfoDict['CsvFilePath'] = file_path
    OneCsvInfoDict['FolderInfo'] = folder_info_def
    OneCsvInfoDict['Loop'] = HorL_def
    if OneCsvInfoDict['Loop'] == 'HIGH':
        OneCsvInfoDict['VgsChannel'] = int(UIInfoDict['HS_Vgs_act_Channel'])
        OneCsvInfoDict['VdsChannel'] = int(UIInfoDict['HS_Vds_act_Channel'])
        OneCsvInfoDict['IdsChannel'] = int(UIInfoDict['HS_Ids_act_Channel'])
        OneCsvInfoDict['IfChannel'] = int(UIInfoDict['HS_Idiode_pas_Channel'])
        OneCsvInfoDict['CrossTalkChannel'] = int(UIInfoDict['HS_Vgs_pas_Channel'])
        OneCsvInfoDict['VfChannel'] = int(UIInfoDict['HS_Vds_pas_Channel'])
        OneCsvInfoDict['ILChannel'] = int(UIInfoDict['HS_IL_Channel'])
        OneCsvInfoDict['VgsHigh'] = float(UIInfoDict['HS_Vgs_positive_voltage'])
        OneCsvInfoDict['VgsLow'] = float(UIInfoDict['HS_Vgs_negative_voltage'])
    elif OneCsvInfoDict['Loop'] == 'LOW':
        OneCsvInfoDict['VgsChannel'] = int(UIInfoDict['LS_Vgs_act_Channel'])
        OneCsvInfoDict['VdsChannel'] = int(UIInfoDict['LS_Vds_act_Channel'])
        OneCsvInfoDict['IdsChannel'] = int(UIInfoDict['LS_Ids_act_Channel'])
        OneCsvInfoDict['IfChannel'] = int(UIInfoDict['LS_Idiode_pas_Channel'])
        OneCsvInfoDict['CrossTalkChannel'] = int(UIInfoDict['LS_Vgs_pas_Channel'])
        OneCsvInfoDict['VfChannel'] = int(UIInfoDict['LS_Vds_pas_Channel'])
        OneCsvInfoDict['ILChannel'] = int(UIInfoDict['LS_IL_Channel'])
        OneCsvInfoDict['VgsHigh'] = float(UIInfoDict['LS_Vgs_positive_voltage'])
        OneCsvInfoDict['VgsLow'] = float(UIInfoDict['LS_Vgs_negative_voltage'])
    else:
        pass
    # 到这里，已经读取了示波器配置文件中的数据，接下来要避免某个接口没有插上的情况

    OneCsvInfoDict = GetClearChannelNum(OneCsvInfoDict)
    return OneCsvInfoDict

def GetClearChannelNum(OneCsvInfoDict):
    ToDoList = ['VgsChannel', 'VdsChannel', 'IdsChannel', 'IfChannel', 'CrossTalkChannel', 'VfChannel', 'ILChannel']
    ChannelNum = [OneCsvInfoDict[ToDoList[0]], OneCsvInfoDict[ToDoList[1]], OneCsvInfoDict[ToDoList[2]], 
                  OneCsvInfoDict[ToDoList[3]], OneCsvInfoDict[ToDoList[4]], OneCsvInfoDict[ToDoList[5]], 
                  OneCsvInfoDict[ToDoList[6]]]
    #print('正在处理中')
    tmp = 1
    tmp3 = 0
    while tmp + tmp3 <= 6:
        #print('调整前：', ChannelNum)
        #print('tmp:', tmp)
        #print('tmp3:', tmp3)
        if tmp in ChannelNum:
            #print('有', tmp, '通道的信息')
            tmp += 1
        else:
            #print('没有', tmp, '通道的信息')
            for tmp2 in ToDoList:
                if OneCsvInfoDict[tmp2] > tmp:
                    OneCsvInfoDict[tmp2] = int(OneCsvInfoDict[tmp2] - 1)
                else:
                    pass
            ChannelNum = [OneCsvInfoDict[ToDoList[0]], OneCsvInfoDict[ToDoList[1]], OneCsvInfoDict[ToDoList[2]], 
                                  OneCsvInfoDict[ToDoList[3]], OneCsvInfoDict[ToDoList[4]], OneCsvInfoDict[ToDoList[5]], 
                                  OneCsvInfoDict[ToDoList[6]]]
            tmp3 += 1
        #print('调整后：', ChannelNum)
        #print()
        
    return OneCsvInfoDict

def ReadChannelCsvFile(file_path):
    '''
    读取示波器通道信息的csv文件，

    输入参数
    file_path: 从示波器中保存的csv文件。
    输出参数
    data: 包含csv文件数据的列表。
    '''
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print("csv_def - ReadChannelCsvFile函数错误，找不到对应文件：", file_path)
    return data

def ReadCsvFile(file_path):
    '''
    读取csv文件并返回数据列表，从'TIME'行开始存储数据。
    输入参数
    file_path: 从示波器中保存的csv文件。
    输出参数
    data: 包含csv文件数据的列表，从'TIME'行及其以下开始。
    '''
    data = []
    start_storing = False  # 用于标记是否开始存储数据
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(_.replace('\x00', '') for _ in f)
            for row in csv_reader:
                if 'TIME' in row:
                    start_storing = True
                    continue  # 跳过'TIME'这一行
                if start_storing:
                    data.append(row)
    except FileNotFoundError:
        print("csv_def - ReadCsvFile函数错误，找不到对应文件：", file_path)
    return data

def FileWrite(file_out, dynamic_data, csv_info, csv_file_name):
    f_out = open(file_out, 'r', encoding='utf-8-sig', newline='')
    csv_reader = csv.reader(f_out)  # 读取文件
    li_PanDuan = list(csv_reader)  # 将文件存储在大列表里
    unit_list = ['loop', 'Ids_off(A)', 'tdon(ns)', 'tr(ns)', 'ton(ns)', 'didt_on(10%~90%)(A/ns)', 'dvdt_on(90%~10%)(V/ns)', 'didt_on(20%~80%)(A/ns)', 
                 'dvdt_on(80%~20%)(V/ns)', 'didt_on(30%~70%)(A/ns)', 'dvdt_on(70%~30%)(V/ns)',   'Eon(mJ)', 
                 'tdoff(ns)', 'tf(ns)', 'toff(ns)', 'didt_off(90%~10%)(A/ns)', 'dvdt_off(10%~90%)(V/ns)', 'didt_off(80%~20%)(A/ns)', 'dvdt_off(20%~80%)(V/ns)',
                 'didt_off(70%~30%)(A/ns)', 'dvdt_off(30%~70%)(V/ns)', 'Actual_Vds(V)','Vspike(V)','Eoff(mJ)','Eon+Eoff(mJ)',
                 'Vgs_max_on(V)', 'Vgs_min_off(V)', 'trr(ns)', 'Irrm(A)', 'Vrrm(V)', 'Qrr(uC)', 'Erec(mJ)', 'didt_irr(50%~50%)(A/ns)', 'dvdt_vrr(10%~90%)(V/ns)', 
                 'dvdt_vrr(10%~fs)(V/ns)', 'dvdt_vrr_max(V/ns)','didt_on_max(A/ns)', 'dvdt_on_max(V/ns)', 'didt_off_max(A/ns)', 'dvdt_off_max(V/ns)',
                 'time_didt_on_max(us)', 'time_dvdt_on_max(us)', 'time_didt_off_max(us)', 'time_dvdt_off_max(us)',
                 'time_dvdt_rrm_max(us)', 'File_Info']
    
    try:
        if li_PanDuan[0] != unit_list:
            # 上一行删除了一个, 'trr(ns)'
            # trr(ns)是通过斜率计算出来的，存在一定误差，暂时不用
            print('表格{}格式有问题，需要重新构建表格。'.format(file_out))
            f_out.close()
            f_out = open(file_out, 'w', encoding='utf-8-sig', newline='')
            csv_writer = csv.writer(f_out)
            csv_writer.writerow(unit_list)  # 写入csv文件时，构建列表头
            f_out.close()
        else:
            f_out.close()
    except IndexError:
        f_out.close()
        f_out = open(file_out, 'w', encoding='utf-8-sig', newline='')
        csv_writer = csv.writer(f_out)
        csv_writer.writerow(unit_list)  # 写入csv文件时，构建列表头
        f_out.close()
    f_out = open(file_out, 'a', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(f_out)  # 基于文件对象构建 csv写入对象
    csv_writer.writerow([csv_info['FolderInfo']] + dynamic_data + [csv_info['CsvFilePath']+ '/' + csv_file_name])
    f_out.close()
    return

def CreateCSVFile(file_out):
    # 获取当前时间
    formatted_time = datetime.now().strftime('%Y%m%d %H%M%S')
    #print(formatted_time)
    file_name = str(file_out + '/' + '动态参数自动读取结果' + formatted_time + '.csv')

    # 使用'with'语句确保文件正确关闭
    with open(file_name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvfile.close()
    return file_name

def TransposedDataListWrite(ToBeWriteList, file_out):
    # 将转置后的结果写入csv文件、
    unit_list = ['loop', 'Ids_off(A)', 'tdon(ns)', 'tr(ns)', 'ton(ns)', 'didt_on(10%~90%)(A/ns)', 'dvdt_on(90%~10%)(V/ns)', 'didt_on(20%~80%)(A/ns)', 
                 'dvdt_on(80%~20%)(V/ns)', 'didt_on(30%~70%)(A/ns)', 'dvdt_on(70%~30%)(V/ns)',   'Eon(mJ)', 
                 'tdoff(ns)', 'tf(ns)', 'toff(ns)', 'didt_off(90%~10%)(A/ns)', 'dvdt_off(10%~90%)(V/ns)', 'didt_off(80%~20%)(A/ns)', 'dvdt_off(20%~80%)(V/ns)',
                 'didt_off(70%~30%)(A/ns)', 'dvdt_off(30%~70%)(V/ns)', 'Actual_Vds(V)','Vspike(V)','Eoff(mJ)','Eon+Eoff(mJ)',
                 'Vgs_max_on(V)', 'Vgs_min_off(V)', 'trr(ns)', 'Irrm(A)', 'Vrrm(V)', 'Qrr(uC)', 'Erec(mJ)', 'didt_irr(50%~50%)(A/ns)', 'dvdt_vrr(10%~90%)(V/ns)', 
                 'dvdt_vrr(10%~fs)(V/ns)', 'dvdt_vrr_max(V/ns)','didt_on_max(A/ns)', 'dvdt_on_max(V/ns)', 'didt_off_max(A/ns)', 'dvdt_off_max(V/ns)',
                 'time_didt_on_max(us)', 'time_dvdt_on_max(us)', 'time_didt_off_max(us)', 'time_dvdt_off_max(us)',
                 'time_dvdt_rrm_max(us)', 'File_Info']
    ToBeWriteList = [unit_list] + ToBeWriteList
    transposed_list = [[' ']] + [list(t) for t in zip(*ToBeWriteList)] # 转置
    f_out = open(file_out, 'a', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(f_out)
    for write_list in transposed_list:
        csv_writer.writerow(write_list)  
    f_out.close()

    '''
    try:
        f_out = open(file_out, 'r', encoding='utf-8-sig', newline='')
        csv_writer = csv.writer(f_out)
        csv_writer.writerow(transposed_list)  # 写入csv文件时，构建列表头
        f_out.close()
    except IndexError:
        f_out.close()'''
    return




if __name__ == "__main__":
    OneCsvInfoDict = {'CsvFilePath':'NoCsvPathError', 'FolderInfo':'NoFolderInfoError', 'Loop':'NoLoopError',
                    'VgsHigh':0, 'VgsLow':-50, 'VgsChannel':0, 'VdsChannel':0, 'IdsChannel':0, 'IfChannel':0, 
                    'CrossTalkChannel':0, 'VfChannel':0, 'ILChannel':0, 'IsFilter':False} # 初始化当前的csv文件信息
    FolderPath = r"D:\test\程序优化专用读取数据"  # 包含全部待读取的文件夹目录
    file_path = r"D:\test\程序优化专用读取数据\HIGH  025C\csv\800V  1200A_ALL.csv"
    folder_info_def = 'HIGH  025C'
    HorL_def = 'HIGH'
    channel_file = r"D:\test\数据处理专用\示波器通道确定.csv" 

    ToDoList = ['VgsChannel', 'VdsChannel', 'IdsChannel', 'IfChannel', 'CrossTalkChannel', 'VfChannel', 'ILChannel']
    ChannelNum = [OneCsvInfoDict[ToDoList[0]], OneCsvInfoDict[ToDoList[1]], OneCsvInfoDict[ToDoList[2]], 
                OneCsvInfoDict[ToDoList[3]], OneCsvInfoDict[ToDoList[4]], OneCsvInfoDict[ToDoList[5]], 
                OneCsvInfoDict[ToDoList[6]]]

    print('示波器通道读取前:' , ChannelNum)
    OneCsvInfoDict = GetWaveChannel(OneCsvInfoDict, file_path, folder_info_def, HorL_def, channel_file)
    #print(OneCsvInfoDict)
    print()
    ChannelNum = [OneCsvInfoDict[ToDoList[0]], OneCsvInfoDict[ToDoList[1]], OneCsvInfoDict[ToDoList[2]], 
                OneCsvInfoDict[ToDoList[3]], OneCsvInfoDict[ToDoList[4]], OneCsvInfoDict[ToDoList[5]], 
                OneCsvInfoDict[ToDoList[6]]]
    print('示波器通道读取后:' , ChannelNum)