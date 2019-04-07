#!/usr/bin/env python
# _*_ coding: utf-8 _*_

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def cifrar(cadena, clave):

	texto_cifrado = ''

	for letra in cadena:
		suma = alfabeto.find(letra) + clave
		modulo = int(suma) % len(alfabeto)
		texto_cifrado = texto_cifrado + str(alfabeto[modulo])

	return texto_cifrado

def decifrar(cadena, clave):

        texto_cifrado = ''

        for letra in cadena:
                suma = alfabeto.find(letra) - clave
                modulo = int(suma) % len(alfabeto)
                texto_cifrado = texto_cifrado + str(alfabeto[modulo])

        return texto_cifrado

def main():
	cadena = str(raw_input('Cadena a cifrar: ')).lower()
	n = int(raw_input('clave numerica: '))
	print cifrar(cadena,n)
        cadenac = str(raw_input('Cadena a decifrar: ')).lower()
        claven = int(raw_input('clave numerica: '))
        print decifrar(cadenac,claven)


if __name__ == '__main__' :
	main()