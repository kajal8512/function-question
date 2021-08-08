def driver_speed(limit):
    i=1
    sum=0
    while i>=70:
        i=i+1
        if i<=70:
            print("ok")
        elif i>70:
            sum=sum+i
            print(sum,"points")
        sum=sum+i
driver_speed(80)