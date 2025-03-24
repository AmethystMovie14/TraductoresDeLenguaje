# Ezequiel Pasillas Gonzalez
from decimal import Decimal
import sys


ERR = -1

ACP = 999

idx = 0

errB = False

entrada = ''

vengoLfunc = False

si_tiene_retorno = False

asignacionLineal = False            

vengo_desde = False

vengoFuncRegresa = False

vengoLeer = False

venFuncSi = False

tok = ''

posicionAsignacion = ''

tipoVarAsignacion = ''

eitquetaFueraBloqueInterrumpe = ''

vengoAsignacion = False

huboComparacion = False

auxLog = 1

valorPosicion = ''

listPars = []

claves = []

listaAsignacion = []


lex = ''

bImp = False

reng = 1

colu = 1

pTipos = []

clase = 'I'

conEtiq = 1

contPars = 0

cteLog=['verdadero', 'falso']

palRes=['interrumpe', 'otro', 'func', 'interface', 'selecciona',
'caso', 'difiere', 'ir', 'mapa', 'estructura','fmt', 'Leer', 'Imprime'
'canal', 'sino', 'ir_a', 'paquete', 'segun', 'principal','Imprimenl',
'const', 'si' , 'rango', 'tipo', 'entero', 'decimal', 'logico',
# Nueva
'Lmp',
'alfabetica','continua', 'desde', 'importar', 'regresa', 'var']

matran = [ # Hacer una linea para cada OpL !. |, =
    #                       %                                               , :
    #                       *                                               ()
    #                       -                       >                       {}
    #_|let  digito  .       +       /       \n      <       =       "       []       |       &      !
    [1,     2,      14,     5,      6,      0,      8,      12,     10,     14,     15,     18,     20],    #00
    [1,     1,      ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP],   #01
    [ACP,   2,      3,      ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP],   #02
    [ERR,   4,      ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR],   #03
    [ACP,   4,      ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP],   #04
    [ACP,   ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP],   #05
    [ACP,   ACP,    ACP,    ACP,    7,      ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP],   #06
    [7,     7,      7,      5,      6,      ACP,    7,      7,      7,      ACP,    ACP,    ACP,    ACP],   #07
    [ACP,   ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    9,      ACP,    ACP,    ACP,    ACP,    ACP],   #08
    [ACP,   ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP],   #09
    [10,    10,     10,     10,     10,     ERR,    10,     10,     11,     10,     ACP,    ACP,    ACP],   #10
    [ACP,   ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP],   #11
    [ACP,   ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    13,     ACP,    ACP,    ACP,    ACP,    ACP],   #12
    [ACP,   ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP],   #13
    [ACP,   ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP],   #14
    [ERR,   ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    16,     ERR,    ERR],   #15
    [ERR,   ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    17,     ERR,    ERR],   #16
    [ACP,   ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP,    ACP],   #17
    [ERR,   ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,     19,    ERR],   #18
    [ERR,   ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    ERR,     17,    ERR],   #19
    [ERR,   ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    21,     ERR,    ERR,    ERR,     ERR,   ERR],   #20
    [ERR,   ERR,    ERR,    ERR,    ERR,    ERR,    ERR,    17,     ERR,    ERR,    ERR,     ERR,   ERR]   #21



]

#mapa de tipos
tiposTab = {"E=E":'', "A=A":'', "D=D":'', "L=L":'', "D=E":'',
            "E+E":'E', "E+D":'D', "E^E":'E', "E^D":'D', "D+E":'D', "D+D":'D', "A+A":'A',
            "E-E":'E', "E-D":'D', "D-E":'D', "D-D":'D',
            "E*E":'E', "E*D":'D', "D*E":'D', "D*D":'D',
            "E/E":'D', "E/D":'D', "D/E":'D', "D/D":'D',
            "E%E":'E', "-E":'E', "-D":'D',
            "L&&L":'L', "L||L":'L', "!L":'L',
            "E>E":'L', "D>E":'L', "E>D":'L', "D>D":'L',
            "E<E":'L', "D<E":'L', "E<D":'L', "D<D":'L',
            "E>=E":'L', "D>=E":'L', "E>=D":'L', "D>=D":'L',
            "E<=E":'L', "D<=E":'L', "E<=D":'L', "D<=D":'L',
            "E!=E":'L', "D!=E":'L', "E!=D":'L', "D!=D":'L', "A!=A":'L',
            "E==E":'L', "D==E":'L', "E==D":'L', "D==D":'L', "A==A":'L' }

tabSim = {}

tabVarCons = {}

dim = '0'

tamArray = 0

valores = []

nomArray = None

tabfunciones = {}

tipoFuncion = 'Void'

nomIde = ''

nomFunc = ''

progm = {}

conLin = 1

archE = ''


def insCodigo(codPL0):
    global progm, conLin
    progm[conLin] = codPL0
    conLin = conLin + 1


def regTabFunciones(key, tipoFunc, data):
    global tabfunciones
    tabfunciones[key]= tipoFunc, data

def regtabSim(key, data):
    global tabSim
    tabSim[key]=data
    
def regtabVarCons(key, data):
    global tabVarCons
    tabVarCons[key]=data

def leetabSim(key):
    global tabSim, reng, colu
    try:
        data = tabSim[key]
    except KeyError:
        erra(reng, colu,'Error de Semantica', 'Identificador NO declarado y llego', key)
        data = []

    return data

def erra(rn, cl, tipE, desE, strE):
    global errB
    errB = True
    if cl == 0: cl = 1
    print('['+str(rn)+']['+str(cl)+']', tipE, desE, strE)
    sys.exit()  

def colCar(s):
    if s.isalpha()              : return 0
    if s.isdigit()              : return 1
    if s == '.'                 : return 2
    if s in ['+', '-', '*', '%','^']: return 3
    if s == '/'                 : return 4
    if s == '\n'                : return 5
    if s in ['<', '>', '<=', '>=', '!=', '==']  : return 6
    if s == '='                 : return 7
    if s == '"'                 : return 8
    if s in ['{', '}', '(', ')',
             '[', ']', ',', ':', ';']: return 9
    if s == '|'                 : return 10
    if s == '&'                 : return 11
    if s == '!'                 : return 12
    #erra('Error Lexico', 'Simbolo No valido', s)
    return ERR

