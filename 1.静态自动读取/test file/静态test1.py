import os
import csv
from datetime import datetime
import pandas as pd
from collections import OrderedDict

class GetIgssObject:
    '''
    存储栅极漏电流Igss的相关数据与获取过程，专门给函数GetIgss()调用。
    '''
    def __init__(self):
        '''
        Igss读取中使用到的参数，随着读取过程更新
        '''
        self.Igss_Vgs_set = 20.0 # Vds短路情况下，Vgs电压值，默认为正向20V

        self.Igss_all_list = [] # 包含Vgs、Igs、其余杂项的整体列表
        self.Igss_Vgs_list = [] # 只存储Vgs的干净列表
        self.Igss_Igs_list = [] # 只存储Igs的干净列表

        self.Igss = 0 # 使用提纯后的列表，读取出栅极漏电流的最终结果。

    def get_Igss_Vgs_set(self, Igss_Vgs_set):
        '''
        修改Igss_Vgs_set的值，尤其在测量反向栅极漏电时使用。
        '''
        self.Igss_Vgs_set = float(Igss_Vgs_set)
        #print('当前Vgs:', self.Igss_Vgs_set)
        return
    
    def get_Igss_data(self, data):
        '''
        获取栅极漏电流Igss的文件名、实验设置参数；
        获取栅极漏电流Igss的实验数据，此数据较为粗糙，包含Vgs、Igs、其余杂。
        '''
        end_storing_flag = False  # 用于判断是否停止存储数据，第一次数据存储结束后停止存储

        for row in data: # 用来将csv全部数据中的有效数据粗略的提取出来，以row控制每行读取
            if ('DataValue' not in row) and end_storing_flag:
                # 结束存储'
                break
            if 'DataName' in row:
                #self.Igss_all_list.append(row) # 注释此行，get_Igss_all_list列表中将不存储DataName一行
                end_storing_flag = True  # 确保不会再次读取到数据
                # 获取实验采集到的数据,读取到DataName时开始存储
                continue
            if 'DataValue' in row:
                self.Igss_all_list.append(row) # 获取实验采集到的数据
                continue
        return

    def get_Igss_Vgs_and_Igs_list(self):
        '''
        获取Vgs与Igs的干净列表
        '''
        for row in self.Igss_all_list: # 将粗糙的列表数据提纯，以row控制每行读取
            self.Igss_Vgs_list.append(float(row[2]))
            self.Igss_Igs_list.append(float(row[1]))
            # 待优化1：判断两边列表哪一个数据更接近IgssPositive_VgsSet_1_2，以免两列存储时交换了。
        return
    
    def get_Igss(self):
        '''
        使用处理干净的列表，读取出栅极漏电的最终结果。
        '''
        derta_Igss_Vgs_list = []
        for tmp in self.Igss_Vgs_list:
            derta_Igss_Vgs_list.append(abs(tmp-self.Igss_Vgs_set))
        l_Igss = derta_Igss_Vgs_list.index(min(derta_Igss_Vgs_list))
        self.Igss = abs(round(((self.Igss_Igs_list[l_Igss]) * 1e9), 2)) # 栅极漏电为nA级别，A转化为nA。
        # 待优化3：可以使用线性差值法提高精度优化
        return

class GetVgsthObject:
    '''
    存储栅极开启阈值电压Vgsth的相关数据与获取过程，专门给函数GetVgsth()调用。
    '''
    def __init__(self):
        '''
        Vgsth读取中使用到的参数，随着读取过程更新
        '''
        self.Vgsth_Ids_set = 1.12 # Vds=Vgs下，增加电压直到Ids达到某一个设定值，默认1.12mA

        self.Vgsth_all_list = [] # 包含Igs,Vgs,Ids,其余杂项的整体列表
        self.Vgsth_Vgs_list = [] # 只存储Vgs的干净列表
        self.Vgsth_Ids_list = [] # 只存储Ids的干净列表

        self.Vgsth = 0 # 使用提纯后的列表，读取出栅极漏电流的最终结果。


    def get_Vgsth_Ids_set(self, Vgsth_Ids_set):
        '''
        修改Vgsth_Ids_set的值
        '''
        self.Vgsth_Ids_set = float(Vgsth_Ids_set) / 1000
        # 主函数中设置的Vgsth_IdsSet_2单位是mA，表格中数据单位为A，除以1000换算。

    def get_Vgsth_data(self, data):
        '''
        获取栅极开启阈值电压Vgsth的文件名、实验设置参数；
        获取栅极开启阈值电压Vgsth的实验数据，此数据较为粗糙，包含Igs,Vgs,Ids和其余杂项。
        '''
        end_storing_flag = False  # 用于判断是否停止存储数据，第一次数据存储结束后停止存储

        for row in data: # 用来将csv全部数据中的有效数据粗略的提取出来，以row控制每行读取
            if ('DataValue' not in row) and end_storing_flag:
                # 结束存储'
                break
            if 'DataName' in row:
                #self.Igss_all_list.append(row) # 注释此行，get_Igss_all_list列表中将不存储DataName一行
                end_storing_flag = True  # 确保不会再次读取到数据
                # 获取实验采集到的数据,读取到DataName时开始存储
                continue
            if 'DataValue' in row:
                self.Vgsth_all_list.append(row) # 获取实验采集到的数据
                continue
    
    def get_Vgsth_Vgs_and_Ids_list(self):
        '''
        获取Vgs与Ids的干净列表
        '''
        try:
            for row in self.Vgsth_all_list: # 将粗糙的列表数据提纯，以row控制每行读取
                self.Vgsth_Vgs_list.append(float(row[2]))
                self.Vgsth_Ids_list.append(float(row[3]))
                # ValueError
                # 待优化1：判断两边列表哪一个数据更接近Vgsth_IdsSet_2，以免两列存储时交换了。
        except ValueError: # 避免数据出现空白位置，存储失败
            pass
        return

    def get_Vgsth(self):
        '''
        使用处理干净的列表，读取出栅极开启阈值电压Vgsth的最终结果。
        '''
        derta_Vgsth_Ids_list = []
        for tmp in self.Vgsth_Ids_list:
            derta_Vgsth_Ids_list.append(abs(round((tmp-self.Vgsth_Ids_set), 2)))
        l_Vgsth = derta_Vgsth_Ids_list.index(min(derta_Vgsth_Ids_list))
        self.Vgsth = round((self.Vgsth_Vgs_list[l_Vgsth]) ,3)
        # 待优化3：可以使用线性差值法提高精度优化
        return

