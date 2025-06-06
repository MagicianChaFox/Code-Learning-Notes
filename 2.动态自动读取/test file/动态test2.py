#该函数主要负责波形处理相关的功能
#ExtractWaveData() 3个优化点
#class GetDynamicDataObject 4个优化点

import scipy.signal as sgn
import matplotlib.pyplot as plt
import numpy as np

class GetDynamicDataObject:
    '''
    专门给函数GetDynamicData()调用的类，通过将不同的参数计算方法写成不同的函数。
    '''
    def __init__(self):
        '''
        使用__init__方法来定义类中会使用到的参数默认值
        '''
        self.Vge_error = 0  # Vge波形是否有错误的判断参数

        self.VgsR = -50  # 经过上下桥判断后，确认当前的栅极负压，默认为-50.0

        self.tl_1_on = 0  # tl表示时间在表格中的位置
        self.tl_1_off = 0  # 这4个时间节点都只是做一个大致的时间段划分
        self.tl_2_on = 0
        self.tl_2_off = 0
        self.tl_midpoint_1 = 0 # 一开与一关的中点
        self.tl_midpoint_2 = 0 # 一关与二开的中点
        self.tl_midpoint_3 = 0 # 二开与二关的中点
        self.tl_on1_off1_Vgs_dvdt_var_min = 0 # Vgs信号波动最小点，取均值作为Vgs+ 待优化

        self.Vge_stable = 0  # 整个开关过程中，Vge高电压的稳定值

        self.Ic_off = 0  # 第一次关断时，电流值最大值
        self.Ic_on = 0  # 第二次开通时，电流反向恢复后的最小值
        self.Irm_on = 0  # 第二次开通时，电流反向恢复的最大值
        self.tl_Irm_on = 0  # 第二次开通时，电流反向恢复的最大值位置
        self.tl_Ic_off = 0  # 第一次关断时，关断电流在列表中出现的位置
        # self.tl_Ic_off暂时不用，有需要可以在getl_Ic_off函数中取消注释

        self.Vce_stable = 0  # 两次开关间隔期间，电压Vce的均值
        self.Vpeak = 0  # 第一次关断时电压尖峰
        self.tl_Vpeak = 0  # 第一次关断时，电压尖峰在列表中出现的位置

        self.tl_on_01Vge = 0  # 以下时间节点的解释见下方函数,tl表示时间在表格中的位置
        self.tl_on_01Ic = 0  # get_key_time_2()中的注释有写到
        self.tl_on_02Ic = 0  
        self.tl_on_03Ic = 0  
        self.tl_on_07Ic = 0  
        self.tl_on_08Ic = 0  
        self.tl_on_09Ic = 0
        self.tl_on_didt_max = 0  # 由滤波后导数得到
        self.tl_on_didt_max_L = 0  # tl_on_didt_max向前推2.5ns，具体数值可修改
        self.tl_on_didt_max_R = 0

        self.tl_on_09Vce = 0
        self.tl_on_08Vce = 0
        self.tl_on_07Vce = 0
        self.tl_on_03Vce = 0
        self.tl_on_02Vce = 0
        self.tl_on_01Vce = 0
        self.tl_on_002Vce = 0
        self.tl_on_dvdt_max_L = 0
        self.tl_on_dvdt_max_R = 0
        self.tl_off1_on2_Vds_dvdt_var_min = 0 # 一关与二开之间，Vds波动最小点，取均值作为Vbus 待优化

        self.tl_off_09Vge = 0
        self.tl_off_09Ic = 0
        self.tl_off_08Ic = 0
        self.tl_off_07Ic = 0
        self.tl_off_03Ic = 0
        self.tl_off_02Ic = 0
        self.tl_off_01Ic = 0
        self.tl_off_002Ic = 0
        self.tl_off_didt_max_L = 0
        self.tl_off_didt_max_R = 0

        self.tl_off_01Vce = 0
        self.tl_off_02Vce = 0
        self.tl_off_03Vce = 0
        self.tl_off_07Vce = 0
        self.tl_off_08Vce = 0
        self.tl_off_09Vce = 0
        self.tl_off_dvdt_max_L = 0
        self.tl_off_dvdt_max_R = 0

        self.tdon = 0
        self.tr = 0  
        self.ton = 0  # 完整的开通时间
        self.Eon = 0

        self.didt_on_01_09 = 0  
        self.dvdt_on_09_01 = 0  
        self.didt_on_02_08 = 0  
        self.dvdt_on_08_02 = 0 
        self.didt_on_03_07 = 0  
        self.dvdt_on_07_03 = 0 
        self.didt_on_max = 0  
        self.dvdt_on_max = 0 
        self.time_didt_on_max = 0
        self.time_dvdt_on_max = 0

        self.tdoff = 0
        self.tf = 0
        self.toff = 0  # 完整的关断时间
        self.Eoff = 0

        self.didt_off_09_01 = 0
        self.dvdt_off_01_09 = 0
        self.didt_off_08_02 = 0
        self.dvdt_off_02_08 = 0
        self.didt_off_07_03 = 0
        self.dvdt_off_03_07 = 0
        self.didt_off_max = 0
        self.dvdt_off_max = 0
        self.time_didt_off_max = 0
        self.time_dvdt_off_max = 0

        self.tl_on_If_max = 0 # 二极管反向恢复电流，开通时下降前的最大值位置(正电流)
        self.tl_on_05If_max = 0 # 50%二极管电流最大值在列表中的位置（正电流）
        self.tl_on_00If = 0 # 二极管电流经过0的时候在列表中的位置（零电流）
        self.tl_on_05If_min = 0 # 50%二极管电流最小值在列表中的位置（负电流）
        self.tl_on_If_min = 0 # 二极管反向恢复电流最小值在列表中的位置（负电流）
        self.tl_on_09If_min = 0 # 90%二极管反向恢复电流最小值在列表中的位置（负电流）
        self.tl_on_025If_min = 0 # 25%二极管反向恢复电流最小值在列表中的位置（负电流）
        self.tl_on_002If_min = 0 # 2%二极管反向恢复电流最小值在列表中的位置（负电流）
        self.tl_on_trr_right = 0 # 反向恢复时间，由on_09If_min和on_025If_min一起计算
        self.tl_on_01Vf = 0 # 10%二极管反向恢复电压均值
        self.tl_on_09Vf = 0 # 90%二极管反向恢复电压均值
        self.tl_on_Vrrm_FS = 0 # 反向恢复电压第一次达到尖峰

        self.Vf_stable = 0 # 二极管电压均值（暂时用Vce均值代替，后面迭代
        self.on_If_max = 0 # 二极管反向恢复电流，开通时下降前的最大值(正电流)
        self.on_If_min = 0 # 二极管反向恢复电流最小值在列表中的位置（负电流）
        self.on_09If_min = 0 # 90%二极管反向恢复电流最小值的值（负电流），与on_025If_min一起计算trr
        self.on_025If_min = 0 # 25%二极管反向恢复电流最小值的值（负电流），与on_09If_min一起计算trr

        self.Vge_D_MAX_on = 0 # 对管栅极开通时电压最大值
        self.Vge_D_MIN_off = 0 # 对管栅极关断时电压最小值

        self.ti = 0 # 二极管反向恢复时间（长
        self.trr = 0 # 二极管反向恢复时间（短
        self.Vf_max = 0 # 二极管反向恢复电压最大值
        self.Irrm = 0 # 二极管反向恢复电流
        self.didt_rr_05_05 = 0 # 二极管反向恢复电流变化率
        self.dvdt_rr_01_09 = 0 # 二极管反向恢复电压变化率
        self.dvdt_rr_01_fs = 0 
        self.dvdt_rr_max = 0 
        self.Qrr = 0 # 二极管反向恢复电荷
        self.Erec = 0 # 二极管反向恢复损耗
        self.time_dvdt_rrm_max = 0

    def get_key_time(self, VgsR, Vgs):
        '''
        先判断Vge波形是否正常
        在Vge正常的情况下，使用Vge大致得到两次的开关时间点
        再根据这4个时间节点进行更精细的计算
        '''
        self.VgsR = VgsR  #  更新栅极负压数据，后期计算串扰时使用
        G_Vge_Filtered = LowPassFilter(G_Vge, fs=6.25e9, f_max=5e7)
        
        #Vge_high = Vge_high_1
        #Vge_low = Vge_low_1
        Vge_high = Vgs - 4.5
        Vge_low = VgsR + 1.5
        if max(G_Vge_Filtered) > Vge_high and min(G_Vge_Filtered) < Vge_low:
            tmp = 0  # 用来在之后的循环中确定各个时间节点位置的计数器。
            narrow_pulse_flag = 0 # 用来确定窄脉宽抑制的节点
            while tmp < len(G_T):
                if G_Vge_Filtered[tmp] > Vge_high:  # 找到第一个Vge大于10V的点，作为第一次开通的时间点
                    self.tl_1_on = tmp
                    break
                else:
                    tmp += 1
            while tmp < len(G_T):  # 找到第一个Vge小于0V的点，作为第一次关断的时间点
                if G_Vge_Filtered[tmp] < Vge_low:
                    self.tl_1_off = tmp
                    break
                else:
                    tmp += 1
            while tmp < len(G_T):
                if G_Vge_Filtered[tmp] > Vge_high:  # 找到第二个Vge大于10V的点，作为第二次开通的时间点
                    self.tl_2_on = tmp
                    break
                else:
                    tmp += 1
            while tmp < len(G_T):  # 找到第二个Vge小于0V的点，作为第二次关断的时间点
                if G_Vge_Filtered[tmp] < Vge_low:
                    self.tl_2_off = tmp
                    break
                else:
                    tmp += 1
            self.tl_midpoint_1 = int(0.5 * self.tl_1_on + 0.5 * self.tl_1_off)
            #self.tl_midpoint_2 = int(0.2 * self.tl_1_off + 0.8 *  self.tl_2_on)
            #self.tl_midpoint_2 = int(0.5 * self.tl_1_off + 0.5 * self.tl_2_on)
            #self.tl_midpoint_2 = int(self.tl_1_off)
            self.tl_midpoint_3 = int(0.5 * self.tl_2_on + 0.5 * self.tl_2_off)

            midpoint_2_var_list = []
            midpoint_2_tl_list = []
            tmp = 0.1
            while tmp < 0.7:
                tl_midpoint_2_tmp = int(tmp * self.tl_2_on + (1 - tmp) * self.tl_1_off)

                midpoint_2_var = np.var(G_Vge[tl_midpoint_2_tmp : tl_midpoint_2_tmp + 1000])
                midpoint_2_var_list.append(midpoint_2_var)
                midpoint_2_tl_list.append(tl_midpoint_2_tmp)
                #print(int(tmp * 100), '%，列表位置：', int(tl_midpoint_2_tmp), '，方差：', round((midpoint_2_var), 4), '，Vgs：', round((G_Vge[tl_midpoint_2_tmp]), 2))
                tmp += 0.1    
            # 找到 midpoint_2_var_list 中的最小值及其索引
            min_var = min(midpoint_2_var_list)
            index = midpoint_2_var_list.index(min_var)
            # 获取对应位置的 midpoint_2_tl_list 值
            corresponding_mean = midpoint_2_tl_list[index]
            self.tl_midpoint_2 = int(corresponding_mean)
            #print(f"midpoint_2_var_list 中的最小值是: {min_var}")
            #print(f"对应的列表位置是: {self.tl_midpoint_2}")
            #print('位置：', midpoint_2_tl_list)
            #print('方差：', midpoint_2_var_list)
            '''
            print('self.tl_1_on:', self.tl_1_on)
            print('self.tl_1_off:', self.tl_1_off)
            print('self.tl_2_on:', self.tl_2_on)
            print('self.tl_2_off:', self.tl_2_off)

            plt.rc('font', family='simhei', size=15)  # 设置中文显示，字体大小
            plt.rc('axes', unicode_minus=False)  # 该参数解决负号显示的问题
            plt.figure(num=1)

            wave_list = [G_T, G_Vge, G_Vce, G_Ic, G_Vf, G_If]
            wave_name = ['TimeLine', 'Vgs', 'Vds', 'Ids', 'Vrrm', 'Irrm']
            wave_show = 1

            #plt.plot(G_T, wave_list[wave_show], 'y-', label = wave_name[wave_show])
            #plt.plot(G_T, LowPassFilter(wave_list[wave_show], fs=6.25e9, f_max=1e8), 'b-', label = wave_name[wave_show] + ' 100M 滤波')
            plt.plot(G_T, LowPassFilter(wave_list[wave_show], fs=6.25e9, f_max=5e7), 'b-', label = wave_name[wave_show] + ' 50M 滤波')
            #plt.plot(G_T, LowPassFilter(Derivatives(wave_list[wave_show]), fs=6.25e9, f_max=1e8), 'g-', label = wave_name[wave_show] + ' 100M 求导')
            
            plt.plot(G_T[self.tl_1_on], G_Vge[self.tl_1_on], 'g-', label='1开', marker = 'o')
            plt.plot(G_T[self.tl_1_off], G_Vge[self.tl_1_off], 'g-', label='1关', marker = 'o')
            plt.plot(G_T[self.tl_2_on], G_Vge[self.tl_2_on], 'g-', label='2开', marker = 'o')
            plt.plot(G_T[self.tl_2_off], G_Vge[self.tl_2_off], 'g-', label='2关', marker = 'o')
            plt.plot(G_T[self.tl_midpoint_1], G_Vge[self.tl_midpoint_1], 'r-', label='1隔断', marker = 'o')
            plt.plot(G_T[self.tl_midpoint_2], G_Vge[self.tl_midpoint_2], 'r-', label='2隔断', marker = 'o')
            plt.plot(G_T[self.tl_midpoint_3], G_Vge[self.tl_midpoint_3], 'r-', label='3隔断', marker = 'o')
            plt.legend(loc='best')
            plt.title('测试阶段波形展示')
            plt.show()
            '''
            
            '''
            # 以下代码测试中使用
            print('粗略确定两次开关时间')
            print('tl_1_on:', self.tl_1_on,':',G_T[self.tl_1_on],'us')
            print('tl_1_off:', self.tl_1_off,':',G_T[self.tl_1_off],'us')
            print('tl_2_on:', self.tl_2_on,':',G_T[self.tl_2_on],'us')
            print('tl_2_off:', self.tl_2_off,':',G_T[self.tl_2_off],'us')
            print('中间点1:', self.tl_midpoint_1,':',G_T[self.tl_midpoint_1],'us')
            print('中间点2:', self.tl_midpoint_2,':',G_T[self.tl_midpoint_2],'us')
            print('中间点3:', self.tl_midpoint_3,':',G_T[self.tl_midpoint_3],'us')
            print()
            '''
        else:
            print('def_wave - class GetDynamicDataObject - get_key_time函数错误：Vgs设定值超出波形范围。')
            self.Vge_error = 1

        error_flag_1 = self.tl_1_on == self.tl_1_off or self.tl_1_on == self.tl_2_on or self.tl_1_on == self.tl_2_off
        error_flag_2 = self.tl_1_off == self.tl_2_on or self.tl_1_off == self.tl_2_off or self.tl_2_on == self.tl_2_off
        if error_flag_1 or error_flag_2: # 一一对比4个参数，如果发现有一样的说明Vge存在重合问题。
            print('def_wave - class GetDynamicDataObject - get_key_time函数错误：开关点存在重合，无法读取。')
            self.Vge_error = 1
        return

    def calibration_timeline(self):
        '''
        使用第二次开通时的波形校准时间轴
        Vce下降时的斜率变化点
        Vf上升时的斜率变化点
        Ic的最大值
        '''
        # 待优化def_wave - class GetDynamicDataObject - calibration_timeline：添加时间轴校准功能
        # 可以使用斜率，寻找最大值或最小值
        # 调整全局变量
        pass
        return
    
    def get_Vge_stable(self):
        self.Vge_stable = np.mean(G_Vge[self.tl_midpoint_1:self.tl_midpoint_1 + 50])
        # 计算Vge的稳定值，在一开和一关的中点处，向右取400个数据取平均值当做Vge稳定值
        # 待优化def_wave - class GetDynamicDataObject - get_Vge_stable：增加Vge的低电压值判断
        # 待优化def_wave - class GetDynamicDataObject - get_Vge_stable：Vge高电压判断逻辑，考虑到宅脉宽情况
        self.Vge_stable = round((self.Vge_stable), 2)

        Vgs_mean_list = []
        tmp = 0.1
        while tmp < 1:
            tl_Vgs_tmp = int(tmp * self.tl_1_off + (1 - tmp) * self.tl_1_on)
            Vgs_mean = np.mean(G_Vge[tl_Vgs_tmp : tl_Vgs_tmp + 50])
            Vgs_mean_list.append(Vgs_mean)
            #print(int(tmp * 100), '%1开1关 均值：', round((Vgs_mean), 2))
            tmp += 0.1        
        max_mean = max(Vgs_mean_list)
        self.Vge_stable = round((max_mean), 2)
        #print(f"对应位置的 Vbus_mean_list 值是: {self.Vge_stable}")
        return
    
    def getl_Ic_off(self):
        #self.Ic_off = max(G_Ic[self.tl_midpoint_1:self.tl_midpoint_2])
        self.Ic_off = max(G_Ic[self.tl_1_on:self.tl_1_off])
        # tl_1_on和tl_1_off的中点,和tl_1_off和tl_2_on的中点之间，寻找最大值作为Ic_off。
        self.tl_Ic_off = G_Ic.index(self.Ic_off) # index返回搜索到的第一个值的地址
        self.Ic_off = round((self.Ic_off), 2)
        
        '''
        self.Irm_on = max(G_Ic[int(0.5 * (self.tl_1_off + self.tl_2_on)):int(0.5 * (self.tl_2_on + self.tl_2_off))])
        # 待解决1：二开与二关中点距离反向恢复尖峰过远，可能出现最大值找到右边去的情况
        cutl_Irm_on_L = int(0.5 * (self.tl_1_off + self.tl_2_on))
        self.tl_Irm_on = cutl_Irm_on_L + G_Ic[cutl_Irm_on_L:].index(max(G_Ic[cutl_Irm_on_L:]))
        print(self.tl_Irm_on)
        print(int(0.5 * (self.tl_2_on + self.tl_2_off)))
        print(G_Ic[self.tl_Irm_on:int(0.5 * (self.tl_2_on + self.tl_2_off))])
        #self.Ic_on = min(G_Ic[self.tl_Irm_on:int(0.5 * (self.tl_2_on + self.tl_2_off))])
    
        print("Ic_off:",self.Ic_off)
        print("Irm_on:",self.Irm_on)
        print("Ic_on:",self.Ic_on)
        print()
        print("Ic_off位置:",self.tl_Ic_off)
        print("cutl_Irm_on_L位置:",cutl_Irm_on_L)
        print("Irm_on位置:",self.tl_Irm_on)
        '''
        self.Ic_on = self.Ic_off # 暂时先使用Ic_off代替Ic_on
        self.Ic_on = round((self.Ic_on), 2)
        return
    
    def getl_Vpeak(self):
        self.Vpeak = max(G_Vce[self.tl_midpoint_1:self.tl_midpoint_2])
        # tl_1_off附近，最大值定位Vpeak。
        self.tl_Vpeak = self.tl_midpoint_3 + G_Vce[self.tl_midpoint_3:].index(max(G_Vce[self.tl_midpoint_3:]))
        # 因为index返回的只是搜索到的第一个值的地址，所以说需要将两部分切开，检索后再拼起来。
        # 否则可能会搜索到第一个数值相同，但是地址不一样的值。
        self.Vpeak = round((self.Vpeak), 2)
        return
    
    def get_Vce_stable(self):

        Vbus_var_list = []
        Vbus_mean_list = []
        tmp = 0.1
        while tmp < 0.7:
            tl_Vbus_tmp = int(tmp * self.tl_2_on + (1 - tmp) * self.tl_1_off)
            #print(round((tmp * 100), 0), '%1关2开位置：', tl_Vbus_tmp)
            Vbus_var = np.var(G_Vce[tl_Vbus_tmp : tl_Vbus_tmp + 1000])
            Vbus_mean = np.mean(G_Vce[tl_Vbus_tmp : tl_Vbus_tmp + 1000])
            Vbus_var_list.append(Vbus_var)
            Vbus_mean_list.append(Vbus_mean)
            #print(int(tmp * 100), '%，均值：', int(Vbus_mean), '，方差：', round((Vbus_var), 2))
            tmp += 0.1        
        # 找到 Vbus_var_list 中的最小值及其索引
        min_var = min(Vbus_var_list)
        index = Vbus_var_list.index(min_var)
        # 获取对应位置的 Vbus_mean_list 值
        corresponding_mean = Vbus_mean_list[index]
        self.Vce_stable = round((corresponding_mean), 2)
        #print(f"Vbus_var_list 中的最小值是: {min_var}")
        #print(f"对应位置的 Vbus_mean_list 值是: {corresponding_mean}")
        #print('均值：', Vbus_mean_list)
        #print('方差：', Vbus_var_list)
        
        '''
        Vce_Filter = LowPassFilter(G_Vce)
        plt.rc('font', family='simhei', size=15)  # 设置中文显示，字体大小
        plt.rc('axes', unicode_minus=False)  # 该参数解决负号显示的问题
        plt.figure(num=1)
        plt.plot(G_T, Vce_Filter, 'b-', label='Vce_Filter')
        #plt.plot(G_T, G_Vce, 'k-', label='Vds')
        plt.plot(G_T[self.tl_1_off], Vce_Filter[self.tl_1_off], 'r-', label='1关', marker = 'o')
        plt.plot(G_T[self.tl_2_on], Vce_Filter[self.tl_2_on], 'r-', label='2开', marker = 'o')
        #plt.plot(G_T[Vce_stable_l_tl], Vce_Filter[Vce_stable_l_tl], 'r-', label='左端点', marker = 'o')
        #plt.plot(G_T[Vce_stable_r_tl], Vce_Filter[Vce_stable_r_tl], 'r-', label='右端点', marker = 'o')
        plt.legend(loc='best')
        plt.title('Vds波形异常调试')
        plt.show()
        print()
        '''

        '''
        # 以下为固定数值的旧代码，暂时不用了
        Vce_stable_l = 0.90
        Vce_stable_r = 0.95
        Vce_stable_l_tl = int(Vce_stable_r * self.tl_1_off + (1.0 - Vce_stable_r) * self.tl_2_on)
        Vce_stable_r_tl = int(Vce_stable_l * self.tl_1_off + (1.0 - Vce_stable_l) * self.tl_2_on)
        self.Vce_stable = np.mean(G_Vce[Vce_stable_l_tl : Vce_stable_r_tl])
        self.Vce_stable = round((self.Vce_stable), 2)
        # tl_1_off和tl_2_on之间，45%~55%的部分取平均值，作为Vce_stable的值
        #self.Vce_stable = 430  # 测试专用，直接定义Vbus
        '''
        return

    def get_key_time_2(self):
        '''
        用来获取第一次关断中90%Vge、10%~90%Vce、90%~2%Ic的位置
        以及第二次开通过程中10%Vge、10%~90%Ic、90~2%Vce的位置
        '''
        # 以下为第一次关断过程中的关键参数点
        tmp = self.tl_midpoint_1
        while tmp < self.tl_2_on:
            if G_Vge[tmp] < 0.9 * self.Vge_stable:
                self.tl_off_09Vge = tmp  # 确定90%Vge的位置
                break
            else:
                tmp += 1
        # Vge/Vgs已经确定，接下来确定Ids/Ice的位置
        tmp = self.tl_Ic_off # 从Ic(off)的位置向后搜索，否则会卡点位置在Ic(off)之前
        while tmp < self.tl_2_on:
            if G_Ic[tmp] < 0.9 * self.Ic_off:
                self.tl_off_09Ic = tmp  # 确定90%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Ic[tmp] < 0.8 * self.Ic_off:
                self.tl_off_08Ic = tmp  # 确定80%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Ic[tmp] < 0.7 * self.Ic_off:
                self.tl_off_07Ic = tmp  # 确定70%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Ic[tmp] < 0.3 * self.Ic_off:
                self.tl_off_03Ic = tmp  # 确定30%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Ic[tmp] < 0.2 * self.Ic_off:
                self.tl_off_02Ic = tmp  # 确定20%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Ic[tmp] < 0.1 * self.Ic_off:
                self.tl_off_01Ic = tmp  # 确定10%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Ic[tmp] < 0.02 * self.Ic_off:
                self.tl_off_002Ic = tmp  # 确定2%Ic的位置
                break
            else:
                tmp += 1
        # Ids/Ice已经确定，接下来确定Vds/Vce的位置
        tmp = self.tl_off_09Vge
        while tmp < self.tl_2_on:
            if G_Vce[tmp] > 0.1 * self.Vce_stable:
                self.tl_off_01Vce = tmp  # 确定10%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Vce[tmp] > 0.2 * self.Vce_stable:
                self.tl_off_02Vce = tmp  # 确定20%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Vce[tmp] > 0.3 * self.Vce_stable:
                self.tl_off_03Vce = tmp  # 确定30%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Vce[tmp] > 0.7 * self.Vce_stable:
                self.tl_off_07Vce = tmp  # 确定70%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Vce[tmp] > 0.8 * self.Vce_stable:
                self.tl_off_08Vce = tmp  # 确定80%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_on:
            if G_Vce[tmp] > 0.9 * self.Vce_stable:
                self.tl_off_09Vce = tmp  # 确定90%Vce的位置
                break
            else:
                tmp += 1

        # 以下为第二次开通过程中的关键参数点
        tmp = self.tl_midpoint_2 # 从一关和二开中间开始搜索
        while tmp < self.tl_2_off:
            if G_Vge[tmp] > 0.1 * self.Vge_stable:
                self.tl_on_01Vge = tmp # 确定10%Vge的位置
                break
            else:
                tmp += 1
        # Vge/Vgs已经确定，接下来确定Ids/Ice的位置
        while tmp < self.tl_2_off:
            if G_Ic[tmp] > 0.1 * self.Ic_on:
                self.tl_on_01Ic = tmp # 确定10%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Ic[tmp] > 0.2 * self.Ic_on:
                self.tl_on_02Ic = tmp # 确定20%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Ic[tmp] > 0.3 * self.Ic_on:
                self.tl_on_03Ic = tmp # 确定30%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Ic[tmp] > 0.7 * self.Ic_on:
                self.tl_on_07Ic = tmp # 确定70%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Ic[tmp] > 0.8 * self.Ic_on:
                self.tl_on_08Ic = tmp # 确定80%Ic的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Ic[tmp] > 0.9 * self.Ic_on:
                self.tl_on_09Ic = tmp # 确定90%Ic的位置
                break
            else:
                tmp += 1
        
        # Ids/Ice已经确定，接下来确定Vds/Vce的位置
        tmp = self.tl_midpoint_2
        while tmp < self.tl_2_off:
            if G_Vce[tmp] < 0.9 * self.Vce_stable:
                self.tl_on_09Vce = tmp  # 确定90%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Vce[tmp] < 0.8 * self.Vce_stable:
                self.tl_on_08Vce = tmp  # 确定80%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Vce[tmp] < 0.7 * self.Vce_stable:
                self.tl_on_07Vce = tmp  # 确定70%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Vce[tmp] < 0.3 * self.Vce_stable:
                self.tl_on_03Vce = tmp  # 确定30%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Vce[tmp] < 0.2 * self.Vce_stable:
                self.tl_on_02Vce = tmp  # 确定20%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Vce[tmp] < 0.1 * self.Vce_stable:
                self.tl_on_01Vce = tmp  # 确定10%Vce的位置
                break
            else:
                tmp += 1
        while tmp < self.tl_2_off:
            if G_Vce[tmp] < 0.02 * self.Vce_stable:
                self.tl_on_002Vce = tmp  # 确定2%Vce的位置
                break
            else:
                tmp += 1
        
        '''
        # 以下代码测试中使用
        print('以下为第一次关断时关键时间点')
        print('一关时90%Vge：', self.tl_off_09Vge)
        print('一关时90% Ic：', self.tl_off_09Ic)
        print('一关时80% Ic：', self.tl_off_08Ic)
        print('一关时70% Ic：', self.tl_off_07Ic)
        print('一关时30% Ic：', self.tl_off_03Ic)
        print('一关时20% Ic：', self.tl_off_02Ic)
        print('一关时10% Ic：', self.tl_off_01Ic)
        print('一关时 2% Ic：', self.tl_off_002Ic)
        print('一关时10%Vce：', self.tl_off_01Vce)
        print('一关时20%Vce：', self.tl_off_02Vce)
        print('一关时30%Vce：', self.tl_off_03Vce)
        print('一关时70%Vce：', self.tl_off_07Vce)
        print('一关时80%Vce：', self.tl_off_08Vce)
        print('一关时90%Vce：', self.tl_off_09Vce)
        print('以下为第二次开通时关键时间点')
        print('二开时10%Vge：', self.tl_on_01Vge)
        print('二开时10% Ic：', self.tl_on_01Ic)
        print('二开时20% Ic：', self.tl_on_02Ic)
        print('二开时30% Ic：', self.tl_on_03Ic)
        print('二开时70% Ic：', self.tl_on_07Ic)
        print('二开时80% Ic：', self.tl_on_08Ic)
        print('二开时90% Ic：', self.tl_on_09Ic)
        print('二开时90%Vce：', self.tl_on_09Vce)
        print('二开时80%Vce：', self.tl_on_08Vce)
        print('二开时70%Vce：', self.tl_on_07Vce)
        print('二开时30%Vce：', self.tl_on_03Vce)
        print('二开时20%Vce：', self.tl_on_02Vce)
        print('二开时10%Vce：', self.tl_on_01Vce)
        print('二开时2% Vce：', self.tl_on_002Vce)
        print()

        
        plt.rc('font', family='simhei', size=15)  # 设置中文显示，字体大小
        plt.rc('axes', unicode_minus=False)  # 该参数解决负号显示的问题
        plt.figure(num=1)
        wave_list = [G_T, G_Vge, G_Vce, G_Ic, G_Vf, G_If]
        wave_name = ['TimeLine', 'Vgs', 'Vds', 'Ids', 'Vrrm', 'Irrm']
        wave_show = 1
        plt.plot(G_T, wave_list[wave_show], 'y-', label = wave_name[wave_show])
        #plt.plot(G_T, LowPassFilter(wave_list[wave_show], fs=6.25e9, f_max=1e8), 'b-', label = wave_name[wave_show] + ' 100M 滤波')
        #plt.plot(G_T, LowPassFilter(wave_list[wave_show], fs=6.25e9, f_max=5e7), 'b-', label = wave_name[wave_show] + ' 50M 滤波')
        #plt.plot(G_T, LowPassFilter(Derivatives(wave_list[wave_show]), fs=6.25e9, f_max=1e8), 'g-', label = wave_name[wave_show] + ' 100M 求导')
        plt.plot(G_T[self.tl_midpoint_2], G_Vge[self.tl_midpoint_2], 'g-', label='2中', marker = 'o')
        #plt.plot(G_T[self.tl_1_off], G_Vge[self.tl_1_off], 'g-', label='1关', marker = 'o')
        #plt.plot(G_T[self.tl_2_on], G_Vge[self.tl_2_on], 'g-', label='2开', marker = 'o')
        #plt.plot(G_T[self.tl_2_off], G_Vge[self.tl_2_off], 'g-', label='2关', marker = 'o')
        #plt.plot(G_T[self.tl_midpoint_1], G_Vge[self.tl_midpoint_1], 'r-', label='1隔断', marker = 'o')
        #plt.plot(G_T[self.tl_midpoint_2], G_Vge[self.tl_midpoint_2], 'r-', label='2隔断', marker = 'o')
        #plt.plot(G_T[self.tl_midpoint_3], G_Vge[self.tl_midpoint_3], 'r-', label='3隔断', marker = 'o')
        plt.legend(loc='best')
        plt.title('测试阶段波形展示')
        plt.show()
        '''
        return
    
    def get_ton_MOSFET(self):
        '''
        开通延时tdon：Vge的10%到Vds的90%
        上升时间：Vds的90%到Vds的10%
        开通时间：开通延时+上升时间
        '''
        self.tdon = round(((G_T[self.tl_on_09Vce]*1000) - (G_T[self.tl_on_01Vge]*1000)), 2) # 单位us化为ns
        self.tr = round(((G_T[self.tl_on_01Vce]*1000) - (G_T[self.tl_on_09Vce]*1000)),2)
        self.ton = round((self.tdon + self.tr), 2)
        return
    
    def get_ton_IGBT(self):
        '''
        开通延时tdon：Vge的10%到Ic的10%
        上升时间：Ic的10%到Ic的90%
        开通时间：开通延时+上升时间
        '''
        self.tdon = round(((G_T[self.tl_on_01Ic]*1000) - (G_T[self.tl_on_01Vge]*1000)), 2) # 单位us化为ns
        self.tr = round(((G_T[self.tl_on_09Ic]*1000) - (G_T[self.tl_on_01Ic]*1000)),2)
        self.ton = round((self.tdon + self.tr), 2)
        return

    def get_Eon_MOSFET(self):
        '''
        二开时，10%Ic到10%Vce期间，Vce*Ic的积分。
        '''
        #print('计算Eon_MOSFET')
        EonVxI = []  # 建立一个空列表，用来存储积分中Vce*Ic的乘积
        try:
            dtEon = float(((G_T[self.tl_on_01Vce] - G_T[self.tl_on_01Ic])*0.001) / (self.tl_on_01Vce - self.tl_on_01Ic))
            # 积分中使用梯形近似法，dtEon相当于每个长方体底边的宽度，已换算成微秒ms，乘以0.001
            tmp = self.tl_on_01Ic  # 循环中读取列表用的计数器
            while (tmp < self.tl_on_01Vce):  # 对Eon上下限内的电流与电压值进行乘积，写入新的列表中
                EonVxI.append(float(G_Vce[tmp]) * float(G_Ic[tmp]) * dtEon)
                tmp += 1  # 读取下一个位置的电流电压值
            self.Eon = sum(EonVxI)
            self.Eon = round((self.Eon), 2)
        except Exception as error:
            self.Eon = 0
            print(error)
            print('def_wave - class GetDynamicDataObject - get_Eon_MOSFET函数错误：Eon计算有误，已经当做0处理。')
        return
    
    def get_Eon_IGBT(self):
        '''
        二开时，10%Vge到2%Vce期间，Vce*Ic的积分。
        '''
        #print('计算Eon_IGBT')
        EonVxI = []  # 建立一个空列表，用来存储积分中Vce*Ic的乘积
        try:
            dtEon = float(((G_T[self.tl_on_002Vce] - G_T[self.tl_on_01Vge])*0.001) / (self.tl_on_002Vce - self.tl_on_01Vge))
            # 积分中使用梯形近似法，dtEon相当于每个长方体底边的宽度，已换算成微秒ms，乘以0.001
            tmp = self.tl_on_01Vge  # 循环中读取列表用的计数器
            while (tmp < self.tl_on_002Vce):  # 对Eon上下限内的电流与电压值进行乘积，写入新的列表中
                EonVxI.append(float(G_Vce[tmp]) * float(G_Ic[tmp]) * dtEon)
                tmp += 1  # 读取下一个位置的电流电压值
            self.Eon = sum(EonVxI)
            self.Eon = round((self.Eon), 2)
        except Exception as error:
            self.Eon = 0
            print(error)
            print('def_wave - class GetDynamicDataObject - get_Eon_IGBT函数错误：Eon计算有误，已经当做0处理。')
        return
    
    def get_didt_dvdt(self, sampling_rate):
        #sampling_rate = 6.25e9
        LR_Time = 2.5e-3
        G_T_np = np.array(G_T)

        dVcedt_flt = list(Derivatives(LowPassFilter(G_Vce, fs=sampling_rate, f_max=1e8)))
        lft_dvdt_on_max = min(dVcedt_flt[self.tl_midpoint_2 : self.tl_midpoint_3]) # 开通过程中dVds/dt滤波后最小的值
        tl_lft_dvdt_on_max = self.tl_midpoint_2 + dVcedt_flt[self.tl_midpoint_2:].index(lft_dvdt_on_max) # 找到dVds/dt滤波后最小的值的列表中位置
        self.time_dvdt_on_max = G_T[tl_lft_dvdt_on_max]
        time_dvdt_on_max_L = G_T[tl_lft_dvdt_on_max] - LR_Time
        time_dvdt_on_max_R = G_T[tl_lft_dvdt_on_max] + LR_Time
        lt_time_dvdt_on_max_L = np.where(np.abs(G_T_np - time_dvdt_on_max_L) == np.min(np.abs(G_T_np - time_dvdt_on_max_L)))[0][0]
        lt_time_dvdt_on_max_R = np.where(np.abs(G_T_np - time_dvdt_on_max_R) == np.min(np.abs(G_T_np - time_dvdt_on_max_R)))[0][0]
        self.dvdt_on_max = abs(((G_Vce[lt_time_dvdt_on_max_R] - G_Vce[lt_time_dvdt_on_max_L])/(G_T[lt_time_dvdt_on_max_R] - G_T[lt_time_dvdt_on_max_L]))/1000)
        #print(f"dvdt_on_max出现的时间: {round(self.time_dvdt_on_max, 6)} us")
        #print(f"2.5ns 前的时间: {round(time_dvdt_on_max_L, 6)} us，对应索引: {lt_time_dvdt_on_max_L}")
        #print(f"2.5ns 后的时间: {round(time_dvdt_on_max_R, 6)} us，对应索引: {lt_time_dvdt_on_max_R}")
        lft_dvdt_off_max = max(dVcedt_flt[self.tl_midpoint_1 : self.tl_midpoint_2]) # 关断过程中dVds/dt滤波后最大的值
        tl_lft_dvdt_off_max = self.tl_midpoint_1 + dVcedt_flt[self.tl_midpoint_1:].index(lft_dvdt_off_max)
        self.time_dvdt_off_max = G_T[tl_lft_dvdt_off_max]
        time_dvdt_off_max_L = G_T[tl_lft_dvdt_off_max] - LR_Time
        time_dvdt_off_max_R = G_T[tl_lft_dvdt_off_max] + LR_Time
        lt_time_dvdt_off_max_L = np.where(np.abs(G_T_np - time_dvdt_off_max_L) == np.min(np.abs(G_T_np - time_dvdt_off_max_L)))[0][0]
        lt_time_dvdt_off_max_R = np.where(np.abs(G_T_np - time_dvdt_off_max_R) == np.min(np.abs(G_T_np - time_dvdt_off_max_R)))[0][0]
        self.dvdt_off_max = abs(((G_Vce[lt_time_dvdt_off_max_R] - G_Vce[lt_time_dvdt_off_max_L])/(G_T[lt_time_dvdt_off_max_R] - G_T[lt_time_dvdt_off_max_L]))/1000)
        #print(f"dvdt_off_max出现的时间: {round(self.time_dvdt_off_max, 6)} us")
        #print(f"2.5ns 前的时间: {round(time_dvdt_off_max_L, 6)} us，对应索引: {lt_time_dvdt_off_max_L}")
        #print(f"2.5ns 后的时间: {round(time_dvdt_off_max_R, 6)} us，对应索引: {lt_time_dvdt_off_max_R}")

        dIcdt_flt = list(Derivatives(LowPassFilter(G_Ic, fs=sampling_rate, f_max=1e8)))
        lft_didt_on_max = max(dIcdt_flt[self.tl_midpoint_2 : self.tl_midpoint_3]) # 开通过程中dIds/dt滤波后最小的值
        tl_lft_didt_on_max = self.tl_midpoint_2 + dIcdt_flt[self.tl_midpoint_2:].index(lft_didt_on_max) # 找到dIds/dt滤波后最小的值的列表中位置
        self.time_didt_on_max = G_T[tl_lft_didt_on_max]
        time_didt_on_max_L = G_T[tl_lft_didt_on_max] - LR_Time
        time_didt_on_max_R = G_T[tl_lft_didt_on_max] + LR_Time
        lt_time_didt_on_max_L = np.where(np.abs(G_T_np - time_didt_on_max_L) == np.min(np.abs(G_T_np - time_didt_on_max_L)))[0][0]
        lt_time_didt_on_max_R = np.where(np.abs(G_T_np - time_didt_on_max_R) == np.min(np.abs(G_T_np - time_didt_on_max_R)))[0][0]
        self.didt_on_max = abs(((G_Ic[lt_time_didt_on_max_R] - G_Ic[lt_time_didt_on_max_L])/(G_T[lt_time_didt_on_max_R] - G_T[lt_time_didt_on_max_L]))/1000)
        #print(f"didt_on_max出现的时间: {round(self.time_didt_on_max, 6)} us")
        #print(f"2.5ns 前的时间: {round(time_didt_on_max_L, 6)} us，对应索引: {lt_time_didt_on_max_L}")
        #print(f"2.5ns 后的时间: {round(time_didt_on_max_R, 6)} us，对应索引: {lt_time_didt_on_max_R}")
        lft_didt_off_max = min(dIcdt_flt[self.tl_midpoint_1 : self.tl_midpoint_2]) # 关断过程中dIds/dt滤波后最大的值
        tl_lft_didt_off_max = self.tl_midpoint_1 + dIcdt_flt[self.tl_midpoint_1:].index(lft_didt_off_max)
        self.time_didt_off_max = G_T[tl_lft_didt_off_max]
        time_didt_off_max_L = G_T[tl_lft_didt_off_max] - LR_Time
        time_didt_off_max_R = G_T[tl_lft_didt_off_max] + LR_Time
        lt_time_didt_off_max_L = np.where(np.abs(G_T_np - time_didt_off_max_L) == np.min(np.abs(G_T_np - time_didt_off_max_L)))[0][0]
        lt_time_didt_off_max_R = np.where(np.abs(G_T_np - time_didt_off_max_R) == np.min(np.abs(G_T_np - time_didt_off_max_R)))[0][0]
        self.didt_off_max = abs(((G_Ic[lt_time_didt_off_max_R] - G_Ic[lt_time_didt_off_max_L])/(G_T[lt_time_didt_off_max_R] - G_T[lt_time_didt_off_max_L]))/1000)
        #print(f"didt_off_max出现的时间: {round(self.time_didt_off_max, 6)} us")
        #print(f"2.5ns 前的时间: {round(time_didt_off_max_L, 6)} us，对应索引: {lt_time_didt_off_max_L}")
        #print(f"2.5ns 后的时间: {round(time_didt_off_max_R, 6)} us，对应索引: {lt_time_didt_off_max_R}")
        #print('关断最大dvdt：', self.dvdt_off_max)
        #print('关断最大didt：', self.didt_off_max)
        #print('开通最大dvdt：', self.dvdt_on_max)
        #print('开通最大didt：', self.didt_on_max)

        # 开通过程
        try:
            self.didt_on_01_09 = ((G_Ic[self.tl_on_09Ic] - G_Ic[self.tl_on_01Ic])/(G_T[self.tl_on_09Ic] - G_T[self.tl_on_01Ic]))/1000
            self.didt_on_02_08 = ((G_Ic[self.tl_on_08Ic] - G_Ic[self.tl_on_02Ic])/(G_T[self.tl_on_08Ic] - G_T[self.tl_on_02Ic]))/1000
            self.didt_on_03_07 = ((G_Ic[self.tl_on_07Ic] - G_Ic[self.tl_on_03Ic])/(G_T[self.tl_on_07Ic] - G_T[self.tl_on_03Ic]))/1000
            self.dvdt_on_09_01 = ((G_Vce[self.tl_on_09Vce] - G_Vce[self.tl_on_01Vce])/(G_T[self.tl_on_01Vce] - G_T[self.tl_on_09Vce]))/1000
            self.dvdt_on_08_02 = ((G_Vce[self.tl_on_08Vce] - G_Vce[self.tl_on_02Vce])/(G_T[self.tl_on_02Vce] - G_T[self.tl_on_08Vce]))/1000
            self.dvdt_on_07_03 = ((G_Vce[self.tl_on_07Vce] - G_Vce[self.tl_on_03Vce])/(G_T[self.tl_on_03Vce] - G_T[self.tl_on_07Vce]))/1000
            
        except Exception as error:
            self.didt_on_01_09 = 0
            self.didt_on_02_08 = 0
            self.didt_on_03_07 = 0
            self.dvdt_on_09_01 = 0
            self.dvdt_on_08_02 = 0
            self.dvdt_on_07_03 = 0
            print(error)
            print('def_wave - class GetDynamicDataObject - get_didt_dvdt函数错误：didt_on，dvdt_on计算有误，已经当做0处理。')
        self.didt_on_01_09 = round((self.didt_on_01_09), 4)
        self.didt_on_02_08 = round((self.didt_on_02_08), 4)
        self.didt_on_03_07 = round((self.didt_on_03_07), 4)
        self.dvdt_on_09_01 = round((self.dvdt_on_09_01), 4)
        self.dvdt_on_08_02 = round((self.dvdt_on_08_02), 4)
        self.dvdt_on_07_03 = round((self.dvdt_on_07_03), 4)
        # 关断过程
        try:
            self.didt_off_09_01 = ((G_Ic[self.tl_off_09Ic] - G_Ic[self.tl_off_01Ic])/(G_T[self.tl_off_01Ic] - G_T[self.tl_off_09Ic]))/1000
            self.didt_off_08_02 = ((G_Ic[self.tl_off_08Ic] - G_Ic[self.tl_off_02Ic])/(G_T[self.tl_off_02Ic] - G_T[self.tl_off_08Ic]))/1000
            self.didt_off_07_03 = ((G_Ic[self.tl_off_07Ic] - G_Ic[self.tl_off_03Ic])/(G_T[self.tl_off_03Ic] - G_T[self.tl_off_07Ic]))/1000
            self.dvdt_off_01_09 = ((G_Vce[self.tl_off_09Vce] - G_Vce[self.tl_off_01Vce])/(G_T[self.tl_off_09Vce] - G_T[self.tl_off_01Vce]))/1000
            self.dvdt_off_02_08 = ((G_Vce[self.tl_off_08Vce] - G_Vce[self.tl_off_02Vce])/(G_T[self.tl_off_08Vce] - G_T[self.tl_off_02Vce]))/1000
            self.dvdt_off_03_07 = ((G_Vce[self.tl_off_07Vce] - G_Vce[self.tl_off_03Vce])/(G_T[self.tl_off_07Vce] - G_T[self.tl_off_03Vce]))/1000

        except Exception as error:
            self.didt_off_09_01 = 0
            self.didt_off_08_02 = 0
            self.didt_off_07_03 = 0
            self.dvdt_off_01_09 = 0
            self.dvdt_off_02_08 = 0
            self.dvdt_off_03_07 = 0
            print(error)
            print('def_wave - class GetDynamicDataObject - get_didt_dvdt函数错误：didt_off、dvdt_off计算有误，已经当做0处理。')
        self.didt_off_09_01 = round((self.didt_off_09_01), 4)
        self.didt_off_08_02 = round((self.didt_off_08_02), 4)
        self.didt_off_07_03 = round((self.didt_off_07_03), 4)
        self.dvdt_off_01_09 = round((self.dvdt_off_01_09), 4)
        self.dvdt_off_02_08 = round((self.dvdt_off_02_08), 4)
        self.dvdt_off_03_07 = round((self.dvdt_off_03_07), 4)
        return

    def get_toff_MOSFET(self):
        '''
        关断延时：Vgs的90%到Vds的10%
        下降时间：Vds的10%到Vds的90%
        关断时间：关断延时+下降时间
        '''
        self.tdoff = (G_T[self.tl_off_01Vce]*1000) - (G_T[self.tl_off_09Vge]*1000)
        # 待解决2：1.0-T4-02.55-07.5-140C-650V-025A_ALL.csv、050A、100A、150A、200A出现tdoff=0，tf很大的情况
        self.tf = (G_T[self.tl_off_09Vce]*1000) - (G_T[self.tl_off_01Vce]*1000)
        self.toff = self.tdoff + self.tf
        self.tdoff = round((self.tdoff), 2)
        self.tf = round((self.tf), 2)
        self.toff = round((self.toff), 2)
        return

    def get_toff_IGBT(self):
        '''
        关断延时：Vge的90%到Ic的90%
        下降时间：Ic的90%到Ic的10%
        关断时间：关断延时+下降时间
        '''
        self.tdoff = (G_T[self.tl_off_09Ic]*1000) - (G_T[self.tl_off_09Vge]*1000)
        # 待解决2：1.0-T4-02.55-07.5-140C-650V-025A_ALL.csv、050A、100A、150A、200A出现tdoff=0，tf很大的情况
        self.tf = (G_T[self.tl_off_01Ic]*1000) - (G_T[self.tl_off_09Ic]*1000)
        self.toff = self.tdoff + self.tf
        self.tdoff = round((self.tdoff), 2)
        self.tf = round((self.tf), 2)
        self.toff = round((self.toff), 2)
        return
    
    def get_Eoff_MOSFET(self):
        '''
        一关时，10%Vce到10%Ic期间，Vce*Ic的积分
        '''
        #print('计算Eoff_MOSFET')
        EoffVxI = []
        try:
            dtEoff = float(((G_T[self.tl_off_01Ic] - G_T[self.tl_off_01Vce])*0.001) / (self.tl_off_01Ic - self.tl_off_01Vce))
            tmp = self.tl_off_01Vce
            while (tmp < self.tl_off_01Ic):
                EoffVxI.append(float(G_Vce[tmp]) * float(G_Ic[tmp]) * dtEoff)
                tmp += 1
            self.Eoff = sum(EoffVxI)
            self.Eoff = round((self.Eoff), 2)
        except Exception as error:
            self.Eoff = 0
            print(error)
            print('def_wave - class GetDynamicDataObject - get_Eoff_MOSFET函数错误：Eoff计算有误，已经当做0处理。')
        return
    
    def get_Eoff_IGBT(self):
        '''
        一关时，90%Vge到2%Ic期间，Vce*Ic的积分
        '''
        #print('计算Eoff_IGBT')
        EoffVxI = []
        try:
            dtEoff = float(((G_T[self.tl_off_002Ic] - G_T[self.tl_off_09Vge])*0.001) / (self.tl_off_002Ic - self.tl_off_09Vge))
            tmp = self.tl_off_09Vge
            while (tmp < self.tl_off_002Ic):
                EoffVxI.append(float(G_Vce[tmp]) * float(G_Ic[tmp]) * dtEoff)
                tmp += 1
            self.Eoff = sum(EoffVxI)
            self.Eoff = round((self.Eoff), 2)
        except Exception as error:
            self.Eoff = 0
            print(error)
            print('def_wave - class GetDynamicDataObject - get_Eoff_IGBT函数错误：Eoff计算有误，已经当做0处理。')
        return

    
    def get_diode_time(self, sampling_rate):
        '''
        获取二极管相关时间信息
        '''
        self.on_If_max = max(G_If[self.tl_midpoint_2:self.tl_midpoint_3]) # 获取IF下降前的最大值
        self.on_If_min = min(G_If[self.tl_midpoint_2:self.tl_midpoint_3]) # 获取IF下降后的最小值
        self.tl_on_If_max = self.tl_midpoint_2 + G_If[self.tl_midpoint_2:self.tl_midpoint_3].index(self.on_If_max) # 获取IF下降前的最大值的位置
        self.tl_on_If_min = self.tl_midpoint_2 + G_If[self.tl_midpoint_2:self.tl_midpoint_3].index(self.on_If_min) # 获取IF下降后的最小值的位置

        tmp = self.tl_midpoint_2
        while tmp < self.tl_midpoint_3:
            if G_Vf[tmp] > 0.1 * self.Vce_stable:
                self.tl_on_01Vf = tmp 
                break
            else:
                tmp += 1
        while tmp < self.tl_midpoint_3:
            if G_Vf[tmp] > 0.9 * self.Vce_stable:
                self.tl_on_09Vf = tmp 
                break
            else:
                tmp += 1
        Vf_flt = Derivatives(LowPassFilter(G_Vf, fs=sampling_rate, f_max=1e8))
        tmp = self.tl_on_01Vf
        while tmp < self.tl_midpoint_3:
            if Vf_flt[tmp] < 0:
                self.tl_on_Vrrm_FS = tmp # 找到Vrrm第一次尖峰
                break
            else:
                tmp += 1
        #print('Vrrm首次尖峰时间：', G_T[self.tl_on_Vrrm_FS])

        tmp = self.tl_on_If_max
        while tmp < self.tl_on_If_min:
            if G_If[tmp] < 0.5 * self.on_If_max:
                self.tl_on_05If_max = tmp 
                break
            else:
                tmp += 1
        while tmp < self.tl_on_If_min:
            if G_If[tmp] < 0.0:
                self.tl_on_00If = tmp 
                break
            else:
                tmp += 1
        while tmp < self.tl_on_If_min:
            if G_If[tmp] < 0.5 * self.on_If_min:
                self.tl_on_05If_min = tmp 
                break
            else:
                tmp += 1
        # 到这里就完成了从If最大值到最小值之间的时间点扫描，接下来开始If从负数最小值恢复的过程
        tmp = self.tl_on_If_min
        while tmp < self.tl_midpoint_3:
            if G_If[tmp] > 0.9 * self.on_If_min:
                self.tl_on_09If_min = tmp 
                break
            else:
                tmp += 1
        while tmp < self.tl_midpoint_3:
            if G_If[tmp] > 0.25 * self.on_If_min:
                self.tl_on_025If_min = tmp 
                break
            else:
                tmp += 1
        while tmp < self.tl_midpoint_3:
            if G_If[tmp] > 0.02 * self.on_If_min:
            #if G_If[tmp] > 2000: # 测试专用，强行触发电流探头飘了的状态
                self.tl_on_002If_min = tmp 
                break
            elif tmp >= self.tl_midpoint_3 - 1:
                #print('电流飘了，电流反向恢复过程未过0点，2%反向恢复电流使用震荡过程电流最小值代替')
                If_Filter = list(LowPassFilter(G_If)) # 先滤波再求导，否则震荡太大
                If_Filter_derivatives = list(Derivatives(If_Filter))
                on_If_Filter_min = min(If_Filter[self.tl_midpoint_2:self.tl_midpoint_3])
                tl_on_If_Filter_min = self.tl_midpoint_2 + If_Filter[self.tl_midpoint_2:self.tl_midpoint_3].index(on_If_Filter_min) 
                tmp2 = tl_on_If_Filter_min + 1
                while tmp2 < self.tl_midpoint_3:
                    if If_Filter_derivatives[tmp2] > 0:
                        self.tl_on_002If_min = tmp2
                        '''lst1 = [0] * len(G_If)
                        plt.rc('font', family='simhei', size=15)  # 设置中文显示，字体大小
                        plt.rc('axes', unicode_minus=False)  # 该参数解决负号显示的问题
                        plt.figure(num=1)
                        plt.plot(G_If, 'r-', label='原始信号')
                        plt.plot(If_Filter, 'b-', lw=2, label='低通滤波信号')
                        plt.plot(If_Filter_derivatives, 'g--', lw=4, label='滤波后求导')
                        plt.plot(lst1, 'k-', lw=4, label='0')
                        plt.legend(loc='best')
                        plt.title('低通快速过滤信号')
                        plt.show()
                        #测试期间专用，画图'''
                        break # 跳出elif里的循环
                    else:
                        tmp2 += 1
                break # 跳出大循环
                
                #此方法不可行，震荡过程可能会将最小值震荡到后面的位置。
            else:
                tmp += 1
        
        # 到这里完成了二极管反向恢复期间的全部时间点扫描
        return
    
    def get_diode_data(self, sampling_rate):
        '''
        计算被动管相关数据
        '''
        if G_Vge_D != []:
            self.Vge_D_MAX_on = max(G_Vge_D[self.tl_midpoint_2:self.tl_midpoint_3]) # 主动管开通时，被动管栅极串扰电压最大值，此电压为光隔离探头直接测量结果，需要校准。
            self.Vge_D_MIN_off = min(G_Vge_D[self.tl_midpoint_1:self.tl_midpoint_2]) # 主动管关断时，被动管栅极串扰电压最小值，此电压为光隔离探头直接测量结果，需要校准。
            #print('正向串扰最大值：', self.Vge_D_MAX_on)
            #print('负向串扰最小值：', self.Vge_D_MIN_off)  # 测试专用代码

            VgsR_Light = 0 # 光隔离测量的栅极负压稳定值，使用第一次开到第一次关的中点，取附近10%的值取平均。
            VgsR_Light_L = 0.45
            VgsR_Light_R = 0.55
            VgsR_Light_L_tl = int(VgsR_Light_R * self.tl_1_on + (1.0 - VgsR_Light_R) * self.tl_1_off)
            VgsR_Light_R_tl = int(VgsR_Light_L * self.tl_1_on + (1.0 - VgsR_Light_L) * self.tl_1_off)
            VgsR_Light = np.mean(G_Vge_D[VgsR_Light_L_tl : VgsR_Light_R_tl])
            VgsR_Light = round((VgsR_Light), 2)
            Derta_V = VgsR_Light - self.VgsR # 光隔离探头的偏移程度，大于零说明光隔离探头向上飘，小于零说明向下飘。
            self.Vge_D_MAX_on = self.Vge_D_MAX_on - Derta_V  # 实际测试结果的串扰值 = 光隔离探头测试结果 - 光隔离探头偏移程度
            self.Vge_D_MIN_off = self.Vge_D_MIN_off - Derta_V
            self.Vge_D_MAX_on = round((self.Vge_D_MAX_on), 2)
            self.Vge_D_MIN_off = round((self.Vge_D_MIN_off), 2)
        else :
            self.Vge_D_MAX_on = 0
            self.Vge_D_MIN_off = 0
        #print('万用表实测栅极负压：', self.VgsR)
        #print('光隔离当前栅极负压：', VgsR_Light)
        #print('修正过程，在光隔离的基础上需要加的偏差值：', round((-Derta_V), 2))
        #print('修正后负向串扰最小值：', self.Vge_D_MAX_on)
        #print('修正后负向串扰最小值：', self.Vge_D_MIN_off)  # 测试专用代码
        
        try:
            self.dvdt_rr_01_09 = abs(((G_Vf[self.tl_on_09Vf] - G_Vf[self.tl_on_01Vf])/(G_T[self.tl_on_01Vf] - G_T[self.tl_on_09Vf]))/1000)
            self.dvdt_rr_01_fs = abs(((G_Vf[self.tl_on_Vrrm_FS] - G_Vf[self.tl_on_01Vf])/(G_T[self.tl_on_01Vf] - G_T[self.tl_on_Vrrm_FS]))/1000)
            self.dvdt_rr_01_09 = round((self.dvdt_rr_01_09), 2)
            self.dvdt_rr_01_fs = round((self.dvdt_rr_01_fs), 2)
        except Exception as error:
            self.dvdt_rr_01_09 = 0
            self.dvdt_rr_01_fs = 0
            print(error)
            print('def_wave - class GetDynamicDataObject - get_diode_data函数错误：dvdt_rr_01_09计算有误，已经当做0处理。')

        self.ti = round(((float(G_T[self.tl_on_002If_min]) * 1000) - float((G_T[self.tl_on_00If] * 1000))), 2)
        self.on_09If_min = float(G_T[self.tl_on_09If_min])
        self.on_025If_min = float(G_T[self.tl_on_025If_min])
        try:
            self.tl_on_trr_right = int(float(G_T[self.tl_on_09If_min]) - (((float(G_T[self.tl_on_09If_min])-float(G_T[self.tl_on_025If_min]))
                                                                   /(float(self.on_09If_min)-float(self.on_025If_min)))*float(self.on_09If_min))) # 斜率计算得来
            self.trr = abs(round(((float(G_T[self.tl_on_trr_right]) * 1000) - (float(G_T[self.tl_on_00If]) * 1000)), 2))
        except Exception as error:
            self.trr = 0
            print(error)
            print('def_wave - class GetDynamicDataObject - get_diode_data函数错误：trr计算有误，已经当做0处理。')
        self.Vf_max = round(max(G_Vf[self.tl_midpoint_2:self.tl_midpoint_3]),2)
        self.Irrm = abs(round((self.on_If_min),2)) # 取正值
        try:
            self.didt_rr_05_05 = abs(round((((G_If[self.tl_on_05If_max] - G_If[self.tl_on_05If_min])/(G_T[self.tl_on_05If_max] - G_T[self.tl_on_05If_min]))/1000),2)) # 取正值
            
        except Exception as error:
            self.didt_rr_05_05 = 0
            print('def_wave - class GetDynamicDataObject - get_diode_data函数错误：二极管didt计算异常，已经当做0处理。')
        Qrr_I = []
        Erec_VxI = []
        try:
            dtErec = float(((G_T[self.tl_on_002If_min] - G_T[self.tl_on_00If])) / (self.tl_on_002If_min - self.tl_on_00If))
            tmp = self.tl_on_00If
            while (tmp < self.tl_on_002If_min):
                Qrr_I.append(float(G_If[tmp]) * dtErec)
                tmp += 1
            #self.Qrr = sum(Qrr_I) * 1000 # 单位化为nC
            self.Qrr = sum(Qrr_I) # 单位化为uC
            self.Qrr = abs(round((self.Qrr), 4))
        except Exception as error:
            self.Qrr = 0
            print(error)
            print('def_wave - class GetDynamicDataObject - get_diode_data函数错误：反向恢复电荷Qrr计算异常，已经当做0处理。')

        try:
            dtErec = float(((G_T[self.tl_on_002If_min] - G_T[self.tl_on_00If])*0.001) / (self.tl_on_002If_min - self.tl_on_00If))
            tmp = self.tl_on_00If
            while (tmp < self.tl_on_002If_min):
                Erec_VxI.append(float(G_Vf[tmp]) * float(G_If[tmp]) * dtErec)
                tmp += 1
            self.Erec = sum(Erec_VxI)
            self.Erec = abs(round((self.Erec), 4))
        except Exception as error:
            self.Erec = 0
            print(error)
            print('def_wave - class GetDynamicDataObject - get_diode_data函数错误：二极管损耗Erec计算异常，已经当做0处理。')

        LR_Time = 2.5e-3
        G_T_np = np.array(G_T)

        dVfdt_flt = list(Derivatives(LowPassFilter(G_Vf, fs=sampling_rate, f_max=1e8)))
        lft_dvdt_rrm_max = max(dVfdt_flt[self.tl_midpoint_2 : self.tl_midpoint_3]) # 反向恢复过程中dVds/dt滤波后最大的值
        tl_lft_dvdt_rrm_max = self.tl_midpoint_2 + dVfdt_flt[self.tl_midpoint_2:].index(lft_dvdt_rrm_max) # 找到dVds/dt滤波后最小的值的列表中位置
        self.time_dvdt_rrm_max = G_T[tl_lft_dvdt_rrm_max]
        time_dvdt_rrm_max_L = G_T[tl_lft_dvdt_rrm_max] - LR_Time
        time_dvdt_rrm_max_R = G_T[tl_lft_dvdt_rrm_max] + LR_Time
        lt_time_dvdt_rrm_max_L = np.where(np.abs(G_T_np - time_dvdt_rrm_max_L) == np.min(np.abs(G_T_np - time_dvdt_rrm_max_L)))[0][0]
        lt_time_dvdt_rrm_max_R = np.where(np.abs(G_T_np - time_dvdt_rrm_max_R) == np.min(np.abs(G_T_np - time_dvdt_rrm_max_R)))[0][0]
        self.dvdt_rr_max = abs(((G_Vf[lt_time_dvdt_rrm_max_R] - G_Vf[lt_time_dvdt_rrm_max_L])/(G_T[lt_time_dvdt_rrm_max_R] - G_T[lt_time_dvdt_rrm_max_L]))/1000)
        #print(f"dvdt_rrm_max出现的时间: {round(self.time_dvdt_rrm_max, 6)} us")
        #print(f"2.5ns 前的时间: {round(time_dvdt_rrm_max_L, 6)} us，对应索引: {lt_time_dvdt_rrm_max_L}")
        #print(f"2.5ns 后的时间: {round(time_dvdt_rrm_max_R, 6)} us，对应索引: {lt_time_dvdt_rrm_max_R}")
        #print('反向恢复最大dvdt：', self.dvdt_rr_max)
        return

