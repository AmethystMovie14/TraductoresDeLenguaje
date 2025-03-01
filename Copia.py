ACP=99
ERR=-1
idx=0
renC = 1
colC = 0
entrada = ''
tData = ''
errB = False
bImp = False
conCod = 1
tabSim  = {}
codProg = {}
# matran=[
#     #           tab  +,-
#     #           sp   *                        ==        
#     #_,let  dig nl   /     %   .    "   del  ops   >    <,   #    Sym
#     [1,     2,   0,   5,   6, ERR,   9,  11,  16,  14,  15,  12,  18],  # #0
#     [1,     1, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #1
#     [ACP,   2, ACP, ACP, ACP,   3, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #2
#     [ERR,   4, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ACP, ACP, ACP, ACP],  # #3
#     [ACP,   4, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #4
#     [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #5
#     [ACP, ACP, ACP, ACP,   7, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #6
#     [7,     7,   7,   7,   7,   7,   7,   7,   7,   7,   7, ACP,   7],  # #7
#     [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #8
#     [9,     9,   9,   9,   9,   9,  10,   9,   9,   9,   9, ACP,   9],  # #9
#     [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #10
#     [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #11
#     [ 12,  12,  12,  12,  12,  12,  12,  12,  12,  12,  12,  13,  12],  # #12
#     [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #13
#     [1,     2, ACP,   5, ACP, ERR, ACP, ERR,  17, ACP, ACP, ACP, ACP],  # #14
#     [1,     2, ACP,   5, ACP, ERR, ACP, ERR,  17, 17,  ACP, ACP, ACP],  # #15
#     [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP,  17, ACP, ACP, ACP, ACP],  # #16
#     [ACP, ACP, ACP, ERR, ACP, ERR, ACP, ERR, ACP, ACP, ACP, ACP, ACP],  # #17
#     [ACP, ACP, ACP, ACP, ACP, ERR, ACP, ERR, ACP, ACP, ACP, ACP, ACP]   # #18
# ]

