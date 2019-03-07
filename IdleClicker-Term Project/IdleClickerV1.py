from tkinter import *


acct = 0
BV = 100
C1 = "#f0f0f0"


class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Idle Clicker V1")
        master.geometry("650x350")
        master.config(bg=C1)


class Harvester(object):
    def __init__(self, click_val, x_grid):
        self.harvester_num = x_grid
        self.auto = False
        self.purchased = False
        self.harv_val = click_val
        self.harv_per_click = 1
        self.b_text = "Harvester " + str(self.harvester_num + 1) + "\nValue: " + str(self.harv_val) + "\nHPC: "\
                      + str(self.harv_per_click) + "\nAuto: " + str(self.auto)
        self.button_harv = Button(text=self.b_text, command=lambda: self.harvest())
        self.button_harv.grid(row=2, column=x_grid)
        self.harvest_total = None
        self.acct_label_text = None
        self.acct_label = None
        if not self.purchased:
            self.button_harv.config(relief="sunken")

    def harvest(self):
        if self.purchased:
            global acct
            self.harvest_total = (self.harv_val * self.harv_per_click)
            acct += self.harvest_total
            auto_click(self.harvester_num)
            self.update_lbl()

    def auto_harv(self):
        global acct
        self.harvest_total = (self.harv_val * self.harv_per_click)
        acct += self.harvest_total

    def update_lbl(self):
        self.acct_label_text = "Your account\nvalue is: " + str(acct)
        self.acct_label = Label(text=self.acct_label_text, bg=C1)
        self.acct_label.grid(row=0, column=0)

    def update_purchased(self):
        if self.purchased:
            self.button_harv.config(relief="raised")

    def update_hv(self, up_val):
        self.harv_val += up_val
        self.b_text = "Harvester " + str(self.harvester_num + 1) + "\nValue: " + str(self.harv_val) + "\nHPC: "\
                      + str(self.harv_per_click) + "\nAuto: " + str(self.auto)
        self.button_harv.config(text=self.b_text)

    def update_hpc(self):
        self.b_text = "Harvester " + str(self.harvester_num + 1) + "\nValue: " + str(self.harv_val) + "\nHPC: " \
                      + str(self.harv_per_click) + "\nAuto: " + str(self.auto)
        self.button_harv.config(text=self.b_text)

    def update_auto(self):
        self.b_text = "Harvester " + str(self.harvester_num + 1) + "\nValue: " + str(self.harv_val) + "\nHPC: " \
                      + str(self.harv_per_click) + "\nAuto: " + str(self.auto)
        self.button_harv.config(text=self.b_text)


class HarvesterPurchase(object):
    def __init__(self, x_grid, harvester, cost):
        self.cost = cost
        self.harvester = harvester
        self.purchased = self.harvester.purchased
        self.button_lbl = "Purchase\nHarvester " + str(x_grid+1) + "?\nCost: " + str(self.cost)
        self.purchase_button = Button(text=self.button_lbl, command=lambda: self.purchase())
        self.purchase_button.grid(row=1, column=x_grid)
        if self.purchased:
            self.purchase_button.config(relief="sunken")

    def purchase(self):
        global acct
        if self.cost <= acct and not self.harvester.purchased:
            acct -= self.cost
            self.harvester.purchased = True
            self.harvester.update_purchased()
            self.purchase_button.config(relief="sunken")
            self.harvester.update_lbl()


class UpHarvVal(object):
    def __init__(self, value, harvester, cost):
        self.cost = cost
        self.up_value = value
        self.harv = harvester
        up_button_text = "Upgrade button?\nUpgrade value: " + str(self.up_value) + "\nCost: " + str(self.cost)
        up_button = Button(text=up_button_text, command=lambda: self.update_hpc())
        up_button.grid(row=3, column=self.harv.harvester_num)

    def update_hpc(self):
        global acct
        if self.cost <= acct:
            self.harv.update_hv(self.up_value)
            acct -= self.cost
            self.harv.update_lbl()


class UpHPC:
    def __init__(self, harv, cost):
        self.harv = harv
        self.cost = cost
        self.b_text = "Add 1 harvest\nper click?\nCost: " + str(self.cost)
        up_hpc_button = Button(text=self.b_text, command=lambda: self.up_hpc())
        up_hpc_button.grid(row=4, column=self.harv.harvester_num)

    def up_hpc(self):
        global acct
        if self.cost <= acct:
            self.harv.harv_per_click += 1
            acct -= self.cost
            self.harv.update_lbl()
            self.harv.update_hpc()


class UpAuto(object):
    def __init__(self, harv, cost):
        self.harv = harv
        self.cost = cost
        self.b_text = "Enable auto-click?\nCost: " + str(self.cost)
        self.up_auto_button = Button(text=self.b_text, command=lambda: self.up_auto())
        self.up_auto_button.grid(row=5, column=self.harv.harvester_num)

    def up_auto(self):
        global acct
        if self.cost <= acct and not self.harv.auto:
            self.harv.auto = True
            acct -= self.cost
            self.harv.update_lbl()
            self.harv.update_auto()
            self.up_auto_button.config(relief="sunken")


def auto_click(current_harv):
    for harv in harv_list:
        if harv.harvester_num != current_harv:
            if harv.auto:
                harv.auto_harv()
            else:
                continue


def main():
    root = Tk()
    MainGUI(root)
    init_acct_label_text = "Your account\nvalue is: " + str(acct)
    init_acct_label = Label(text=init_acct_label_text, bg=C1)
    init_acct_label.grid(row=0, column=0)
    harv1 = Harvester(BV, 0)
    harv1.purchased = True
    harv1.button_harv.config(relief="raised")
    harv2 = Harvester(BV*5, 1)
    harv3 = Harvester(BV*25, 2)
    harv4 = Harvester(BV*250, 3)
    harv5 = Harvester(BV*750, 4)
    harv6 = Harvester(BV*1000, 5)
    global harv_list
    harv_list = [harv1, harv2, harv3, harv4, harv5, harv6]
    HarvesterPurchase(0, harv1, 0)
    HarvesterPurchase(1, harv2, BV*100)
    HarvesterPurchase(2, harv3, BV*1000)
    HarvesterPurchase(3, harv4, BV * 10000)
    HarvesterPurchase(4, harv5, BV * 100000)
    HarvesterPurchase(5, harv6, BV * 1000000)
    UpHarvVal(BV, harv1, BV*20)
    UpHarvVal(BV*5, harv2, BV*200)
    UpHarvVal(BV*50, harv3, BV*2000)
    UpHarvVal(BV * 250, harv4, BV * 20000)
    UpHarvVal(BV * 750, harv5, BV * 200000)
    UpHarvVal(BV * 1000, harv6, BV * 2000000)
    UpHPC(harv1, BV*50)
    UpHPC(harv2, BV*500)
    UpHPC(harv3, BV*5000)
    UpHPC(harv4, BV * 50000)
    UpHPC(harv5, BV * 500000)
    UpHPC(harv6, BV * 5000000)
    UpAuto(harv1, BV*100)
    UpAuto(harv2, BV*1000)
    UpAuto(harv3, BV*10000)
    UpAuto(harv4, BV * 100000)
    UpAuto(harv5, BV * 1000000)
    win_button = UpAuto(harv6, BV * 10000000)
    win_button.up_auto_button.config(text="Press to Win!\nCost: 10000000")
    root.mainloop()


main()
