import pandas as pd
import matplotlib.pyplot as plt


def menu():
    print("***********************************************************")
    print("                      BUS RESERVATION SYSTEM                ")
    print("************************************************************")
    print()
    print("      1. Know about the project                             ")
    print("      2. Reading file bus                                   ")
    print("      3. Adding new bus detail in file                      ")
    print("      4. Schedule of all buses                              ")
    print("      5. Sorting buses names                                ")
    print("      6. Fare of b953                                       ")
    print("      7. Fare of a247                                       ")
    print("      8. Bus enquiry                                        ")
    print("      9. Cancel bus                                         ")
    print("     10. Change of arrival things                           ")
    print("     11. Search by starting bus stop                        ")
    print("     12. Find total no. of buses                            ")
    print("     13. Update fare of bus 953                             ")
    print("     14. Ticket reservation                                 ")
    print("     15. Specific column                                    ")
    print("     16. Top and bottom records from passenger              ")
    print("     17. Reading file passenger                             ")
    print("     18. Adding new passenger tickets detail in file        ")
    print("     19. Find total sale of tickets                         ")
    print("     20. Line plot                                          ")
    print("     21. Line1 plot                                         ")
    print("     22. Barh plot                                          ")
    print("     23. Barh plot                                          ")
    print("     24. Bar plot                                           ")
    print("     25. bar1 plot                                          ")
    print()
    print()
    print("************************************************************")

menu()


def about():
    print("The project is developed on BUS RESERVATION SYSTEM.It contain 25 options.")
    print("      In project 4 CSV Files are used... bus,passenger,b953 and a247.      ")


def read_buses():
    print("Reading details of file bus")
    print()
    print()
    df=pd.read_csv("c:\\users\\varnika\\downloads\\bus.csv",index_col=0)
    print(df)


def new_buses():
    print("Adding new bus in file bus")
    df=pd.read_csv("c:\\users\\Varnika\\Downloads\\bus.csv",index_col=0)
    print(df)
    n=(input("Enter bus no. :"))
    a=(input("Enter bus name:"))
    b=(input("Enter start:"))
    c=(input("Enter stop:"))
    d=float(input("Enter departure:"))
    e=float(input("Enter arrival:"))
    f=float(input("Enter duration of journey:"))
    r=int(input("Enter frequency:"))
    df.loc[n]=[a,b,c,d,e,f,r]
    print(df)


def schedule():
    print("Schedule of all buses")
    print()
    df=pd.read_csv("c:\\users\\varnika\\Downloads\\bus.csv",usecols=["busname","departure","arrival"],index_col=0)
    print(df)


def sort_buses():
    print("sorting of buses")
    print()
    df=pd.read_csv("c:\\users\\varnika\\downloads\\bus.csv",index_col=0)
    df=df.sort_values("busno")
    print(df)


def b953_fare():
    print("Show fares of b953 bus")
    print()
    df=pd.read_csv("c:\\users\\Varnika\\Downloads\\B953.csv",usecols=["start","stop","fare"],index_col=0)
    print(df)


def a247_fare():
    print("Show fares of a247 bus")
    print()
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\A247.csv",usecols=["start","stop","fare"],index_col=0)
    print(df)


def enquiry():
    print("Find out time table of a bus ")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\bus.csv",index_col=0,usecols=["busname","start","departure","arrival","duration"])
    print(df)


def cancelbus():
    print("Deleting cancelled bus detail")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\bus.csv",index_col="busname")
    print(df)
    tnum=(input("Enter bus name:"))
    df.drop(tnum,axis=0,inplace=True)
    print("Record of bus temperorily deleted")
    print()
    print(df)


def changetiming():
    df=pd.read_csv("c:\\users\\Varnika\\Downloads\\bus.csv")
    print("Previous timings of arrival")
    print()
    print(df)
    print()
    df.loc[df["busname"]=="Taj express",["arrival"]]=df["arrival"]+ .20
    print()
    print(df)


