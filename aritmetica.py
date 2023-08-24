#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No puedo dividir entre 0")