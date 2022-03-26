import csv
from matplotlib import pyplot as plt

new_item_cost = 80000
first_year_cost = 3000
yearly_costs = 5000
marr = 0.05
n = 20
prv_sig = 0
cr_arr = []
euac_arr = []
euao_arr = []
time_arr = []
with open('lifetime.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['years', 'CR', 'Q&M', 'PV SIGMA Q&M', 'EUAO', 'EUAC'])
for j in range(1,n+1):
    cr = new_item_cost * ((marr * (1 + marr) ** j) / (((1 + marr) ** j) - 1))
    qm = first_year_cost + yearly_costs * (j-1)
    pv_step1 = qm / ((1+marr)**j)
    if j == 1:
        pv_sig = pv_step1
        prv_sig = pv_sig
    else:
        pv_sig = prv_sig + pv_step1
        prv_sig = pv_sig
    euao = pv_sig * ((marr * (1 + marr) ** j) / (((1 + marr) ** j) - 1))
    euac = cr + euao
    line = [j, round(cr,2), round(qm,2), round(pv_sig,2), round(euao,2), round(euac,2)]
    time_arr.append(j)
    cr_arr.append(cr)
    euao_arr.append(euao)
    euac_arr.append(euac)
    with open('lifetime.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(line)


plt.plot(time_arr,cr_arr)
plt.plot(time_arr,euac_arr)
plt.plot(time_arr,euao_arr)
plt.grid()
plt.show()