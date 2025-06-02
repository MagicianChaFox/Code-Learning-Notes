import os
import shutil

def move_files_by_keywords(src_folder, dest_folder, keywords, file_types):
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(src_folder):
        file_path = os.path.join(src_folder, filename)
        
        # 检查文件是否是文件夹
        if os.path.isfile(file_path):
            # 检查文件名是否包含关键字
            for keyword in keywords:
                if keyword in filename:
                    # 创建以关键字命名的子文件夹
                    keyword_folder = os.path.join(dest_folder, keyword)
                    if not os.path.exists(keyword_folder):
                        os.makedirs(keyword_folder)
                    
                    # 根据文件类型进一步分类
                    for file_type in file_types:
                        if filename.endswith(file_type):
                            type_folder = os.path.join(keyword_folder, file_type.strip('.'))
                            if not os.path.exists(type_folder):
                                os.makedirs(type_folder)
                            
                            # 移动文件到新的位置
                            shutil.move(file_path, os.path.join(type_folder, filename))
                            break  # 文件已处理，跳出循环

# 使用示例
source_folder_path = r'D:\File\0.公司相关\1.1.黄山MOSFET\8并1200V\22.GLB短路测试\1.静态\CB64'
destination_folder_path = source_folder_path
#keywords = ['1.1.Igss负', '1.2.Igss正', '2.Vth-Vds=Vgs', '3.Rds(on)', '4.Transfer', '5.Vf负', '5.Vf正(小Vgs)', '6.Idss']
keywords = ['1.1.Igss负', '1.2.Igss正', '2.Vth_双源', '3.Rds(on)',  '5.Vf负', '5.Vf正', '6.Idss']
file_types = ['.csv', '.bmp']

move_files_by_keywords(source_folder_path, destination_folder_path, keywords, file_types)
