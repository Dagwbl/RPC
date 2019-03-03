import time
import tkinter as tk
from tkinter import messagebox

class StopWatch(tk.Frame):
    '''实现一个秒表部件'''
    msec=50
    def __init__(self,parent=None,**kw):
        tk.Frame.__init__(self,parent,kw)
        self._start = 0.0
        self._elapsedtime =0.0
        self._running = False
        self._limittime =45
        self.timestr = tk.StringVar()
        self.makeWidgets()
        self.minuteTips = 0
    def makeWidgets(self):
        '''制作时间标签'''
        l = tk.Label(self,textvariable=self.timestr,font=("Times 12 bold"))
        self._setTime(self._elapsedtime)
        l.pack(fill=tk.X,expand=tk.NO,pady=2,padx=2)
    def _update(self):
        '''用逝去的时间更新标签'''
        self._elapsedtime=time.time() - self._start
        self._setTime(self._elapsedtime,self._limittime)
        self.timer = self.after(self.msec,self._update)
    def _setTime(self,elap,limitx = 10):
        '''将时间格式改为分：秒：百分秒'''
        minutes = int(elap/60)
        seconds = int(elap-minutes*60.0)
        hseconds = int((elap-minutes*60.0-seconds)*100)
        self.timestr.set('%02d:%02d:%02d'%(minutes,seconds,hseconds))
        if not minutes%limitx and minutes!=0 and self.minuteTips!=minutes:
            messagebox.showwarning('警告',str(minutes) + '分钟已经到了！')
            self.Stop()
            self.minuteTips = minutes
    #     self._Setlimit()
    # def _Setlimit(self):
    #     if self._elapsedtime>self.limittime:
    #         messagebox.showinfo('Tips','分钟已经到了！')

    def Start(self):
        '''开始秒表'''
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True
    def Stop(self):
        '''停止秒表'''
        if self._running:
            self.after_cancel(self.timer)
            self._elapsedtime = time.time()-self._start
            self._setTime(self._elapsedtime)
            self._running = False
    def Reset(self):
        '''重设秒表'''
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)
if __name__ =='__main__':
    def main():
        # import tkinter
        root =tk.Tk()
        sw =StopWatch()
        sw.pack(side=tk.TOP)
        tk.Button(root,text='Start',command=sw.Start).pack(side=tk.LEFT)
        tk.Button(root,text='Stop',command=sw.Stop).pack(side=tk.LEFT)
        tk.Button(root,text='Reset',command=sw.Reset).pack(side=tk.LEFT)
        tk.Button(root,text='Quit',command=sw.quit).pack(side=tk.LEFT)
        root.mainloop()
    main()