def scanner():
    global ERR, ACP, matran, idx, entrada, reng, colu
    estado = 0
    lexema = ''
    lex = ''
    tok = ''
    try:
      while idx < len(entrada) and estado != ERR and estado != ACP:        
        c = entrada[idx]
        idx = idx + 1
        while estado == 0 and c in ['\n', '\t', ' ']:                       
            c = entrada[idx]
            if c == '\n':
                reng = reng + 1
                colu = 0
            else: colu = colu + 1
            idx = idx + 1

        if estado == 0 and not(c in ['\n', '\t', ' ']):
            idx = idx - 1

        while estado == 7 and c != '\n':
            c = entrada[idx]
            idx = idx + 1

        if estado in [7] and c == '\n':
            idx = idx - 1

        if estado in [11]:
            idx = idx - 1
        if estado == 7 or estado == 0 or estado == 11:
            if c == '\n':
                reng = reng + 1
                colu = 0
            else: colu = colu + 1
            c = entrada[idx]
            idx = idx + 1
        elif c == '\n':
            reng = reng + 1
            colu = 0
        elif c != '\n': colu = colu + 1

        col = colCar( c )
        if estado == 10 and not(c in ['\n', '"']):
            col = 1
        if col >= 0 and col <= 12:
            estAnt = estado
            estado = matran[estado][col]
            if estado in [ERR, ACP]:
                idx = idx - 1
                break
            else: lexema = lexema + c
        else: break

    except:
          erra(reng, colu, 'Error Lexico', f'No se permiten mas [enter] despues de la ultima llave de cierre', idx)
      
    
    if not(estado in [ERR, ACP]): estAnt = estado
    if estAnt == 1:
        lex = lexema
        tok = "Ide"
        if   lexema in palRes: tok = 'Res'
        elif lexema in cteLog: tok = 'CtL'
    elif estAnt == 2:
        lex = lexema
        tok = 'Ent'
    elif estAnt == 4:
        lex = lexema
        tok = 'Dec'
    elif estAnt in [5, 6]:
        lex = lexema
        tok = 'OpA'
    elif estAnt == 7:
        lex = ''
        tok = 'Com'
    elif estAnt == 11:
        lex = lexema
        tok = 'CtA'
    elif estAnt == 12:
        lex = lexema
        tok = 'OpS'
    elif estAnt in [8, 9, 13]:
        lex = lexema
        tok = 'OpR'
    elif estAnt == 14:
        tok = 'Del'
        lex = lexema
    elif estAnt in [16, 19, 21]:
        tok = 'OpL'
        lex = lexema
    elif estAnt == 3:
        erra(reng, colu, 'Error Lexico',
                           'Constante decimal incompleta', lexema)
        tok = 'Dec'
        lex = lexema
    elif estAnt == 10:
        erra(reng, colu, 'Error Lexico',
                           'Constante Alfabetica SIN cerrar', lexema)
        tok = 'CtA'
        lex = lexema

    return tok, lex

def lexico():
    tok, lex = scanner()
    while tok == 'Com':
        tok, lex = scanner()

    return tok, lex

def importar():
    global tok, lex, reng, colu
    #print(tok, '\t\t', lex)
    tok, lex = lexico()
    if tok != 'CtA' and lex != '(':
       erra(reng, colu, 'Error de Sintaxis', 'Se esperaba nombre de libreria o grupo libs y llego', lex)
    if lex == '(': #gpoLibs
        tok, lex = lexico()
        while tok == 'CtA':
            tok, lex = lexico()
        if lex != ')':
            erra('Error de Sintaxis', 'Se esperaba ")" y llego', lex)

    tok, lex = lexico()
    
def convertirValores(valor):
    if valor == 'A':         
        return 'CtA'
    elif valor == 'L':         
        return 'CtL'
    elif valor == 'E': 
        return 'Ent'
    elif valor == 'D': 
        return 'Dec'
    
def convertirValoresComple(valor):
    if valor == 'CtA':         
        return 'A'
    elif valor == 'CtL':         
        return 'L'
    elif valor == 'Ent': 
        return 'E'
    elif valor == 'Dec': 
        return 'D'
    
        

def gpoctes(): 
    global tok, lex, reng, colu, tamArray , valores, tabSim, nomArray   
    tok, lex = lexico()
    counter = 1
    try:
                
        
        if nomArray not in tabSim:
            raise ValueError("No se asigno correctamente el nombre del arreglo")
        
        array = tabSim[nomArray]
        
        tipoDato = convertirValores(array[1])
                    
        while lex != '}':
            
            if counter > tamArray:                    
                    raise ValueError('Arreglo fuera de rango')
            
            while counter <= tamArray:
                if tok == 'OpA':
                    operador = lex
                    tok, lex = lexico()
                    lex = operador + lex

                if tok not in ['Ent', 'Dec', 'CtA', 'CtL']:            
                    erra(reng, colu, 'Error de Sintaxis', 'Se esperaba una constante valida (Ent, Dec, CtA, CtL) y llego', lex)
                
                if tok != tipoDato:
                    raise ValueError(f'El valor {lex} no coincide con el tipo de dato {tipoDato}')
                
                valores.append(lex)  # Se gaurada el valor
                
                tok, lex = lexico()  
                if lex == ',': 
                    tok, lex = lexico()
                elif lex != '}':
                    erra(reng, colu, 'Error de Lexico', 'Se esperaba "," o "}" y llegó', lex)

                counter = counter +1
                
                if lex == '}':                
                    counter = tamArray + 1    
                    
    except ValueError as error:
        erra(reng, colu, 'Error de Sintaxis', error, lex)            
        
    
    counter = 1
    if len(valores) < tamArray:
        valoresFaltantes = tamArray - len(valores) 
        
        while counter <= valoresFaltantes:
            valores.append(str(0))
            counter = counter +1
            
    
    
    # tok, lex = lexico()      


def dimen(): 
    global tok, lex, dim, reng, colu, tamArray
    try:
        clase = None
        tok, lex = lexico()
        tipodeIde = lex
        tipoTok = tok
        if tok == 'Ide':        
            if lex in tabVarCons:
                clase = tabVarCons[lex][0]        
                lex = tabVarCons[lex][2]        
            else:
                erra(reng, colu, 'Error de Semantica', 'Se esperaba una variable previamente declarada', lex)


        if tok != 'Ent' and not str(lex).isnumeric(): 
            erra(reng, colu, 'Error de Semantica', f'Se esperaba que la constante {tipodeIde} debe ser entera como tamaño de dimension y llego', tipoTok)

        if int(lex) > 0: 
            if clase == 'C':
                try:
                    dim = int(lex) 
                    tamArray = dim
                    dim = str(dim)
                except TypeError:
                    erra(reng, colu, 'Error de Semantica', f'Se esperaba un tipo de dato compatible pero llego', tipodeIde)
            else:
                erra(reng, colu, 'Error de Semantica', f'Se esperaba una constante pero llego una variable', tipodeIde)
        else:
            erra(reng, colu, 'Error de Semantica', 'Se esperaba una valor positivo o mayor a 0 para el array pero llego:', lex)


        tok, lex = lexico()
        if lex != ']':
            erra(reng, colu, 'Error de Lexico', 'Se esperaba "]" y llegó', lex)

        tok, lex = lexico()
    except ValueError:
        erra(reng, colu, 'Error de Semantica', 'Llego un tipo no valido', lex)


