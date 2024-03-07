from tkinter import *

win=Tk()
win.title('SIMPLE CALCULATOR')
win.geometry('450x350')
win.resizable(False,False)

win.config(bg='burlywood1')


def num(a):
    
    if a=='7':
        text=entry1.get()
        entry1.delete(0,END)
        text_seven=text+'7'
        
        entry1.insert(0,text_seven)
    
    elif a=='8':
        text=entry1.get()
        entry1.delete(0,END)
        
        text_eight=text+'8'
        
        entry1.insert(0,text_eight)
        
    elif a=='9':
        text=entry1.get()
        entry1.delete(0,END)
        
        text_nine=text+'9'
        
        entry1.insert(0,text_nine)
        
    elif a=='+':
       text=entry1.get()
       entry1.delete(0,END)
         
       text_add=text+'+'
         
       entry1.insert(0,text_add)
         
    elif a=='=':
        text=entry1.get()
        entry1.delete(0,END)
          
        text_eql=text+'='
          
        entry1.insert(0,text_eql)
        
             
        
        exp=entry1.get()
        
        length=len(entry1.get())
        
        expr=exp[0:length-1]
        
        if '%' in expr:
                      
            expr=expr.replace('%','')
            a,b =expr.split('*')
            a,b=float(a),float(b)
            value=a*b/100
            label1.config(text=value)
                        
        else:        
            value=eval(expr)      
            label1.config(text=value)
        
    elif a=='C':
        
        entry1.delete(0,END)
        label1.config(text='')
         
    elif a=='-':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_sub=text+'-'
         
        entry1.insert(0,text_sub)
        
    elif a=='.':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_point=text+'.'
         
        entry1.insert(0,text_point)
    
    elif a=='*':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_mult=text+'*'
         
        entry1.insert(0,text_mult)
        
    elif a=='/':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_div=text+'/'
         
        entry1.insert(0,text_div)
        
    elif a=='4':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_four=text+'4'
         
        entry1.insert(0,text_four)
        
    elif a=='5':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_five=text+'5'
         
        entry1.insert(0,text_five)
        
    elif a=='6':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_six=text+'6'
         
        entry1.insert(0,text_six)
        
    elif a=='1':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_one=text+'1'
         
        entry1.insert(0,text_one)
        
    elif a=='2':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_two=text+'2'
         
        entry1.insert(0,text_two)
        
    elif a=='3':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_three=text+'3'
         
        entry1.insert(0,text_three)
        
    elif a=='0':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_zero=text+'0'
         
        entry1.insert(0,text_zero)
        
    elif a=='(':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_brac1=text+'('
         
        entry1.insert(0,text_brac1)


    elif a==')':
        text=entry1.get()
        entry1.delete(0,END)
         
        text_brac2=text+')'
          
        entry1.insert(0,text_brac2)        
        
    elif a=='%':
        
        text=entry1.get()
        entry1.delete(0,END)
         
        text_per=text+'%'
          
        entry1.insert(0,text_per)
        
 
    
z=StringVar()
entry1=Entry(win,font=("Arial",20),justify='right',textvariable=z,width=25,bg='burlywood3')
entry1.grid(row=0,column=0,columnspan=5,padx=5,pady=5)

label1=Label(win,width=30,justify=RIGHT,font=("Arial",20),bg='burlywood1')
label1.grid(row=1,column=0,columnspan=5)
# Row 2 
btnC=Button(win, text='C',bg='burlywood3',width=5,height=2,command=lambda : num('C'),activebackground='burlywood3')
btnC.grid(row=2,column=0,padx=5,pady=5)

btn_brac=Button(win, text='(',bg='burlywood3',command=lambda: num('('),width=5,height=2,activebackground='burlywood3')
btn_brac.grid(row=2,column=1,padx=5,pady=5)

btn_per=Button(win, text=')',bg='burlywood3',width=5,height=2,command=lambda: num(')'),activebackground='burlywood3')
btn_per.grid(row=2,column=2,padx=5,pady=5)

btn_div=Button(win, text='/',bg='darkgoldenrod3',width=5,height=2,command=lambda:num('/'),activebackground='darkgoldenrod3')
btn_div.grid(row=2,column=3,padx=5,pady=5)

# Row 3

btn7=Button(win, text='7',bg='burlywood3',width=5,height=2,command=lambda: num('7'),activebackground='burlywood3')
btn7.grid(row=3,column=0,pady=5)

btn8=Button(win, text='8',bg='burlywood3',width=5,height=2,command=lambda:num('8'),activebackground='burlywood3')
btn8.grid(row=3,column=1,pady=5)

btn9=Button(win, text='9',bg='burlywood3',width=5,height=2,command=lambda:num('9'),activebackground='burlywood3')
btn9.grid(row=3,column=2,pady=5)

btn_mult=Button(win, text='*',bg='darkgoldenrod3',width=5,height=2,command=lambda : num('*'),activebackground='darkgoldenrod3')
btn_mult.grid(row=3,column=3,pady=5)
# Row 4 

btn4=Button(win, text='4',bg='burlywood3',width=5,height=2,command=lambda : num('4'),activebackground='burlywood3')
btn4.grid(row=4,column=0,padx=5,pady=5)

btn5_brac=Button(win, text='5',bg='burlywood3',width=5,height=2,command=lambda : num('5'),activebackground='burlywood3')
btn5_brac.grid(row=4,column=1,padx=5,pady=5)

btn6_brac2=Button(win, text='6',bg='burlywood3',width=5,height=2,command=lambda : num('6'),activebackground='burlywood3')
btn6_brac2.grid(row=4,column=2,padx=5,pady=5)

btn_sub=Button(win, text='-',bg='darkgoldenrod3',width=5,height=2,command=lambda : num('-'),activebackground='darkgoldenrod3')
btn_sub.grid(row=4,column=3,padx=5,pady=5)

# Row 5

btn1=Button(win, text='1',bg='burlywood3',width=5,height=2,command=lambda : num('1'),activebackground='burlywood3')
btn1.grid(row=5,column=0,pady=5)

btn2=Button(win, text='2',bg='burlywood3',width=5,height=2,command=lambda : num('2'),activebackground='burlywood3')
btn2.grid(row=5,column=1,pady=5)

btn3=Button(win, text='3',bg='burlywood3',width=5,height=2,command=lambda : num('3'),activebackground='burlywood3')
btn3.grid(row=5,column=2,pady=5)

btn_add=Button(win, text='+',bg='darkgoldenrod3',width=5,height=2,command=lambda : num('+'),activebackground='darkgoldenrod3')
btn_add.grid(row=5,column=3,pady=5)

# Row 6

btn_per=Button(win, text='%',bg='burlywood3',width=5,height=2,command=lambda : num('%'),activebackground='burlywood3')
btn_per.grid(row=6,column=0,padx=5,pady=5)

btn0=Button(win, text='0',bg='burlywood3',width=5,height=2,command=lambda : num('0'),activebackground='burlywood3')
btn0.grid(row=6,column=1,padx=5,pady=5)

btn_point=Button(win, text='.',bg='burlywood3',width=5,height=2,command=lambda: num('.'),activebackground='burlywood3')
btn_point.grid(row=6,column=2,padx=5,pady=5)

btn_equals=Button(win, text='=',bg='darkgoldenrod3',width=5,height=2,command=lambda: num('='),activebackground='darkgoldenrod3')
btn_equals.grid(row=6,column=3,padx=5,pady=5)


win.mainloop()
