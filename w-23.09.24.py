# a. צור רשימה ריקה והכנס לתוכה את המספרים 1-100 בלולאת for באמצעות append
# b. הדפס את האיבר הראשון ברשימה שייצרת )רמז אינדקס 0(
# c. הדפס את האיבר האחרון ברשימה שייצרת )רמז אינדקס -1(
# d. הדפס כמה איברים יש ברשימה )רמז: len )
# e. צור והדפס רשימה של המספרים 3-12 כולל )רמז: נקודותיים ]סיום:התחלה[ (
# f. צור והדפס רשימה של המספרים 80 ועד לסוף הרשימה )רמז: נקודותיים חצי ריק (
# g. צור והדפס רשימה של המספרים מתחילת הרשימה ועד אינדקס 17
# h. הדפס את הרשימה בסדר הפוך )רמז פעמיים נקודותיים עם -1 (
# i. הדפס את כל המספרים הזוגיים ב רשימה כלומר ,2 ,4 ,6 8 ... )רמז: התחל מאינדקס
# של המספר 2 וקפוץ בדילוגים של 2 השתמש בפעמיים נקודותיים 0:100:2(
# j. הדפס את כל המספרים המתחלקים ב 3 ללא שארית , כלומר ,3 ,6 ,9 12 ...
# k. הדפס את כל המספרים המתחלקים ב 7 ללא שארית , כלומר ,7 ,14 21 ...
# l. הדפס את כל הכפולות של ,10 כלומר ,10 ,20 30 ...
# m. הדפס את המספרים מ 99 ועד 66 בדילוגים של ,3 כלומר ,99 ,96 ...,93ועד 66
# n. הכנס את המספר 999 במרכז הרשימה )רמז insert )
# o. הוצא את המספר 100 מהרשימה )רמז: pop )

#start

numbers:list[int]=[]
for i in range(1,100+1):
    numbers.append(i)
print(numbers[:])
print(f"the first member  {numbers[0]}")
print(f"the last member  {[len (numbers)-1]}")
print(f"lengt"
      f"h  {len(numbers)}")
book:list[int]=[]
for i in range(1,12+1):
    book.append(i)
print(f" numbers {book [ : ]}")
num:list[int]=[]
for i in range(80,100+1):
    num.append(i)
print(f"numbers{num [:100]}  ")
#עקב שאמרת ליצור תוכנית נוספת אפשר לעשות בדרך הבאה:
print(f"numbers{num [:]}  ")
w1:list[int]=[]
for i in range(1,20+1):
    w1.append(i)
print(f"numbers{w1 [ :17]}")
print(f"revers{numbers[::-1]}")
print(f"even{numbers[1::2]}")
print(f"three{numbers[2::3]}")
print(f"seven{numbers[6::7]}")
print(f"multiplied{numbers[9::10]}")
print(f"skips{numbers[98:66:-3]}")
numbers.insert(50,999)
print(numbers[:])
numbers.pop()
print(numbers[:])

#stop