import os
#    定义：取最新测试报告
class Get_File():
    def new_file(self,test_dir):
        # 列举test_dir目录下的所有文件，结果以列表形式返回。
        lists = os.listdir(test_dir)
        # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
        # 最后对lists元素，按文件修改时间大小从小到大排序。
        lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
        # 获取最新文件的绝对路径
        file_path = os.path.join(test_dir, lists[-1])
        #    L=file_path.split('\\')
        #    file_path='\\\\'.join(L)
        return file_path