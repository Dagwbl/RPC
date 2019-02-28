import tkinter as tk
import time
class StopWatch(tk.Frame):
    '''实现一个秒表部件'''
    msec=50
    def __init__(self,parent=None,**kw):
        tk.Frame.__init__(self,parent,kw)
        self._start = 0.0
        self._elapsedtime =0.0
        self._running = False
        self.timestr = tk.StringVar()
        self.makeWidgets()
    def makeWidgets(self):
        '''制作时间标签'''
        l = tk.Label(self,textvariable=self.timestr,font=("Times 12 bold"))
        self._setTime(self._elapsedtime)
        l.pack(fill=tk.X,expand=tk.NO,pady=2,padx=2)
    def _update(self):
        '''用逝去的时间更新标签'''
        self._elapsedtime=time.time() - self._start
        self._setTime(self._elapsedtime)
        self.timer = self.after(self.msec,self._update)
    def _setTime(self,elap):
        '''将时间格式改为分：秒：百分秒'''
        minutes = int(elap/60)
        seconds = int(elap-minutes*60.0)
        hseconds = int((elap-minutes*60.0-seconds)*100)
        self.timestr.set('%02d:%02d:%02d'%(minutes,seconds,hseconds))
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
        import tkinter
        root =tk.Tk()
        sw =StopWatch()
        sw.pack(side=tk.TOP)
        tk.Button(root,text='Start',command=sw.Start).pack(side=tk.LEFT)
        tk.Button(root,text='Stop',command=sw.Stop).pack(side=tk.LEFT)
        tk.Button(root,text='Reset',command=sw.Reset).pack(side=tk.LEFT)
        tk.Button(root,text='Quit',command=sw.quit).pack(side=tk.LEFT)
        root.mainloop()
    main()