from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
import random
import time

class DataEntryForm:

    def __init__(self,root):
        self.root = root
        self.root.title = ("Data Entry Form")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background = "gainsboro")
        

        StockCode=StringVar()
        Description=StringVar()
        Date=StringVar()
        Quantity=StringVar()
        Price=StringVar()
        Weight=StringVar()
        Transportation=StringVar()
        VAT=StringVar()
        Transfer=StringVar()
        Total=StringVar()
        Search=StringVar()
        DateDay=StringVar()
        DateToDay=StringVar()

        MainFrame = Frame(self.root, bd =10, width=1350, height =700 , relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd =5, width=1340, height =200, relief=RIDGE, bg= 'cadet blue')
        TopFrame1.grid(row=0,column=0)
        TopFrame2 = Frame(MainFrame, bd =5, width=1340, height =50, relief=RIDGE, bg= 'cadet blue')
        TopFrame2.grid(row=1,column=0)
        TopFrame3 = Frame(MainFrame, bd =5, width=1340, height =300, relief=RIDGE, bg= 'cadet blue')
        TopFrame3.grid(row=2,column=0)

        InnerTopFrame1 = Frame(TopFrame1, bd =5, width=1330, height =190, relief=RIDGE)
        InnerTopFrame1.grid()
        InnerTopFrame2 = Frame(TopFrame2, bd =5, width=1330, height =48, relief=RIDGE)
        InnerTopFrame2.grid()
        InnerTopFrame3 = Frame(TopFrame3, bd =5, width=1330, height =280, relief=RIDGE)
        InnerTopFrame3.grid()

        Date.set(time.strftime("%d/%m/%Y"))
        

        def Reset():
            StockCode.set("")
            Description.set("")
            Date.set("")
            Quantity.set("")
            Price.set("")
            Weight.set("")
            Transportation.set("")
            VAT.set("")
            Transfer.set("")
            Total.set("")
            Search.set("")
            
            

            Date.set(time.strftime("%d/%m/%Y"))

            

        def iExit():
            iExit = tkinter.messagebox.askyesno("Data Entry Form","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return
        def addData():
            if StockCode.get()=="" or Description.get()=="" or Quantity.get()=="" :
                tkinter.messagebox.showerror("Enter correct details")
            else:
                sqlCon=pymysql.connect(host="localhost",user="root",password="",database="dataentry")
                cur=sqlCon.cursor()
                cur.execute("insert into dataentry values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                StockCode.get(),
                Description.get(),
                Date.get(),
                Quantity.get(),
                Price.get(),
                Weight.get(),
                Transportation.get(),
                VAT.get(),
                Transfer.get(),
                Total.get()
                ))

                sqlCon.commit()
                DisplayData()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successfully")
            
        def DisplayData():
            sqlCon =pymysql.connect(host="localhost",user="root",password="#enter your password here from MySQL Workbench ",database="dataentry")
            cur =sqlCon.cursor()
            cur.execute("select * from dataentry")
            result=cur.fetchall()
            if len(result) !=0:
                tree_records.delete(*tree_records.get_children())
                for row in result:
                    tree_records.insert(parent='',index='end',values = row)
                    sqlCon.commit()
                sqlCon.close()

        def Info(ev):
            viewInfo = tree_records.focus()
            Data = tree_records.item(viewInfo)
            row = Data ['values']
            StockCode.set(row[0])
            Description.set(row[1])
            Date.set(row[2])
            Quantity.set(row[3])
            Price.set(row[4])
            Weight.set(row[5])
            Transportation.set(row[6])
            VAT.set(row[7])
            Transfer.set(row[8])
            Total.set(row[9])
            
        def update():
            sqlCon =pymysql.connect(host="localhost", user="root",password="", database="dataentry")
            cur =sqlCon.cursor()
            cur.execute("update dataentry set Description= %s,Date= %s,Quantity= %s,Price= %s, \
            Weight= %s,Transportation= %s,VAT= %s,Transfer= %s,Total= %s where StockCode= %s",(
            Description.get(),
            Date.get(),
            Quantity.get(),
            Price.get(),
            Weight.get(),
            Transportation.get(),
            VAT.get(),
            Transfer.get(),
            Total.get(),
            StockCode.get()
            ))

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Successfully Updated")
        
            
        def deleteDB():
            sqlCon =pymysql.connect(host="localhost",user="root",password="",database="dataentry")
            cur =sqlCon.cursor()
            cur.execute("delete from dataentry where StockCode=%s",StockCode.get())

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form","Record Successfully Deleted")

        def searchDB():

            try:
                            
                sqlCon =pymysql.connect(host="localhost",user="root",password="",database="dataentry")
                cur =sqlCon.cursor()
                cur.execute("select * from dataentry where StockCode='%s'"%Search.get())

                row =cur.fetchone()

                StockCode.set(row[0])
                Description.set(row[1])
                Date.set(row[2])
                Quantity.set(row[3])
                Price.set(row[4])
                Weight.set(row[5])
                Transportation.set(row[6])
                VAT.set(row[7])
                Transfer.set(row[8])
                Total.set(row[9])

                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form","No Such Record Found")
                Reset()
            sqlCon.close()
            Search.set("")
                

            

        #=====================================WIDGETS=====================================
        lblStockCode = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Stock Code", bd=10)
        lblStockCode.grid(row=0,column=0, sticky=W)
        txtStockCode = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left',
                             textvariable=StockCode)
        txtStockCode.grid(row=0, column=1)

        lblDescription = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Description", bd=10)
        lblDescription.grid(row=1,column=0, sticky=W)
        txtDescription = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justif='left',
                               textvariable=Description)
        txtDescription.grid(row=1,column=1)

        lblQuantity = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Quantity", bd=10)
        lblQuantity.grid(row=2,column=0, sticky=W)
        txtQuantity = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justif='left',
                            textvariable=Quantity)
        txtQuantity.grid(row=2,column=1)

        self.lblPrice = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Price ($)", bd=10, )
        self.lblPrice.grid(row=0,column=2, sticky=W)
        self.txtPrice = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justif='left',
                              textvariable=Price)
        self.txtPrice.grid(row=0,column=3)

        self.lblWeight = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Weight (kg)", bd=10, )
        self.lblWeight.grid(row=1,column=2, sticky=W)
        self.txtWeight= Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left',
                              textvariable=Weight)
        self.txtWeight.grid(row=1,column=3)

        self.lblTransportation = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Transportation ($)", bd=10, )
        self.lblTransportation.grid(row=2,column=2, sticky=W)
        self.txtTransportation = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left',
                                       textvariable=Transportation)
        self.txtTransportation.grid(row=2, column=3)

        self.lblVAT = Label(InnerTopFrame1, font =('arial',12,'bold'),text="VAT ($)", bd=10, )
        self.lblVAT.grid(row=0,column=4, sticky=W)
        self.txtVAT = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left',
                            textvariable=VAT)
        self.txtVAT.grid(row=0, column=5)

        self.lblTransfer = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Transfer ($)", bd=10, )
        self.lblTransfer.grid(row=1,column=4, sticky=W)
        self.txtTransfer = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left',
                                 textvariable=Transfer)
        self.txtTransfer.grid(row=1, column=5)

        self.lblTotal = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Total ($)", bd=10, )
        self.lblTotal.grid(row=2,column=4, sticky=W)
        self.txtTotal = Entry(InnerTopFrame1, font =('arial',12,'bold'), bd=5, width=32, justify='left',
                              textvariable=Total)
        self.txtTotal.grid(row=2, column=5)

        self.lblSearch = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Search", bd=10, )
        self.lblSearch.grid(row=3,column=4,sticky=W)
        self.txtSearch = Entry(InnerTopFrame1,font =('arial',12,'bold'), bd=5, width=32, justify='left',
                               textvariable=Search)
        self.txtSearch.grid(row=3,column=5)

        self.lblDate = Label(InnerTopFrame1, font =('arial',12,'bold'),text="Date (dd/mm/yy)", bd=10, )
        self.lblDate.grid(row=3,column=0,sticky=W)
        self.txtDate = Entry(InnerTopFrame1,font =('arial',12,'bold'), bd=5, width=83, justify='left',
                             textvariable=Date)
        self.txtDate.grid(row=3,column=1,columnspan=3)
        #==============================================================================================
        scroll_x=Scrollbar(InnerTopFrame3, orient=HORIZONTAL)
        scroll_y=Scrollbar(InnerTopFrame3, orient=VERTICAL)
        tree_records=ttk.Treeview(InnerTopFrame3,height=13,columns=("StockCode","Description","Date","Quantity","Price","Weight","Transportation","VAT","Transfer","Total"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side =BOTTOM, fill=X)
        scroll_x.pack(side =RIGHT, fill=Y)

        tree_records.heading("StockCode",text="Stock Code")
        tree_records.heading("Description",text="Description")
        tree_records.heading("Date",text="Date")
        tree_records.heading("Quantity",text="Quantity")
        tree_records.heading("Price",text="Price($)")
        tree_records.heading("Weight",text="Weight(kg)")
        tree_records.heading("Transportation",text="Transportation($)")
        tree_records.heading("VAT",text="VAT($)")
        tree_records.heading("Transfer",text="Transfer($)")
        tree_records.heading("Total",text="Total($)")

        tree_records['show']='headings'

        tree_records.column("StockCode",width=100)
        tree_records.column("Description",width=150)
        tree_records.column("Date",width=150)
        tree_records.column("Quantity",width=252)
        tree_records.column("Price",width=100)
        tree_records.column("Weight",width=100)
        tree_records.column("Transportation",width=100)
        tree_records.column("VAT",width=100)
        tree_records.column("Transfer",width=150)
        tree_records.column("Total",width=100)

        tree_records.pack(fill =BOTH, expand=1)
        tree_records.bind("<ButtonRelease-1>",Info)
        DisplayData()

        
        



        #==============================================================================================
        self.btnAddNew = Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Add New",command=addData)
        self.btnAddNew.grid(row=0,column=0,padx=3)

        self.btnDisplay = Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Display",command=DisplayData)
        self.btnDisplay.grid(row=0,column=1,padx=3)

        self.btnUpdate = Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Update",command=update)
        self.btnUpdate.grid(row=0,column=2,padx=3)

        self.btnDelete = Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Delete",command=deleteDB)
        self.btnDelete.grid(row=0,column=3,padx=3)

        self.btnReset = Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Reset",command=Reset)
        self.btnReset.grid(row=0,column=4,padx=3)

        self.btnExit = Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Exit",command=iExit)
        self.btnExit.grid(row=0,column=5,padx=3)

        self.btnSearch = Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Search",command=searchDB)
        self.btnSearch.grid(row=0,column=6,padx=3)
        #==============================================================================================
        

        



        
        

if __name__=='__main__':
    root = Tk()
    application = DataEntryForm(root)
    root.mainloop()
