class DivisorNegativoError(Exception):
    """Excepción lanzada cuando se divide por números negativos"""
    pass

def mostrar_division_entera(dividendo, divisor):
    try:
        assert divisor >= 0, "Mandaron un número negativo"
        # El assert valida lo mismo que el raise de la excepción personalizada pero lanza AssertionError
        if divisor < 0:
            raise DivisorNegativoError("Mandaron un número negativo")
        print("Intentando hacer la división")
        resultado = dividendo // divisor
        print(f"El resultado entero de la divisón es: {resultado}")
    except TypeError:
        print('Revisar los operandos hay un dato mal cargado...')
    except ZeroDivisionError:
        print('No se puede dividir por cero...')
    except Exception as ex:
        print(f'Algo anduvo mal: {ex}')
    else:
        print("Este programa nunca falla..")
    finally:
        print('El super programa ha finalizado..')

mostrar_division_entera(2, -1)
mostrar_division_entera(2, 0)
mostrar_division_entera("1", "2")
mostrar_division_entera(1, 2)


    