def varsconsts():
    global tok, lex, dim, clase, reng, colu, tamArray, valores, nomArray, nomIde
    
    estadimensionada = False
    
    if lex == 'var':
        clase = 'V'
    elif lex == 'const':
        clase = 'C'
    
    tok, lex = lexico()
    
    if tok != 'Ide':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba Ide y llego', lex)
    
    nomIde = lex
    tipo = 'I'
    validarTipo = 'I'
    valor = '0'    
    
    if nomIde in tabVarCons and clase != '':
         erra(reng, colu,'Error de Sintaxis',
            'Ya hay una variable registrada con el mismo nombre', lex)
    
    tok, lex = lexico()
    
    if lex == '[': 
        dimen()
        estadimensionada = True
        
    
    if not(lex in ['alfabetico', 'decimal',
                   'entero', 'logico']):
        erra(reng, colu,'Error de Sintaxis',
            'Se esperaba tipo de dato y llego', lex)
    
    elif lex == 'alfabetico': 
        tipo = 'A'
        validarTipo = 'CtA'
    elif lex == 'logico': 
        tipo = 'L'
        validarTipo = 'CtL'
    elif lex == 'entero': 
        tipo = 'E'
        validarTipo = 'Ent'
    elif lex == 'decimal': 
        tipo = 'D'
        validarTipo = 'Dec'
    
    
    
    regtabSim(nomIde, [clase, tipo, str(dim), '0'])
    
    tok, lex = lexico()
    
    if clase == 'C' and lex != '=':
        erra(reng, colu,'Error de Semantica', 'Una constante no se puede inicializar sin un valor', nomIde )             
    
    
    if estadimensionada and lex != '=':
        erra(reng, colu,'Error de Semantica', 'Una un array necestia tener valores declarados', nomIde )             
        
    if lex == '=':
        tok, lex = lexico()
        if lex == '{' and tamArray > 0: 
            # insCodigo(['LIT', tipoVar, '0'])
            # insCodigo(['STO', 0, nomIde])
            nomArray = nomIde
            gpoctes()        
            nomArray = None
        else:
            if not (tok in ['CtA', 'CtL', 'Dec', 'Ent']):
                erra(reng, colu,'Error de Sintaxis', 'Se esperaba CtA, CtL, Ent o Dec y llego', lex )
                        
            if clase in ['C', 'V']:            
                try:
                    if tok == 'CtA' and tok == validarTipo:
                        valor = str(lex)
                    elif tok == 'CtL' and tok == validarTipo: 
                        valor = bool(lex)
                    elif tok == 'Dec' and tok == validarTipo: 
                        valor = Decimal(lex)
                    elif tok == 'Ent' and tok == validarTipo: 
                        valor = int(lex)
                    else:
                        raise ValueError('No es un valido la asignación')
                except ValueError:
                    erra(reng, colu, 'Error de Semantica', f'Se esperaba un valor de tipo "{tipo}" y llego uno que no es compatible con el tipo', lex)
                
            if clase == 'C' and valor == None:
                erra(reng, colu, 'Error de Semantica', 'Se esperaba un tipo de dato valido para', nomIde)
            
       
        tok, lex = lexico()
    
    
    
    regtabVarCons(nomIde, [clase, tipo, str(valor), str(tamArray)])                        
    
        
    tipoVar = 'Var'
        
    if clase == 'C':
        tipoVar = 'Cte'
            
    # insCodigo(['LIT', str(valor), '0'])
    
    # if(tamArray > 0):
    #     insCodigo(['LIT', str(tamArray), '0'])
        
    
    # insCodigo(['STO', '0', nomIde])
       
            
            
            
    if tamArray > 0 :
        for i, valor in enumerate(valores):
            insCodigo(['LIT', str(i + 1), '0'])
            insCodigo(['LIT', str(valor), '0'])
            insCodigo(['STO', '0', nomIde])
    else:
        insCodigo(['LIT', str(valor), '0'])
        insCodigo(['STO', '0', nomIde])
        
    dim = '0'
    tamArray = 0
    valores = []
    
    
    if lex == ',': varsconsts()

def pars(): 
    global tok, lex, reng, colu, conEtiq, nomIde, conLin, nomFunc, contPars, listPars
    contPars = contPars + 1
    # etiq = "_E" + str(conEtiq)   
    # conEtiq = conEtiq + 1     
    if tok != 'Ide':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba un Ide y llego', lex)
    nomIde = lex
    tok, lex = lexico()    
    if lex not in ['alfabetico','decimal', 'entero', 'logico']:        
        erra(reng, colu,'Error de Semantica', 'Se esperaba un tipo de variable y llego', lex)
    tipo = lex.upper()

    
    regtabVarCons((nomFunc + '_' + str(contPars) + '_' + nomIde), ['R', tipo[0], '', '0'])     
    # insCodigo(['LOD', etiq, '0'])
    # insCodigo(['CAL', nomIde, '0'])                           
    
    listPars.append(nomIde)
                                   
    
    tok, lex = lexico()    
                          
    if lex == ',': 
        tok, lex = lexico()            
        pars()
        return

    lista_invertida = list(reversed(listPars))   
    for valor in lista_invertida:
        regtabSim(valor, ['R', tipo[0], '0', '0'])           
        insCodigo(['STO', '0', valor]) 
    listPars = []                      

        