def ExtractWaveData(data, OneCsvInfoDict, UIInfoDict):
    '''
    从数据列表中提取时间、栅极电压、漏极电压、漏极电流、反向恢复电压、反向恢复电流。

    输入参数
    data: 包含csv文件数据的列表，已经除去了前几行的数据信息
    OneCsvInfoDict:字典，包含路径、回路、栅极正负压、示波器通道位置信息。
    输出参数
    G_T, G_Vge, G_Vce, G_Ic, G_Vf, G_If：列表，以小数形式存储。
    is_accurate：布尔值，只起到警告作用，判断时间精度。
    '''


    #print(Ch_define)
    global G_T, G_Vge, G_Vce, G_Ic, G_Vge_D, G_Vf, G_If, is_accurate

    G_T, G_Vge, G_Vce, G_Ic, G_Vge_D, G_Vf, G_If = [], [], [], [], [], [], []
    is_accurate = True # 判断时间存储精度是否足够

    if OneCsvInfoDict['Loop'] == 'HIGH' :
        G_Vge_Reverse = UIInfoDict['HS_Vgs_act_Reverse']
        G_Vce_Reverse = UIInfoDict['HS_Vds_act_Reverse']
        G_Ic_Reverse = UIInfoDict['HS_Ids_act_Reverse']
        G_Vge_D_Reverse = UIInfoDict['HS_Vgs_pas_Reverse']
        G_Vf_Reverse = UIInfoDict['HS_Vds_pas_Reverse']
        G_If_Reverse = UIInfoDict['HS_Idiode_pas_Reverse']
        G_IL_Reverse = UIInfoDict['HS_IL_Reverse']
    elif OneCsvInfoDict['Loop'] == 'LOW' :
        G_Vge_Reverse = UIInfoDict['LS_Vgs_act_Reverse']
        G_Vce_Reverse = UIInfoDict['LS_Vds_act_Reverse']
        G_Ic_Reverse = UIInfoDict['LS_Ids_act_Reverse']
        G_Vge_D_Reverse = UIInfoDict['LS_Vgs_pas_Reverse']
        G_Vf_Reverse = UIInfoDict['LS_Vds_pas_Reverse']
        G_If_Reverse = UIInfoDict['LS_Idiode_pas_Reverse']
        G_IL_Reverse = UIInfoDict['LS_IL_Reverse']


    for row in data:
        G_T.append(float(row[0]) * 1000000) #单位s化为us
        if OneCsvInfoDict['VgsChannel'] != 0:
            G_Vge.append(float(row[OneCsvInfoDict['VgsChannel']]) * G_Vge_Reverse)
        if OneCsvInfoDict['VdsChannel'] != 0:
            G_Vce.append(float(row[OneCsvInfoDict['VdsChannel']]) * G_Vce_Reverse)
        if OneCsvInfoDict['CrossTalkChannel'] != 0:
            G_Vge_D.append(float(row[OneCsvInfoDict['CrossTalkChannel']]) * G_Vge_D_Reverse)
        if OneCsvInfoDict['VfChannel'] != 0:
            G_Vf.append(float(row[OneCsvInfoDict['VfChannel']]) * G_Vf_Reverse)
        
        
        if OneCsvInfoDict['IdsChannel'] != 0:
            G_Ic.append(float(row[OneCsvInfoDict['IdsChannel']]) * G_Ic_Reverse)
            #print('1.读取Ids')
            if OneCsvInfoDict['IfChannel'] != 0:
                G_If.append((-float(row[OneCsvInfoDict['IfChannel']])) * G_If_Reverse)
                #print('2.读取If，直接读取')
            elif (OneCsvInfoDict['IfChannel'] == 0) & (OneCsvInfoDict['ILChannel'] != 0):
                G_If.append((float(row[OneCsvInfoDict['ILChannel']] * G_IL_Reverse)) - (float(row[OneCsvInfoDict['IdsChannel']]) * G_Ic_Reverse))
                #print('3.读取If，用Ids和Il算')
            else:
                pass
                print('def_wave - ExtractWaveData错误：缺少被动管或电感电流，无法计算被动管电流相关内容。')
        elif OneCsvInfoDict['IdsChannel'] == 0:
            if (OneCsvInfoDict['IfChannel'] != 0) & (OneCsvInfoDict['ILChannel'] != 0):
                G_Ic.append((float(row[OneCsvInfoDict['ILChannel']] * G_IL_Reverse)) + (float(row[OneCsvInfoDict['IfChannel']]) * G_If_Reverse))
                G_If.append((-float(row[OneCsvInfoDict['IfChannel']])) * G_If_Reverse)
                #print('4.读取Ids，用If和Il算')
                #print('5.读取If')
            else:
                print('def_wave - ExtractWaveData错误：缺少主动管或电感电流，无法计算主动管电流相关内容。')

    '''
    # 这部分代码用来画图，后期使用函数替换
    plt.rc('font', family='simhei', size=15)  # 设置中文显示，字体大小
    plt.rc('axes', unicode_minus=False)  # 该参数解决负号显示的问题
    plt.figure(num=1)
    #plt.plot(G_T, G_Vge, 'y-', label='Vgs')
    #plt.plot(G_T, G_Vce, 'b-', label='Vds')
    plt.plot(G_T, G_Ic, 'r-', label='Ids')
    #plt.plot(G_T, G_Vge_D, 'g-', label='crosstalk')
    #plt.plot(G_T, G_Vf, 'o-', label='Vf')
    #plt.plot(G_T, G_If, 'k-', label='If')
    plt.legend(loc='best')
    plt.title('整体波形')
    plt.show()
    '''

    if G_T[2]-G_T[1]==0.0:
        is_accurate = False
        print("def_wave.ExtractWaveData警告：时间存储精度过低，可能出现损耗计算失败问题。")
        # 待优化def_wave.ExtractWaveData：加一个函数，判断时间数据是否精确。
        # 待优化def_wave.ExtractWaveData：加一个函数，通过读取csv文件，自定义各通道的内容。
        # 待优化def_wave.ExtractWaveData：加一个函数，将图像画出来。
    return G_T, G_Vge, G_Vce, G_Ic, G_Vf, G_If, is_accurate

