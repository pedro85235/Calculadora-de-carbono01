print('Calculadora de carbono')
n1 = float(input('Digite a distância de cada entrega em km:'))
n2 = float(input('Digite as entregas feitas por dia:'))
dpd = n1*n2
n3 = float(input('Digite a média de km com 1L de combustìvel:'))
mc = dpd/n3
cu = str(input('Que tipo de combustível foi usado? '))
c1 = cu.lower()
if c1=='gasolina':
  ec = mc*2.28
elif c1=='diesel':
  ec = mc*3.2
elif c1=='etanol':
  et = str(input('Etanol anidro ou hidratado?'))
  et = et.lower()
  if et=='anidro':
    ec = mc*2.71
  elif et=='hidratado':
    ec = mc*1,86
cc = ec/1000
print("""No dia de hoje sua pegada de carbono foi {:.2f} crédito de carbono necessário {:.2f}
 Pense na suas atitudes =)""".format(ec, cc))