def obtener_pars():
    global tok, lex, reng, colu, conEtiq, nomIde, conLin, contPars, vengoLfunc        
    parametros_func = []
    
    for k, v in tabVarCons.items():
        if k.startswith(nomIde + '_'):
            parametros_func.append(v)
    try:
      if len(parametros_func) > 0:    
        tipo = convertirValores(parametros_func[contPars][1])
        if tok == 'Ide':
            
            cantidadParams = len(parametros_func)
            for num in range(cantidadParams):
                nombreParam = nomIde + '_' + str(num + 1) + '_' + lex
                if nombreParam in tabVarCons:
                    parametro = tabVarCons[nombreParam]
                    tipoPrametro = parametro[1] 
                    tipoPrametro = convertirValores(tipoPrametro)                   
                    if tipoPrametro != tipo:
                        erra(reng, colu,'Error de Semantica', f'Se esperaba tipo de dato valido para el parametro de la funcion', (nomIde + '()'))                    
                    break
                        
        elif tok != tipo:
            erra(reng, colu,'Error de Sintaxis', f'Se esperaba tipo de dato valido para el parametro de la funcion', (nomIde + '()'))
    
        if len(parametros_func) <= 0 and lex != ')':
            erra(reng, colu,'Error de Semantica', f'La funcion {nomIde }() no esperaba el parametro', lex)
    except:
        erra(reng, colu,'Error de Semantica', f'La funcion {nomIde }() no esperaba el parametro', lex)

    
    
    if vengoLfunc == True:    
        contPars = contPars + 1
        
    
    
    

def lfunc():
    global tok, lex, reng, colu, conEtiq, nomIde, conLin, contPars   , vengoLfunc, pTipos, nomFunc
    tok, lex = lexico()        
    
    #? Obtener los parametros de la funcion 
    obtener_pars()       
    
    
    sm = lex
    nomFuncCal = nomIde
    etiq = "_E" + str(conEtiq)
    conEtiq = conEtiq + 1
    insCodigo(['LOD', etiq, '0'])
    while sm != ')':
        vengoLfunc = True         
        expr()
        sm = lex
        # ? que pasa si lo dejamos
        # pTipos.pop()
        tipo = 'A'
        if pTipos != []:
            tipo = pTipos.pop()
        if tipo not in ['E', 'D', 'L', 'A']:
            erra(reng, colu,'Error de Semantica', 'tipo en llamada de funcion NO valido', tipo)
        if lex == ',':
            tok, lex = lexico()       
    
    insCodigo(['CAL', nomFuncCal, '0'])
    regtabSim(etiq, ['I', 'I', str(conLin), '0'])
    
    nomIde = nomFuncCal
    
    contPars = 0

    tok, lex = lexico()
    
     
            
def validar_tipo_dato_retorno():
    global tok, lex, reng, colu, nomIde, vengoLfunc, vengoFuncRegresa, nomFunc, si_tiene_retorno

    tipoDato = ''
    funcLlamda = tabSim[nomFunc]    
    if tok != 'Ide':
        tipoDato = convertirValoresComple(tok) 
    elif tok == 'Ide':
        tipoDato = leetabSim(lex)   
        tipoDato = tipoDato[1]
    
    
    if  funcLlamda[1] not in  ['A','D', 'E', 'L'] and tipoDato not in ['', 'Ide']:
        erra(reng, colu,'Error de Semantica', 'El tipo de la variable no es igual al de retorno de la funcion', lex)        
    elif funcLlamda[1] in  ['A','D', 'E', 'L'] and lex in tabVarCons:        
        
            varRetorno = tabVarCons[lex]

            if varRetorno[1] != funcLlamda[1]:
                erra(reng, colu,'Error de Semantica', 'El tipo de la variable no es igual al de retorno de la funcion', lex)
    elif funcLlamda[1] in  ['A','D', 'E', 'L'] and tipoDato in ['A','D', 'E', 'L']:         
            if tipoDato != funcLlamda[1]:
                erra(reng, colu,'Error de Semantica', 'El tipo de la variable no es igual al de retorno de la funcion', lex)                             
    elif funcLlamda[1] in ['I', 'V']:
        si_tiene_retorno = False        
        if lex in tabVarCons:                        
            erra(reng, colu,'Error de Semantica', 'Una funcion void no puede regresar una variable', lex)                             
        elif tipoDato in ['A','D', 'E', 'L']:
            erra(reng, colu,'Error de Semantica', 'No se puede regresar un valor de una funcion void', lex)                             
            
        return
    else:
        erra(reng, colu,'Error de Semantica', 'La funcion no permite retornar valores', nomFunc)
        
    si_tiene_retorno = True
        
                
       
        


def termino():
    global tok, lex, reng, colu, nomIde, vengoLfunc, vengoFuncRegresa, contPars, asignacionLineal
    # if lex == ',':
    #     tok, lex = lexico()            
    if lex == '(':
        tok, lex = lexico()
        expr()
        if lex != ')':
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba ")" y llego', lex)
    elif tok in ['CtA','CtL', 'Dec', 'Ent']:        
        
        if vengoLfunc == True:
            obtener_pars()
        
        if vengoFuncRegresa  == True:
            validar_tipo_dato_retorno()
     
        
        if tok == 'CtA': pTipos.append('A')
        elif tok == 'CtL': pTipos.append('L')
        elif tok == 'Dec': pTipos.append('D')
        elif tok == 'Ent': pTipos.append('E')

        #? Cambios
        #tok # Se comento
        if tok == 'CtL':
            if lex == 'verdadero':
                cte = 'V'
            elif lex == 'falso':
                cte = 'F'

        else:
            cte = lex
        insCodigo(['LIT', cte, '0'])

    elif tok == 'Ide':
        if vengoLfunc == True:
            obtener_pars()
            
        if vengoFuncRegresa  == True:
            validar_tipo_dato_retorno()
            
        nomIde = lex
        
        tok, lex = lexico()        
        data = leetabSim(nomIde)
        if data != []:
            tipo = data[1]
        else: 
            tipo = 'I'
        pTipos.append(tipo)

        #? Cambios
        # Dim o func
        if lex == '(':
            contPars = 0            
            lfunc()
        elif lex == '[':
            asignacionLineal = False
            udim()        
        insCodigo(['LOD', nomIde, '0'])
        
        # if lex in [')', ',']:
        #     return
        
            
            
    vengoLfunc = False
    vengoFuncRegresa = False
    # tok, lex = lexico()
    if lex not in [')', ',', '+', '{', '}', 'fmt', '-', '<', '>', '<=', '>=', '!=', '==', '*', '%','^', ';'] and lex not in tabSim:
        tok, lex = lexico()
    #     termino()
    
    