def IsFilter(flag, G_Vge, G_Vce, G_Ic, G_Vf, G_If, UIInfoDict):
    '''
    是否启动低通滤波器的选项

    输入参数
    flag：布尔值，判断是否启动滤波器，启动为True，不启动为False。
    G_T, G_Vge, G_Vce, G_Ic, G_Vf, G_If：列表，滤波前的波形。
    输出参数
    G_T, G_Vge, G_Vce, G_Ic, G_Vf, G_If：列表，经过滤波器后输出的波形。
    '''
    #nyquist_freq = 1000* UIInfoDict['sampling_rate'] / 2
    #Wn = UIInfoDict['cutoff_frequency'] / nyquist_freq
    #print(Wn)

    if flag == True:
        print('启动低通滤波器')
        G_Vge = list(LowPassFilter(G_Vge, UIInfoDict['sampling_rate'], UIInfoDict['cutoff_frequency']))
        G_Vce = list(LowPassFilter(G_Vce, UIInfoDict['sampling_rate'], UIInfoDict['cutoff_frequency']))
        G_Ic = list(LowPassFilter(G_Ic, UIInfoDict['sampling_rate'], UIInfoDict['cutoff_frequency']))
        G_Vf = list(LowPassFilter(G_Vf, UIInfoDict['sampling_rate'], UIInfoDict['cutoff_frequency']))
        G_If = list(LowPassFilter(G_If, UIInfoDict['sampling_rate'], UIInfoDict['cutoff_frequency']))
        #print('完成滤波')
    else:
        pass
    return G_Vge, G_Vce, G_Ic, G_Vf, G_If