class GetOutputCurveObject:
    '''
    存储输出曲线的相关数据与获取过程，专门给函数GetOutputCurve()调用。
    '''
    def __init__(self):
        '''
        输出曲线读取中使用到的参数，随着读取过程更新
        '''
        self.Igss_Vgs_set = 20.0 # Vds短路情况下，Vgs电压值，默认为正向20V

        self.output_curve_setup_title = 'No data, please check' # Igss文件名
        self.output_curve_setup_data = [16,600] # 输出曲线的实验设置参数
        # output_curve_setup_data为列表形式存储，分别存储Vgs与Ids的值，默认为18V和650A

        self.output_curve_all_list = [] # 包含Vds、Ids、其余杂项的整体列表
        self.output_curve_Vds_list = [[]] # 只存储Vds的干净列表
        self.output_curve_Ids_list = [[]] # 只存储Ids的干净列表
        self.output_curve_Vgs_list = [[]] # 确定输出曲线的Vgs条件
        self.output_curve_Rdson_list = [[]] # 只存储Rdson的干净列表

        self.Rdson = 0 # 使用提纯后的列表，读取出Rdson的最终结果(MOSFET)
        self.Vcesat = 0 # 使用提纯后的列表，读取出Vcesat的最终结果(IGBT)

    def get_output_curve_set(self, output_curve_set):
        '''
        修改output_curve_set的值。
        '''
        self.output_curve_setup_data[0] = float(output_curve_set[0])
        self.output_curve_setup_data[1] = float(output_curve_set[1])
        return
    
    def get_output_curve_data(self, data):
        '''
        获取输出曲线output_curve的文件名、实验设置参数；
        获取输出曲线output_curve的实验数据，此数据较为粗糙，包含Vds、Ids、其余杂项的整体列表。
        '''
        end_storing_flag = False  # 用于判断是否停止存储数据，第一次数据存储结束后停止存储

        for row in data: # 用来将csv全部数据中的有效数据粗略的提取出来，以row控制每行读取
            if ('DataValue' not in row) and end_storing_flag:
                # 结束存储'
                break
            if ('\ufeffSetupTitle' in row) or ('SetupTitle' in row):
                self.output_curve_setup_title = row[1] # 获取文件名
                continue
            if 'DataName' in row:
                #self.Igss_all_list.append(row) # 注释此行，get_Igss_all_list列表中将不存储DataName一行
                end_storing_flag = True  # 确保不会再次读取到数据
                # 获取实验采集到的数据,读取到DataName时开始存储
                continue
            if 'DataValue' in row:
                self.output_curve_all_list.append(row) # 获取实验采集到的数据
                continue
        return
    
    def get_output_curve_list(self):
        '''
        获取Ids、Vds、Vgs、Rdson的干净列表
        '''
        num_of_data = 0 # 记录这是第几组数据
        Vgs_before = float(-100.0) # 记录上一次的Vgs，默认值设置为-100V
        is_line_break = False # 是否需要换行的判断标志
        for row in self.output_curve_all_list: # 将粗糙的列表数据提纯，以row控制每行读取
            try:
                is_line_break = ((row[3] == ' ') or ((Vgs_before != float(-100.0)) and ((abs(float(row[3])- Vgs_before))>=0.8)))
            except Exception as error:
                is_line_break = True
            if is_line_break == False: # 不需要换行，在当前的Vgs执行存储操作
                try:
                    self.output_curve_Vds_list[num_of_data].append(float(row[2]))
                except Exception as error:
                    self.output_curve_Vds_list[num_of_data].append(0.0)
                try:
                    self.output_curve_Ids_list[num_of_data].append(float(row[1]))
                except Exception as error:
                    self.output_curve_Ids_list[num_of_data].append(0.0)
                try:
                    self.output_curve_Vgs_list[num_of_data].append(float(row[3]))
                except Exception as error:
                    self.output_curve_Vgs_list[num_of_data].append(0.0)
                try:
                    self.output_curve_Rdson_list[num_of_data].append(float(row[4]))
                except Exception as error:
                    self.output_curve_Rdson_list[num_of_data].append(0.0)
            elif is_line_break == True: # 需要换行，列表里新建一个子列表，执行下一个Vgs的存储操作
                num_of_data += 1
                self.output_curve_Vds_list.append([])
                self.output_curve_Ids_list.append([])
                self.output_curve_Vgs_list.append([])
                self.output_curve_Rdson_list.append([])
                try:
                    self.output_curve_Vds_list[num_of_data].append(float(row[2]))
                except Exception as error:
                    self.output_curve_Vds_list[num_of_data].append(0.0)
                try:
                    self.output_curve_Ids_list[num_of_data].append(float(row[1]))
                except Exception as error:
                    self.output_curve_Ids_list[num_of_data].append(0.0)
                try:
                    self.output_curve_Vgs_list[num_of_data].append(float(row[3]))
                except Exception as error:
                    self.output_curve_Vgs_list[num_of_data].append(0.0)
                try:
                    self.output_curve_Rdson_list[num_of_data].append(float(row[4]))
                except Exception as error:
                    self.output_curve_Rdson_list[num_of_data].append(0.0)
            else :
                break
            try:
                Vgs_before = float(row[3])  
            except Exception as error:
                pass
        num = 0 # 用于将Vgs_list简化成单个数值
        for list in self.output_curve_Vgs_list:
            self.output_curve_Vgs_list[num] = round((sum(list)/len(list)),1)
            num +=1
        return
    
    def get_Rdson(self):
        '''
        使用处理干净的列表，读取出Rdson的最终结果。
        '''
        derta_output_curve_Ids_list = []
        #Ids_list_num = []
        #derta_output_curve_Vcesat_list = []
        #derta_output_curve_Rdson_list = []
        is_Vgs_find_flag = False # 用来判断表格中是否有需要的Vgs值
        Vgs_list_num = 0 # 确定当前列表位置
        for Vgs in self.output_curve_Vgs_list:
            if self.output_curve_setup_data[0] == Vgs:
                is_Vgs_find_flag = True
                #Ids_num = 0 # 确定Ids列表的位置
                for tmp in self.output_curve_Ids_list[Vgs_list_num]:
                    derta_output_curve_Ids_list.append(abs(tmp - self.output_curve_setup_data[1]))
                    #Ids_list_num.append(Ids_num)
                    #Ids_num += 1
                    l_Ids = derta_output_curve_Ids_list.index(min(derta_output_curve_Ids_list))
                    self.Rdson = round(((self.output_curve_Rdson_list[Vgs_list_num][l_Ids]) * 1000), 2) # Rdson为mΩ级别，Ω转化为mΩ。
                    self.Vcesat = round((self.output_curve_Vds_list[Vgs_list_num][l_Ids]), 2) # Vcesat单位V
            else:
                Vgs_list_num += 1
        return