def multi():
    global tok, lex, pTipos, tipoVarAsignacion, vengoAsignacion, huboComparacion
    op = '*'
    bOp = False
    
    while op in ['*', '/', '%', '^']:
        tipo = op
        op = ''
        termino()
        if bOp:
            #print('pila Tipos=', pTipos)
            bOp = False
            
            if tipo == '*': 
                code = '4'
            elif tipo == '/': 
                code = '5'
            elif tipo == '%': 
                code = '6'
            elif tipo == '^': 
                code = '7'            
                
                
                
            tipo = ''
            
            insCodigo(['OPR', '0', code])
            
            tRes = ''
            kTipo = pTipos.pop()  #tipo derecho
            kTipo = pTipos.pop() + kTipo #Sale el Op
            kTipo = pTipos.pop() + kTipo #Sal tipo Izquierdo
            try:
                tRes = tiposTab[kTipo]
            except KeyError:
                erra(reng, colu,'Error de Semantica', 'conflicto en el tipo de operador', kTipo)
                tRes = 'I'
            if tRes != '':
                
                if vengoAsignacion:
                    if tRes != tipoVarAsignacion:
                        erra(reng, colu,'Error de Semantica', f'No se puede asignar el valor de {tRes} a', tipoVarAsignacion)
                       
                huboComparacion = True 
                pTipos.append(tRes)

        if lex in ['*', '/', '%', '^']:
            op = lex
            bOp = 'True'
            pTipos.append(op)
            tok, lex = lexico()

def suma():
    global tok, lex, pTipos, reng, colu, tipoVarAsignacion, vengoAsignacion, huboComparacion
    op = '+'
    bOp = False
    while op in ['+', '-']:
        tipo = op
        op = ''
        multi()
        if bOp:
            #print('pila Tipos=', pTipos)
            bOp = False
            
            if tipo == '+': 
                code = '2'
            elif tipo == '-': 
                code = '3'
                
                
            tipo = ''
            
            insCodigo(['OPR', '0', code])
            
            tRes = ''
            kTipo = pTipos.pop()  #tipo derecho
            kTipo = pTipos.pop() + kTipo #Sale el Op
            kTipo = pTipos.pop() + kTipo #Sal tipo Izquierdo
            try:
                tRes = tiposTab[kTipo]
            except KeyError:
                erra(reng, colu,'Error de Semantica', 'conflicto en el tipo de operador', kTipo)
                tRes = 'I'
            if tRes != '':
                
                if vengoAsignacion:
                    if tRes != tipoVarAsignacion:
                        erra(reng, colu,'Error de Semantica', f'No se puede asignar el valor de {tRes} a', tipoVarAsignacion)
                
                huboComparacion = True        
                pTipos.append(tRes)

        if lex in ['+', '-']:
            op = lex
            bOp = 'True'
            pTipos.append(op)
            tok, lex = lexico()

def oprel():
    global tok, lex, tipoVarAsignacion, vengoAsignacion, huboComparacion
    bOp = False    
    op = '<'
    while op in ['<', '>', '<=', '>=', '!=', '==']:
        tipo = op        
        op = ''
        suma()        
        if bOp:
            #print('pila Tipos=', pTipos)
            bOp = False
            
            if tipo == '<': 
                code = '9'
            elif tipo == '>': 
                code = '10'
            elif tipo == '<=': 
                code = '11'
            elif tipo == '>=': 
                code = '12'
            elif tipo == '!=': 
                code = '13'
            elif tipo == '==': 
                code = '14'
                
                
            tipo = ''
            
            insCodigo(['OPR', '0', code])
            
            tRes = ''
            kTipo = pTipos.pop()  #tipo derecho
            kTipo = pTipos.pop() + kTipo #Sale el Op
            kTipo = pTipos.pop() + kTipo #Sal tipo Izquierdo
            try:
                tRes = tiposTab[kTipo]
            except KeyError:
                erra(reng, colu,'Error de Semantica', 'conflicto en el tipo de operador', kTipo)
                tRes = 'I'
            if tRes != '':
                
                if vengoAsignacion:
                    if tRes != tipoVarAsignacion:
                        erra(reng, colu,'Error de Semantica', f'No se puede asignar el valor de {tRes} a', tipoVarAsignacion)
                                            

                huboComparacion = True

                pTipos.append(tRes)
                

        if lex in ['<', '>', '<=', '>=', '!=', '==']:
            op = lex
            bOp = True                
            pTipos.append(op)
            tok, lex = lexico()

def opy():
    global tok, lex, tipoVarAsignacion, vengoAsignacion, huboComparacion
    op = 'y'
    bOp = False
    while op in ['y', '&&']:
      op = ''
      opno()
      
      if bOp:
            bOp = False    
            op = ''                                   
            huboComparacion = True
            insCodigo(['OPR', '0', '15'])                    
      
      if lex in ['y', '&&']:
            op = lex
            bOp = True      
            pTipos.append(op)                                  
            tok, lex = lexico()
            

def opno():
    global tok, lex, tipoVarAsignacion, vengoAsignacion, huboComparacion            
    op = 'no'
    bOp = False    
    while op in ['no', '!']:
      op = ''
      oprel()
      
      
      if bOp:
            bOp = False          
            op = ''                             
            huboComparacion = True
            insCodigo(['OPR', '0', '17'])                    
      
      if lex in ['no', '!']:
            op = lex
            bOp = True      
            pTipos.append(op)                                  
            tok, lex = lexico()
      
        


def expr():
    global tok, lex, tipoVarAsignacion, vengoAsignacion, huboComparacion
    op = 'o'
    bOp = False    
    while op in ['o', '||']:
        op = ''
        opy()
      
      
        if bOp:
            bOp = False          
            op = ''                 
            huboComparacion = True
            insCodigo(['OPR', '0', '16'])   
            
      
        if lex in ['o', '||']:
            op = lex
            bOp = True      
            pTipos.append(op)                                  
            tok, lex = lexico()
            
        
         

def udim():
    global tok, lex, reng, colu, nomIde, valorPosicion, vengoLeer, posicionAsignacion, asignacionLineal                
                
    
    tok, lex = lexico()
    
    if tok not in ['Ent', 'Ide'] :
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba un numero entero y llego', lex)
    
    if tok == 'Ide':
        
        valor = leetabSim(lex)
        
        if valor[1] != 'E':
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba un numero entero y llego', valor[1])        
            
        
        if asignacionLineal == False:
            insCodigo(['LOD', lex, '0'])                                    
        # insCodigo(['LIT', posicion, '0'])    
        
    else:        

        if asignacionLineal == False:
            insCodigo(['LIT', lex, '0'])
        
    posicionAsignacion = lex    
    
    tok, lex = lexico()
    
    if lex != ']':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ] y llego', lex)
        
    if vengoLeer == True:
        insCodigo(['LOD', valorPosicion, '0'])        
        insCodigo(['STO', '0', nomIde])
        tok, lex = lexico()
        
    
        
    
    

