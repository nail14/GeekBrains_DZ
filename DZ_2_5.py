my_list = [57.833, 46.5115] #, 97, 1999.9, 2399, 14289.00, 461.23, 11.99, 5999, 149799.00 ]
rub, Kop = ['Руб','Коп']
my_list_COPY = my_list.copy()
m1, m2 = my_list.copy()
mes_4 = '{m1:>15}! На счете {m2:.2f}'.format(m1=m1, m2=m2)
print(mes_4, rub[0::1])
# my_list_COPY[0] = (7+5)**3 #подмена
print(rub[0],'{:.2f},{:f}',rub[1] .format(57.8, 46.51))