def LowPassFilter(sig, fs=6.25e9, f_max=1e8, N=8):
    '''
    滤波器,默认使用低通滤波器
    N：滤波器阶数
    Wn：截止频率，0.1表示截止频率为100Hz
    btype：过滤器类型，'lowpass'低通 'highpass'高通 'bandpass'带通 'bandstop'带阻
    analog: False数字滤波器，True模拟滤波器
    output: 输出类型，'ba’返回数组b、a，'zpk’返回数组z、p、浮点型k，'sos’返回数组sos

    输入参数
    sig：滤波前的波形。
    输出参数
    f_pad：滤波后的波形。

    计算Nyquist频率：Nyquist频率 = 采样频率 / 2
    计算归一化截止频率 Wn：Wn = 截止频率 / Nyquist频率
    
    截止频率是一个表示在滤波器中信号被抑制的频率。对于低通滤波器来说，截止频率是指在该频率之上的信号被滤波器抑制。
    在设计巴特沃斯滤波器时，截止频率是以采样率的一半为基准的。采样率是指在单位时间内对信号进行采样的次数。在数字信号处理中，采样率通常以赫兹（Hz）为单位。
    如果你希望滤除300 MHz以上的信号，那么你需要先确定你的信号的采样率。假设你的采样率为1 GHz（即1秒内进行10^9次采样），那么你可以将截止频率设置为300 MHz / (0.5 * 1 GHz) = 0.6。
    因此，在这种情况下，你可以将代码中的0.8改为0.6来实现滤除300 MHz以上信号的效果。注意，实际应用中可能还需要对滤波器的阶数和滤波器类型进行调整以获得更好的滤波效果。
    '''
    Wn = f_max / (fs / 2)  # 归一化到 Nyquist 频率
    # 检查 Wn 是否有效
    if Wn >= 1:
        raise ValueError("f_max must be less than fs / 2 (Nyquist frequency)")
    # 设计滤波器
    b, a = sgn.butter(N=N, Wn=Wn, btype='lowpass', analog=False, output='ba')
    # 应用滤波器
    f_pad = sgn.filtfilt(b=b, a=a, x=sig)
    
    return f_pad

