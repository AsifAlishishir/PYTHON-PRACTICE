phy=int(input("Enter physics mark: "))
math=int(input("Enter math mark: "))
bio=int(input("Enter biology mark: "))

total=phy+math+bio

total_per=(total/300)*100
total_phy=(phy/100)*100
total_math=(math/100)*100
total_bio=(bio/100)*100

if(total_per >=40 and total_phy>=33 and total_math>=33 and total_bio>=33):
    print(f"You have passed in the exam!! Total Percentage: {total_per:.2f}")
else:
    print( f"You have failed. Total Percentage:  {total_per:.2f}")