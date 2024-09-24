import random
import time

stockList = {
    246: {
        "symbol": "AAPL",
        "name": "Apple",
        "group": "NASDAQ",
        "market_cap": 2500000,  # 2.5 Million USD
        "stocks": []
    },
    235: {
        "symbol": "MSFT",
        "name": "Microsoft",
        "group": "NASDAQ",
        "market_cap": 2100000,  # 2.1 Million USD
        "stocks": []
    },
    301: {
        "symbol": "YPF",
        "name": "YPF S.A.",
        "group": "BYMA",
        "market_cap": 5000000000,  # 5 Billion USD
        "stocks": []
    },
    310: {
        "symbol": "GGAL",
        "name": "Grupo Financiero Galicia S.A.",
        "group": "BYMA",
        "market_cap": 2500000000,  # 2.5 Billion USD
        "stocks": []
    },
    303: {
        "symbol": "MELI",
        "name": "MercadoLibre Inc.",
        "group": "MERVAL",
        "market_cap": 40000000000,  # 40 Billion USD
        "stocks": []
    },
    305: {
        "symbol": "TS",
        "name": "Tenaris S.A.",
        "group": "NYSE",
        "market_cap": 15000000000,  # 15 Billion USD
        "stocks": []
    },
    308: {
        "symbol": "PAMP",
        "name": "Pampa Energía S.A.",
        "group": "BYMA",
        "market_cap": 1500000000,  # 1.5 Billion USD
        "stocks": []
    },
    218: {
        "symbol": "TM",
        "name": "Toyota Motor Corporation",
        "group": "Nikkei 225",
        "market_cap": 300000000000,  # 300 Billion USD (aproximado)
        "stocks": []
    },
    191: {
        "symbol": "SONY",
        "name": "Sony Group Corporation",
        "group": "Nikkei 225",
        "market_cap": 120000000000,  # 120 Billion USD (aproximado)
        "stocks": []
    },
    266: {
        "symbol": "KO",
        "name": "The Coca-Cola Company",
        "group": "Dow Jones",
        "market_cap": 250000000000,  # 250 Billion USD (aproximado)
        "stocks": []
    },
    217: {
        "symbol": "NVDA",
        "name": "NVIDIA Corporation",
        "group": "NASDAQ",
        "market_cap": 1100000000000,  # 1.1 Trillion USD (aproximado)
        "stocks": []
    },
    278: {
        "symbol": "STLA",
        "name": "Stellantis N.V. (Dodge)",
        "group": "NYSE",
        "market_cap": 70000000000,  # 70 Billion USD (aproximado)
        "stocks": []
    },
    331: {
        "symbol": "GLOB",
        "name": "Globant S.A.",
        "group": "MERVAL",
        "market_cap": 10000000000,  # 10 Billion USD (aproximado)
        "stocks": []
    },
    329: {
        "symbol": "BMA",
        "name": "Banco Macro S.A.",
        "group": "MERVAL",
        "market_cap": 2500000000,  # 2.5 Billion USD (aproximado)
        "stocks": []
    },
    319: {
        "symbol": "TECO2",
        "name": "Telecom Argentina S.A.",
        "group": "MERVAL",
        "market_cap": 1000000000,  # 1 Billion USD (aproximado)
        "stocks": []
    },
    252: {
        "symbol": "INTC",
        "name": "Intel Corporation",
        "group": "NASDAQ",
        "market_cap": 200000000000,  # 200 Billion USD (aproximado)
        "stocks": []
    },
    213: {
        "symbol": "PEP",
        "name": "PepsiCo, Inc.",
        "group": "NASDAQ",
        "market_cap": 250000000000,  # 250 Billion USD (aproximado)
        "stocks": []
    },
    354: {
        "symbol": "BHP",
        "name": "BHP Group",
        "group": "ASX",
        "market_cap": 200000000000,  # 200 Billion USD (aproximado)
        "stocks": []
    },
    335: {
        "symbol": "NESN",
        "name": "Nestlé S.A.",
        "group": "SIX Swiss Exchange",
        "market_cap": 350000000000,  # 350 Billion USD (aproximado)
        "stocks": []
    },
    339: {
        "symbol": "BABA",
        "name": "Alibaba Group",
        "group": "NYSE",
        "market_cap": 400000000000,  # 400 Billion USD (aproximado)
        "stocks": []
    },
    400: {
        "symbol": "DOW",
        "name": "Dow Jones Industrial Avg.",
        "group": "Stock Index",
        "market_cap": 15000000000,  
        "stocks": []
    },
    401: {
        "symbol": "SP500",
        "name": "S&P 500",
        "group": "Stock Index",
        "market_cap": 52000000000,  
        "stocks": []
    },
    403: {
        "symbol": "FTSE",
        "name": "FTSE 100",
        "group": "Stock Index",
        "market_cap": 2500000000,  
        "stocks": []
    },
    404: {
        "symbol": "NIKKEI",
        "name": "Nikkei 225",
        "group": "Stock Index",
        "market_cap": 3200000000,  
        "stocks": []
    },
}