def search_by_bus_stop():
    print("Search by last stop")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\bus.csv",index_col="busname")
    print(df)
    print()
    df=df.loc[df["stop"]=="Agra cantt"]
    print(df)


def totalbuses():
    print("find total buses")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\bus.csv",usecols=["busname","frequency"])
    print(df)
    print()
    Totalbuses=df["frequency"].sum()
    print("Total buses are:", Totalbuses)


def update_b953():
    print("To increase fare and save")
    print("previous fares")
    print()
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\B953.csv")
    print(df)
    print()
    print("increase fare by rs. 50")
    print()
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\B953.csv")
    df["fare"]+=50
    print(df)


def ticket_reservation():
    print("WE HAVE THE FOLLOWING BUSES FOR YOU:-")
    print("Bus b953 to Bhopal from New Delhi:-")
    print("For b953-----")
    print()
    print("1. If you want to get down at Indore pay Rs. 1200")
    print("2. If you want to get down at Lalitpur pay Rs. 1800")
    print("3. If you want to get down at Nagpur pay Rs. 2500")
    print("4. If you want to get down at Bhopal pay Rs. 3000")
    print()
    print("For a247-----")
    print("1. If you want to get down at Faridabad pay Rs. 1000")
    print("2. If you want to get down at Kosi pay Rs. 1200")
    print("3. If you want to get down at Mathura pay Rs. 1500")
    print("4. If you want to get down at agra pay Rs. 1800")
    busname=(input("ENTER YOUR CHOICE OF BUS NO. "))
    print(busname)
    x=int(input("ENTER YOUR CHOICE OF STOP"))
    n=int(input("HOW MANY TICKETS YOU NEED:"))

    if (busname=="b953"):
        if(x==1):
            print("YOU HAVE CHOSEN 1st STOP INDORE")
            s=1200*n
        elif(x==2):
            print("YOU HAVE CHOSEN 2nd STOP LALITPUR")
            s=1800*n
        elif(x==3):
            print("YOU HAVE CHOSEN 3rd STOP NAGPUR")
            s=2500*n
        elif(x==4):
            print("YOU HAVE CHOSEN 4th STOP BHOPAL")
            s=3000*n
        else:
            print("Invalid option")

            print("PLEASE CHOOSE A CORRECT BUS NO.")
        print("YOUR TOTAL TICKET PRICE IS =",s,"\n")
    elif(busname=="a247"):
        if(x==1):
            print("YOU HAVE CHOSEN 1st STOP FARIDABAD")
            s=1000*n
        elif(x==2):
            print("YOU HAVE CHOSEN 2nd STOP KOSI")
            s=1200*n
        elif(x==3):
            print("YOU HAVE CHOSEN 3rd STOP MATHURA")
            s=1500*n
        elif(x==4):
            print("YOU HAVE CHOSEN LAST STOP AGRA")
            s=1800*n
        else:
            print("Invalid option")

            print("PLEASE CHOOSE A CORRECT BUS NO.")
        print("YOUR TOTAL TICKET PRICE IS =",s,"\n")
    else:
        print("Bus not available")


def spec_col():
    print("Show only busname, its last stop and duration of journey")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\bus.csv",usecols=["busname","stop","duration"])
    print(df)


def top_bottom():
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\B953.csv")
    print("top 2 rows")
    print(df.head(2))
    print()
    print()
    print("last 2 rows")
    print(df.tail(2))


def read_passenger():
    print("Reading file passenger")
    print()
    print()
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\passenger.csv")
    print(df)


def new_passenger():
    print("Adding new passenger tickets details in fila ")
    print()
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\B953.csv",index_col=0)
    print("b953 to bhopal")
    print(df)
    print()
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\A247.csv",index_col=0)
    print("a247 to Agra")
    print(df)
    print()
    print()
    print("Record of previous sale of tickets")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\passenger.csv")
    print(df)
    n=(input("Enter bus no:"))
    a=(input("Enter tickets:"))
    b=(input("Enter start:"))
    c=(input("Enter stop:"))
    r=int(input("Fare:"))
    f=a*r
    df.loc[3]=[n,a,b,c,f]
    print(df)


