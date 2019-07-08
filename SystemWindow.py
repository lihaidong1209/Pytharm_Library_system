class View(object):
    def printView(self):
        print('================================================================')
        print('****************************************************************')
        print('*                                                              *')
        print('*                                                              *')
        print('*             <<欢迎光临百知教育在线图书管理系统！>>           *')
        print('*                                                              *')
        print('*                                    官方网站:www.baizhi.com   *')
        print('****************************************************************')
        print('-----------------系统正在载入中，请等待.....--------------------')
    def printLogOut(self):
        print('================================================================')
        print('****************************************************************')
        print('*                                                              *')
        print('*                                                              *')
        print('*            <<成功图书管理退出系统，欢迎下次光临！>>          *')
        print('*                                                              *')
        print('*                                                              *')
        print('****************************************************************')
    def printLogging(self):
        print('================================================================')
        print('****************************************************************')
        print('*               <<请输入你要进行的操作指令>>                   *')
        print('*         [注册]----[1]             [登录]----[2]              *')
        print('*                                                              *')
        print('*         [游客]----[3]             [退出]----[4]              *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printRegister(self):
        print('================================================================')
        print('****************************************************************')
        print('*               <<请输入你要进行的操作指令>>                   *')
        print('*                                                              *')
        print('*         [开始注册]--[1]             [退出注册]--[2]          *')
        print('*                                                              *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printLoginer(self):
        print('================================================================')
        print('****************************************************************')
        print('*               <<请输入你要进行的操作指令>>                   *')
        print('*                                                              *')
        print('*         [开始登录]--[1]             [退出登录]--[2]          *')
        print('*                                                              *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printChioceLoginersr(self):
        print('================================================================')
        print('****************************************************************')
        print('*               <<请输入你要进行的操作指令>>                   *')
        print('*                                                              *')
        print('*         [继续登录]--[1]             [退出登录]--[2]          *')
        print('*                                                              *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printMain(self):
        print('================================================================')
        print('****************************************************************')
        print('*               <<-请选择书籍访问操作指令->>                   *')
        print('*     [查询所有书籍] - -[1]       [修改书籍信息] - -[2]        *')
        print('*                                                              *')
        print('*     [增加新的书籍] - -[3]       [删除没用书籍] - -[4]        *')
        print('*                                                              *')
        print('*     [修改用户信息] - -[5]       [退 出 系 统 ] - -[6]        *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printChangeChoicer(self):
        print('================================================================')
        print('****************************************************************')
        print('*    <<已显示所有书籍，是否退出查询界面:YES--[1]               *')
        print('*                                                              *')
        print('*                       [YES]--[1]                             *')
        print('*                                                              *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printChangeChoice(self):
        print('================================================================')
        print('****************************************************************')
        print('*           <<请按照修改需求输入修改书籍信息指令>>             *')
        print('*      [修改书籍名称]--[1]          [修改书籍价格]--[2]        *')
        print('*                                                              *')
        print('*      [修改书籍类别]--[3]          [修改书籍编号]--[4]        *')
        print('*                                                              *')
        print('*      [修改书籍数量]--[5]          [保存退出界面]--[6]        *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printChangeBooksSort(self):
        print('================================================================')
        print('****************************************************************')
        print('*           <<请选择想要修改的书籍类别编号>>                   *')
        print('*         [武侠类]--[1]               [文学类]--[2]            *')
        print('*                                                              *')
        print('*         [百科类]--[3]               [哲学类]--[4]            *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printAddBooks(self):
        print('================================================================')
        print('****************************************************************')
        print('*            <<请按照需求输入书籍信息对应编号>>                *')
        print('*      [添加书籍名称]--[1]          [添加书籍价格]--[2]        *')
        print('*                                                              *')
        print('*      [添加书籍类别]--[3]          [添加书籍编号]--[4]        *')
        print('*                                                              *')
        print('*      [添加书籍数量]--[5]          [保存退出界面]--[6]        *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printAddBooksSort(self):
        print('================================================================')
        print('****************************************************************')
        print('*           <<请选择想要添加的书籍类别编号>>                   *')
        print('*         [武侠类]--[1]               [文学类]--[2]            *')
        print('*                                                              *')
        print('*         [百科类]--[3]               [哲学类]--[4]            *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printDelBooks(self):
        print('================================================================')
        print('****************************************************************')
        print('*    <<书籍存在，是否要对书籍进行删除:YES--[1]/[NO]--[2]       *')
        print('*                                                              *')
        print('*           [YES]--[1]               [NO ]--[2]                *')
        print('*                                                              *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')
    def printChangeUser(self):
        print('================================================================')
        print('****************************************************************')
        print('*           <<请输入你要修改信息的指令编号>>                   *')
        print('*         [修改用户名称]--[1]       [修改用户密码]--[2]        *')
        print('*                                                              *')
        print('*         [退出当前界面]--[3]                                  *')
        print('*              <<注意:  指令必须为整型数字!>>                  *')
        print('****************************************************************')