def GetDynamicData(module_type, VgsR, Vgs, sampling_rate):
    '''
    用来提取开通和关断过程的动态参数
    输入参数
    待更新

    输出参数
    Vce_stable：电压稳定值，由第一次关断和第二次开通之间的电压确定。
    Ic_off：第一次关断电流值。
    Vpeak：第二次开通时电压尖峰。
    tdon：开通延时。
    tr：上升时间。
    ton：开通时间。
    Eon：开通损耗。
    didt_on_01_09：开通期间电流变化率。
    dvdt_on_09_01：开通期间电压变化率。
    tdoff：关断延时。
    tf：下降时间。
    toff：关断时间。
    Eoff：关断损耗。
    didt_off_09_01：关断期间电流变化率。
    dvdt_off_01_09：关断期间电压变化率。
    ti：二极管反向恢复时间（长
    trr：二极管反向恢复时间（短
    Vf_max：二极管反向恢复电压最大值
    Irrm：二极管反向恢复电流
    didt_rr_05_05：二极管反向恢复电流变化率
    Qrr：二极管反向恢复电荷
    Erec：二极管反向恢复损耗
    输出参数以浮点小数形式输出，保存在一个元组中。
    '''
    Get = GetDynamicDataObject()
    Get.get_key_time(VgsR, Vgs) # 通过Vge获取两次的开关时间点
    if Get.Vge_error == 0: # 如果Vge波形有问题，则进行报错
        Get.calibration_timeline()
        Get.get_Vge_stable()
        Get.getl_Ic_off()
        Get.getl_Vpeak()
        Get.get_Vce_stable() # 到这里没问题
        Get.get_key_time_2()
        Get.get_didt_dvdt(sampling_rate)
        if module_type == 'MOSFET':
            Get.get_Eon_MOSFET()
            Get.get_Eoff_MOSFET()
            Get.get_ton_MOSFET()
            Get.get_toff_MOSFET()
        elif module_type == 'IGBT':
            Get.get_Eon_IGBT()
            Get.get_Eoff_IGBT()
            Get.get_ton_IGBT()
            Get.get_toff_IGBT()
        else :
            Get.get_Eon_MOSFET()
            Get.get_Eoff_MOSFET()
            Get.get_ton_MOSFET()
            Get.get_toff_MOSFET()
        Get.get_diode_time(sampling_rate)
        Get.get_diode_data(sampling_rate)
    else:
        pass
   
    
    #以下打印代码只是在修改功能时使用
    '''print('-'*100)  # {}中加入:.2f表示保留两位小数
    print('Vceh = {:.2f} (V)'.format(Get.Vce_stable))
    print('Ic_off = {:.2f} (A)'.format(Get.Ic_off))
    print('Vpeak = {:.2f} (V)'.format(Get.Vpeak))
    print('-'*50)
    print('td(on) = {:.2f} ns'.format(Get.tdon))
    print('tr = {:.2f} ns'.format(Get.tr))
    print('ton = {:.2f} ns'.format(Get.ton))
    print('Eon = {:.2f} mJ'.format(Get.Eon))
    print('dI/dt(on) = {:.2f} (GA/s)'.format(Get.didt_on_01_09))
    print('dV/dt(on) = {:.2f} (GV/s)'.format(Get.dvdt_on_09_01))
    print('-'*50)
    print('td(off) = {:.2f} ns'.format(Get.tdoff))
    print('tf = {:.2f} ns'.format(Get.tf))
    print('toff = {:.2f} ns'.format(Get.toff))
    print('Eoff = {:.2f} mJ'.format(Get.Eoff))
    print('dI/dt(off) = {:.2f} (GA/s)'.format(Get.didt_off_09_01))
    print('dV/dt(off) = {:.2f} (GV/s)'.format(Get.dvdt_off_01_09))
    print('-'*50)
    print('ti(on) = {:.2f} ns'.format(Get.ti))
    print('trr(on) = {:.2f} ns'.format(Get.trr))
    print('Vf_max = {:.2f} (V)'.format(Get.Vf_max))
    print('Irrm = {:.2f} (A)'.format(Get.Irrm))
    print('dI/dt(rr) = {:.2f} (GA/s)'.format(Get.didt_rr_05_05))
    print('dV/dt(rr) = {:.2f} (GV/s)'.format(Get.dvdt_rr_01_09))
    print('Qrr = {:.2f} uC'.format(Get.Qrr))
    print('Erec = {:.2f} mJ'.format(Get.Erec))
    print('-'*100)'''

    return_list = [Get.Ic_off, Get.tdon, Get.tr, Get.ton, Get.didt_on_01_09, Get.dvdt_on_09_01, Get.didt_on_02_08, Get.dvdt_on_08_02, Get.didt_on_03_07, Get.dvdt_on_07_03, Get.Eon, Get.didt_on_max, Get.dvdt_on_max, 
            Get.tdoff, Get.tf, Get.toff, Get.didt_off_09_01, Get.dvdt_off_01_09, Get.didt_off_08_02, Get.dvdt_off_02_08, Get.didt_off_07_03, Get.dvdt_off_03_07, Get.didt_off_max, Get.dvdt_off_max, Get.Vce_stable, Get.Vpeak, Get.Eoff, Get.Eon+Get.Eoff,
            Get.Vge_D_MAX_on, Get.Vge_D_MIN_off, Get.ti, Get.Irrm, Get.Vf_max, Get.Qrr, Get.Erec, Get.didt_rr_05_05, Get.dvdt_rr_01_09, Get.dvdt_rr_01_fs, Get.dvdt_rr_max,
            Get.time_didt_on_max, Get.time_dvdt_on_max, Get.time_didt_off_max, Get.time_dvdt_off_max, Get.time_dvdt_rrm_max, ]
    return (return_list)

def Derivatives(sig):
    '''
    求导函数
    '''
    h = abs(sig[0] - sig[1]) # 保证导数不会因为初始数据的波动而有正负差异
    #h = sig[0] - sig[1] 
    f_derivatives = np.gradient(sig, h)
    return f_derivatives