def sale():
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\passenger.csv")
    print(df)
    print()
    print("Total sale of tickets")
    print(df[("fare")].sum())


def line_plot():
    print("Line plot")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\B953.csv")
    print(df)
    x=df["stop"]
    y=df["fare"]
    plt.title("Fare for b953",fontsize=14,color="r")
    plt.xlabel("stops",fontsize=14,color="r")
    plt.ylabel("fare",fontsize=14,color="r")
    plt.plot(x,y,marker="x",markerfacecolor="g",ls="dashed",linewidth=4,color="r")
    plt.show()


def line1_plot():
    df=pd.read_csv("c:\\users\\Varnika\\Downloads\\A247.csv")
    print(df)
    plt.plot(df["stop"],df["fare"],marker="o",label="fare")
    plt.title("fare for a247",fontsize=14,color="b")
    plt.xlabel("stops",fontsize=14,color="b")
    plt.ylabel("fare",fontsize=14,color="b")
    plt.xticks(rotation=30)
    plt.legend()
    plt.grid(True)
    plt.show()


def barh_plot():
    print("Horizontal bar plot")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\B953.csv")
    print(df)
    x=df["stop"]
    y=df["fare"]
    plt.title("Fare for b953",fontsize=14,color="b")
    plt.xlabel("fare",fontsize=14,color="b")
    plt.ylabel("stops of buses",fontsize=14,color="b")
    plt.barh(x,y,color="blue",edgecolor="pink")
    plt.show()


def barh1_plot():
    print("Horizontal bar plot")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\A247.csv")
    print(df)
    x=df["stop"]
    y=df["fare"]
    plt.title("Fare for a247",fontsize=14,color="r")
    plt.xlabel("fare",fontsize=14,color="r")
    plt.ylabel("stops of buses",fontsize=14,color="r")
    plt.barh(x,y,color="silver",edgecolor="red")
    plt.show()


def bar_plot():
    print("Bar plot")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\bus.csv")
    print(df)
    x=df["busname"]
    y=df["frequency"]
    plt.title("No. of buses for each destination",fontsize=14,color="r")
    plt.xlabel("bus name",fontsize=14,color="r")
    plt.ylabel("frequency",fontsize=14,color="r")
    plt.bar(x,y,width=0.3,color="gold",edgecolor="red")
    plt.show()
    

def bar1_plot():
    print("Bar plot")
    df=pd.read_csv("c:\\Users\\Varnika\\Downloads\\B953.csv")
    print(df)
    x=df["stop"]
    y=df["distance(km)"]
    plt.title("distance of all destination")
    plt.xlabel("last stop")
    plt.ylabel("distance in km")
    plt.bar(x,y,color="cyan",edgecolor="red")
    plt.show()


opt=""
opt=int(input("enter your choice:"))
if opt==1:
    about()
elif opt==2:
    read_buses()
elif opt==3:
    new_buses()
elif opt==4:
    schedule()
elif opt==5:
    sort_buses()
elif opt==6:
    b953_fare()
elif opt==7:
    a247_fare()
elif opt==8:
    enquiry()
elif opt==9:
    cancelbus()
elif opt==10:
    changetiming()
elif opt==11:
    search_by_bus_stop()
elif opt==12:
    totalbuses()
elif opt==13:
    update_b953()
elif opt==14:
    ticket_reservation()
elif opt==15:
    spec_col()
elif opt==16:
    top_bottom()
elif opt==17:
    read_passenger()
elif opt==18:
    new_passenger()
elif opt==19:
    sale()
elif opt==20:
    line_plot()
elif opt==21:
    line1_plot()
elif opt==22:
    barh_plot()
elif opt==23:
    barh1_plot()
elif opt==24:
    bar_plot()
elif opt==25:
    bar1_plot()
else:
    print("invalid option")
    print("\a")
