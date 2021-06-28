from selenium import webdriver
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import win32gui
import win32con
import win32api
import tkinter as tk
from tkinter import *
import threading
from selenium.webdriver.common.by import By
from tkinter import messagebox 

root = tk.Tk(className=' Automation')
root.geometry("400x200")

options = webdriver.ChromeOptions()
options.add_extension('MetaMask.crx')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.google.com/")

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

class My_App(tk.Frame):
	bFlag = False
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.parent = parent

		entryText = tk.StringVar()
		lblUrl = Label(self.parent, font="Verdana 10 bold", text = "Presale URL : ", justify='right')
		lblUrl.place(x=10, y=40)
		self.txtUrl = tk.Entry(root, font=('calibre',10,'normal'), width=39) 
		self.txtUrl.place(x=110, y=40)
		lblGas = Label(self.parent, font="Verdana 10 bold", text = "Gas Price : ", justify='right')
		lblGas.place(x=30, y=90)
		self.txtGas = tk.Entry(root, font=('calibre',10,'normal'), text = "50", width=39, textvariable=entryText) 
		self.txtGas.place(x=110, y=90)
		entryText.set( "50" )
		self.btnStart = tk.Button(self.parent, text="Start", command = self.OnStart, width=12)
		self.btnStart.pack()
		self.btnStart.place(x=110, y=140)
		self.btnStop = tk.Button(self.parent, text="Stop", command = self.OnStop, width=12)
		self.btnStop.pack()
		self.btnStop.place(x=295, y=140)
		self.btnStop["state"] = DISABLED


	def OnCheck(self):
		driver.get(self.txtUrl.get())
		while(True):
			try:
				if My_App.bFlag == True:
					break
				
				driver.find_element(By.XPATH, '//span[text()="Claim Tokens"]').click()
				
				time.sleep(4)
				win2find = "MetaMask Notification"
				hwndMain = win32gui.FindWindowEx(None, None, None, win2find)
				hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)

				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x09, 0)
				time.sleep(0.1)
				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x09, 0)
				time.sleep(0.1)
				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x09, 0)
				time.sleep(0.1)
				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x09, 0)
				time.sleep(0.1)
				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x09, 0)
				time.sleep(0.1)
				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x09, 0)
				time.sleep(0.2)

				for i in str(self.txtGas.get()):
					win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x30 + int(i), 0)
					time.sleep(0.2)

				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x09, 0)
				time.sleep(0.1)
				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x09, 0)
				time.sleep(0.1)
				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x09, 0)
				time.sleep(0.1)
				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x09, 0)
				time.sleep(0.1)

				win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x0D, 0)
				time.sleep(4)
				self.btnStart["state"] = NORMAL
				self.txtUrl["state"] = NORMAL
				self.txtGas["state"] = NORMAL
				self.btnStop["state"] = DISABLED
				break
			except:
				time.sleep(0.4)
				pass

	def OnStart(self):
		if self.txtUrl.get() == "":
			messagebox.showwarning("Warning", "Please input the Url")
			return

		if self.txtGas.get().isdigit() == False:
			messagebox.showwarning("Warning", "Please check the Gas price again.")
			return

		driver.switch_to.window(driver.window_handles[0])
		
		self.btnStart["state"] = DISABLED
		self.txtUrl["state"] = DISABLED
		self.txtGas["state"] = DISABLED
		self.btnStop["state"] = NORMAL
		My_App.bFlag = False
		Thread(self.OnCheck)
		

	def OnStop(self):
		self.btnStart["state"] = NORMAL
		self.txtUrl["state"] = NORMAL
		self.txtGas["state"] = NORMAL
		self.btnStop["state"] = DISABLED
		My_App.bFlag = True

root.resizable(False, False) 
My_App(root)
root.mainloop()