class GetDiodeOutputCurveObject:
    '''
    存储二极管输出曲线的相关数据与获取过程，专门给函数GetDiodeOutputCurve()调用。
    '''
    def __init__(self):
        '''
        输出曲线读取中使用到的参数，随着读取过程更新
        '''
        self.diode_output_curve_setup_title = 'No data, please check' # Igss文件名
        self.diode_output_curve_setup_data = [-2,450] # 输出曲线的实验设置参数
        # output_curve_setup_data为列表形式存储，分别存储Vgs与Ids的值，默认为18V和650A

        self.diode_output_curve_all_list = [] # 包含Vds、Ids、其余杂项的整体列表
        self.diode_output_curve_Vsd_list = [[]] # 只存储Vsd的干净列表
        self.diode_output_curve_Isd_list = [[]] # 只存储Isd的干净列表
        self.diode_output_curve_Vgs_list = [[]] # 确定输出曲线的Vgs条件

        self.Vf = 0 # 使用提纯后的列表，读取出Vf的最终结果

    def get_diode_output_curve_set(self, diode_output_curve_set):
        '''
        修改diode_output_curve_set的值。
        '''
        self.diode_output_curve_setup_data[0] = float(diode_output_curve_set[0])
        self.diode_output_curve_setup_data[1] = float(diode_output_curve_set[1])
        return
    
    def get_diode_output_curve_data(self, data):
        '''
        获取二极管输出曲线diode_output_curve的文件名、实验设置参数；
        获取二极管输出曲线diode_output_curve的实验数据，此数据较为粗糙，包含Vsd、Isd、其余杂项的整体列表。
        '''
        end_storing_flag = False  # 用于判断是否停止存储数据，第一次数据存储结束后停止存储

        for row in data: # 用来将csv全部数据中的有效数据粗略的提取出来，以row控制每行读取
            if ('DataValue' not in row) and end_storing_flag:
                # 结束存储'
                break
            if ('\ufeffSetupTitle' in row) or ('SetupTitle' in row):
                self.diode_output_curve_setup_title = row[1] # 获取文件名
                continue
            if 'DataName' in row:
                #self.Igss_all_list.append(row) # 注释此行，get_Igss_all_list列表中将不存储DataName一行
                end_storing_flag = True  # 确保不会再次读取到数据
                # 获取实验采集到的数据,读取到DataName时开始存储
                continue
            if 'DataValue' in row:
                self.diode_output_curve_all_list.append(row) # 获取实验采集到的数据
                continue
        return
    
    def get_diode_output_curve_list(self):
        '''
        获取Isd、Vsd、Vgs的干净列表
        '''
        num_of_data = 0 # 记录这是第几组数据
        is_any_data_flag = True # 用来判断列表此处是空还是数据
        Vgs_before = float(-100.0) # 记录上一次的Vgs，默认值设置为-100V
        is_line_break = False
        for row in self.diode_output_curve_all_list: # 将粗糙的列表数据提纯，以row控制每行读取
            try:
                is_line_break = (row[1] == ' ') or ((Vgs_before != float(-100)) and ((abs(float(row[1])- Vgs_before))>=0.8))
            except Exception as error:
                is_line_break = True
            #is_line_break确定是否使用下一个Vgs存储
            if is_line_break == False: # 不需要换行，在当前的Vgs执行存储操作
                try:
                    self.diode_output_curve_Vsd_list[num_of_data].append(float(row[4]))
                except Exception as error:
                    self.diode_output_curve_Vsd_list[num_of_data].append(0.0)
                try:
                    self.diode_output_curve_Isd_list[num_of_data].append(float(row[5]))
                except Exception as error:
                    self.diode_output_curve_Isd_list[num_of_data].append(0.0)
                try:
                    self.diode_output_curve_Vgs_list[num_of_data].append(float(row[1]))
                except Exception as error:
                    self.diode_output_curve_Vgs_list[num_of_data].append(0.0)
            elif is_line_break == True: # 需要换行，列表里新建一个子列表，执行下一个Vgs的存储操作
                num_of_data += 1
                self.diode_output_curve_Vsd_list.append([])
                self.diode_output_curve_Isd_list.append([])
                self.diode_output_curve_Vgs_list.append([])
                try:
                    self.diode_output_curve_Vsd_list[num_of_data].append(float(row[4]))
                except Exception as error:
                    self.diode_output_curve_Vsd_list[num_of_data].append(0.0)
                try:
                    self.diode_output_curve_Isd_list[num_of_data].append(float(row[5]))
                except Exception as error:
                    self.diode_output_curve_Isd_list[num_of_data].append(0.0)
                try:
                    self.diode_output_curve_Vgs_list[num_of_data].append(float(row[1]))
                except Exception as error:
                    self.diode_output_curve_Vgs_list[num_of_data].append(0.0)
            else :
                break
            try:
                Vgs_before = float(row[1])
            except Exception as error:
                pass
        num = 0 # 用于将Vgs_list简化成单个数值
        for list in self.diode_output_curve_Vgs_list:
            self.diode_output_curve_Vgs_list[num] = round((sum(list)/len(list)),1)
            num +=1
        return
    
    def get_Vf(self):
        '''
        使用处理干净的列表，读取出Vf的最终结果。
        '''
        derta_diode_output_curve_Isd_list = []
        #Ids_list_num = []
        #derta_output_curve_Vcesat_list = []
        #derta_output_curve_Rdson_list = []
        is_Vgs_find_flag = False # 用来判断表格中是否有需要的Vgs值
        Vgs_list_num = 0 # 确定当前列表位置
        for Vgs in self.diode_output_curve_Vgs_list:
            if self.diode_output_curve_setup_data[0] == Vgs:
                is_Vgs_find_flag = True
                #Ids_num = 0 # 确定Ids列表的位置
                for tmp in self.diode_output_curve_Isd_list[Vgs_list_num]:
                    derta_diode_output_curve_Isd_list.append(abs(tmp - self.diode_output_curve_setup_data[1]))
                    #Ids_list_num.append(Ids_num)
                    #Ids_num += 1
                    l_Isd = derta_diode_output_curve_Isd_list.index(min(derta_diode_output_curve_Isd_list))
                    self.Vf = round((self.diode_output_curve_Vsd_list[Vgs_list_num][l_Isd]), 2) # Vcesat单位V
            else:
                Vgs_list_num += 1
        return

