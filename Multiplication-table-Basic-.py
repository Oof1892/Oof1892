import tkinter as tk          #นำเข้าไลบรารี่ Tkinter เพื่อควบคุมกล่อง ข้อความ

window = tk.Tk()        #เรียกใช้ไลบรารี่

def show_output():            #สร้างฟังก์ชั่น
      number = int(input_number.get())          #แปลงชนิดข้อมูลให้เป็นตัวเลข
       
      output = ''       #ใช้เก็บข้อความที่แสดงผลในสูตร
      for i in range (1, 13):       #สร้างลูป 1-12 
            output += str(number) + ' x ' + str(i)      #แปลงตัวเลขเป็นข้อความแล้วแปลง iเป็นจำนวนเต็ม
            output += ' = ' + str(number * i) + '\n'     #เอาตัวเลขมาคูณ i แล้วเว้นบรรทัด
      output_number.configure(text=output)#
      
window.title("สูตรคูณ")         #ชื่อหัวข้อบนสุด

window.minsize(width=500 ,height=500 )          #ขนาดความ ก*ย ของกล่อง

window_title = tk.Label(master=window ,text='สูตรคูณแม่')            #หัวข้อรอง
window_title.pack()           #แสดงผล

input_number = tk.Entry(master=window)          #รับข้อมูลตัวแปรเข้า
input_number.pack()           #แสดงผล

button = tk.Button(master=window , text='ได้แก่' ,command=show_output)          #ปุ่ม
button.pack()           #แสดงผล

output_number = tk.Label(master=window)         #แสดงผลลัพธ์สูตรคูณ
output_number.pack()          #แสดงผล

window.mainloop()  #สตาร์ทแอพ