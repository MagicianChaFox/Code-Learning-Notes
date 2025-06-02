import pandas as pd
from collections import OrderedDict

# 提供的原始列表
ToDolist = [
    ['Vgsth', 'Vgsth_Ids_set=100(mA)', 'HIGH', '025C', 3.3, 'V', 'BC47'],
    ['Vgsth', 'Vgsth_Ids_set=100(mA)', 'HIGH', '175C', 2.5, 'V', 'BC47'],
    ['Vgsth', 'Vgsth_Ids_set=100(mA)', 'LOW', '025C', 3.325, 'V', 'BC47'],
    ['Vgsth', 'Vgsth_Ids_set=100(mA)', 'LOW', '175C', 2.5, 'V', 'BC47'],
    ['Igss+', 'Igss_Vgs_set=21(V)', 'HIGH', '025C', 0.08, 'nA', 'BC47'],
    ['Igss+', 'Igss_Vgs_set=21(V)', 'HIGH', '175C', 3.62, 'nA', 'BC47'],
    ['Igss+', 'Igss_Vgs_set=21(V)', 'LOW', '025C', 0.19, 'nA', 'BC47'],
    ['Igss+', 'Igss_Vgs_set=21(V)', 'LOW', '175C', 5.34, 'nA', 'BC47'],
    ['Igss-', 'Igss_Vgs_set=-4(V)', 'HIGH', '025C', 0.66, 'nA', 'BC47'],
    ['Igss-', 'Igss_Vgs_set=-4(V)', 'HIGH', '175C', 1.22, 'nA', 'BC47'],
    ['Igss-', 'Igss_Vgs_set=-4(V)', 'LOW', '025C', 0.67, 'nA', 'BC47'],
    ['Igss-', 'Igss_Vgs_set=-4(V)', 'LOW', '175C', 1.2, 'nA', 'BC47'],
    ['Idss', 'Idss_Vds_set=1200(V)', 'HIGH', '025C', 6.06, 'uA', 'BC47'],
    ['Idss', 'Idss_Vds_set=1200(V)', 'HIGH', '175C', 42.55, 'uA', 'BC47'],
    ['Idss', 'Idss_Vds_set=1200(V)', 'LOW', '025C', 4.94, 'uA', 'BC47'],
    ['Idss', 'Idss_Vds_set=1200(V)', 'LOW', '175C', 41.04, 'uA', 'BC47'],
    ['BV', 'BV_Ids_set=2(mA)', 'HIGH', '025C', 1200.0, 'V', 'BC47'],
    ['BV', 'BV_Ids_set=2(mA)', 'HIGH', '175C', 1200.0, 'V', 'BC47'],
    ['BV', 'BV_Ids_set=2(mA)', 'LOW', '025C', 1200.0, 'V', 'BC47'],
    ['BV', 'BV_Ids_set=2(mA)', 'LOW', '175C', 1200.0, 'V', 'BC47'],
    ['Rdson', 'Vgs=18(V) Ids=550(A)', 'HIGH', '025C', 1.3, 'mΩ', 'BC47'],
    ['Rdson', 'Vgs=18(V) Ids=550(A)', 'HIGH', '175C', 3.27, 'mΩ', 'BC47'],
    ['Rdson', 'Vgs=18(V) Ids=550(A)', 'LOW', '025C', 1.4, 'mΩ', 'BC47'],
    ['Rdson', 'Vgs=18(V) Ids=550(A)', 'LOW', '175C', 3.51, 'mΩ', 'BC47'],
    ['Vf-', 'Vgs=-2(V) Isd=360(A)', 'HIGH', '025C', 3.44, 'V', 'BC47'],
    ['Vf-', 'Vgs=-2(V) Isd=360(A)', 'HIGH', '175C', 3.33, 'V', 'BC47'],
    ['Vf-', 'Vgs=-2(V) Isd=360(A)', 'LOW', '025C', 3.52, 'V', 'BC47'],
    ['Vf-', 'Vgs=-2(V) Isd=360(A)', 'LOW', '175C', 3.42, 'V', 'BC47'],
    ['Vf+', 'Vgs=18(V) Isd=360(A)', 'HIGH', '025C', 0.45, 'V', 'BC47'],
    ['Vf+', 'Vgs=18(V) Isd=360(A)', 'HIGH', '175C', 1.1, 'V', 'BC47'],
    ['Vf+', 'Vgs=18(V) Isd=360(A)', 'LOW', '025C', 0.49, 'V', 'BC47'],
    ['Vf+', 'Vgs=18(V) Isd=360(A)', 'LOW', '175C', 1.2, 'V', 'BC47']
]

# 创建 DataFrame
df = pd.DataFrame(ToDolist, columns=['名称', '项目', '状态', '温度', '数值', '单位', '类型'])

# 提取原始顺序中的唯一名称和项目组合
name_project_order = list(OrderedDict.fromkeys([(row[0], row[1]) for row in ToDolist]))

result = []

for name, project in name_project_order:
    # 获取对应的组
    group = df[(df['名称'] == name) & (df['项目'] == project)]
    unit = group['单位'].iloc[0]
    device_type = group['类型'].iloc[0]
    
    # 收集所有温度
    temps = group['温度'].unique()
    
    # 添加 -40C 行，放在 025C 之前
    result.append([name, project, '-40C', 'HIGH', 'LOW', 0, 0, unit, device_type])
    
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
        
        result.append(new_row)

# 打印结果
for row in result:
    print(row)