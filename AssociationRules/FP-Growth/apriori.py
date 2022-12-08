from datetime import datetime

class Apriori():

    def __init__(self, dataset):
        self.dataset = dataset
        self.support_data = {}
        self.freq_itemsets = []
        self.t_num = float(len(self.dataset))


    def __create_C1(self):
        """
        Create frequent candidate 1-itemset C1 by scaning data set.
        Args:
            data_set: A list of transactions. Each transaction contains several items.
        Returns:
            C1: A set which contains all frequent candidate 1-itemsets一个集合，包含所有频繁1项集。
        """
        C1 = set()
        for t in self.dataset:      ##从dataset的列表行开始进行检索
            for item in t:          ##行：开始一个一个的检索这一行的数据。
                item_set = frozenset([item])    ##item_set为每一个item建立一个冻结的集合。冻结这个集合是为了可以放入另一个集合。
                ##即C1这个集合。而且注意的，item_set是不断的更新的。可以观察到这一个事情。
                C1.add(item_set)
        return C1
        ##C1是包含所有元素的集合。

    def __create_Ck(self, Lksub1, k):
        """
        Create Ck, a set which contains all all frequent candidate k-itemsets
        by Lk-1's own connection operation.

        L1 = self.__generate_Lk_by_Ck(C1, min_sup)      ##确定第一表。 Lksub1 = L1.copy()
        
        Args:
            Lksub1: Lk-1, a set which contains all frequent candidate (k-1)-itemsets. 
            k: the item number of a frequent itemset.
        Return:
            Ck: a set which contains all all frequent candidate k-itemsets.
        """
        Ck = set()
        len_Lksub1 = len(Lksub1)
        list_Lksub1 = list(Lksub1)
        for i in range(len_Lksub1):
            for j in range(1, len_Lksub1):
                l1 = list(list_Lksub1[i])
                l2 = list(list_Lksub1[j])
                l1.sort()
                l2.sort()
                if l1[0:k-2] == l2[0:k-2]:
                    Ck_item = list_Lksub1[i] | list_Lksub1[j]   #或运算。
                    # pruning
                    if self.__is_apriori(Ck_item, Lksub1):
                        Ck.add(Ck_item)
        return Ck

    def __is_apriori(self, Ck_item, Lksub1):
        """
        Judge whether a frequent candidate k-itemset satisfy Apriori property.
        Args:
            Ck_item: a frequent candidate k-itemset in Ck which contains all frequent
                    candidate k-itemsets.
            Lksub1: Lk-1, a set which contains all frequent candidate (k-1)-itemsets.
        Returns:
            True: satisfying Apriori property.
            False: Not satisfying Apriori property.
        """
        for item in Ck_item:
            sub_Ck = Ck_item - frozenset([item])
            if sub_Ck not in Lksub1:
                return False
        return True





    def __generate_Lk_by_Ck(self, Ck, min_sup):
        """
        Generate Lk by executing a delete policy from Ck.
        Args:
            data_set: A list of transactions. Each transaction con tains several items.
            Ck: A set which contains all all frequent candidate k-itemsets.
            min_sup: The minimum support.最小的支持度
            support_data: A dictionary. The key is frequent itemset and the value is support.
        Returns:
            Lk: A set which contains all all frequent k-itemsets.
        """
        Lk = set()  #建立一个名为LK的集合
        item_count = {}
        for t in self.dataset:
            for item in Ck:
                if item.issubset(t):
                    if item not in item_count:
                        item_count[item] = 1
                    else:
                        item_count[item] += 1
##issubset 是比较内容是否相同的函数。在这个例子中就是通过比较来确定各个项集的个数
        for item in item_count:
            if (item_count[item] / self.t_num) >= min_sup:
                Lk.add(item)
                self.support_data[item] = item_count[item] / self.t_num
##排除项集，小于最小支持度的舍掉，大于的则添加到LK集合中。并且储存每个item的支持度的大小。
        return Lk


    def generate_L(self, min_sup):
        """
        Generate all frequent itemsets.
        Args:
            data_set: A list of transactions. Each transaction contains several items.
            k: Maximum number of items for all frequent itemsets.
            min_sup: The minimum support.
        Returns:
            L: The list of Lk.
            support_data: A dictionary. The key is frequent itemset and the value is support.
        """
        start = datetime.now()
        C1 = self.__create_C1() #调用建立一项集的函数。
        deltatime = datetime.now() - start
        create_Ck_time = deltatime.seconds + deltatime.microseconds / 1000000
        ##检查函数运行的时间。即读取表的时间。
        start = datetime.now()
        L1 = self.__generate_Lk_by_Ck(C1, min_sup)      ##确定第一表。
        deltatime = datetime.now() - start
        generate_Lk_time = deltatime.seconds + deltatime.microseconds / 1000000
        
        Lksub1 = L1.copy()
        for lk_i in Lksub1:
            self.freq_itemsets.append((lk_i, self.support_data[lk_i]))
        i = 2

##上面的是建立第一个频繁一项集的方法。C1为一项集，L1为频繁一项集。它是通过一项集来的。因为它的输入有min_sup这一项。
##LKsub1是一个中间变量。从下面的语句：Lksub1 = Li.copy()可以知道：LKsub1是每一个频繁k项集的中间项。

        while True:
            start = datetime.now()
            Ci = self.__create_Ck(Lksub1, i)
            deltatime = datetime.now() - start
            create_Ck_time += deltatime.seconds + deltatime.microseconds / 1000000

            start = datetime.now()
            Li = self.__generate_Lk_by_Ck(Ci, min_sup)
            deltatime = datetime.now() - start
            generate_Lk_time += deltatime.seconds + deltatime.microseconds / 1000000

            Lksub1 = Li.copy()
            
            if len(Lksub1) == 0:
                break
            for lk_i in Lksub1:
                self.freq_itemsets.append((lk_i, self.support_data[lk_i]))
            i += 1
        
        print("Create Ck time (s): ", create_Ck_time)
        print("Generate Lk time (s): ", generate_Lk_time)

        return self.freq_itemsets