globalFactor = random.randint(95,105)/100

def getWeekDays(totalDays):
    currTime = time.localtime()
    currentDay = currTime.tm_wday
    weekDays = 0
    while totalDays != 0:
        if(currentDay != 0):
            weekDays += 1
            totalDays -= 1
            currentDay -= 1
        else:
            totalDays -= 2
            currentDay = 4
    return weekDays

def inputPriceData(stockList,weekDaysTotal,stockId,selectedTime,returnMode):
    mu = random.randint(100,250)
    sigma = random.randint(10,30)
    stockValues = stockList[stockId]["stocks"]
    for day in range(0,weekDaysTotal,5):
        stockValues.append([random.gauss(mu, sigma) * globalFactor for i in range(5)])
    #print(random.gauss(mu, sigma)) 
    performTechnicalAnalysis(selectedTime,stockId,returnMode)
    
def calculateRsi(weeklyStockValues):
    earnings = 0
    losses = 0
    for i in range(1, len(weeklyStockValues)):
        change = weeklyStockValues[i] - weeklyStockValues[i-1]
        if change > 0:
            earnings += change
        else:
            losses += -change
            
    averageEarnings = earnings/len(weeklyStockValues)
    averageLosses = losses/len(weeklyStockValues)
    if averageLosses != 0:
        rs = averageEarnings/averageLosses
        rsi = 100 - (100 / (1 + rs))
        return rsi
    else:
        return 100
    
def calculateMovingAverage(weeklyStockValues):
    valuesSum = 0
    for i in range(len(weeklyStockValues)):
            valuesSum += weeklyStockValues[i]
    return valuesSum/len(weeklyStockValues)


def calculateWeeklyReturn(weeklyStockValues):
    openValue = weeklyStockValues[0]
    closeValue = weeklyStockValues[len(weeklyStockValues)-1]
    weeklyReturn = (closeValue - openValue) / openValue
    return weeklyReturn
        
        
def stockInfoTable(stockValues,stockReturn,movingAverages,rsiList):
    print("\n")
    print(f"{'Fecha':<11}{'Apertura':<13}{'Cierre':<11}{'Precio Promedio':<19}{'RSI':<9}{'Rendimiento':<15}{'Vela':<9}")
    print("=" * 85)
    
    for week in range(len(stockValues)):
        if stockReturn[week] > 0:
            candle = '▲'  # Subida
        elif stockReturn[week] < 0:
            candle = '▼'  # Bajada
        else:
            candle = '━'  # Estable

        print(f"Week {stockValues.index(stockValues[week])+1:<6}{stockValues[week][0]:<13.2f}{stockValues[week][len(stockValues[week])-1]:<12.2f}{movingAverages[week]:<18.2f}{rsiList[week]:<12.2f}{stockReturn[week]:<13.2f}{candle:<9}")
       
        
    print("\n\n")
    aux = input("Ingrese cualquier tecla para volver al buscador ")
    findStock('single')

def recommendedAction(stockReturn,movingAverages,rsiList):
    
    avrgReturn = sum(stockReturn) / len(stockReturn)
    avrgMovingMedia = sum(movingAverages) / len(movingAverages)
    avrgRsi = sum(rsiList) / len(rsiList)
    
    print(f"Considerando el valor promedio de ${avrgMovingMedia:<.2f}, se ha notado:")
    if avrgReturn > 0:
        print("Una tendencia alcista, lo que sugiere que el precio de la acción está aumentando en promedio.")
    elif avrgReturn < 0:
        print("Una tendencia bajista, lo que indica que el precio de la acción está disminuyendo en promedio.")
    else:
        print("El retorno promedio es cero, lo que sugiere que el precio de la acción se ha mantenido estable.")

    if avrgMovingMedia > movingAverages[-1]:  
        print("La media móvil está en aumento, indicando que los precios recientes son más altos que los anteriores.")
    else:
        print("La media móvil está en descenso, lo que indica que los precios recientes son más bajos que los anteriores.")

    if avrgRsi > 70:
        print("El RSI indica sobrecompra, lo que puede significar que el precio está inflado y podría corregirse.")
    elif avrgRsi < 30:
        print("El RSI indica sobreventa, sugiriendo que el precio podría aumentar en el futuro.")
    else:
        print("El RSI se encuentra en un rango normal, lo que sugiere que no hay condiciones extremas en el mercado.")
    print("\n")
    aux = input("Ingrese cualquier tecla para volver al buscador ")
    findStock('single')


