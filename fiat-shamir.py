####################################################################
## Universidad de La Laguna						 				  ##
## Escuela Superior de Ingeniería y Tecnología	 				  ##
## Grado en Ingeniería Informática				 				  ##
## Seguridad en Sistemas Informáticos			 				  ##
## Fecha: 02/05/2017							 				  ##
## Autor: Kevin Estévez Expósito (alu0100821390) 				  ##
## 																  ##
## Práctica 7: Algoritmo de Fiat-Shamir							  ##
## Descripción: Demostración de conocimiento nulo de Fiat-Shamir. ##
##											 					  ##
## Ejecución: py fiat-shamir.py									  ##
####################################################################


import sys


##### FUNCIONES #####

# Función de exponenciación rápida modular
def exp_rapida(base, exponente, modulo):
	x = 1
	y = base % modulo
	b = exponente
	while (b > 0):
		if ((b % 2) == 0):  # Si b es par...
			y = (y * y) % modulo
			b = b / 2
		else:  # Si b es impar...
			x = (x * y) % modulo
			b = b - 1
	return x

	
##### PROGRAMA PRINCIPAL #####

print ()
# Se pide el número primo 'p'
p = int(input("Introduzca el número [preferiblemente] primo 'p': "))
# Se pide el número primo 'q'
q = int(input("Introduzca el número [preferiblemente] primo 'q': "))

# Se calcula el valor de N
N = p * q
# Se muestra el valor de N
print ()
print ("N = " + str(N))
print ()

# Se pide la identificación secreta de A
s = int(input("Usuario A: Introduzca la identificación secreta: "))
# Si no se ha introducido un valor válido, se vuelve a pedir
while (s < 1 and s >= N):
	print ("La identificación secreta debe ser un número entre 1 y " + str(N))
	s = int(input("Usuario A: Introduzca la identificación secreta: "))

# Se calcula la identificación pública de A
v = exp_rapida(s, 2, N)
# Se muestra la identificación pública de A
print ()
print ("v = " + str(v))
print ()

# Se pide el número de iteraciones a realizar
i = int(input("Introduzca el número de iteraciones a realizar: "))

conoce = True
j = 0
# Se itera tantas veces como se haya introducido mientras el usuario A conozca la información que se le pide
while ((bool(conoce)) and (j < i)):
	j += 1
	print ()
	print ()
	print ("--- " + str(j) + "ª iteración ---")
	print ()
	
	# Se pide el compromiso secreto de A
	x = int(input("Usuario A: Introduzca el número de compromiso secreto: "))
	# Si no se ha introducido un valor válido, se vuelve a pedir
	while (x < 1 and x >= N):
		print ("El compromiso secreto debe ser un número entre 1 y " + str(N))
		x = int(input("Usuario A: Introduzca el número de compromiso secreto: "))
	
	# Se calcula el testigo
	a = exp_rapida(x, 2, N)
	# Se muestra el testigo
	print ()
	print ("a = " + str(a))
	print ()
	
	# Se pide el bit para el reto
	e = int(input("Usuario B: Introduzca el bit para el reto (0/1): "))
	# Si no se ha introducido un valor válido, se vuelve a pedir
	while (not((e == 0) or (e == 1))):
		print ("El bit para el reto debe ser 0 ó 1")
		e = int(input("Usuario B: Introduzca el bit para el reto (0/1): "))
	
	print ()
	# Si el bit 'e' introducido es 0...
	if (e == 0):
		# Se calcula la 'y'
		y = x % N
		print ("y = " + str(y))
		print ("Comprobando que " + str(y) + "^2(mod " + str(N) + ") = " + str(a) + "(mod " + str(N) + ")... ", end = "")
		# Si se cumple la condición del usuario B...
		if ((y**2)%N == a%N):
			print ("Correcto!")
		# Si no se cumple la condición del usuario B...
		else:
			# El usuario A no conoce la información pedida, por lo que se termina el bucle cambiando el valor de 'conoce'
			conoce = False
	
	# Si el bit 'e' introducido es 1...
	if (e == 1):
		# Se calcula la 'y'
		y = (x * s) % N
		print ("y = " + str(y))
		print ("Comprobando que " + str(y) + "^2(mod " + str(N) + ") = " + str(a) + "*" + str(v) + "(mod " + str(N) + ")... ", end = "")
		# Si se cumple la condición del usuario B...
		if ((y**2)%N == (a*v)%N):
			print ("Correcto!")
		# Si no se cumple la condición del usuario B...
		else:
			# El usuario A no conoce la información pedida, por lo que se termina el bucle cambiando el valor de 'conoce'
			conoce = False

print ()
print ()
if (bool(conoce)):
	print ("PERFECTO! El usuario A conoce la información.")
else:
	print ("ERROR! El usuario A NO conoce la información.")


sys.exit(0)
