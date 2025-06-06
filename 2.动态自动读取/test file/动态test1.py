import def_csv
import def_wave

def test_program(UIInfoDict):
        ModuleType = ['MOSFET', 'IGBT'][0]

        FolderPath = UIInfoDict['input_folder_path']
        FileOut = UIInfoDict['output_file_path']
        FileOut = def_csv.CreateCSVFile(FileOut)
        IsFilterFlag = [False, True][UIInfoDict['Is_low_pass_filter']]

        AllCsvInfoDict = []
        G_T, G_Vge, G_Vce, G_Ic, G_Vf, G_If = [], [], [], [], [], []

        folder_list = def_csv.GetFolderList(FolderPath)
        for file_name in folder_list:
            def_csv.check_file_type(AllCsvInfoDict, FolderPath, file_name, UIInfoDict)
        #到此已经获取了需要读取的全部csv文件夹，以及对应文件夹是上桥还是下桥
        csv_num = 0  # 获取总共需要处理的文件数
        for tmp in AllCsvInfoDict:
            CSVFolderList = def_csv.GetFolderList(tmp['CsvFilePath'])
            csv_num += len(CSVFolderList)
        flag = 1
        for tmp in AllCsvInfoDict:
            CSVFolderList = def_csv.GetFolderList(tmp['CsvFilePath'])
            for csv_tmp in CSVFolderList:  # 使用csv_tmp循环读取列表中内容。
                print('Processing:', tmp['FolderInfo'], csv_tmp)
                Data = def_csv.ReadCsvFile(tmp['CsvFilePath'] + '\\' + csv_tmp)
                VgsR = -50.0  # 经过上下桥判断后，确认当前的栅极负压，默认为-50.0
                Vgs = 0.0  # 经过上下桥判断后，确认当前的栅极正压，默认为0.0
                VgsR = tmp['VgsLow']  #  该参数在驱动板通电后，使用万用表测量上桥gs电压，用于校准光隔离探头整体测量值偏移的问题。
                Vgs = tmp['VgsHigh'] #  正向驱动电压
                G_T, G_Vge, G_Vce, G_Ic, G_Vf, G_If, is_accurate = def_wave.ExtractWaveData(Data, tmp, UIInfoDict)
                G_Vge, G_Vce, G_Ic, G_Vf, G_If = def_wave.IsFilter(IsFilterFlag, G_Vge, G_Vce, G_Ic, G_Vf, G_If, UIInfoDict)
                DynamicData =def_wave.GetDynamicData(ModuleType, VgsR, Vgs)
                def_csv.FileWrite(FileOut, DynamicData, tmp, csv_tmp)
                #print('Completed：', tmp['FolderInfo'], csv_tmp)
                #self.textBrowser_003_main_printf.append('Progress:' + str(flag) + '/' + str(csv_num))
                print('Completed!  Progress:' + str(flag) + '/' + str(csv_num))
                flag += 1
                print()

if __name__ == "__main__":
    UIInfoDict = {'HS_Vgs_act_Channel':4, 'HS_Vds_act_Channel':5, 'HS_Ids_act_Channel':3, 'HS_Idiode_pas_Channel':0, 
                  'HS_Vgs_pas_Channel':1, 'HS_Vds_pas_Channel':2, 'HS_IL_Channel':6, 
                  'LS_Vgs_act_Channel':1, 'LS_Vds_act_Channel':2, 'LS_Ids_act_Channel':0, 'LS_Idiode_pas_Channel':3, 
                  'LS_Vgs_pas_Channel':4, 'LS_Vds_pas_Channel':5, 'LS_IL_Channel':6, 
                  'HS_Vgs_act_Reverse':1, 'HS_Vds_act_Reverse':1, 'HS_Ids_act_Reverse':1, 'HS_Idiode_pas_Reverse':1, 
                  'HS_Vgs_pas_Reverse':1, 'HS_Vds_pas_Reverse':1, 'HS_IL_Reverse':1, # 未翻转使用1表示，翻转用-1表示，后期直接乘，避免if判断
                  'LS_Vgs_act_Reverse':1, 'LS_Vds_act_Reverse':1, 'LS_Ids_act_Reverse':1, 'LS_Idiode_pas_Reverse':-1, 
                  'LS_Vgs_pas_Reverse':1, 'LS_Vds_pas_Reverse':1, 'LS_IL_Reverse':1, 
                  'HS_Vgs_positive_voltage':18, 'HS_Vgs_negative_voltage':-4, 
                  'LS_Vgs_positive_voltage':18, 'LS_Vgs_negative_voltage':-4, 
                  'Is_low_pass_filter':0, 'sampling_rate':6.25e9, 'cutoff_frequency':400e6,
                  'input_folder_path':r"C:\Users\23000222\Desktop\CSP-PreB-Sichain-8.5m-35mm2-200C - zisheng\测试专用", 
                  'output_file_path':r"C:\Users\23000222\Desktop\CSP-PreB-Sichain-8.5m-35mm2-200C - zisheng\读取结果"} # 初始化UI界面获取的信息

    test_program(UIInfoDict)