def performTechnicalAnalysis(selectedTime,stockId,returnMode):
    
    weekDays = getWeekDays(selectedTime)
    stockValues = stockList[stockId]["stocks"]
    if weekDays <= len(stockValues) * 5 and len(stockValues) > 0:
        if returnMode != 'candleVis':
            stockReturn = []
            movingAverages = []
            rsiList = []
            for week in range(len(stockValues)):
                stockReturn.append(calculateWeeklyReturn(stockValues[week])) # Calculamos el porcentaje de perdida/ganancia de la semana
                movingAverages.append(calculateMovingAverage(stockValues[week])) # Calculamos el valor promedio de la semana
                rsiList.append(calculateRsi(stockValues[week])) # Calculamos el Indice de fuerza relativa
            if returnMode == 'recomendation':
                recommendedAction(stockReturn,movingAverages,rsiList)
            else:
                stockInfoTable(stockValues,stockReturn,movingAverages,rsiList)

        else:
            candlesVisualizer(stockValues)
    
    else:
        inputPriceData(stockList,weekDays,stockId,selectedTime,returnMode)
    

def candlesVisualizer(stockValues):
    
    maxValue = max(list(map(lambda x: max(x),stockValues)))
    minValue =  min(list(map(lambda x: min(x),stockValues)))

    chartHeight = 15 
    valueRange = maxValue - minValue
    step = valueRange / chartHeight

    print("\n")
    # Crear gráfico
    for i in range(chartHeight, -1, -1):
        linePrice = minValue + i * step
        row = f"{linePrice:>7.2f} | "
        
        stockValuesList = []
        for week in stockValues:
            for i in week:
                stockValuesList.append(i)

        for value in stockValuesList:
            if value >= linePrice:
                row += "|"  # Velas arriba del precio actual
            else:
                row += " "  # Espacios vacíos
        print(row)
        
    print("         " + "-" * len(stockValuesList))
    print("\n")
    aux = input("Ingrese cualquier tecla para volver al buscador ")
    findStock('single')

def stockActions(stockId):
    print("Que operacion le gustaria hacer?\n1. Analisis Tecnico de los datos\n2. Visualizacion de su actividad\n3. Recomendacion de compra/venta")
    selectedOption = input()
    print("\n\n")
    if selectedOption == '1':
        subOption = input("Plazo:\n1. Ultimos 30 dias\n2. Ultimos 60 dias\n3. Ultimos 120 dias\n") 
        selectedTime = 0
        if subOption == '1':
            selectedTime = 30     
        elif subOption == '2':
            selectedTime = 60     
        elif subOption == '3':
            selectedTime = 120
        if selectedTime != 0:     
            performTechnicalAnalysis(selectedTime,stockId,"technical")

    elif selectedOption == '2':
        subOption = input("Plazo:\n1. Ultimos 30 dias\n2. Ultimos 60 dias\n3. Ultimos 120 dias\n")
        selectedTime = 0
        if subOption == '1':
            selectedTime = 30     
        elif subOption == '2':
            selectedTime = 60     
        elif subOption == '3':
            selectedTime = 120
        if selectedTime != 0:     
            performTechnicalAnalysis(selectedTime,stockId,"candleVis")
    elif selectedOption == '3':
        performTechnicalAnalysis(60,stockId,"recomendation")

    else:  
        print(f"El valor {selectedOption} no es válido")



def tableVisualizer(tableContents):
    # Encabezados de la tabla
    print("\n")
    print("|" + "-" * 93 + "|")
    print(f"{'ID':<10} {'Symbol':<10} {'Nombre':<27} {'Grupo':<19} {'Capital':<25}")
    print("|" + "-" * 8 + "|" + "-" * 10 + "|" + "-" * 27 + "|" + "-" * 19 + "|" + "-" * 25 + "|")  # Línea de separación

    for stockId, stockInfo in tableContents:
        # Formatear el market_cap con puntos
        marketCapFormatted = f"{stockInfo['market_cap']:,}".replace(',', '.')
        print(f"{stockId:<10} {stockInfo['symbol']:<10} {stockInfo['name']:<27} {stockInfo['group']:<19} {marketCapFormatted:<25}")
        print("|" + "-" * 8 + "|" + "-" * 10 + "|" + "-" * 27 + "|" + "-" * 19 + "|" + "-" * 25 + "|")  # Línea de separación

    print("\n\n")

