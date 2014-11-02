MonthsDays={"Jan":31, "Feb":28, "Mar":31, "Apr":30, "May":31, "Jun":30, "Jul":31,
        "Aug":31, "Sep":30, "Oct":31, "Nov":30, "Dec":31}
LeapMonths={"Jan":31, "Feb":29, "Mar":31, "Apr":30, "May":31, "Jun":30, "Jul":31,
        "Aug":31, "Sep":30, "Oct":31, "Nov":30, "Dec":31}
Months="Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

Year=1900
Days=["Sun","Mon","Tue", "Wed","Thu","Fri","Sat"]
TodayOfWeek=1
DayOfMonth=1
Month=0
MondayFirstOfMonth=0
Leap=MonthsDays
while (Year!=2001):
    
    if TodayOfWeek==0 and DayOfMonth==1:
        MondayFirstOfMonth+=1
        print("Today is {}, {} {} {} \n".format(Days[TodayOfWeek],DayOfMonth,Months[Month], Year))
    if Leap[Months[Month]]==DayOfMonth:
        TodayOfWeek=(TodayOfWeek+1)%7
        DayOfMonth=1
        if Month==11:
            Year+=1
            Month=0
            #print("Today is {}, {} {} {} \n".format(Days[TodayOfWeek],DayOfMonth,Months[Month], Year))
            if Year % 4==0 and Year %400!=0:
                Leap=LeapMonths
            else:
                Leap=MonthsDays
        else:
            Month+=1
    else:
        TodayOfWeek=(TodayOfWeek+1)%7
        DayOfMonth+=1
    #print("Today is {}, {} {} {} \n".format(Days[TodayOfWeek],DayOfMonth,Months[Month], Year))
print("Today is {}, {} {} {} \n".format(Days[TodayOfWeek],DayOfMonth,Months[Month], Year))

print MondayFirstOfMonth
    
        