def fmtleer():
    global tok, lex, reng, colu, vengoLeer, valorPosicion
    tok, lex = lexico()
    if lex != '(':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ( y llego', lex)
    tok, lex = lexico()
    if tok != 'Ide':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba Identificador y llego', lex)
    else:
        variable = leetabSim(lex)
        
        if int(variable[2]) > 0: 
            # insCodigo(['OPR', f'aux{lex}', '19'])            
            vengoLeer = True 
            valorPosicion = lex                                    
        
        insCodigo(['OPR', lex, '19'])
    tok, lex = lexico()
    if lex == '[': udim()
    if lex != ')':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba Identificador y llego', lex)
    tok, lex = lexico()
    vengoLeer = False


def fmtimprime():
    global tok, lex, bImp, pTipos, reng, colu
    tok, lex = lexico()
    if lex != '(':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ( y llego', lex)
    tok, lex = lexico()
    sp = ','
    while sp == ',':
        tipo = 'A'
        if pTipos != []:
            tipo = pTipos.pop()
        if tipo not in ['E', 'D', 'L', 'A', 'V']:
            erra(reng, colu,'Error de Semantica', 'tipo en imprime NO valido', tipo)
        sp = ''
        expr()
        sp = lex
        if sp == ',':
            insCodigo(['OPR', '0', '20'])
            tok, lex = lexico()

    if lex != ')':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ) y llego', lex)

    cImp = '20'

    if bImp:
        cImp = '21'

    insCodigo(['OPR', '0', cImp])

    tok, lex = lexico()

def fmtlmp():
    global tok, lex, reng, colu
    tok, lex = lexico()
    if lex != '(':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ( y llego', lex)
    tok, lex = lexico()
    if lex != ')':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba Identificador y llego', lex)
    insCodigo(['OPR', '0', '18'])
    tok, lex = lexico()

def funcSiNo():
    global tok, lex, bImp, reng, colu, nomFunc, conEtiq, nomIde, conLin, venFuncSi   
                 
    tok, lex = lexico()
    
    venFuncSi = True
    
    # etiq = "_E" + str(conEtiq)
    # conEtiq = conEtiq + 1
    
    # insCodigo(['JMP', '0', etiq])        
    # regtabSim(etiq, ['I', 'I', str(conLin), '0'])       
    if lex != '{':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba { y llego', lex)
    
    bloque()    
    
    if lex != '}':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba } y llego', lex)
        
    venFuncSi = False
       

def funcSi():
    global tok, lex, bImp, reng, colu, nomFunc, conEtiq, nomIde, conLin, venFuncSi   
    tok, lex = lexico()
    
    etiq = "_E" + str(conEtiq)
    saltoEnFalso = etiq
    conEtiq = conEtiq + 1 
    
    venFuncSi = True
    
        
    expr()   
    
    # insCodigo(['LOD', etiq, '0'])    
    insCodigo(['JMC', 'F', etiq])        
    if lex != '{':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba { y llego', lex)
    
    bloque()    
    etiq = "_E" + str(conEtiq)
    conEtiq = conEtiq + 1 
    insCodigo(['JMP', '0', etiq])    
        
    regtabSim(saltoEnFalso, ['I', 'I', str(conLin), '0'])       
    
    
    
    if lex != '}':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba } y llego', lex)
    
    tok, lex = lexico()
    
    venFuncSi = False
    
    
    if lex == 'sino':
        funcSiNo()      
        tok, lex = lexico()
        
        
    regtabSim(etiq, ['I', 'I', str(conLin), '0'])       
    # etiq = "_E" + str(conEtiq)
    # conEtiq = conEtiq + 1     
        

    
def funcDesde():
    global tok, lex, bImp, reng, colu, nomFunc, conEtiq, nomIde, conLin, claves, vengo_desde, eitquetaFueraBloqueInterrumpe
    tok, lex = lexico()
    
    # dirEtiqueta = ''
    # ultiDeclaEtiqueta = ''
    # eitquetaFueraBloque = ''
    
    
             
    no_tiene_aignacion = False
    vengo_desde = True
    
    
    if lex != '{':
        claves = [k for k in tabVarCons.keys() if k.startswith(nomFunc) and k.endswith("_" + lex)]
        if lex in tabVarCons or claves:        
            asignarValores()
        else:  
            erra(reng, colu, 'Error de Sintaxis', 'Se esperaba una variable ya declarada para asignar una valor y llego', lex)
                                    
        if lex != ';':
            erra(reng, colu, 'Error de Sintaxis', 'Se esperaba ";" y llego', lex)
        
        tok, lex = lexico()
        
        
        
        etiq = "_E" + str(conEtiq)
        conEtiq = conEtiq + 1 
        
        dirEtiqueta = etiq
        
        regtabSim(dirEtiqueta, ['I', 'I', str(conLin), '0'])  
        
        
        etiq = "_E" + str(conEtiq)
        eitquetaFueraBloque = etiq
        conEtiq = conEtiq + 1
        
        expr()
        
        insCodigo(['JMC', 'F', eitquetaFueraBloque])
        
        
        etiquetabloque = "_E" + str(conEtiq)
        conEtiq = conEtiq + 1
        insCodigo(['JMP', '0', etiquetabloque])        
                

        
        if lex == ')':
            tok, lex = lexico()
            
        
        if lex != ';':
            erra(reng, colu, 'Error de Sintaxis', 'Se esperaba ";" y llego', lex)
        
        
        
        tok, lex = lexico()
        
        claves = [k for k in tabVarCons.keys() if k.startswith(nomFunc) and k.endswith("_" + lex)]
        if lex in tabVarCons or claves:
            etiq = "_E" + str(conEtiq)
            conEtiq = conEtiq + 1 
        
            ultiDeclaEtiqueta = etiq        
            regtabSim(ultiDeclaEtiqueta, ['I', 'I', str(conLin), '0'])  
            
            asignarValores()
            insCodigo(['JMP', '0', dirEtiqueta])        
            
        else:  
            erra(reng, colu, 'Error de Sintaxis', 'Se esperaba una variable ya declarada para asignar una valor y llego', lex)
    
    else:
             
        no_tiene_aignacion = True
        
        etiq = "_E" + str(conEtiq)
        conEtiq = conEtiq + 1 
        
        dirEtiqueta = etiq
        
        regtabSim(dirEtiqueta, ['I', 'I', str(conLin), '0']) 
             
        
    if lex != '{':        
        erra(reng, colu, 'Error de Sintaxis', 'Se esperaba ";" y llego', lex)

    if no_tiene_aignacion == False:
        regtabSim(etiquetabloque, ['I', 'I', str(conLin), '0'])      
        
    
    bloque()
    
    if no_tiene_aignacion == False:
        insCodigo(['JMP', '0', ultiDeclaEtiqueta])        
    else:
        insCodigo(['JMP', '0', dirEtiqueta])        
        
    
        
    if lex != '}':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba } y llego', lex)
    
    tok, lex = lexico()
    
    # insCodigo(['JMP', '0', str(dirEtiqueta)])        
    
    if no_tiene_aignacion == False:    
        regtabSim(eitquetaFueraBloque, ['I', 'I', str(conLin), '0'])
    
    if eitquetaFueraBloqueInterrumpe:
        regtabSim(eitquetaFueraBloqueInterrumpe, ['I', 'I', str(conLin), '0'])
        
    eitquetaFueraBloqueInterrumpe = ''
        
      
        
    vengo_desde = False
            
        
def guardarValor():
    global tok, lex, bImp, reng, colu, nomFunc, tipoVarAsignacion, vengoAsignacion, huboComparacion, claves, listaAsignacion, posicionAsignacion, asignacionLineal                              
            
    try:
        aux = None        
        tok, lex = lexico()  


        if tok == 'Ide':
            claves = [k for k in tabVarCons.keys() if k.startswith(nomFunc) and k.endswith("_" + lex)]
            if claves:
                aux = lex
                lex = claves[0]
            tipoVar = tabVarCons[lex]

            if aux:
                lex = aux

            tipoAsignar = tipoVar[1]
            tipoAsignar = convertirValores(tipoAsignar)
        else:
            tipoAsignar = tok                              


        if lex in tabVarCons or tok in ['CtA','CtL', 'Ent', 'Dec'] or claves: 
             expr()


        if huboComparacion != True:
            if listaAsignacion[0][1] != tipoAsignar :
                raise ValueError(f'No se puede asignar el valor de {tipoAsignar} a')            

        insCodigo(['STO', '0', listaAsignacion[0][0]])    
        listaAsignacion.pop(0) 
        if len(listaAsignacion) > 0:
            if len(listaAsignacion[0]) > 2:
                insCodigo(['LOD', listaAsignacion[0][2], '0'])    
                

            guardarValor()
    except UnboundLocalError as e: 
        erra(reng, colu, 'Error de Sintaxis', e, listaAsignacion[0][0]) 
    except ValueError as e: 
        erra(reng, colu, 'Error de Sintaxis', e, listaAsignacion[0][0]) 
    except Exception as e: 
        erra(reng, colu, 'Expresion no valida', e, listaAsignacion[0][0])      
    
           
    
                     
def asignarValores():
    global tok, lex, bImp, reng, colu, nomFunc, tipoVarAsignacion, vengoAsignacion, huboComparacion, claves, listaAsignacion, posicionAsignacion, asignacionLineal
    
    # obtener la key de la los parametros    
    if claves:
        lex = claves[0]
    var = tabVarCons[lex]
    nomVar = lex        
    try:                                  
        tipoVarAsignacion = var[1]
        vengoAsignacion = True
        huboComparacion = False
        if tipoVarAsignacion == 'A':                 
            validarTipo = 'CtA'
        elif tipoVarAsignacion == 'L':                 
            validarTipo = 'CtL'
        elif tipoVarAsignacion == 'E':                 
            validarTipo = 'Ent'
        elif tipoVarAsignacion == 'D':                 
            validarTipo = 'Dec'    
                    
        tok, lex = lexico()
        
        
        listaAsignacion.append([nomVar, validarTipo])
        
        if lex == '[':            
            udim()
            
            if lex != ']':
                erra(reng, colu,'Error de Sintaxis', 'Se esperaba ] y llego', lex) 
                
            listaAsignacion[-1] = [nomVar, validarTipo, posicionAsignacion]

                                    
            tok, lex = lexico()                                                                               
        
        if lex == '=':
            if var[0] == 'C':
                raise ValueError('No se puede cambiar el valor de una constante')            
            
            guardarValor()                        
                

            
            
                        
                
        if lex == ',':
            asignacionLineal = True 
            tok, lex = lexico() 
            asignarValores()                    
            
            
        
                                
                
        
            
            
        
            
    except UnboundLocalError as e: 
        erra(reng, colu, 'Error de Sintaxis', e, nomVar) 
    except ValueError as e: 
        erra(reng, colu, 'Error de Sintaxis', e, nomVar) 
    except Exception as e: 
        erra(reng, colu, 'Expresion no valida', e, nomVar)     
        
    vengoAsignacion = False
    huboComparacion = False
    listaAsignacion = []   
    asignacionLineal = False           


def comando():
    global tok, lex, bImp, reng, colu, nomFunc, claves, vengo_desde, eitquetaFueraBloqueInterrumpe, conEtiq
    
    # obtener la key de la los parametros
    claves = [k for k in tabVarCons.keys() if k.startswith(nomFunc) and k.endswith("_" + lex)]
    
    if lex == 'regresa':
        regresa()        
    elif lex == 'si':
        funcSi()     
    elif lex == 'desde':
        funcDesde()                 
    elif lex == 'fmt':
        tok, lex = lexico()
        if lex != '.':
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba . y llego', lex)
        tok, lex = lexico()
        if lex == 'Imprime': fmtimprime()
        elif lex == 'Imprimenl':
            bImp = True
            fmtimprime()
            bImp = False
            
        elif lex == 'Leer': fmtleer()
        elif lex == 'Lmp': fmtlmp()
        else:
            erra(reng, colu,'Error de Sintaxis','Se esperaba funcion de lib fmt [Leer, Imprime o Imprimenl] y llego', lex)
    elif lex in tabVarCons or claves:        
        asignarValores()        
    elif lex in tabfunciones:
        expr()      
    elif lex == 'interrumpe':
        if vengo_desde:
            # insCodigo(['OPR', '0', '1'])
            etiq = "_E" + str(conEtiq)
            eitquetaFueraBloqueInterrumpe = etiq
            conEtiq = conEtiq + 1
            insCodigo(['JMP', '0', str(eitquetaFueraBloqueInterrumpe)])        
            
            tok, lex = lexico()                    
            return
        else:
            erra(reng, colu,'Error de Sintaxis', 'No se permite un interrumpe fuera de un desde', lex)                         
    # elif lex == ';':
    #     tok, lex = lexico()        
    else:        
        erra(reng, colu,'Error de Sintaxis', 'Tipo no valido', lex)     
        



def estatutos():
    global tok, lex
    while lex != '}':
        comando()

def bloque():
    global tok, lex, si_tiene_retorno, nomFunc, venFuncSi, vengoFuncRegresa, vengo_desde

    tok, lex = lexico()   
    if lex != '}':
        estatutos()
        
    if (nomFunc != 'principal'):
        funcion = tabSim[nomFunc]
        if funcion[1] not in ['I', 'V']:
            if si_tiene_retorno != True and venFuncSi == False and vengo_desde == False:
                erra(reng, colu,'Error de Sintaxis', 'La funcion esperaba un retorno', nomFunc)            
                
    vengoFuncRegresa = False
    
    
            
            

def regresa():
    global tok, lex, tabSim, reng, colu, conLin, nomFunc, vengoFuncRegresa, venFuncSi
    tok, lex = lexico()    
    
    vengoFuncRegresa = True
    if lex != ')':
        expr()        
        if si_tiene_retorno != False:
            insCodigo(['STO', '0', nomFunc])
        
    insCodigo(['OPR', '0', '1'])
    
    if lex != '}':
        tok, lex = lexico()
        
    if venFuncSi:
        vengoFuncRegresa = True
         
    
    
    

def funciones():
    global tok, lex, tabSim, reng, colu, conLin, nomFunc, tipoFuncion, contPars, si_tiene_retorno
    #print('tabSim=', tabSim)
    tok, lex = lexico()

    # Cambios
    nomFunc = ''
    nomFunc = lex
    
    
    
    if nomFunc in tabfunciones:
        erra(reng, colu, 'Error', 'Ya hay una funcion con el mismo nombre', nomFunc)

    if lex != 'principal' and tok != 'Ide':
        erra(reng, colu,'Error de Sintaxis',
            'Se esperaba nombre de funcion y llego', lex)
    elif tok == 'Res' and nomFunc == 'principal':
        regtabSim("_P", [ 'I',   "I",   "1", '0'])
    else:
        regtabSim(nomFunc, [ 'I',   "I",   str(conLin), '0'])
        


    tok, lex = lexico()
    
    tipo = ''

    # tok, lex = lexico()
    if lex != '(':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ( y llego', lex)
    tok, lex = lexico()
    if lex != ')': pars()
    if lex != ')':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ) y llego', lex)
    tok, lex = lexico()
    if lex in ['alfabetico','decimal', 'entero', 'logico']:
        tipoFuncion = lex    
        may = lex.upper()
        tipo = may[0]
        if nomFunc != 'principal':
            regtabSim(nomFunc, [ 'F',   tipo,   str(conLin - contPars ), '0'])

        
        tok, lex = lexico()
    elif lex == '{':
        if nomFunc != 'principal':
            if tipo == '':
                tipo = 'V'
            regtabSim(nomFunc, [ 'F',   tipo,   str(conLin - contPars ), '0'])
        else:
            regtabSim(('_' + nomFunc), [ 'F',   'I',   str(conLin - contPars), '0'])

    if lex == '{':
        bloque()
        
        if nomFunc == 'principal':                                    
            regTabFunciones(nomFunc, 'Void', [])            
            insCodigo(['OPR', '0', '0'])
        else:            
            regTabFunciones(nomFunc, tipoFuncion, [])
            insCodigo(['OPR', '0', '1'])     

               
            
    
            
    else:
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba { y llego', lex)    
    
    tipoFuncion = 'Void'
    tok, lex = lexico()
    
    contPars = 0
    si_tiene_retorno = False
    if lex == 'func':
        funciones()
    if lex == 'funcion':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba func y llego', lex)            



def prgm():
    global entrada, idx, errB, tok, lex, archE, reng, colu
    archE = ''
    print(archE[len(archE)-3:])
    while (archE[len(archE)-3:] != 'icc'):
        archE = input('Archivo a compilar (*.icc) [.]=Salir: ')
        if archE == '.': exit(0)
        aEnt = None
        try:
            aEnt = open(archE, 'r+')
            break
        except FileNotFoundError:
            print(archE, 'No exite volver a intentar')

    if aEnt != None:
        while (linea := aEnt.readline()):
            entrada += linea
        aEnt.close()

    print('\n\n' + entrada + '\n\n')
    #while idx < len(entrada):
    idx = 0
    errB = False
    tok, lex = lexico()
        
    importaciones = False
    variables = False
    funciones_b = False
    
    while lex == 'importar':
        importar()
        importaciones = True
     
    if not(importaciones):
        print('WARNING: No realizo importaciones')              

    if lex in ['variable', 'constante']:
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ["var", "const"] y llego', lex)            

    while lex in ['var', 'const']:
        varsconsts()
        if lex in ['variable', 'constante']:
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba ["var", "const"] y llego', lex)            
        variables = True
        
    if not(variables):
        print('WARNING: No realizo declaracion de variables')              
    
    
    insCodigo(['JMP', '0', '_principal'])

    if lex == 'funcion':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba func y llego', lex)            
            
    while lex == 'func':        
        funciones()
        
        funciones_b = True
        
    if not(funciones_b):
        print('WARNING: No realizo declaracion de funciones')  
            
    if not(errB):
        print(archE, 'Compilo con EXITO!!!')

if __name__ == '__main__':
    prgm()
    if not(errB):
        archS = archE[0:len(archE)-3] + 'eje'
        try:
            # print(tabSim.items())
            with open(archS, 'w') as aSal:
                for x, y in tabSim.items():
                    aSal.write(x + ',')
                    aSal.write(y[0] + ',')
                    aSal.write(y[1] + ',')
                    aSal.write(str(y[2]) + ',')
                    aSal.write(str(y[3]) + ',')
                    aSal.write('#,\n')
                aSal.write('@\n')
                for x , y in progm.items():
                    aSal.write(str(x) + ' ')                    
                    aSal.write(y[0] + ' ')                    
                    aSal.write(y[1] + ', ')                    
                    aSal.write(y[2] + '\n')                    
                aSal.close()
        except FileNotFoundError:
            print(archE, 'No existe, vuelve a intentar')

