#daydayup.py
def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [0,6]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
defe = 0.01
while dayup(defe)<37.78:
    defe = defe+0.001
print("{:.3f}".format(defe))
        
