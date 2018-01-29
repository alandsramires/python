#!/usr/bin/python
#-*- coding: utf8 -*-
import os, getpass

def login():
	usuario = raw_input("Usuario: ")
	senha = getpass.getpass("Senha: ")
	if usuario == "t" and senha == "123":
		return "Passou"

while(True):
	os.system("clear")
	resultado = login()
	if resultado == "Passou" :
		break	

def modificar():
	print "Funcao Modificar"
	os.system("sleep 3")

while(True):
	os.system("clear")
	print "1) - modificar palavra"
	print "2) - sair"
	opcao = raw_input("Digite uma opção: ")
	if opcao == "1":
		modificar()
	elif opcao == "2":
		break
	else:
		print "Opção Inválida"
		os.system("sleep 3")	
		
#print("O usuario é: " + usuario + ". E a senha é: " + senha)