matran=[
    #           tab  +,-
    #           sp   *                        ==        
    #_,let  dig nl   /     %   .    "   del  ops   >    <,   #    Sym
    [1,     2,   0,   5,   6, ERR,   9,  11,  16,  14,  15,  12,  18],  # #0
    [1,     1, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #1
    [ACP,   2, ACP, ACP, ACP,   3, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #2
    [ERR,   4, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ACP, ACP, ACP, ACP],  # #3
    [ACP,   4, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #4
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #5
    [ACP, ACP, ACP, ACP,   7, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #6
    [7,     7,   7,   7,   7,   7,   7,   7,   7,   7,   7, ACP,   7],  # #7
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #8
    [9,     9,   9,   9,   9,   9,  10,   9,   9,   9,   9, ACP,   9],  # #9
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #10
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #11
    [ 12,  12,  12,  12,  12,  12,  12,  12,  12,  12,  12,  13,  12],  # #12
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # #13
    [1,     2, ACP,   5, ACP, ERR, ACP, ERR,  17, ACP, ACP, ACP, ACP],  # #14
    [1,     2, ACP,   5, ACP, ERR, ACP, ERR,  17, 17,  ACP, ACP, ACP],  # #15
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP,  17, ACP, ACP, ACP, ACP],  # #16
    [ACP, ACP, ACP, ERR, ACP, ERR, ACP, ERR, ACP, ACP, ACP, ACP, ACP],  # #17
    [ACP, ACP, ACP, ACP, ACP, ERR, ACP, ERR, ACP, ACP, ACP, ACP, ACP]   # #18
]

opLog=['y', 'no', 'o']
cteLog=['falso', 'verdadero']
palRes=['interrumpe', 'si',  'sino',   'funcion',  
        'entera', 'decimal', 'lógica', 'alfabetica',
        'constante', 'hasta', 'hacer', 'incr', 
        'inicio', 'fin','continua', 'desde',
        'regresa', 'variable', 'que', 'mientras', 
        'lmp', 'imprime', 'lee', 'imprimeln', 'principal']

def insTabSim(key, data):
    global tabSim
    tabSim[key] = data

def insCodigo(code):
    global codProg, conCod
    codProg[conCod] = code  
    conCod += 1 

def colCar( c ):
    if c == '_' or c.isalpha(): return 0
    if c.isdigit()            : return 1
    if c in ['\n', ' ', '\t'] : return 2
    if c in ['+', '-', '*', 
                     '/', '^']: return 3
    if c == '%'               : return 4
    if c == '.'               : return 5
    if c == '"'               : return 6
    if c in ['[', ']', '{', 
             '}', ',', ';', ':', 
             '(', ')']        : return 7
    if c == '='               : return 8
    if c == '>'               : return 9
    if c == '<'               : return 10
    if c == '#'               : return 11 
    if c == ['$', '¿', '¡',
     '?', '!']                : return 12 
    return ERR

def erra(ren, col, tipE, desE):
    global errB
    print("["+str(ren)+"]["+str(col)+"]", tipE, desE)
    errB = True

def lexical():
    global idx, entrada, renC, colC
    estado = 0
    estAnt = 0
    col = 0
    lex = ''
    tok = ''
    while idx < len(entrada) and estado != ERR and estado != ACP:
        x = entrada[idx]
        if x == '\n' and estado in [0, 7, 9, 12]:
            renC += 1
            colC = 0
        elif x == '\t' and estado == 0: 
            colC += 3
        else:
            colC += 1 
        idx += 1
        col = colCar(x)
        if col >= 0 and col <= 12:
            if estado == 7:
                lex = ''
                if x == '\n':
                    estado = 8
            else:
                estado = matran[estado][col]
            if estado not in [ERR, ACP]:
                estAnt = estado
                if estado == 9 or (estado not in [7, 9, 12] and x not in [' ', '\t', '\n']):
                    lex += x

    #Clasificacion de Tokens, Lexemas
    if estado in [ACP, ERR]:
        idx -= 1
    else: estAnt = estado
    if estAnt == 3:
        tok = 'Dec'
        erra(renC, colC, "Error Lexico", "constante DECIMAL sin cerrar "+lex);
    elif estAnt == 9:
        tok = 'CtA'
        erra(renC, colC, "Error Lexico", "constante Alfabetica sin cerrar ");
    if estAnt == 12:
        tok = 'Cml' 
        erra (renC, colC, "Error Lexico", "Comentario de multiple linea sin cerrar");
    if estAnt == 1:
        tok='Ide'
        if   lex in cteLog: tok = 'CtL'
        elif lex in opLog : tok = 'OpL'
        elif lex in palRes: tok = 'Res'
    elif estAnt == 2:
        tok = 'Ent'
    elif estAnt == 4:
        tok = 'Dec'
    elif estAnt in [5, 6]:
        tok = 'OpA'
    elif estAnt == 7:
        tok = 'CdL'
    elif estAnt == 8:
        tok = 'Com'
    elif estAnt == 10:
        tok = 'CtA'
    elif estAnt == 11:
        tok = 'Del'
    elif estAnt == 13:
        tok = 'Cml'
    elif estAnt in [14, 15, 17]:
        tok = 'OpR'
    elif estAnt == 16:
        tok = 'OpS'
    elif estAnt == 18:
        tok = 'Sys'

    return tok, lex

def lexico():
    tok, lex = lexical()
    while tok in ['Com', 'Cml']:
        tok, lex = lexical()
    
    return tok, lex

def dimen(): pass

def ctes(): pass

def const():
    global toke, lexe, renC, colC, bImp, conCod

def vars(): 
    global toke, lexe, renC, colC, bImp, conCod, tData
    toke, lexe = lexico()
    tipo()
    deli = ','
    dim1 = '0'
    while deli == ',':
        deli = ';'
        nIde = lexe
        if toke != 'Ide':
            erra(renC, colC, 'Error de Sintaxis', 'se esperaba Identificador y llego ' + lexe)
        toke, lexe = lexico()
        if lexe == '[': dimen()
        if lexe == '=': 
            toke, lexe = lexico()
            if lexe == '{':
                toke, lexe = lexico()
                ctes()
                toke, lexe = lexico()
                if lexe != '}':
                    erra(renC, colC, 'Error de Sintaxis', 'se esperaba } y llego ' + lexe)
                toke, lexe = lexico()
            else:
                if not( toke in ['Ent', 'Dec', 'CtA', 'CtL']):
                    erra(renC, colC, 'Error de Sintaxis', 'se esperaba Constante y llego ' + lexe)
                toke, lexe = lexico()
        insTabSim(nIde,['V', tData, dim1, '0'])
        if lexe == ',': 
            deli = lexe
            toke, lexe = lexico()

    if lexe != ';':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ; y llego ' + lexe)
    toke, lexe = lexico()

def varconst(): 
    global toke, lexe, renC, colC, bImp, conCod
    if lexe == 'constante': const()
    elif lexe == 'variable': vars()


def eSi(): pass

def asigna(): pass

def cfunc(): pass

def udim(): pass

def termino():
    global toke, lexe, renC, colC, bImp, conCod
    if lexe == '(':
        toke, lexe = lexico()
        expr()
        if lexe != ')':
           erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) ' + lexe)
    elif toke == 'Ide': 
        nIde = lexe
        #validar udimen o llamada a llamada funcion
        insCodigo(['LOD', nIde, '0'])

    elif toke in ['Ent', 'Dec', 'CtA', 'CtL']:
        cte = lexe
        if   lexe == 'verdadero': cte = 'V'
        elif lexe == 'falso'    : cte = 'F'
        insCodigo(['LIT', cte, '0'])
        
    toke, lexe = lexico()


def signo():
    global toke, lexe, renC, colC, bImp 
    if lexe == '-':
        toke, lexe = lexico()
    termino()

def expo():
    global toke, lexe, renC, colC, bImp
    signo()

def multi():
    global toke, lexe, renC, colC, bImp
    signo()

def multi():
    global toke, lexe, renC, colC, bImp
    expo()

def oprel():
    global toke, lexe, renC, colC, bImp
    suma()

def suma():
    global toke, lexe, renC, colC, bImp
    multi()

def oprel():
    global toke, lexe, renC, colC, bImp
    suma()

def opy():
    global toke, lexe, renC, colC, bImp
    op = 'y'
    while op == 'y':
        opno()
        op = lexe    


def opno():
    global toke, lexe, renC, colC, bImp 
    if lexe == 'no':
        toke, lexe = lexico()
    oprel()

def expr():
    global toke, lexe, renC, colC, bImp
    op = 'o'
    while op == 'o':
        opy()
        op = lexe    

def imprimir():
    global toke, lexe, renC, colC, bImp
    if lexe != '(':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ( ' + lexe)
    deli = ','
    while deli == ',':
        toke, lexe = lexico()
        expr()
        if lexe == ',':
            insCodigo(['OPR', '0', '20'])
        deli = lexe       
    if lexe != ')':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) ' + lexe)
    else:
        if bImp: insCodigo(['OPR', '0', '21'])
        else: insCodigo(['OPR', '0', '20'])
    toke, lexe = lexico()

def lee():
    global toke, lexe, renC, colC, conCod
    toke, lexe = lexico()
    nIde = ''
    if lexe != '(':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ( ' + lexe)
    toke, lexe = lexico()
    if toke != "Ide":
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba Identificador ' + lexe)
    else: 
        nIde = lexe
    toke, lexe = lexico()
    if lexe == '[': udim()
    if lexe != ')':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) ' + lexe)
    insCodigo(['OPR', nIde, '19'])
    toke, lexe = lexico()
     
def comando():
    global toke, lexe, renC, colC, bImp, conCod
    if lexe in ['imprime', 'imprimeln']:
        if lexe == 'imprimeln': bImp = True
        toke, lexe = lexico()
        imprimir()
    elif lexe == 'si': eSi()
    elif lexe == 'lmp':
        insCodigo(['OPR', '0', '18'])
        toke, lexe = lexico()
    elif lexe == 'lee': lee()
    elif toke == 'Ide':
        toke, lexe = lexico()
        if lexe == '(': 
            cfunc()
        else: 
            asigna()


def estatutos(): 
    global toke, lexe, renC, colC
    delim = ';'
    while (delim == ';'):
        if lexe == ';':
            toke, lexe = lexico()
        if lexe != ';':
            comando()
        delim = lexe


def tipo():
    global toke, lexe, renC, colC, tData
    if not (lexe in ['alfabetica','decimal','entera', 'logica']): 
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba tipo: alfabetica, decimal, entera o logica y llego '+lexe)
    tData = lexe.upper()
    tData = tData[0]
    toke, lexe = lexico()

def block():
    global lexe, toke, renC, colC
    if lexe != 'inicio':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba inicio llego ' + lexe)
    toke, lexe = lexico()
    if lexe != 'fin':
        estatutos()
    if lexe != 'fin':
        erra(renC, colC, 'Error de Sintaxis', 'se esperaba fin llego ' + lexe)
    toke, lexe = lexico()

def params(): pass

def funciones():
    global toke, lexe, conCod
    toke, lexe = lexico()
    nomF = lexe
    if toke != 'Ide' and lexe != 'principal':
        tipo()
    if toke == 'Ide' or lexe == 'principal':
        if lexe == 'principal':
            insTabSim('_P',['E', 'I', str(conCod), '0'])
        toke, lexe = lexico()
        if lexe != '(':
           erra(renC, colC, 'Error de Sintaxis', 'se esperaba ( llego ' + lexe)
        toke, lexe = lexico()
        if lexe != ')': params()                   
        if lexe != ')':
           erra(renC, colC, 'Error de Sintaxis', 'se esperaba ) llego ' + lexe)
        toke, lexe = lexico()
        block()
        if nomF == 'principal':
              insCodigo(['OPR', '0', '0'])
        else: insCodigo(['OPR', '0', '1'])

def programa():
    global toke, lexe, renC, colC
    toke, lexe = lexico()
    while lexe in ['constante','variable']: 
        varconst()
    if lexe != 'funcion':
        erra(renC, colC,'Error de Sintaxis', 
             'Un programa en CPAS debe tener al menos una FUNCION' + lexe)
    else:
        while lexe == 'funcion':
            funciones()
    
        
def prgm():
    global entrada, idx, errB, tok, lex, \
           archE, renC, colC, tabSim, codProg
    archE = ''
    print(archE[len(archE)-3:])
    while (archE[len(archE)-3:] != 'icc'):
        renC = 1
        colC = 0
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

    idx = 0
    errB = False
    programa()
    
    
if __name__ == '__main__':
    prgm()
    
    if not(errB):
        print(archE, "COMPILO con Exito!!")
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
                for x , y in codProg.items():
                    aSal.write(str(x) + ' ')                    
                    aSal.write(y[0] + ' ')                    
                    aSal.write(y[1] + ', ')                    
                    aSal.write(y[2] + '\n')                    
                aSal.close()
        except FileNotFoundError:
            print(archE, 'No existe, vuelve a intentar')



# if __name__ == '__main__':
#     entrada = input('Texto a analizar [.]=Salir: ')
#     while entrada != '.':
#         idx = 0
#         print('--------------------')
#         print('Token\t\tLexema')
#         print('--------------------')
#         while (idx < len(entrada)):
#             token, lexema = lexico()
#             print(token, '\t\t', lexema)
#         entrada = input('Texto a analizar [.]=Salir: ')