class GetVoltageCurveObject:
    '''
    存储Idss的相关数据与获取过程，专门给函数GetVoltageCurve()调用。
    '''
    def __init__(self):
        '''
        Idss读取中使用到的参数，随着读取过程更新
        '''
        self.Idss_Vds_set = 1200 # 默认1200V
        self.BV_Ids_set = float(2 / 1000) # 默认2mA

        self.Idss_all_list = [] # 包含Vds,Ids,其余杂项的整体列表
        self.Idss_Vds_list = [] # 只存储Vds的干净列表
        self.Idss_Ids_list = [] # 只存储Ids的干净列表

        self.Idss = 0 # 使用提纯后的列表，读取出栅极漏电流Idss的最终结果。
        self.BV = 0 # 使用提纯后的列表，读取出击穿电压BV的最终结果。


    def get_Idss_Vds_set(self, Voltage_Curve_set):
        '''
        修改Idss_Vds_set和BV_Ids_set的值
        '''
        self.Idss_Vds_set = float(Voltage_Curve_set[0])
        # 主函数中设置的Idss_VdsSet_6_1单位是V。
        self.BV_Ids_set = float(Voltage_Curve_set[1] / 1000)
        # 主函数中设置的BV_Ids_set_6_2单位是mA。

    def get_Idss_data(self, data):
        '''
        获取栅极开启阈值电压Vgsth的文件名、实验设置参数；
        获取栅极开启阈值电压Vgsth的实验数据，此数据较为粗糙，包含Igs,Vgs,Ids和其余杂项。
        '''
        end_storing_flag = False  # 用于判断是否停止存储数据，第一次数据存储结束后停止存储

        for row in data: # 用来将csv全部数据中的有效数据粗略的提取出来，以row控制每行读取
            if ('DataValue' not in row) and end_storing_flag:
                # 结束存储'
                break
            if 'DataName' in row:
                #self.Igss_all_list.append(row) # 注释此行，get_Igss_all_list列表中将不存储DataName一行
                end_storing_flag = True  # 确保不会再次读取到数据
                # 获取实验采集到的数据,读取到DataName时开始存储
                continue
            if 'DataValue' in row:
                self.Idss_all_list.append(row) # 获取实验采集到的数据
                continue
    
    def get_Idss_Ids_and_Vds_list(self):
        '''
        获取Ids与Vds的干净列表
        '''
        try:
            for row in self.Idss_all_list: # 将粗糙的列表数据提纯，以row控制每行读取
                self.Idss_Vds_list.append(float(row[4]))
                self.Idss_Ids_list.append(float(row[3]))
        except ValueError: # 避免数据出现空白位置，存储失败
            pass
        return

    def get_Idss(self):
        '''
        使用处理干净的列表，读取出栅极开启阈值电压Vgsth的最终结果。
        '''
        derta_Idss_Vds_list = []
        for tmp in self.Idss_Vds_list:
            derta_Idss_Vds_list.append(abs(tmp-self.Idss_Vds_set))
        l_Idss = derta_Idss_Vds_list.index(min(derta_Idss_Vds_list))
        self.Idss = round((self.Idss_Ids_list[l_Idss])*1000000 ,2)
        # 原始数据中单位为A，化为uA
        # 待优化3：可以使用线性差值法提高精度优化
        return
    
    def get_BV(self):
        '''
        使用处理干净的列表，读取击穿电压BV的最终结果。
        '''
        derta_BV_Ids_list = []
        for tmp in self.Idss_Ids_list:
            derta_BV_Ids_list.append(abs(tmp-self.BV_Ids_set))
        l_BV = derta_BV_Ids_list.index(min(derta_BV_Ids_list))
        self.BV = round((self.Idss_Vds_list[l_BV]) ,2)
        # 原始数据中单位为V
        # 待优化3：可以使用线性差值法提高精度优化
        return
    