def performSearch(searchQuery):
    
    # Busqueda por id
    if(searchQuery[:1] == '#'):
        searchId = int(searchQuery[1:])
        if searchId in stockList:
            tableVisualizer([(searchId, stockList[searchId])])
        else:
            print(f"No se han encontrado resultados con el id {searchId}")
            
    # Busqueda por Grupo
    elif(searchQuery[:1] == '-'):
        groupName = searchQuery[1:]
        groupStocks = []
        for stockId in stockList:
            if stockList[stockId]["group"].lower() == groupName.lower():
                groupStocks.append((stockId, stockList[stockId]))
        if len(groupStocks) > 0:
            tableVisualizer(groupStocks)
        else:
            print(f"No se han encontrado resultados con el grupo {groupName}")
            
    # Busqueda por simbolo o nombre
    else:
        for stockId, stockInfo in stockList.items():
            if searchQuery.lower() == stockInfo["name"].lower():
                tableVisualizer([(stockId, stockInfo)])
                break
            elif searchQuery.lower() == stockInfo["symbol"].lower():
                tableVisualizer([(stockId, stockInfo)])
                break
        else: 
            print(f"No se han encontrado resultados")
            
            
def getMostValuedStocks(searchAmount):
    mostValued = list((stockInfo['market_cap'],(stockId, stockInfo)) for stockId, stockInfo in stockList.items()) 
    if len(mostValued) > 0:
        mostValued.sort(reverse=True, key=lambda x: x[0])
        mostValued = mostValued[:searchAmount]
        tableVisualizer(list(map(lambda x: x[1], mostValued)))
    else:
        print("No se han encontrado valores de capitalizacion de mercado en nuestros sistemas.")
        
def getStockIndexes(searchAmount):
        stockIndexes = []
        for stockId in stockList:
            if stockList[stockId]["group"].lower() == 'stock index':
                stockIndexes.append((stockId, stockList[stockId]))
        if len(stockIndexes) > 0:
            tableVisualizer(stockIndexes)
        else:
            print(f"No se han encontrado resultados con de Indices Bursatiles.")

def findStock(mode):
    
    if mode == 'single':
        print("Estas son las empresas de mayor valuacion en nuestro sistema:")
        getMostValuedStocks(10)
    elif mode == 'multiple':
        print("Estos son los Indices Bursatiles mas destacados:")
        getStockIndexes(5)


    print("Para buscar una Accion, escriba su ID (Empieze con #), Grupo(Empieze con -) o nombre\nSi necesita mas informacion de alguna, escriba !info + su ID, para ver las acciones mas valoradas escriba !top + cantidad que quiera.\nPara volver al anterior menu, escriba '!exit")

    while(True):
        userQuery = input("Buscar: ")
        print("\n\n")
        if "!info" in userQuery:
            stockId = userQuery.replace("!info ","")
            if stockId.isdigit():
                stockId = int(stockId)
                stockActions(stockId)
            else:
                print(f"El valor {stockId} no se encuentra bien escrito, por favor intentelo de nuevo")
        elif "!exit" in userQuery:
            break
        elif "!top" in userQuery:
            searchAmount = userQuery.replace("!top ","")
            if searchAmount.isdigit():
                searchAmount = int(searchAmount)
                getMostValuedStocks(searchAmount)
            else:
                print(f"El valor {searchAmount} no se encuentra bien escrito, por favor intentelo de nuevo")
        else: 
            performSearch(userQuery)
    
    
def startMenu():
    print("""
  ____  _                           _     _                                    _       _ _ 
 |  _ \(_)                         (_)   | |                                  (_)     | | |
 | |_) |_  ___ _ ____   _____ _ __  _  __| | ___    _   _ ___ _   _  __ _ _ __ _  ___ | | |
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \  | | | / __| | | |/ _` | '__| |/ _ \| | |
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) | | |_| \__ \ |_| | (_| | |  | | (_) |_|_|
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_|___/\__,_|\__,_|_|  |_|\___/(_|_)
""")
    while True:
        print("""
  ___      _           _                                              _  __      _ 
 / __| ___| |___ __ __(_)___ _ _  ___   _  _ _ _  __ _   ___ _ __  __(_)/_/ _ _ (_)
 \__ \/ -_) / -_) _/ _| / _ \ ' \/ -_) | || | ' \/ _` | / _ \ '_ \/ _| / _ \ ' \ _ 
 |___/\___|_\___\__\__|_\___/_||_\___|  \_,_|_||_\__,_| \___/ .__/\__|_\___/_||_(_)
                                                            |_|                    
""")
        print("|" + "=" * 3 + "|" + "=" * 20 + "|" )
        print(" 1.  Analisis unitario ")
        print("|" + "=" * 3 + "|" + "=" * 20 + "|" )
        print(" 2.  Analisis Múltiple con Indices")
        print("|" + "=" * 3 + "|" + "=" * 20 + "|" )
        print(" 3.  Salir ")

        selectedOption = input()
        print("\n\n")
        if selectedOption == '1':
            findStock('single')    
        elif selectedOption == '2':
            findStock('multiple')    
        elif selectedOption == '3':
            break
        else:  
            print(f"El valor {selectedOption} no es válido")
            
    

startMenu()