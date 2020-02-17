# -*- coding: utf-8 -*-

###########################################################################
## 程序设计 danscort yu (c)2018
##
##
##
###########################################################################
###########################################################################
## 本代码使用wxPython + ftplib 编写 注意 只能在python版本高于3的环境下执行,不支持python2
## 专门适应XFile家庭文件服务器软件的跨平台运行播放客户端,本程序属于备胎,如果windows和android客户端由于某些原因不再允许使用,才会发展python客户端,否则本程序只提供基本点播功能
## 代码里硬代码支持中文和英文,当然你也可以扩展支持各种其他语言,外挂也可以,但是我不想在细节上花费太多时间,因为windows平台已经有专用客户端,主要是支持Linux/unix平台用
## 注意 如果要使用标准FTP服务器软件 则必须注销掉SLST HTTP等扩展指令 并且换用不安全的明文口令,
## XFile服务器软件下载 http://www.phoenixp2p.com
## List列表指令采用XFile专用的简化格式列表 去掉SLST 可以切换回标准FTP列表
##
## 我们支持XFile加密口令 [加盐md5口令],这里我们套用了移动端简化验证口令 两种方式 都是加盐的验证 可以抗破解
## 但是在python里,我们使用的是一次加盐加密口令,而windows/android专用配套客户端采用的是两次加盐加密,这里简化了
## 因为各种限制 ,只做了检索支持
## python 和wxPython我都是第一次使用, 不熟悉,项目比较粗糙,无法象native c++开发界面那样精确
## 执行方式 命令行下 输入 python xftp.py 或者建立一个批处理的快捷方式放到桌面上
## 目录下的xftpset文件是外部播放器程序的播放指令等信息 您应该根据你播放器的实际安装目录进行修改
## 在windows端支持 vlc mpv kodi 等主流播放器 ,注意,如果目录中包含空格,应该使用双引号将目录完整的包裹起来 否则出错
## Player_cmd=H:\VLC\vlc.exe "$url" 或者 Player_cmd="c:\Program Files\VLC\vlc.exe" "$url"
##
## Player_cmdunix=vlc.exe "$url"
## 前一个Player_cmd用于windows环境 ,后一个用于非windows环境 ,请根据实际进行修改 $url 代表实际连接
## 为了运行本程序,必须在您的电脑上安装python3 https://www.python.org/ , 此外还需要安装wxpython https://www.wxpython.org
## 如果是正式版本,请将全局变量_debugmode 设置为False
## 2019.10 第二次修改,加入http流播放实现,python端没有实现的功能包括自动sha256加密口令登录模式(目前需要手动设置为True,前提是服务器必须打开并支持,默认是不采用) 动态ipv6服务器地址电子邮件解析 数据备份 二维码图片连接等
##
## 在可以使用我们专用客户端的平台,如windows,android,不建议你使用python客户端,但是在Linux等没有配套客户端的平台,这可能是唯一的解决办法
##
##
##
##
##
##
##
## 您可以任意修改本代码 但是请保留本说明部分
## 作者: danscort@phoenixp2p.com
## 最后编辑:2019.09.30
###########################################################################
import sys
import os
import time
import wx.xrc
import socket

##import wx
import ftplib
from ftplib import FTP
from ftplib import FTP_TLS
import configparser
import hashlib
import wx

# from StringIO import StringIO
# import images

###########################################################################
## Class MyFrameMain
###########################################################################
# global m_ftp
# global m_ftps
# global mb_con
##以下是全局变量部分
_ftp = FTP()
_ftps = FTP_TLS()
_mbcon = True
_mbssl = False
_mbhttpstream = True
# 2019.10版本，实现http流播放功能 默认采用http流播放 如果要采用ftp播放 请将 _mbhttpstream设置为Falses
_httpport = 0
_httpsll = False
_debugmode = True
# 如果是正式发行版本 请修改为 _debugmode=False
_curworkdir = "/"
_chineseversion = True
_timersec = 0
# 播放调用程序 默认是vlc.exe 我们从配置文件读这个播放接口 这里只是预配置
_playercmd = 'vlc.exe "$url"'
# 配置文件
_configfile = "xftpset.ini"
_dlgitemfile = "dlgitem.ini"
# 随机数 XFile专用的随机数字符串
_srandomcode = "0"
# 全局登录口令 是二次MD5, 但是注意 这个全局字符串有时间限制 可能在服务器某次刷新后就发生变动
_sglobalpass = ""
# 2019.10新添加 用来支持将来版本的sha256加密口令模式 目前代码暂时还不能支持自动识别服务器是否要求sha256加密,未来版本添加自动识别功能
_mbsha256 = False