def GetIgss(folder_path, Igss_Vgs_set):
    '''
    栅极漏电Igss其中s:short 短路
    测试方法：Vds = 0V，Vgs一定值(例如：20V)
    测量ge端的电流值Igs
    '''
    folder_list = GetFolderList(folder_path)
    for csv_tmp in folder_list:  # 使用csv_tmp循环读取列表中内容。
        print('正在处理：', csv_tmp)
        data = ReadCsvFile(folder_path + '\\' + csv_tmp)
        GetIgss = GetIgssObject() # 读取栅极漏电Igss文件
        GetIgss.get_Igss_Vgs_set(Igss_Vgs_set) # 更新Vgs的参数
        GetIgss.get_Igss_data(data) # 获取csv文件中的信息，次数据格式较为粗糙
        GetIgss.get_Igss_Vgs_and_Igs_list() # 数据格式提纯，获取Vgs与Igs
        GetIgss.get_Igss()
        print('Igss:', GetIgss.Igss, '(nA)')
        #print('处理完成：', csv_tmp)
        data_name_info = DataNameToInfo(csv_tmp)
        Igss_info = data_name_info + [folder_path.split('/')[-1], 'Igss_Vgs_set=' + str(Igss_Vgs_set) + '(V)', GetIgss.Igss]
        GetStaticData(Igss_info)
    return

def GetVgsth(folder_path, Vgsth_Ids_set):
    '''
    开启电压Vgsth其中th:threshold 阈值
    测试方法：Vds = Vgs不断升压，直到看到Ids大于某一值(例如：10mA)
    Ids的值由芯片的data sheet决定
    测量ge端的电压值Vgs
    '''
    folder_list = GetFolderList(folder_path)
    for csv_tmp in folder_list:  # 使用csv_tmp循环读取列表中内容。
        print('正在处理：', csv_tmp)
        data = ReadCsvFile(folder_path + '/' + csv_tmp)
        GetVgsth = GetVgsthObject()
        GetVgsth.get_Vgsth_Ids_set(Vgsth_Ids_set) # 更新Ids的参数
        GetVgsth.get_Vgsth_data(data)
        GetVgsth.get_Vgsth_Vgs_and_Ids_list()
        GetVgsth.get_Vgsth()
        print('Vgsth:', GetVgsth.Vgsth, '(V)')
        '''
        添加Vgsth_info的中间相获取
        由文件名得到项目名、模块号、测试回路、测试温度、测试项目、测试条件
        '''
        data_name_info = DataNameToInfo(csv_tmp)
        Vgsth_info = data_name_info + [folder_path.split('/')[-1], 'Vgsth_Ids_set=' + str(Vgsth_Ids_set) + '(mA)', GetVgsth.Vgsth]
        GetStaticData(Vgsth_info)
    return

def GetOutputCurve(folder_path, output_curve_set):
    '''
    输出曲线
    output_curve_set为列表形式存储，分别存储RdsonVcesat_VgsSet_3, RdsonVcesat_IdsSet_3
    表示读取的Vgs与Ids位置
    '''
    folder_list = GetFolderList(folder_path)
    for csv_tmp in folder_list:  # 使用csv_tmp循环读取列表中内容。
        print('正在处理：', csv_tmp)
        data = ReadCsvFile(folder_path + '/' + csv_tmp)
        GetOutputCurve = GetOutputCurveObject()
        GetOutputCurve.get_output_curve_set(output_curve_set) # 更新输出曲线的读取条件
        GetOutputCurve.get_output_curve_data(data)
        GetOutputCurve.get_output_curve_list() # 数据格式提纯，获得Ids、Vds、Vgs、Rdson的干净列表
        GetOutputCurve.get_Rdson()
        print('Rdson:', GetOutputCurve.Rdson, '(mΩ)')
        print('Vcesat:', GetOutputCurve.Vcesat, '(V)')
        data_name_info = DataNameToInfo(csv_tmp)
        output_curve_info = data_name_info + [folder_path.split('/')[-1], 'Vgs='+str(output_curve_set[0])+'(V)'+
                                                          ' Ids='+str(output_curve_set[1])+'(A)', [GetOutputCurve.Rdson,GetOutputCurve.Vcesat]]
        GetStaticData(output_curve_info)
    return

def GetTransferCurve():
    '''
    待添加
    '''
    print('4.计算转移曲线 功能编写中')
    return

def GetDiodeOutputCurve(folder_path, diode_output_curve_set):
    '''
    二极管输出曲线
    '''
    folder_list = GetFolderList(folder_path)
    for csv_tmp in folder_list:  # 使用csv_tmp循环读取列表中内容。
        print('正在处理：', csv_tmp)
        data = ReadCsvFile(folder_path + '/' + csv_tmp)
        GetDiodeOutputCurve = GetDiodeOutputCurveObject()
        GetDiodeOutputCurve.get_diode_output_curve_set(diode_output_curve_set) # 更新输出曲线的读取条件
        GetDiodeOutputCurve.get_diode_output_curve_data(data)
        GetDiodeOutputCurve.get_diode_output_curve_list() # 数据格式提纯，获得Ids、Vds、Vgs、Rdson的干净列表
        GetDiodeOutputCurve.get_Vf()
        print('Vcesat:', GetDiodeOutputCurve.Vf, '(V)')
        data_name_info = DataNameToInfo(csv_tmp)
        diode_output_curve_info = data_name_info + [folder_path.split('/')[-1], 'Vgs='+str(diode_output_curve_set[0])+'(V)'+
                                                          ' Isd='+str(diode_output_curve_set[1])+'(A)', GetDiodeOutputCurve.Vf]
        GetStaticData(diode_output_curve_info)
    return

def GetIdss(folder_path, Voltage_Curve_set):
    '''
    耐压曲线Idss或Ices
    '''
    folder_list = GetFolderList(folder_path)
    for csv_tmp in folder_list:  # 使用csv_tmp循环读取列表中内容。
        print('正在处理：', csv_tmp)
        data = ReadCsvFile(folder_path + '/' + csv_tmp)
        GetIdss = GetVoltageCurveObject()
        GetIdss.get_Idss_Vds_set(Voltage_Curve_set) # 更新Ids的参数
        GetIdss.get_Idss_data(data)
        GetIdss.get_Idss_Ids_and_Vds_list()
        GetIdss.get_Idss()
        GetIdss.get_BV()
        print('Idss:', GetIdss.Idss, '(uA)')
        print('BV:', GetIdss.BV, '(V)')

        #添加Idss_info的中间相获取
        #由文件名得到项目名、模块号、测试回路、测试温度、测试项目、测试条件
        data_name_info = DataNameToInfo(csv_tmp)
        Ids_info = data_name_info + [folder_path.split('/')[-1], ['Idss_Vds_set=' + str(Voltage_Curve_set[0]) + '(V)', 
                                                                  'BV_Ids_set=' + str(Voltage_Curve_set[1]) + '(mA)'], [GetIdss.Idss, GetIdss.BV]]
        GetStaticData(Ids_info)
        #写到这了，该将结果打印出来了
    return

