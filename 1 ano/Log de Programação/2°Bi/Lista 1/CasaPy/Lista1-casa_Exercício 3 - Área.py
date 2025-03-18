h_parede = float(input('Digite a altura de sua parede, em metros: '))
l_parede = float(input('Agora, digite a largura da mesma, em metros: '))
h_azulejo = float(input('Digite a altura de seu azulejo, em metros: '))
l_azulejo = float(input('Por fim, digite a largura do azulejo, também em metros: '))
a_parede = h_parede * l_parede
a_azulejo = h_azulejo * l_azulejo
qntd_azulejo = a_parede / a_azulejo
print('Serão necessários {:.2f}'.format(qntd_azulejo), 'azulejos para preencher a parede.')