class MyFrameMain(wx.Frame):
    def __init__(self, parent):
        global _chineseversion
        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title="XFtp",
            pos=wx.DefaultPosition,
            size=wx.Size(800, 530),
            style=wx.CAPTION | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer1.SetMinSize(wx.Size(600, 20))
        bSizer2.SetMinSize(wx.Size(600, 20))
        if _chineseversion:
            self.m_staticText1 = wx.StaticText(
                self, wx.ID_ANY, "服务器地址 ", wx.DefaultPosition, wx.Size(60, 15), 0
            )
        else:
            self.m_staticText1 = wx.StaticText(
                self, wx.ID_ANY, "Server ", wx.DefaultPosition, wx.Size(60, 15), 0
            )

        self.m_staticText1.Wrap(-1)

        bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        if _chineseversion:
            self.m_textCtrlServer = wx.TextCtrl(
                self, wx.ID_ANY, "127.0.0.1", wx.DefaultPosition, wx.Size(100, 15), 0
            )

        else:
            self.m_textCtrlServer = wx.TextCtrl(
                self, wx.ID_ANY, "127.0.0.1", wx.DefaultPosition, wx.Size(100, 15), 0
            )

        # self.m_textCtrlServer = wx.TextCtrl( self, wx.ID_ANY, "127.0.0.1", wx.DefaultPosition, wx.Size( 100,15 ), 0 )
        bSizer1.Add(self.m_textCtrlServer, 0, wx.ALL, 5)

        if _chineseversion:
            self.m_staticText2 = wx.StaticText(
                self, wx.ID_ANY, "端口", wx.DefaultPosition, wx.Size(30, 15), 0
            )

        else:
            self.m_staticText2 = wx.StaticText(
                self, wx.ID_ANY, "Port", wx.DefaultPosition, wx.Size(30, 15), 0
            )

        # self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.Size( 30,15 ), 0 )
        self.m_staticText2.Wrap(-1)

        bSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrlPort = wx.TextCtrl(
            self, wx.ID_ANY, "21", wx.DefaultPosition, wx.Size(45, 15), 0
        )
        bSizer1.Add(self.m_textCtrlPort, 0, wx.ALL, 5)

        if _chineseversion:
            self.m_staticText3 = wx.StaticText(
                self, wx.ID_ANY, "用户名", wx.DefaultPosition, wx.Size(50, 15), 0
            )

        else:
            self.m_staticText3 = wx.StaticText(
                self, wx.ID_ANY, "User", wx.DefaultPosition, wx.Size(50, 15), 0
            )

        # self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, "User", wx.DefaultPosition, wx.Size( 50,15 ), 0 )
        self.m_staticText3.Wrap(-1)

        bSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrlUsername = wx.TextCtrl(
            self, wx.ID_ANY, "admin", wx.DefaultPosition, wx.Size(80, 15), 0
        )
        bSizer1.Add(self.m_textCtrlUsername, 0, wx.ALL, 5)

        if _chineseversion:
            self.m_staticText4 = wx.StaticText(
                self, wx.ID_ANY, "口令", wx.DefaultPosition, wx.Size(50, 15), 0
            )

        else:
            self.m_staticText4 = wx.StaticText(
                self, wx.ID_ANY, "Password", wx.DefaultPosition, wx.Size(50, 15), 0
            )

        # self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, "Password", wx.DefaultPosition, wx.Size( 50,15 ), 0 )
        self.m_staticText4.Wrap(-1)

        bSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrlPassword = wx.TextCtrl(
            self,
            wx.ID_ANY,
            "88888888",
            wx.DefaultPosition,
            wx.Size(70, 15),
            style=wx.TE_PASSWORD,
        )
        # 这里加入 设置textctrl 是口令模式

        bSizer1.Add(self.m_textCtrlPassword, 0, wx.ALL, 5)

        if _chineseversion:
            self.m_checkBoxHttp = wx.CheckBox(
                self, wx.ID_ANY, "Http流优先", wx.DefaultPosition, wx.Size(80, 15), 0
            )

        else:
            self.m_checkBoxHttp = wx.CheckBox(
                self, wx.ID_ANY, "Http stream", wx.DefaultPosition, wx.Size(80, 15), 0
            )

        # self.m_checkBoxHttp = wx.CheckBox( self, wx.ID_ANY, u"Http stream", wx.DefaultPosition, wx.Size( 65,15 ), 0 )
        bSizer1.Add(self.m_checkBoxHttp, 0, wx.ALL, 5)

        if _chineseversion:
            self.m_checkBoxSsl = wx.CheckBox(
                self, wx.ID_ANY, "SSL加密", wx.DefaultPosition, wx.Size(60, 15), 0
            )

        else:
            self.m_checkBoxSsl = wx.CheckBox(
                self, wx.ID_ANY, "TLS/SSL", wx.DefaultPosition, wx.Size(60, 15), 0
            )

        # self.m_checkBoxSsl = wx.CheckBox( self, wx.ID_ANY, "SSL", wx.DefaultPosition, wx.Size( 45,15 ), 0 )
        bSizer1.Add(self.m_checkBoxSsl, 0, wx.ALL, 5)

        if _chineseversion:
            self.m_buttonLogin = wx.Button(
                self, wx.ID_ANY, "连接", wx.DefaultPosition, wx.DefaultSize, 0
            )

        else:
            self.m_buttonLogin = wx.Button(
                self, wx.ID_ANY, "Connect", wx.DefaultPosition, wx.DefaultSize, 0
            )

        # self.m_buttonLogin = wx.Button( self, wx.ID_ANY, "Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add(self.m_buttonLogin, 0, wx.ALL, 5)

        # 这里我决定添加检索功能
        self.m_staticinfo = wx.StaticText(
            self, wx.ID_ANY, "/", wx.DefaultPosition, wx.Size(220, 18), wx.ALIGN_LEFT
        )
        self.m_staticinfo.Wrap(-1)
        bSizer2.Add(self.m_staticinfo)
        if _chineseversion:
            self.m_staticsearch = wx.StaticText(
                self,
                wx.ID_ANY,
                "关键词:",
                wx.DefaultPosition,
                wx.Size(80, 18),
                wx.ALIGN_LEFT,
            )

        else:
            self.m_staticsearch = wx.StaticText(
                self,
                wx.ID_ANY,
                "Keywords:",
                wx.DefaultPosition,
                wx.Size(80, 18),
                wx.ALIGN_LEFT,
            )

        # self.m_staticsearch=wx.StaticText( self, wx.ID_ANY, "Keywords:", wx.DefaultPosition, wx.Size( 80,18 ), wx.ALIGN_LEFT )
        self.m_staticsearch.Wrap(-1)
        bSizer2.Add(self.m_staticsearch)
        self.m_textsearch = wx.TextCtrl(
            self, wx.ID_ANY, ".mkv", wx.DefaultPosition, wx.Size(120, 18), wx.ALIGN_LEFT
        )
        bSizer2.Add(self.m_textsearch, 0, wx.ALL, 5)
        if _chineseversion:
            self.m_buttonSearch = wx.Button(
                self,
                wx.ID_ANY,
                "检索",
                wx.DefaultPosition,
                wx.DefaultSize,
                wx.ALIGN_RIGHT,
            )

        else:
            self.m_buttonSearch = wx.Button(
                self,
                wx.ID_ANY,
                "Search",
                wx.DefaultPosition,
                wx.DefaultSize,
                wx.ALIGN_RIGHT,
            )

        # self.m_buttonSearch = wx.Button( self, wx.ID_ANY, "Search", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        bSizer2.Add(self.m_buttonSearch, 0, wx.ALL, 5)

        bSizer3.Add(bSizer1, 1, wx.ALIGN_TOP | wx.FIXED_MINSIZE | wx.LEFT, 5)
        bSizer3.Add(bSizer2, 1, wx.ALIGN_TOP | wx.FIXED_MINSIZE | wx.LEFT, 5)
        bSizerList = wx.BoxSizer(wx.VERTICAL)

        self.il = wx.ImageList(16, 16)
        # self.idx1 = self.il.Add(images.Smiles.GetBitmap())
        # self.sm_up = self.il.Add(images.SmallUpArrow.GetBitmap())
        # self.sm_dn = self.il.Add(images.SmallDnArrow.GetBitmap())
        self.m_listCtrlFtp = wx.ListCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800, 500), wx.LC_REPORT
        )
        self.m_listCtrlFtp.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        bSizerList.Add(self.m_listCtrlFtp, 0, wx.ALL, 5)
        bSizer3.Add(bSizerList, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnMyClose)
        self.m_buttonLogin.Bind(wx.EVT_BUTTON, self.OnMyButtonClick)
        self.m_buttonSearch.Bind(wx.EVT_BUTTON, self.OnMySearchButtonClick)
        self.m_listCtrlFtp.Bind(wx.EVT_LIST_COL_CLICK, self.OnMyListColClick)
        self.m_listCtrlFtp.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnMyListItemActivated)
        self.m_listCtrlFtp.Bind(
            wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnMyListItemRightClick
        )
        # self.m_listCtrlFtp.Bind( wx.EVT_LIST_COL_RIGHT_CLICK, self.OnMyRightClick)
        # for wxMSW
        self.m_listCtrlFtp.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnMyRightClick)

        # for wxGTK
        self.m_listCtrlFtp.Bind(wx.EVT_RIGHT_UP, self.OnMyRightClick)

        # insert list columns  num attr size filename
        # self.m_listCtrlFtp.InsertColumn(0,"Num")
        # self.m_listCtrlFtp.InsertColumn(1,"Type")
        # self.m_listCtrlFtp.InsertColumn(2,"Size")
        # self.m_listCtrlFtp.InsertColumn(3,"Name")
        # we need to insert images for list
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        if _chineseversion:
            info.Text = "编号"
        else:
            info.Text = "Num"
        # info.Text = u"Num"
        self.m_listCtrlFtp.InsertColumn(0, info)

        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT
        # info.Image = -1
        info.Align = 0
        if _chineseversion:
            info.Text = "类型"
        else:
            info.Text = "Type"
        # info.Text = u"Type"
        self.m_listCtrlFtp.InsertColumn(1, info)

        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT
        # info.Image = -1
        info.Align = 0
        info.SetWidth(120)
        if _chineseversion:
            info.Text = "大小"
        else:
            info.Text = "Size"
        # info.Text = "Size"
        self.m_listCtrlFtp.InsertColumn(2, info)

        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT
        # info.Image = -1
        info.Align = 0
        if _chineseversion:
            info.Text = "名称"
        else:
            info.Text = "Name"
        # info.Text = "Name"
        info.SetWidth(480)
        self.m_listCtrlFtp.InsertColumn(3, info)
        # Bind all EVT_TIMER events to self.OnTest1Timer
        # 设置定时器 主要是用来支持定时发送NOOP指令 防止服务器断开连接
        self.timer1 = wx.Timer(self, 8801)
        # 必须指定只处理timer1事件
        self.Bind(wx.EVT_TIMER, self.OnMyTimerMsg, self.timer1)
        # 注意 绑定是在这里

        self.FuncChangeButton()
        # Load dlg item strings
        self.FuncLoadDlgItem()

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnMyClose(self, event):
        # event.Skip()
        global _mbcon
        global _ftp
        global _ftps
        global _mbssl
        if _mbcon:
            pass
        else:
            try:
                if mbssl:
                    _ftps.close()
                else:
                    _ftp.close()
            except:
                pass
        self.FuncSaveDlgItem()
        event.Skip()

    def FuncSaveDlgItem(self):
        # 在退出的时候保存参数
        global _dlgitemfile
        global _debugmode
        if _debugmode:
            print("Now will save dlg string to file")
        cf = configparser.RawConfigParser()
        cf.add_section("Dlgitem")
        cf.set("Dlgitem", "server_addr", self.m_textCtrlServer.GetLineText(0))
        cf.set("Dlgitem", "server_port", self.m_textCtrlPort.GetLineText(0))
        cf.set("Dlgitem", "server_username", self.m_textCtrlUsername.GetLineText(0))
        cf.set("Dlgitem", "server_password", self.m_textCtrlPassword.GetLineText(0))
        str1 = "0"
        if self.m_checkBoxSsl.GetValue():
            str1 = "1"
        cf.set("Dlgitem", "server_ssl", str1)
        str1 = "0"
        if self.m_checkBoxHttp.GetValue():
            str1 = "1"
        cf.set("Dlgitem", "server_http", str1)
        # cf.set('Dlgitem', 'server_addr', self.m_textCtrlServer.GetLineText(0))
        # cf.set('Dlgitem', 'server_addr', self.m_textCtrlServer.GetLineText(0))
        with open(_dlgitemfile, "wt") as configfile:
            cf.write(configfile)

        return

    def FuncLoadDlgItem(self):
        # 读取主界面的部分参数
        global _dlgitemfile
        global _debugmode
        cf = configparser.ConfigParser()
        try:
            cf.read(_dlgitemfile)
        except IOError as e:
            if _debugmode:
                print("Failed to load string file")
            return
        except:
            if _debugmode:
                print("Unknwon error to load string file")
            return
        # 现在保证已经正常打开配置文件 那么尝试读取吧
        str1 = ""
        try:
            str1 = cf.get("Dlgitem", "server_addr")
            if len(str1) >= 1:
                self.m_textCtrlServer.SetLabelText(str1)
            str1 = ""
            str1 = cf.get("Dlgitem", "server_port")
            if len(str1) >= 1:
                self.m_textCtrlPort.SetLabelText(str1)
            str1 = ""
            str1 = cf.get("Dlgitem", "server_username")
            if len(str1) >= 1:
                self.m_textCtrlUsername.SetLabelText(str1)
            str1 = ""
            str1 = cf.get("Dlgitem", "server_password")
            if len(str1) >= 1:
                self.m_textCtrlPassword.SetLabelText(str1)
            if cf.get("Dlgitem", "server_ssl") == "1":
                self.m_checkBoxSsl.SetValue(True)
            if cf.get("Dlgitem", "server_http") == "1":
                self.m_checkBoxHttp.SetValue(True)

        except (
            configparser.MissingSectionHeaderError,
            configparser.NoSectionError,
            configparser.NoOptionError,
        ) as e:
            if _debugmode:
                print("Read string section error")
            return
        except:
            if _debugmode:
                print("Read string section unknown error")
                return
        return

    def FuncLoadConfigFile(self):
        # 读取配置文件
        # 默认是当前目录下的xftp.ini
        # 如果你要支持多国家语言 事实上也可以在这里进行
        # 我是贪图方便 只做了英文和简体中文 硬编码 当然用c++的客户端我是采用的配置文件实现多国语言支持
        global _configfile
        global _playercmd
        global _debugmode
        cf = configparser.ConfigParser()
        # cf=configparser.RawConfigParser( )
        try:
            # cf.read(_configfile,'utf-8')
            # with open(_configfile, 'rb') as f:
            # 	content = f.read().decode('utf-8-sig').encode('utf8')
            # 	cf.readfp(StringIO(content))
            cf.read(_configfile)

        except IOError as e:
            if _debugmode:
                print("Failed to load config file")
            return

        except:
            if _debugmode:
                print("Unknwon error to load config file")
            return
        str1 = ""
        try:
            # 这里根据不同的操作系统读取不同的执行命令
            if os.name == "nt":
                str1 = cf.get("XFtp_Set", "Player_cmd")
            else:
                str1 = cf.get("XFtp_Set", "Player_cmdunix")
        except (
            configparser.MissingSectionHeaderError,
            configparser.NoSectionError,
            configparser.NoOptionError,
        ) as e:
            if _debugmode:
                print("Read section error")
            return
        except:
            if _debugmode:
                print("Unknown error to read section")
            str1 = ""
        if len(str1) <= 0:
            _playercmd = 'vlc.exe "$url"'
        else:
            _playercmd = str1
        if _debugmode:
            print(_playercmd)
        return

    def OnMySearchButtonClick(self, event):
        # 如果用户按了检索按钮
        global _mbcon
        global _mbssl
        global _ftp
        global _ftps
        # str6=""
        if _mbcon:
            return
        str5 = self.m_textsearch.GetLineText(0)
        if len(str5) <= 1:
            return
        str5 = "SKEY " + str5
        if _mbssl:
            try:
                _ftps.sendcmd(str5)
            except (socket.error, socket.gaierror):
                self.FuncDisconnect()
                return
            except ftplib.error_perm:
                return
            except:
                self.FuncDisconnect()
                return
        else:
            try:
                _ftp.sendcmd(str5)
            except (socket.error, socket.gaierror):
                self.FuncDisconnect()
                return
            except ftplib.error_perm:
                return
            except:
                self.FuncDisconnect()
                return

        if self.FuncGetList() == 0:
            self.FuncDisconnect()
            return

        return

    def FuncGetList(self):
        # 如果连接失败 则返回0 如果目录不存在等 则返回 -1
        global _chineseversion
        global _timersec
        data = []
        if _debugmode:
            print("Func getlist is called")
        _timersec = 0
        # 这里需要加入获取当前目录的操作函数

        if _mbssl:
            try:
                # 如果需要使用加密获取目录列表 那么每次都要重新发送prot_p
                # 我这里直接采用明文,因为并不是什么机密内容 单纯将登录过程进行保密已经足够了
                _ftps.retrlines("LIST", data.append)
            except (socket.error, socket.gaierror):
                return 0
            except ftplib.error_perm:
                return -1
            except:
                return 0
            else:
                pass
        else:
            try:
                _ftp.retrlines("LIST", data.append)
            except (socket.error, socket.gaierror):
                return 0
            except ftplib.error_perm:
                return -1
            except:
                return 0
        # 现在可以保证已经获取到了数据
        # 我们的目标服务器是XFile服务器 因此提供的是XFile标准扩展格式
        # 格式如下
        # 现在处理data数据
        # filesie 1/0 modtime |filename or dirname
        # filesize=64bit long int
        arr1 = []
        iline = 0
        filesize = 0
        modtime = 0
        isdir = 0
        self.m_listCtrlFtp.DeleteAllItems()
        iline = self.m_listCtrlFtp.InsertItem(self.m_listCtrlFtp.GetItemCount(), "", -1)
        self.m_listCtrlFtp.SetItem(iline, 0, str(iline))
        if _chineseversion:
            self.m_listCtrlFtp.SetItem(iline, 1, "目录")
        else:
            self.m_listCtrlFtp.SetItem(iline, 1, "Dir")

        # self.m_listCtrlFtp.SetItem(iline,1,"Dir")
        self.m_listCtrlFtp.SetItem(iline, 2, "0")
        self.m_listCtrlFtp.SetItem(iline, 3, "..")

        for str2 in data:
            if _debugmode:
                print(str2)

            if len(str2) < 5:
                continue
            # spilit line by |
            i2 = str2.find("|")
            if i2 <= 3 or i2 >= len(str2):
                continue
            else:
                str3 = str(str2[i2 + 1 :])
                str3.strip("\n")
                str3.strip("\r")
                str3.strip(" ")
                # 文件名提取成功 下面提取文件长度等信息
            arr1 = str2.split()
            if len(arr1) < 3:
                continue
            # 执行数字转换吧
            # 注意格式
            filesize = int(arr1[0], 16)
            isdir = not int(arr1[1])
            modtime = int(arr1[2], 16)
            # 完成转换 现在执行插入操作
            iline = self.m_listCtrlFtp.InsertItem(
                self.m_listCtrlFtp.GetItemCount(), "", -1
            )
            self.m_listCtrlFtp.SetItem(iline, 0, str(iline))
            if isdir:
                if _chineseversion:
                    self.m_listCtrlFtp.SetItem(iline, 1, "目录")
                else:
                    self.m_listCtrlFtp.SetItem(iline, 1, "Dir")
                # self.m_listCtrlFtp.SetItem(iline,1,"Dir")
                self.m_listCtrlFtp.SetItem(iline, 2, "0")
            else:
                if _chineseversion:
                    self.m_listCtrlFtp.SetItem(iline, 1, "文件")
                else:
                    self.m_listCtrlFtp.SetItem(iline, 1, "File")
                # self.m_listCtrlFtp.SetItem(iline,1,"File")
                self.m_listCtrlFtp.SetItem(iline, 2, str(filesize))
            self.m_listCtrlFtp.SetItem(iline, 3, str3)
            # 定时器
            # self.timer1 = wx.Timer(self)
        return 1

    def FuncGetRandomCode(self):
        global _ftp
        global _ftps
        global _srandomcode
        global _mbssl
        global _debugmode

        str5 = ""
        try:
            if _mbssl:
                str5 = _ftps.sendcmd("MKEY")
            else:
                str5 = _ftp.sendcmd("MKEY")
        except (socket.error, socket.gaierror):
            return False

        except ftplib.error_perm:
            if _debugmode:
                print("Error: server do not support MKEY")
            return False
        except:
            return False
        # 现在分解返回的参数吧
        arr2 = []
        arr2 = str5.split(" ")
        if len(arr2) < 3:
            if _debugmode:
                print("Error: bad response from server of MKEY")

            return False
        if _debugmode:
            print(str5)
            print(arr2[1])
        _srandomcode = arr2[1]
        return True

    def FunXFileExtend(self):
        global _mbcon
        global _debugmode
        global _mbssl
        global _ftp
        global _ftps
        global _httpport
        global _sglobalpass
        global _mbhttpssl
        global _mbsha256

        _sglobalpass = self.m_textCtrlPassword.GetLineText(0)

        if _debugmode:
            print("XFileExteng function is called")
        str3 = "SLST 0"
        str4 = ""
        _httpport = 0
        # 这里我偷懒了, 预先生成sha256加密口令 无论是否用的上 格式为原始口令加 www.phoenixp2p.com ,然后生成sha256
        strsha256 = ""
        md256 = hashlib.sha256()
        md256.update(
            (
                self.m_textCtrlPassword.GetLineText(0).strip() + "www.phoenixp2p.com"
            ).encode(encoding="utf-8")
        )
        strsha256 = md256.hexdigest().lower()
        if _debugmode:
            print(strsha256)
            # 调试模式下 输出sha256加密后的口令

        if _mbssl:
            _ftps.set_pasv(True)
            try:
                str4 = _ftps.sendcmd(str3)
            except (socket.error, socket.gaierror):
                return 0

            except ftplib.error_perm:
                if _debugmode:
                    print("Reponse error for SLST command")
                return 0
            except:
                return 0
            # https模式 需要新加入是采用p或者c模式支持
            try:
                # 改用明文模式
                _ftps.prot_c()
                # _ftps.prot_p( )
                # _ftps._prot_p=True

            except (socket.error, socket.gaierror):
                return 0
            except ftplib.error_perm:
                if _debugmode:
                    print("Reponse error for PROT command")
                return 0
            except:
                return 0
            # 发送SALT指令获取全局随机数
            str3 = "SALT"
            try:
                str4 = _ftps.sendcmd(str3)
            except ftplib.error_perm:
                return 0
            except:
                return 0
            # 提取服务器的回答
            arr8 = []
            arr8 = str4.split(" ")
            if len(arr8) >= 2:
                str4 = arr8[1]
            if _debugmode:
                print(str4)
            # 执行清理
            str4.strip(" ")
            str4.strip("\n")
            str4.strip("\r")
            # 这里可以生成全局的登录口令了
            strnew = str4
            # 这里需要注意 可能以后版本会要求sha256 这里必须进行判断
            if _mbsha256:
                strnew += strsha256
            else:
                strnew += self.m_textCtrlPassword.GetLineText(0)
            # strnew+=self.m_textCtrlPassword.GetLineText(0)
            strnew += str4
            strnew += "()"
            if _debugmode:
                print(strnew)
            md55 = hashlib.md5()
            md55.update(strnew.encode(encoding="utf-8"))
            strnew = md55.hexdigest()
            if _debugmode:
                print(strnew)
            str3 = strnew[0:2]
            str3 += "_"
            str3 += strnew[3:]
            strnew = str4
            strnew += "<>"
            strnew += str3
            # 再次生成MD5加密口令
            if _debugmode:
                print(strnew)
            md55 = hashlib.md5()
            md55.update(strnew.encode(encoding="utf-8"))
            strnew = md55.hexdigest()
            str3 = strnew[0:2]
            str3 += "_"
            str3 += strnew[3:]
            if _debugmode:
                print(str3)
            _sglobalpass = str3

            # 发送http指令获取服务端口
            # if(_debugmode):
            # print(str4)

            str3 = "HTTP 0"
            try:
                str4 = _ftps.sendcmd(str3)
            except ftplib.error_perm:
                return 1
            except:
                return 0

        else:
            _ftp.set_pasv(True)
            try:
                str4 = _ftp.sendcmd(str3)
            except (socket.error, socket.gaierror):
                return 0
            except ftplib.error_perm:
                return 0
            except:
                return 0
            if _debugmode:
                print(str4)

            str3 = "SALT"
            try:
                str4 = _ftp.sendcmd(str3)
            except ftplib.error_perm:
                return 0
            except:
                return 0
            # 提取服务器的回答
            arr8 = []
            arr8 = str4.split(" ")
            if len(arr8) >= 2:
                str4 = arr8[1]
            if _debugmode:
                print(str4)
            str4.strip(" ")
            str4.strip("\n")
            str4.strip("\r")
            # 这里可以生成全局的登录口令了
            #
            #
            strnew = str4
            # 这里需要注意 以后版本 可能会采用sha256加密口令 这里做了预判断
            if _mbsha256:
                strnew += strsha256
            else:
                strnew += self.m_textCtrlPassword.GetLineText(0)
            # strnew+=self.m_textCtrlPassword.GetLineText(0)
            strnew += str4
            strnew += "()"
            if _debugmode:
                print(strnew)
            md55 = hashlib.md5()
            md55.update(strnew.encode(encoding="utf-8"))
            strnew = md55.hexdigest()
            if _debugmode:
                print(strnew)
            str3 = strnew[0:2]
            str3 += "_"
            str3 += strnew[3:]
            strnew = str4
            strnew += "<>"
            strnew += str3
            if _debugmode:
                print(strnew)
            # 再次生成MD5加密口令
            md55 = hashlib.md5()
            md55.update(strnew.encode(encoding="utf-8"))
            strnew = md55.hexdigest()
            str3 = strnew[0:2]
            str3 += "_"
            str3 += strnew[3:]
            if _debugmode:
                print(str3)
            _sglobalpass = str3
            # 完成第三方登录口令的制作 可以防止破解

            #

            str3 = "HTTP 0"
            try:
                str4 = _ftp.sendcmd(str3)
            except (socket.error, socket.gaierror):
                return 0
            except ftplib.error_perm:
                return 1
            except:
                return 0

            # 对str4 进行分解 提取http端口号
            # 返回 200 端口号 无用的0
            if _debugmode:
                print(str4)
            arr5 = []
            arr5 = str4.split(" ")
            if len(arr5) >= 2:
                _httpport = int(arr5[1], 10)
            else:
                _httpport = 0
            if int(arr5[0]) >= 201:
                _mbhttpssl = True
            else:
                _mbhttpssl = False
            # 完成分解操作	无论用户是否钩选优先使用Http 都会执行一次  我是简化代码 当然如果你有兴趣可以加入判断来减少执行
            #

        # 如果成功设置了简化模式输出 那么就返回成功 虽然我们有更多的方法来验证服务器是XFile服务器
        # 但是用这个指令的方法更简单
        # 将来如果有需要 可以将口令采用加盐Hash方式进行验证 这样更不容易被破解
        #
        if _debugmode:
            print("Success get http number=" + str(_httpport))

        return 1

    def FuncChangeButton(self):
        global _mbcon
        global _chineseversion
        if _mbcon:
            if _chineseversion:
                self.m_buttonLogin.SetLabelText("连接")
            else:
                self.m_buttonLogin.SetLabelText("Connect")
            self.m_listCtrlFtp.DeleteAllItems()
            self.m_staticinfo.SetLabelText("/")
            self.m_buttonSearch.Disable()
            self.m_textsearch.Disable()
            self.m_textCtrlPassword.Enable()
            self.m_textCtrlPort.Enable()
            self.m_textCtrlServer.Enable()
            self.m_textCtrlUsername.Enable()
            self.m_checkBoxSsl.Enable()
            self.m_checkBoxHttp.Enable()

        else:
            if _chineseversion:
                self.m_buttonLogin.SetLabelText("中断")
            else:
                self.m_buttonLogin.SetLabelText("Disconnect")
            self.m_buttonSearch.Enable()
            self.m_textsearch.Enable()
            self.m_textCtrlPassword.Disable()
            self.m_textCtrlPort.Disable()
            self.m_textCtrlServer.Disable()
            self.m_textCtrlUsername.Disable()
            self.m_checkBoxSsl.Disable()
            self.m_checkBoxHttp.Disable()

    def OnMyButtonClick(self, event):
        global _mbcon
        global _ftp
        global _ftps
        global _debugmode
        global _mbssl
        global _srandomcode
        global _mbsha256
        str7 = ""

        if _mbcon:
            # load player file again
            self.FuncLoadConfigFile()
            # connect the server
            strserver = self.m_textCtrlServer.GetLineText(0).strip()
            strusername = self.m_textCtrlUsername.GetLineText(0).strip()
            strpassword = self.m_textCtrlPassword.GetLineText(0).strip()
            iportnum = int(self.m_textCtrlPort.GetLineText(0))
            if _debugmode:
                print(strserver)
                print(strusername)
                print(strpassword)
                print("portnum=" + str(iportnum))
            if self.m_checkBoxSsl.GetValue():
                if _debugmode:
                    print("Now will in TLS-SSL connection mode")
                _mbssl = True
                _ftps.encoding = "utf-8"
            else:
                if _debugmode:
                    print("Now will in Standard connection mode")
                _mbssl = False
                _ftp.encoding = "utf-8"
            if (
                len(strserver) <= 0
                or len(strusername) <= 0
                or len(strpassword) <= 0
                or iportnum <= 0
                or iportnum >= 65535
            ):
                # pop dialog , parameters error
                dlg = wx.MessageDialog(
                    self, "Bad parameters found", "Error", wx.OK | wx.ICON_INFORMATION
                )
                dlg.ShowModal()
                dlg.Destroy()
                return
            else:
                str7 = ""
                if _debugmode:
                    print("Debug: now will try to connect remote server")
                if _mbssl:
                    try:
                        str7 = _ftps.connect(host=strserver, port=iportnum, timeout=23)
                    except (socket.error, socket.gaierror):
                        dlg = wx.MessageDialog(
                            self,
                            "Failed to connect server with ftp ssl",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()
                        return
                    except:
                        dlg = wx.MessageDialog(
                            self,
                            "Failed to connect server with ftp ssl 2",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()
                        return
                    if _debugmode:
                        print(str7)

                    if self.FuncGetRandomCode() == False:
                        dlg = wx.MessageDialog(
                            self,
                            "Bad server type, only support XFile(www.phoenixp2p.com)",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()
                        return
                    # 这里添加转换 因为明文不安全 这里转换成md5模式的口令
                    # 注意 这是XFile服务器才支持的格式 普通FTP服务器是不支持的
                    # 注意 2019.10或者更新的版本XFile 可能会使用sha256加密口令 这里做了分支判断
                    if _mbsha256:
                        strsha2561 = strpassword + "www.phoenixp2p.com"
                        mhash256 = hashlib.sha256(strsha2561.encode(encoding="UTF-8"))
                        strpassword = _srandomcode + mhash256.hexdigest().lower()
                        if _debugmode:
                            print(strpassword)
                    else:
                        strpassword = _srandomcode + strpassword
                    # strpassword=_srandomcode+strpassword
                    if _debugmode:
                        print(strpassword)

                    # 生成MD5加密口令
                    mhash = hashlib.md5(strpassword.encode(encoding="UTF-8"))
                    str7 = mhash.hexdigest()

                    if _debugmode:
                        print(str7)
                    strpassword = "__" + str7
                    try:
                        _ftps.login(strusername, strpassword)
                    except ftplib.error_perm:
                        _ftps.close()
                        dlg = wx.MessageDialog(
                            self,
                            "Failed to login server, check your username and password",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()
                        return
                    except:
                        _ftps.close()
                        dlg = wx.MessageDialog(
                            self,
                            "Failed to login server, check your username and password 2",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()

                        return
                    # 现在可以保证已经登录到服务器了 那么尝试获取列表吧 是否加密呢 这是个问题
                    # 乱用SSL会导致性能问题
                    # 注意上面不能用quit 因为quit遇到特殊的服务器回答 会引发投递异常

                else:
                    try:
                        str7 = _ftp.connect(host=strserver, port=iportnum, timeout=15)
                    except (socket.error, socket.gaierror):
                        dlg = wx.MessageDialog(
                            self,
                            "Failed to connect server with ftp",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()
                        return
                    except:
                        dlg = wx.MessageDialog(
                            self,
                            "Failed to connect server with ftp 2",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()
                        return
                    if _debugmode:
                        print(str7)
                    if self.FuncGetRandomCode() == False:
                        dlg = wx.MessageDialog(
                            self,
                            "Bad server type, only support XFile(www.phoenixp2p.com)",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()
                        return

                    # strpassword=_srandomcode+strpassword
                    # 这里需要进行转换了 未来版本可能会支持sha256加密口令
                    if _mbsha256:
                        strsha2561 = strpassword + "www.phoenixp2p.com"
                        mhash256 = hashlib.sha256(strsha2561.encode(encoding="UTF-8"))
                        strpassword = _srandomcode + mhash256.hexdigest().lower()
                        if _debugmode:
                            print(strpassword)
                    else:
                        strpassword = _srandomcode + strpassword

                    if _debugmode:
                        print(strpassword)

                    # 生成MD5加密口令
                    mhash = hashlib.md5(strpassword.encode(encoding="UTF-8"))
                    str7 = mhash.hexdigest()

                    if _debugmode:
                        print(str7)

                    strpassword = "__" + str7

                    try:
                        _ftp.login(strusername, strpassword)
                    except ftplib.error_perm:
                        _ftp.close()
                        dlg = wx.MessageDialog(
                            self,
                            "Failed to login server, check your username and password",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()
                        return
                    except (socket.error, socket.gaierror):
                        _ftp.close()
                        dlg = wx.MessageDialog(
                            self,
                            "Disconnected by server",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()
                        return
                    except:
                        _ftp.close()
                        dlg = wx.MessageDialog(
                            self,
                            "Disconnected by server 2",
                            "Error",
                            wx.OK | wx.ICON_INFORMATION,
                        )
                        dlg.ShowModal()
                        dlg.Destroy()
                        return
            if self.FunXFileExtend() == 0:
                dlg = wx.MessageDialog(
                    self,
                    "Server does not support XFILE command",
                    "Error",
                    wx.OK | wx.ICON_INFORMATION,
                )
                dlg.ShowModal()
                dlg.Destroy()
                if _mbssl:
                    try:
                        _ftps.close()
                    except (socket.error, socket.gaierror):
                        return
                    except:
                        return

                else:
                    try:
                        _ftp.close()
                    except (socket.error, socket.gaierror):
                        return
                    except:
                        return

                return
                # 直接失败 返回吧 事实上上面的close也可能抛出异常 因为概率太小 我直接忽略了
            # 如果成功了 那么调用列表函数进行刷新操作吧
            # 并修改当前目录
            # 连接成功
            _mbcon = False
            self.FuncGetList()

            if _mbcon == False:
                # self.timer1.SetOwner(None,8801)
                self.timer1.Start(10000)
                # 每10秒触发一次

            # 连接成功
            # _mbcon=False
            self.FuncChangeButton()
        else:
            if _mbssl:
                try:
                    _ftps.close()
                except (socket.error, socket.gaierror):
                    pass
                except:
                    pass
            else:
                try:
                    _ftp.close()
                except (socket.error, socket.gaierror):
                    pass
                except:
                    pass
            self.timer1.Stop()
            _mbcon = True
            self.FuncChangeButton()

            # 关闭定时器
        event.Skip()

    def OnMyListColClick(self, event):
        event.Skip()

    def MyFuncMapHttpFile(self, sname):
        global _debugmode
        global _mbcon
        global _mbssl
        global _ftp
        global _ftps
        global _httpport
        global _curworkdir
        global _playercmd
        global _sglobalpass
        global _mbhttpstream
        if _debugmode:
            print("Map http file function is called")
        if len(sname) <= 0:
            return ""
        strres = ""

        if _mbssl:
            try:
                strres = _ftps.sendcmd("MAPF " + sname)
            except (socket.error, socket.gaierror):
                return ""
            except ftplib.error_perm:
                return ""
            except:
                return ""
        else:
            try:
                strres = _ftp.sendcmd("MAPF " + sname)
            except (socket.error, socket.gaierror):
                return ""
            except ftplib.error_perm:
                return ""
            except:
                return ""
        sarr1 = []
        sarr1 = strres.strip().split(" ")
        if len(sarr1) < 2:
            return ""
        # 否则 sarr1[1]就是映射的文件url
        if _debugmode:
            print(sarr1[1])
        return sarr1[1]

    def OnMyListItemActivated(self, event):
        global _debugmode
        global _mbcon
        global _mbssl
        global _ftp
        global _ftps
        global _httpport
        global _curworkdir
        global _playercmd
        global _sglobalpass
        global _mbhttpstream
        global _mbhttpssl

        if _debugmode:
            print("List item actived called")
        itnum = self.m_listCtrlFtp.GetFirstSelected()
        if itnum == -1:
            return
        if _mbcon:
            return
        if itnum == 0:
            # 返回上级目录
            #
            self.OnPopupRoot(event)
            return
        else:
            # 注意 有可能是检索得到的结果
            # 也就是带目录的完整结果
            str1 = self.m_listCtrlFtp.GetItemText(itnum, 3)
            str2 = self.m_listCtrlFtp.GetItemText(itnum, 1)
            if _debugmode:
                print(str1)
                print(str2)
            if len(str2) < 1:
                return
            if len(str1) <= 0:
                return
            # 根据目录或者文件分别处理
            if str2 == "File" or str2 == "文件":
                # 这是文件
                if _debugmode:
                    print("Found it is file or 文件")
                if str1.find("/") >= 0:
                    # 这是完整的带目录文件
                    if _debugmode:
                        print("Found file is abs dir + file")
                    pass
                else:
                    # 这是普通的文件
                    # 需要添加当前目录
                    str1 = _curworkdir + "/" + str1
                # 然后根据os 分别处理播放
                # 是否支持http映射呢 这以后进行扩展吧 注意http 也有可能是tls/ssl
                # ///////这里先注销掉http 流播放模式
                ##if(self.m_checkBoxHttp.IsChecked() and _httpport!=0):
                # 如果是http模式
                #
                ##else:
                # 按标准FTP进行播放
                if _debugmode:
                    print(str1)
                if _mbhttpstream == False or _httpport <= 0:
                    # 这里原来是True 2019.10 新修改 这里按http流还是ftp流进行区分

                    strurl = "ftp://"

                    strurl += self.m_textCtrlUsername.GetLineText(0)
                    strurl += ":"
                    # strurl+=self.m_textCtrlPassword.GetLineText(0)
                    strurl += _sglobalpass
                    strurl += "@"
                    strserver = self.m_textCtrlServer.GetLineText(0)
                    if strserver.find(":") >= 0 and strserver.find("[") < 0:
                        # 如果是ipv6地址 并且简单的判断没有加入[]
                        strserver = "[" + strserver
                        strserver += "]"

                    # 如果端口号不是21 应该加上端口号
                    strurl += strserver
                    # 加入服务器地址
                    # 请注意 ipv6地址加入端口号,在某些移动平台的播放器,会解析失败 不过原因是那些播放器软件本身解析的问题
                    strurl += ":"
                    strurl += self.m_textCtrlPort.GetLineText(0)
                    strurl += str1
                    # 由于windows 目录文件可能有空格 这里使用双引号
                    # strurl='"'+strurl
                    # strurl+='"'

                    # 到这里完成了完整的ftp url 构成
                    if _debugmode:
                        print(strurl)
                    # 根据os的不同进行调用吧
                    # mpv 有py_mpv , 可以直接在python里非常简单的调用播放器
                    # 但是由于升级很频繁 我们还是建议你调用外部播放器方式来实现
                    # 虽然
                    if os.name == "nt":
                        # 这是windows 操作系统
                        # 如果存在mpv 那么使用mpv 进行播放
                        # 如果存在vlc 那么使用vlc 进行播放
                        str10 = _playercmd
                        str10 = str10.replace("$url", strurl)
                        if _debugmode:
                            print(str10)
                        # os.system(str10)
                        os.popen(str10)
                        # if(_debugmode):
                        # print()
                    else:
                        # 按Linux进行处理 posix
                        str10 = _playercmd
                        str10 = str10.replace("$url", strurl, 1)
                        if _debugmode:
                            print(str10)
                        # os.system(str10)
                        os.popen(str10)
                else:
                    # http 流模式进行播放 http流具有更好的播放效率，注意，标准ftp服务器是没有这个功能的 只有XFile服务器才支持这个功能
                    if _debugmode:
                        print("in http stream mode")
                    # 需要将文件映射为http连接
                    strhttpcmd = self.MyFuncMapHttpFile(str1)
                    if len(strhttpcmd) <= 0:
                        return
                    # 注意 ， 有可能映射失败 因此需要进行判断
                    strurl = "http://"
                    if _mbhttpssl:
                        strurl = "https://"

                    strserver = self.m_textCtrlServer.GetLineText(0)
                    if strserver.find(":") >= 0 and strserver.find("[") < 0:
                        # 如果是ipv6地址 并且简单的判断没有加入[]
                        strserver = "[" + strserver
                        strserver += "]"

                    # 如果端口号不是21 应该加上端口号
                    strurl += strserver
                    # 加入服务器地址
                    # 请注意 ipv6地址加入端口号,在某些移动平台的播放器,会解析失败 不过原因是那些播放器软件本身解析的问题
                    strurl += ":"
                    strurl += str(_httpport)
                    strurl += "/"
                    strurl += strhttpcmd
                    if _debugmode:
                        print(strurl)
                    # 现在可以调用播放器执行播放功能了
                    #
                    #
                    # 根据os的不同进行调用吧
                    # mpv 有py_mpv , 可以直接在python里非常简单的调用播放器
                    # 但是由于升级很频繁 我们还是建议你调用外部播放器方式来实现
                    # 虽然
                    if os.name == "nt":
                        # 这是windows 操作系统
                        # 如果存在mpv 那么使用mpv 进行播放
                        # 如果存在vlc 那么使用vlc 进行播放
                        # 这里特别提醒注意 如果是windows平台 由于路径中允许存在空格字符 而python默认的popen遇到命令行就停止,因此需要用双引号进行引用 防止误判
                        str10 = _playercmd
                        str10 = str10.replace("$url", strurl)
                        #
                        if _debugmode:
                            print(str10)
                        # os.system(str10)
                        os.popen(str10)
                        # if(_debugmode):
                        # print()
                    else:
                        # 按Linux进行处理 posix
                        str10 = _playercmd
                        str10 = str10.replace("$url", strurl, 1)
                        if _debugmode:
                            print(str10)
                        # os.system(str10)
                        os.popen(str10)

            else:
                # 这是目录 注意可能是完整目录
                if _debugmode:
                    print("this is dir")
                # if(str1.find("/")>=0):
                # 	#这是绝对目录
                # 	pass
                # else:
                # 	#这是相对目录
                # 	# 调用切换目录函数
                # 	pass
                if self.FuncChangeDir(str1) == False:
                    self.FuncDisconnect()
                else:
                    if self.FuncGetWorkDir() == False:
                        self.FuncDisconnect()
                if _debugmode:
                    print("change dir done")

        # event.Skip()

    def FuncGetWorkDir(self):
        global _mbssl
        global _ftp
        global _ftps
        global _curworkdir
        global _debugmode
        global _timersec
        strres = ""
        _timersec = 0
        if _debugmode:
            print("FuncGetWorkDir funciton is called")
        if _mbssl:
            try:
                strres = _ftps.sendcmd("PWD")
            except (socket.error, socket.gaierror):
                return False
            except ftplib.error_perm:
                return False
            except:
                return False
        else:
            try:
                strres = _ftp.sendcmd("PWD")
            except (socket.error, socket.gaierror):
                return False
            except ftplib.error_perm:
                return False
            except:
                return False
        # 分解服务器应答
        #
        #
        # 需要提取出"""内容
        if _debugmode:
            print(strres)
            print("Now will change work dir")
        arr6 = []
        arr6 = strres.split('"')
        if len(arr6) < 3:
            return False
        _curworkdir = arr6[1]
        if _debugmode:
            print(_curworkdir)
            print("Success get cur workdir")
        self.m_staticinfo.SetLabelText(_curworkdir)
        return True

    def FuncDisconnect(self):
        # 中断连接
        global _ftp
        global _ftps
        global _mbcon
        global _mbssl
        if _mbcon:
            return
        if _mbssl:
            try:
                _ftps.close()
            except:
                pass
        else:
            try:
                _ftp.close()
            except:
                pass
        _mbcon = True
        self.m_listCtrlFtp.DeleteAllItems()
        self.m_staticinfo.SetLabelText("/")
        self.timer1.Stop()
        self.FuncChangeButton()

    def FuncChangeDir(self, sdir):
        # 切换目录 同时已经刷新了列表
        global _ftp
        global _ftps
        global _mbssl
        global _curworkdir
        if len(sdir) <= 0:
            sdir = "/"
        scmd = "CWD "
        scmd += sdir
        bsucc = True
        # 切换目录
        if _mbssl:
            # ssl
            try:
                _ftps.sendcmd(scmd)
            except (socket.error, socket.gaierror):
                # _ftps.close( )
                return False
            except ftplib.error_perm:
                bsucc = False

        else:
            try:
                _ftp.sendcmd(scmd)
            except (socket.error, socket.gaierror):
                # _ftp.close( )
                return False
            except ftplib.error_perm:
                bsucc = False
        # 可能目录切换失败 那么切换到根目录吧
        if bsucc == False:
            sdir = "/"
            scmd = "CWD /"
            if _mbssl:
                try:
                    _ftps.sendcmd(scmd)
                except (socket.error, socket.gaierror):
                    # _ftps.close( )
                    return False
                except ftplib.error_perm:
                    # _ftps.close( )
                    return False
            else:
                try:
                    _ftp.sendcmd(scmd)
                except (socket.error, socket.gaierror):
                    # _ftps.close( )
                    return False
                except ftplib.error_perm:
                    # _ftps.close( )
                    return False
            # 现在可以保证已经成功了 那么执行列表操作吧
            #
        if self.FuncGetList() == 0:
            return False
        # _curworkdir=sdir
        # self.m_staticinfo.SetLabelText(sdir)
        return True
        # 完成操作

    def OnMyRightClick(self, event):
        global _chineseversion
        if not hasattr(self, "popupIDRoot"):
            self.popupIDRoot = wx.NewIdRef()
            self.popupIDUp = wx.NewIdRef()
            self.popupIDList = wx.NewIdRef()
            self.popupIDPlay = wx.NewIdRef()
            self.popupIDRefresh = wx.NewIdRef()
            self.Bind(wx.EVT_MENU, self.OnPopupRoot, id=self.popupIDRoot)
            self.Bind(wx.EVT_MENU, self.OnPopupUp, id=self.popupIDUp)
            self.Bind(wx.EVT_MENU, self.OnPopupRefresh, id=self.popupIDRefresh)
            self.Bind(wx.EVT_MENU, self.OnPopupPlay, id=self.popupIDPlay)
            self.Bind(wx.EVT_MENU, self.OnPopupList, id=self.popupIDList)
            # pop menu
        menu = wx.Menu()
        # add some items
        if _chineseversion:
            # 如果是中文版本
            menu.Append(self.popupIDRoot, "根目录")
            menu.Append(self.popupIDUp, "上级目录")
            menu.Append(self.popupIDList, "列表")
            menu.Append(self.popupIDPlay, "播放")
            menu.Append(self.popupIDRefresh, "刷新")
        else:
            # 英文版本
            menu.Append(self.popupIDRoot, "Root")
            menu.Append(self.popupIDUp, "Upgread")
            menu.Append(self.popupIDList, "List")
            menu.Append(self.popupIDPlay, "Play")
            menu.Append(self.popupIDRefresh, "Refresh")

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()

    def OnMyListItemRightClick(self, event):
        # event.Skip( )
        global _debugmode
        if _debugmode:
            print("OnMyListItemRightClick function")
        event.Skip()

    def OnPopupRoot(self, event):
        # event.Skip( )
        global _mbcon
        global _timersec
        if _mbcon:
            return
        # 修改定时器计数为0
        _timersec = 0
        if self.FuncChangeDir("/") == False:
            self.FuncDisconnect()
            return
        else:
            if self.FuncGetWorkDir() == False:
                self.FuncDisconnect()

        return

    def OnPopupUp(self, event):
        # event.Skip( )
        global _mbcon
        global _timersec
        if _mbcon:
            return
        _timersec = 0
        if self.FuncChangeDir("..") == False:
            self.FuncDisconnect()
            return

    def OnPopupList(self, event):
        # event.Skip( )
        global _mbcon
        global _timersec

        i3 = self.m_listCtrlFtp.GetFirstSelected()
        if i3 == -1:
            return
        if _mbcon:
            return

        str22 = self.m_listCtrlFtp.GetItemText(i3, 1)
        if str22 == "File" or str22 == "文件":
            return
        _timersec = 0
        self.OnMyListItemActivated(event)

    def OnPopupPlay(self, event):
        # event.Skip( )
        global _mbcon
        global _timersec

        i3 = self.m_listCtrlFtp.GetFirstSelected()
        if i3 == -1:
            return
        if _mbcon:
            return
        str22 = self.m_listCtrlFtp.GetItemText(i3, 1)
        if str22 == "Dir" or str22 == "目录":
            return
        _timersec = 0
        self.OnMyListItemActivated(event)

    def OnPopupRefresh(self, event):
        # event.Skip( )
        global _mbcon
        global _timersec
        if _mbcon:
            return
        _timersec = 0
        if self.FuncGetList() == 0:
            self.FuncDisconnect()
            return

    def OnMyTimerMsg(self, event):
        global _mbcon
        global _debugmode
        global _timersec
        if _debugmode:
            print("OnTimer msg")
        if _mbcon:
            # 连接已经中断 那么直接断开吧 是否需要使用锁定?
            return
        _timersec += 1
        if _timersec >= 6:
            # 发送Noop指令给服务器吧
            _timersec = 0
            if self.FuncSendRawCmd("NOOP") == False:
                self.FuncDisconnect()

        event.Skip()

    def FuncSendRawCmd(self, scmd):
        global _mbcon
        global _debugmode
        global _ftp
        global _ftps
        global _mbssl
        if _debugmode:
            print("Found timer to send noop command now")
        if len(scmd) <= 0:
            scmd = "NOOP"
        try:
            if _mbssl:
                _ftps.sendcmd(scmd)
            else:
                _ftp.sendcmd(scmd)
        except (socket.error, socket.gaierror):
            return False
        except ftplib.error_perm:
            return True
        except:
            return False
        return True


if __name__ == "__main__":
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MyFrameMain(None)
    frm.Show()
    app.MainLoop()