def DataNameToInfo(file_path):
    '''
    读取某一文件名后，输出其中关键信息
    '''
    #print(file_path)
    start_flag = ' '
    end_flag = '; '
    # 以如下静态测试命名规则为例，使用' _'作为文件名的读取开始，'_; '作为结束，截取干净的文件命名
    # 开启Vgs=Vds [(1) _钱塘江-061-Q1-175C_; 11_16_2023 2_33_14 PM].csv
    #print(file_path.index(start_flag))
    #print(file_path.index(end_flag))
    clear_name = file_path[file_path.index(start_flag) + 2:file_path.index(end_flag)]
    #  + 2是因为[a:b]切片过程中，a截取的结果中包含截取部分，而b部分不包括，index返回值为第一次检索到目标字符串位置
    #print(clear_name)
    #print(clear_name.split('-')) # 使用小写减号-将干净的文件名拆分，确定其中包含多少关键信息
    if len(clear_name.split('-')) == 4:
        data_name_info = clear_name.split('-')
        # 确定文件名中的信息为：项目名称、模块号、测试回路、测试温度
    else :
        data_name_info = [clear_name, clear_name, clear_name, clear_name]
    return data_name_info[1:4] # 返回值不包括文件名，只保留模块编号、回路、温度就够了

def GetFolderList(folder_path):
    folder_list = os.listdir(folder_path)  # 将待处理文件夹目录中，全部的文件名称以列表形式存储。
    return folder_list

def ReadCsvFile(file_path):
    '''
    读取csv文件并返回数据列表，从'TIME'行开始存储数据。
    输入参数
    file_path: 从示波器中保存的csv文件。
    输出参数
    data: 包含csv文件全部数据的列表。
    '''
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print("错误代码1：找不到文件。", file_path)
    return data

def GetAllFolderPath(folder_path_root):
    '''
    获取各静态数据文件夹目录，需要确保每个文件夹命名正确
    '''
    folder_path_list = []

    folder_path_Igss_R_1_1 = folder_path_root + '\\1.1.Igss负\\csv'
    folder_path_Igss_1_2 = folder_path_root + '\\1.2.Igss正\\csv'
    folder_path_Vgsth_2 = folder_path_root + '\\2.Vth_双源\\csv'
    folder_path_output_curve_3 = folder_path_root + '\\3.Rds(on)\\csv'
    folder_path_Transfer_curve_4 = folder_path_root + '\\4.转移曲线\\csv'
    folder_path_diode_output_curve_R_5 = folder_path_root + '\\5.Vf负\\csv'
    folder_path_diode_output_curve_5_2 = folder_path_root + '\\5.Vf正\\csv'
    folder_path_Idses_6 = folder_path_root + '\\6.Idss\\csv'

    folder_path_list.append(folder_path_Igss_R_1_1)
    folder_path_list.append(folder_path_Igss_1_2)
    folder_path_list.append(folder_path_Vgsth_2)
    folder_path_list.append(folder_path_output_curve_3)
    folder_path_list.append(folder_path_Transfer_curve_4)
    folder_path_list.append(folder_path_diode_output_curve_R_5)
    folder_path_list.append(folder_path_diode_output_curve_5_2)
    folder_path_list.append(folder_path_Idses_6)
    return folder_path_list

def GetStaticData(static_data_list):
    '''
    全部的静态数据读取结束后汇总
    格式如下：
    0:Item测试内容
    1:Unit单位，若是Rdson，需要MOSFET和IGBT区分，以列表形式存储mΩ和V
    2:ModuleNum模块编号
    3:Loop测试回路
    4:Temp测试温度
    5:文件目录，该项只为判断测试内容，不写入最终csv表格
    6:Condition测试条件
    7:Values测试结果
    '''

    
    #print(static_data_list)
    l_folder_path = 3 # 文件夹目录在static_data_list的位置
    if '1.1.Igss负' in static_data_list[l_folder_path]:
        G_Igss_or_Iges_Negative_1_1.append([['Igss-', 'Iges-'], 'nA'] + static_data_list)
        print('1.1.Igss负 信息+1')
    elif '1.2.Igss正' in static_data_list[l_folder_path]:
        G_Igss_or_Iges_Positive_1_2.append([['Igss+', 'Iges+'], 'nA'] + static_data_list)
        print('1.2.Igss正 信息+1')
    elif '2.Vth_双源' in static_data_list[l_folder_path]:
        G_Vgsth_or_Vgeth_2.append([['Vgsth', 'Vgeth'], 'V'] + static_data_list)
        print('2.Vth_双源 信息+1')
    elif '3.Rds(on)' in static_data_list[l_folder_path]:
        G_Rdson_or_Vcesat_3.append([['Rdson', 'Vcesat'], ['mΩ', 'V']] + static_data_list)
        print('3.Rds(on) 信息+1')
    elif '5.Vf负' in static_data_list[l_folder_path]:
        G_Vf_VgsNegative_5_1.append(['Vf-', 'V'] + static_data_list)
        print('5.Vf负 信息+1')
    elif '5.Vf正' in static_data_list[l_folder_path]:
        G_Vf_VgsPositive_5_2.append(['Vf+', 'V'] + static_data_list)
        print('5.Vf正 信息+1')
    elif '6.Idss' in static_data_list[l_folder_path]:
        G_Idss_or_Ices_6.append([['Idss', 'Ices'], 'uA'] + static_data_list)
        print('6.Idss 信息+1')
    else :
        pass


    return 

