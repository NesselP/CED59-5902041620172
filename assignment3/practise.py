#1 สร้างตัวแปร my_lst เก็บค่า 3 ค่า ผลรวมเท่ากับ 100
mylist = [50,40,10]
print("sum =",sum(mylist))

#2 สร้างตัวแปร my_tuple เป็น single value กี่ตัวก็ได้ ค่าไม่ซ้ำกัน
mytuple = (5,9,12,77,90,100)
print("mytuple =", mytuple)

#3 เปลี่ยนแปลงตัวแปลใน set2 เพื่อนำมา intersection กับ set1 ให้ได้ค่าออกมา > {5,77,9,12}
set1={12,9,77,5,-3}
set2=(5,12,9,90,100,77)
print("intersection = ",set1.intersection(set2))
