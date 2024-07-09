num1=float(input('Digite o primeiro número:'))
num2=float(input('Digite o segundo número:'))
operacao=input('Qual operação desejar realizar?(Adição +)(Subtração -)(Multiplicação *)(Divisão /)')
calculo=0
if operacao=='+':
	calculo=num1+num2
	print('Você escolheu adição, o resultado é:',calculo)
elif operacao=='-':
	calculo=num1-num2
	print('Você escolheu subtração, o resultado é:',calculo)
elif operacao=='*':
	calculo=num1*num2
	print('Você escolheu multiplicação, o resultado é: ',calculo)
elif operacao=='/':
	calculo=num1/num2
	print('Você escolheu divisão, o resultado é:',calculo)
else:
	print('Caractere inválido!')