def GetToBeWrite(is_MOSFET_or_IGBT):
    '''
    使用函数GetStaticData里更新的全局变量，更新列表G_To_Be_Write
    更新后的表格可以直接写入csv文件
    '''
    flag = 0 if is_MOSFET_or_IGBT == 'MOSFET' else 1
    
    for row in G_Vgsth_or_Vgeth_2:
        G_To_Be_Write.append([row[0][flag], row[6], row[3],row[4], row[7], row[1], row[2]])
    for row in G_Igss_or_Iges_Positive_1_2:
        G_To_Be_Write.append([row[0][flag], row[6], row[3],row[4], row[7], row[1], row[2]])
    for row in G_Igss_or_Iges_Negative_1_1:
        G_To_Be_Write.append([row[0][flag], row[6], row[3],row[4], row[7], row[1], row[2]])
    for row in G_Idss_or_Ices_6: # 写入Idss相关数据
        G_To_Be_Write.append([row[0][flag], row[6][0], row[3],row[4], row[7][0], row[1], row[2]])
    for row in G_Idss_or_Ices_6: # 写入BV相关数据
        G_To_Be_Write.append(['BV', row[6][1], row[3],row[4], row[7][1], 'V', row[2]])
    for row in G_Rdson_or_Vcesat_3:
        G_To_Be_Write.append([row[0][flag], row[6], row[3],row[4], row[7][flag], row[1][flag], row[2]])
    for row in G_Vf_VgsNegative_5_1:
        G_To_Be_Write.append([row[0], row[6], row[3],row[4], row[7], row[1], row[2]])
    for row in G_Vf_VgsPositive_5_2:
        G_To_Be_Write.append([row[0], row[6], row[3],row[4], row[7], row[1], row[2]])

    # 创建 DataFrame
    df = pd.DataFrame(G_To_Be_Write, columns=['名称', '项目', '状态', '温度', '数值', '单位', '类型'])

    # 提取原始顺序中的唯一名称和项目组合
    name_project_order = list(OrderedDict.fromkeys([(row[0], row[1]) for row in G_To_Be_Write]))

    for name, project in name_project_order:
        # 获取对应的组
        group = df[(df['名称'] == name) & (df['项目'] == project)]
        unit = group['单位'].iloc[0]
        device_type = group['类型'].iloc[0]
        
        # 收集所有温度
        temps = group['温度'].unique()
        
        # 添加 -40C 行，放在 025C 之前
        G_result.append([name, project, '-40C', 'HIGH', 'LOW', 0, 0, unit, device_type])
        
        # 处理现有温度，按特定顺序排序
        temp_order = ['-40C', '025C', '175C']  # 这里 -40C 已经添加，所以从现有温度中排除
        existing_temps = [temp for temp in temps if temp in temp_order[1:]]  # 只考虑 025C 和 175C
        
        # 按照 025C、175C 的顺序处理
        for temp in existing_temps:
            new_row = [name, project, temp, 'HIGH', 'LOW', 0, 0, unit, device_type]
            
            # 查找匹配的 HIGH 和 LOW 值填充到新行中
            high_value = group[(group['温度'] == temp) & (group['状态'] == 'HIGH')]['数值'].values[0] if not group[(group['温度'] == temp) & (group['状态'] == 'HIGH')].empty else 0
            low_value = group[(group['温度'] == temp) & (group['状态'] == 'LOW')]['数值'].values[0] if not group[(group['温度'] == temp) & (group['状态'] == 'LOW')].empty else 0
            
            new_row[5] = high_value
            new_row[6] = low_value
            
            G_result.append(new_row)

    return

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

def FileWrite(file_out):
    '''
    将最终结果写入csv文件中
    '''
    # 这里将全局变量重新排序
    try:
        # 尝试以utf-8-sig编码读取文件，使用errors='replace'处理不可解码字符
        with open(file_out, 'r', encoding='utf-8-sig', errors='replace', newline='') as f_out:
            csv_reader = csv.reader(f_out)
            li_PanDuan = list(csv_reader)

        # 检查文件头是否符合预期
        expected_header = ['Item', 'Condition', 'Temp', 'Loop1', 'Loop2', 'Values1', 'Values2', 'Unit', 'ModuleNum']
        if not li_PanDuan or li_PanDuan[0] != expected_header:
            #print(f'表格{file_out}格式有问题，需要重新构建表格。')
            with open(file_out, 'w', encoding='utf-8-sig', newline='') as f_out:
                csv_writer = csv.writer(f_out)
                csv_writer.writerow(expected_header)

        # 追加数据
        with open(file_out, 'a', encoding='utf-8-sig', newline='') as f_out:
            csv_writer = csv.writer(f_out)
            for row in G_result:
                csv_writer.writerow(row)

        return True
    except Exception as e:
        print(f"发生错误: {e}")
        return False
    
