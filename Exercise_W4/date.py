

def shamsi_to_miladi(year,month,day):
    sal_kabiseh_shamsi=year//4
    roz_sal_shamsi=(year-1)*365
    if month<7:
        roz_mah_shamsi=(month-1)*31
    else:
        roz_mah_shamsi=(month-1)*31
    kol_rozha_shamsi=roz_sal_shamsi + roz_mah_shamsi + day + sal_kabiseh_shamsi
    kol_rozha_miladi=kol_rozha_shamsi+226899


    sal_kabiseh_miladi=(year+621)//4

    sal_miladi=((kol_rozha_miladi-sal_kabiseh_miladi)//365)+1


    roz_miladi=(kol_rozha_miladi-sal_kabiseh_miladi)%365

    miladi_month_list=( 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    month_index=0
    while roz_miladi>miladi_month_list[month_index] and month_index<12:
        roz_miladi-=miladi_month_list[month_index]
        month_index+=1
    mah_miladi=month_index+1    
    return "*** year:", sal_miladi,"month: ", mah_miladi,"  day: ",roz_miladi," ***" 
   




def miladi_to_shamsi(year,month,day):
    sal_kabiseh_miladi=year//4
    roz_sal_miladi=(year-1)*365
    miladi_month_list=( 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    roz_mah_miladi=0
    for i in range(month):
        roz_mah_miladi+=miladi_month_list[i]

    kol_rozha_miladi=roz_sal_miladi + roz_mah_miladi-1 + day + sal_kabiseh_miladi
    kol_rozha_shamsi=kol_rozha_miladi-226899

    sal_kabiseh_shamsi=(year-621)//4

    sal_shamsi=((kol_rozha_shamsi-sal_kabiseh_shamsi)//365)+1

    roz_shamsi=(kol_rozha_shamsi-sal_kabiseh_shamsi)%365


    shamsi_month_list=(31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29)

    month_index=0
    while roz_shamsi>shamsi_month_list[month_index] and month_index<12:
        roz_shamsi-=shamsi_month_list[month_index]
        month_index+=1
    mah_shamsi=month_index 

    return "*** year:", sal_shamsi,"month: ", mah_shamsi,"  day: ",roz_shamsi," ***"  



 
 

year,month,day,calender=int(input("year:")),int(input("month:")),int(input("day:")),input("enter your calender type miladi or shamsi:")
if calender=="shamsi":
    print(shamsi_to_miladi(year,month,day))


if calender=="miladi":
    print(miladi_to_shamsi(year,month,day))
