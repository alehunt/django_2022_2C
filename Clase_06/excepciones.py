import sys

class DivisorNegativoError(Exception):
    """Excepción lanzada cuando se divide por números negativos"""
    pass


def mostrar_division_entera(dividendo, divisor):
    """
    parametros:
        dividendo: un numero entero que será divido
        divisor: el número divisor mayor a cero
    
    excepciones:
        lanzará una excepción DivisorNegativoError cuando el divisor sea negativo  
    """
    try:
        # assert divisor > 0, "Mandaron un número cero o negativo"
        # # El assert valida lo mismo que el raise de la excepción personalizada pero lanza AssertionError
        if divisor < 0:
            raise DivisorNegativoError("Mandaron un número negativo")
        print("Intentando hacer la división")
        resultado = dividendo // divisor
        print(f"El resultado entero de la divisón es: {resultado}")
    except AssertionError as assert_error:
        print(assert_error)
        print("Le erraste a un dato..")
    except TypeError:
        print('Revisar los operandos hay un dato mal cargado...')
    except ZeroDivisionError as zero:
        print('No se puede dividir por cero...')
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(exc_type)
        print(exc_value)
        print(exc_traceback)
    # except Exception as ex:
    #     print(f'Algo anduvo mal: {ex}')
    else:
        print("Este programa nunca falla..")
    finally:
        print('El super programa ha finalizado..')


mostrar_division_entera(2, -1)
mostrar_division_entera(2, 0)
mostrar_division_entera("1", "2")
mostrar_division_entera(1, 2)