if __name__ == "__main__":
    global G_Igss_or_Iges_1_1, G_Igss_or_Iges_R_1_2, G_Vgsth_or_Vgeth_2, G_Rdson_or_Vcesat_3
    global G_Vf_VgsNegative_5_1, G_Vf_VgsPositive_5_2, G_Idss_or_Ices_6, G_To_Be_Write, G_result

    G_Igss_or_Iges_Negative_1_1 = []
    G_Igss_or_Iges_Positive_1_2 = []
    G_Vgsth_or_Vgeth_2 = []
    G_Rdson_or_Vcesat_3 = []
    G_Vf_VgsNegative_5_1 = []
    G_Vf_VgsPositive_5_2 = []
    G_Idss_or_Ices_6 = []
    G_To_Be_Write = []
    G_result = []
    
    FolderPathRoot = r"D:\File\0.公司相关\1.1.黄山MOSFET\8并1200V\20.黄山BC档 Datasheet制作\1.静态\BC47"
    FileOut = r'D:\File\0.公司相关\1.1.黄山MOSFET\8并1200V\20.黄山BC档 Datasheet制作\1.静态\BC47\静态参数自动读取.csv'
    FolderPathList = GetAllFolderPath(FolderPathRoot)
    IsMOSFETorIGBT = ['MOSFET', 'IGBT'][0]

    '''
    IgssNegative_VgsSet_1_1 = -10 # 1.2栅极漏电-反向测试中，Vgs的设置值，单位V。
    IgssPositive_VgsSet_1_2 = 22 # 1.1栅极漏电-正向测试中，Vgs的设置值，单位V。
    Vgsth_IdsSet_2 = 80 # 2.Vth_双源测试中，Ids的设置值，单位mA。
    RdsonVcesat_VgsSet_3 = 18  # 3.Rds(on)测试中，Vgs的设置值，单位V。
    RdsonVcesat_IdsSet_3 = 800  # 3.Rds(on)测试中，Ids的设置值，单位A。
    Vf_VgsSet_Negative_5_1 = -5  # 5.Vf负测试中，Vgs的设置值，单位V。
    Vf_IsdSet_Negative_5_1 = 800  # 5.Vf负测试中，Isd的设置值，单位A。
    Vf_VgsSet_Positive_5_2 = 18  # 5.2.二极管输出曲线(正向)测试中，Vgs的设置值，单位V。
    Vf_IsdSet_Positive_5_2 = 800  # 5.2.二极管输出曲线(正向)测试中，Isd的设置值，单位A。
    Idss_VdsSet_6_1 = 1200 # 6.1.Idss测试中，Vds的设置值，单位V。
    BV_IdsSet_6_2 = 2 # 6.2.击穿电压BV测试中，Ids的设置值，单位mA。
    # ST专用
    '''

    
    IgssNegative_VgsSet_1_1 = -4 # 1.2栅极漏电-反向测试中，Vgs的设置值，单位V。
    IgssPositive_VgsSet_1_2 = 21 # 1.1栅极漏电-正向测试中，Vgs的设置值，单位V。
    Vgsth_IdsSet_2 = 100 # 2.Vth_双源测试中，Ids的设置值，单位mA。
    RdsonVcesat_VgsSet_3 = 18  # 3.Rds(on)测试中，Vgs的设置值，单位V。
    RdsonVcesat_IdsSet_3 = 550  # 3.Rds(on)测试中，Ids的设置值，单位A。
    Vf_VgsSet_Negative_5_1 = -2  # 5.Vf负测试中，Vgs的设置值，单位V。
    Vf_IsdSet_Negative_5_1 = 360  # 5.Vf负测试中，Isd的设置值，单位A。
    Vf_VgsSet_Positive_5_2 = 18  # 5.2.二极管输出曲线(正向)测试中，Vgs的设置值，单位V。
    Vf_IsdSet_Positive_5_2 = 360  # 5.2.二极管输出曲线(正向)测试中，Isd的设置值，单位A。
    Idss_VdsSet_6_1 = 1200 # 6.1.Idss测试中，Vds的设置值，单位V。
    BV_IdsSet_6_2 = 2 # 6.2.击穿电压BV测试中，Ids的设置值，单位mA。
    # Rohm专用
    

    '''
    IgssNegative_VgsSet_1_1 = -4 # 1.2栅极漏电-反向测试中，Vgs的设置值，单位V。
    IgssPositive_VgsSet_1_2 = 15 # 1.1栅极漏电-正向测试中，Vgs的设置值，单位V。
    Vgsth_IdsSet_2 = 99.9 # 2.Vth_双源测试中，Ids的设置值，单位mA。
    RdsonVcesat_VgsSet_3 = 15  # 3.Rds(on)测试中，Vgs的设置值，单位V。
    RdsonVcesat_IdsSet_3 = 580.8  # 3.Rds(on)测试中，Ids的设置值，单位A。
    Vf_VgsSet_Negative_5_1 = -4  # 5.Vf负测试中，Vgs的设置值，单位V。
    Vf_IsdSet_Negative_5_1 = 290  # 5.Vf负测试中，Isd的设置值，单位A。
    Vf_VgsSet_Positive_5_2 = 15  # 5.2.二极管输出曲线(正向)测试中，Vgs的设置值，单位V。
    Vf_IsdSet_Positive_5_2 = 290  # 5.2.二极管输出曲线(正向)测试中，Isd的设置值，单位A。
    Idss_VdsSet_6_1 = 1200 # 6.1.Idss测试中，Vds的设置值，单位V。
    BV_IdsSet_6_2 = 2 # 6.2.击穿电压BV测试中，Ids的设置值，单位mA。
    # DFS专用
    '''

    print()
    print('1.1.Igss负')
    GetIgss(folder_path = FolderPathList[0], Igss_Vgs_set = IgssNegative_VgsSet_1_1)
    print()
    print('1.2.Igss正')
    GetIgss(folder_path = FolderPathList[1], Igss_Vgs_set = IgssPositive_VgsSet_1_2)
    print()
    print('2.Vth_双源')
    GetVgsth(folder_path = FolderPathList[2], Vgsth_Ids_set = Vgsth_IdsSet_2)
    print()
    print('3.Rds(on)')
    GetOutputCurve(folder_path = FolderPathList[3], output_curve_set = [RdsonVcesat_VgsSet_3, RdsonVcesat_IdsSet_3])
    print()
    print('5.Vf负')
    GetDiodeOutputCurve(folder_path = FolderPathList[5], diode_output_curve_set = [Vf_VgsSet_Negative_5_1, Vf_IsdSet_Negative_5_1])
    print()
    print('5.Vf正')
    GetDiodeOutputCurve(folder_path = FolderPathList[6], diode_output_curve_set = [Vf_VgsSet_Positive_5_2, Vf_IsdSet_Positive_5_2])
    print()
    print('6.Idss')
    GetIdss(folder_path = FolderPathList[7], Voltage_Curve_set = [Idss_VdsSet_6_1, BV_IdsSet_6_2])
    print()
    GetToBeWrite(IsMOSFETorIGBT)
    
    FileWrite(CreateCSVFile(FolderPathRoot))