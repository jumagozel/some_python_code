# case 1
# week=["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# day = int(input("enter day number: "))
# if day==1:
#     print(week[1])
# elif day == 2:
#     print(week[2])
# elif day == 3:
#     print(week[3])
# elif day == 4:
#     print(week[4])
# elif day == 5:
#     print(week[5])
# elif day == 6:
#     print(week[6])
# elif day == 7:
#     print(week[7])

# case 2

# k=int(input("enter k:"))
# exam_mark=["", "bad", "unsatisfactory", "mediocre", "good", "excellent"]


# if 6>k>0:
#     pass
#     get_results = exam_mark[k]
#     print(get_results)
# else:
#     print("you must enter between 1 an 5")

# case dictionary

# k=int(input("enter k: "))
# exam_mark = {
#     1: "bad",
#     2: "unsatisfactory",
#     3: "mediocre",
#     4: "good",
#     5: "excellent"
# }

# if 6>k>0:
#     get_results = exam_mark[k]
#     print(get_results)
# else:
#     print("you must enter between 1 an 5")

# case 16

b=int(input("enter the year:"))
years=["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
years_dig=["", "", "twenty", "thirty", "fourty", "fifty", "sixty"]

a=b%10
c=b//10

if 70>b>19:
    d=years_dig[c]+years[a]
    print("22-", d)

