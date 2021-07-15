#Media, Varianza y desviación de vectores normalziados
    #Amp
    ampMean = stats.mean(ampN)
    ampVar = stats.variance(ampN)
    ampStd = stats.stdev(ampN)

    #Pha
    phaMean = stats.mean(phaN)
    phaVar = stats.variance(phaN)
    phaStd = stats.stdev(phaN)

    # Máximos y ubiciones
    dctpicospha = {}
    dctpicosamp = {}

    for i in range(len(phaN)):
        if (i != 0) and (i != len(phaN) - 1):
            if (phaN[i] > phaN[i - 1]) and (phaN[i] > phaN[i + 1]):
                dctpicospha[i] = phaN[i]

        if (i != 0) and (i != len(ampN) - 1):
            if (ampN[i] > ampN[i - 1]) and (ampN[i] > ampN[i + 1]):
                dctpicosamp[i] = ampN[i]

    # Máximo global
    globalmaxpha = {}
    countmaxpha = 0
    for i, j in dctpicospha.items():
        if j == 1:
            print(i)
            countmaxpha += 1
            globalmaxpha[i] = j
            frecGloMaxPha = frec[i]
    
    if len(globalmaxpha) == 0:
        print("flag")
        globalmaxpha[0] = 1
        frecGloMaxPha = frec[0]


    globalmaxamp = {}
    countmaxamp = 0
    for i, j in dctpicosamp.items():
        if j == 1:
            countmaxamp += 1
            globalmaxamp[i] = j
            frecGloMaxAmp = frec[i]

    if len(globalmaxamp) == 0:
        print("flag")
        globalmaxamp[0] = 1
        frecGloMaxAmp = frec[0]

    # Mínimos y ubicaciones
    dctminimospha = {}
    dctminimosamp = {}

    for i in range(len(phaN)):
        if (i != 0) and (i != len(amp) - 1):
            if (phaN[i] < phaN[i - 1]) and (phaN[i] < phaN[i + 1]):
                dctminimospha[i] = phaN[i]

        if (i != 0) and (i != len(ampN) - 1):
            if (ampN[i] < ampN[i - 1]) and (ampN[i] < ampN[i + 1]):
                dctminimosamp[i] = ampN[i]


    # Mínimo global
    globalminpha = {}
    countminpha = 0
    minset = 1
    for i, j in dctminimospha.items():
        if j < minset:
            minset = j

    for i, j in dctminimospha.items():
        if j == minset:
            countminpha += 1
            globalminpha[i] = j
            frecGloMinPha = frec[i]

    if len(globalminpha) == 0:
        print("flag")
        globalminpha[0] = 1
        frecGloMinPha = frec[0]

    globalminamp = {}
    countminamp = 0
    minset = 1
    for i, j in dctminimosamp.items():
        if j < minset:
            minset = j

    for i, j in dctminimosamp.items():
        if j == minset:
            countminamp += 1
            globalminamp[i] = j
            frecGloMinAmp = frec[i]

    if len(globalminamp) == 0:
        print("flag")
        globalminamp[0] = 1
        frecGloMinAmp = frec[0]

    # Potencía total
    freqAmp, psdAmp = signal.welch(ampN)

    ampPow = []
    for i in range(len(freqAmp)):
        ampPow.append(freqAmp[i]*psdAmp[i])

    ampPowMean = stats.mean(ampPow)
    ampPowVar = stats.variance(ampPow)
    ampPowStd = stats.stdev(ampPow)


    freqPha, psdPha = signal.welch(phaN)

    phaPow = []
    for i in range(len(freqPha)):
        phaPow.append(freqPha[i]*psdPha[i])

    
    phaPowMean = stats.mean(phaPow)
    phaPowVar = stats.variance(phaPow)
    phaPowStd = stats.stdev(phaPow)

    # Potencias antes y después de max y min 
    # max

    if list(globalmaxpha.keys())[0] != len(ampN):
        afSigPhaMax = phaN[0:list(globalmaxpha.keys())[0]]
        bfSigPhaMax = phaN[list(globalmaxpha.keys())[0]:len(phaN)]
    if list(globalmaxamp.keys())[0] != len(ampN):
        afSigAmpMax = ampN[0:list(globalmaxamp.keys())[0]]
        bfSigAmpMax = ampN[list(globalmaxamp.keys())[0]:len(ampN)]
    if list(globalminamp.keys())[0] != len(ampN):
        afSigAmpMin = ampN[0:list(globalminamp.keys())[0]]
        bfSigAmpMin = ampN[list(globalminamp.keys())[0]:len(ampN)]
    if list(globalminpha.keys())[0] != len(ampN):
        afSigPhaMin = phaN[0:list(globalminpha.keys())[0]]
        bfSigPhaMin = phaN[list(globalminpha.keys())[0]:len(phaN)]

    if len(afSigAmpMax) != 0:
        ampAfMaxMean = stats.mean(afSigAmpMax)
        ampAfMaxVar = stats.variance(afSigAmpMax)
        ampAfMaxStd = stats.stdev(afSigAmpMax)

        frAfAmp, psdAmpAf = signal.welch(afSigAmpMax)

        afPowAmpMax = []
        for i in range(len(frAfAmp)):
            afPowAmpMax.append(frAfAmp[i]*psdAmpAf[i])
        meanPowAmpAfMax = stats.mean(afPowAmpMax)
    else:
        ampAfMaxMean = 0
        ampAfMaxVar = 0
        ampAfMaxStd = 0
        meanPowAmpAfMax = 0

    if len(bfSigAmpMax) != 0:
        ampBfMaxMean = stats.mean(bfSigAmpMax)
        ampBfMaxVar = stats.variance(bfSigAmpMax)
        ampBfMaxStd = stats.stdev(bfSigAmpMax)
        
        frBfAmp, psdAmpBf = signal.welch(bfSigAmpMax)

        bfPowAmpMax = []
        for i in range(len(frBfAmp)):
            bfPowAmpMax.append(frBfAmp[i]*psdAmpBf[i])
        meanPowAmpBfMax = stats.mean(bfPowAmpMax)
    else:
        ampBfMaxMean = 0
        ampBfMaxVar = 0
        ampBfMaxStd = 0
        meanPowAmpBfMax = 0

    if len(afSigAmpMin) != 0:
        ampAfMinMean = stats.mean(afSigAmpMin)
        ampAfMinVar = stats.variance(afSigAmpMin)
        ampAfMinStd = stats.stdev(afSigAmpMin)

        frAfAmp, psdAmpAf = signal.welch(afSigAmpMin)

        afPowAmpMin = []
        for i in range(len(frAfAmp)):
            afPowAmpMin.append(frAfAmp[i]*psdAmpAf[i])
        meanPowAmpAfMin = stats.mean(afPowAmpMin)
    else:
        ampAfMinMean = 0
        ampAfMinVar = 0
        ampAfMinStd = 0
        meanPowAmpAfMin = 0

    if len(bfSigAmpMin) != 0:
        ampBfMinMean = stats.mean(bfSigAmpMin)
        ampBfMinVar = stats.variance(bfSigAmpMin)
        ampBfMinStd = stats.stdev(bfSigAmpMin)

        frBfAmp, psdAmpBf = signal.welch(bfSigAmpMin)

        bfPowAmpMin = []
        for i in range(len(frBfAmp)):
            bfPowAmpMin.append(frBfAmp[i]*psdAmpBf[i])
        meanPowAmpBfMin = stats.mean(bfPowAmpMin)
    else:
        ampBfMinMean =  0
        ampBfMinVar = 0
        ampBfMinStd = 0
        meanPowAmpBfMin = 0

    if len(afSigPhaMax) != 0:
        phaAfMaxMean = stats.mean(afSigPhaMax)
        phaAfMaxVar = stats.variance(afSigPhaMax)
        phaAfMaxStd = stats.stdev(afSigPhaMax)

        frAfPha, psdPhaAf = signal.welch(afSigPhaMax)

        afPowPhaMax = []
        for i in range(len(frAfPha)):
            afPowPhaMax.append(frAfPha[i]*psdPhaAf[i])
        meanPowPhaAfMax = stats.mean(afPowPhaMax)
    else:
        phaAfMaxMean = 0
        phaAfMaxVar = 0
        phaAfMaxStd = 0
        meanPowPhaAfMax = 0
    
    if len(bfSigPhaMax) != 0:
        phaBfMaxMean = stats.mean(bfSigPhaMax)
        phaBfMaxVar = stats.variance(bfSigPhaMax)
        phaBfMaxStd = stats.stdev(bfSigPhaMax)

        frBfPha, psdPhaBf = signal.welch(bfSigPhaMax)

        bfPowPhaMax = []
        for i in range(len(frBfPha)):
            bfPowPhaMax.append(frBfPha[i]*psdPhaBf[i])
        meanPowPhaBfMax = stats.mean(bfPowPhaMax)
    else:
        phaBfMaxMean = 0
        phaBfMaxVar = 0
        phaBfMaxStd = 0
        meanPowPhaBfMax = 0
        
    if len(afSigPhaMin) != 0:
        phaAfMinMean = stats.mean(afSigPhaMin)
        phaAfMinVar = stats.variance(afSigPhaMin)
        phaAfMinStd = stats.stdev(afSigPhaMin)

        frAfPha, psdPhaAf = signal.welch(afSigPhaMin)

        afPowPhaMin = []
        for i in range(len(frAfPha)):
            afPowPhaMin.append(frAfPha[i]*psdPhaAf[i])
            meanPowPhaAfMin = stats.mean(afPowPhaMin)
    else:
        phaAfMinMean = 0
        phaAfMinVar = 0
        phaAfMinStd = 0
        meanPowPhaAfMin = 0
    
    if len(bfSigPhaMin) != 0:
        phaBfMinMean = stats.mean(bfSigPhaMin)
        phaBfMinVar = stats.variance(bfSigPhaMin)
        phaBfMinStd = stats.stdev(bfSigPhaMin)

        frBfPha, psdPhaBf = signal.welch(bfSigPhaMin)

        bfPowPhaMin = []
        for i in range(len(frBfPha)):
            bfPowPhaMin.append(frBfPha[i]*psdPhaBf[i])
        meanPowPhaBfMin = stats.mean(bfPowPhaMin)
    else:
        phaBfMinMean = 0
        phaBfMinVar = 0
        phaBfMinStd = 0
        meanPowPhaBfMin = 0

    #Potencia promedio por ventajas de 10, 50 y 200 Khz
    v10 = 7; # Para barrer cada 10,5 Khz
    v51 = 34; # Para barrer cada 51 Khz
    v201 = 134; # Para barrer cada 201 Khz

    p10Amp = []
    p51Amp = []
    p201Amp = []

    # Amplitud
    for i in range(0, len(ampN)-v10, v10):
        sig = ampN[i:(i+v10)]
        frSig, psdSig = signal.welch(sig)
        p10Amp.append(stats.mean(frSig)*stats.mean(psdSig))
    ampP10Mean = stats.mean(p10Amp)
    ampP10Var = stats.variance(p10Amp)
    ampP10Std = stats.stdev(p10Amp)

    sig = []
    frSig = []
    psdSig = []    
    for i in range(0, len(ampN)-v51, v51):
        sig = ampN[i:(i+v51)]
        frSig, psdSig = signal.welch(sig)
        p51Amp.append(stats.mean(frSig)*stats.mean(psdSig))
    ampP51Mean = stats.mean(p51Amp)
    ampP51Var = stats.variance(p51Amp)
    ampP51Std = stats.stdev(p51Amp)

    sig = []
    frSig = []
    psdSig = []  
    for i in range(0, len(ampN)-v201, v201):
        sig = ampN[i:(i+v201)]
        frSig, psdSig = signal.welch(sig)
        p201Amp.append(stats.mean(frSig)*stats.mean(psdSig))
    ampP201Mean = stats.mean(p201Amp)
    ampP201Var = stats.variance(p201Amp)
    ampP201Std = stats.stdev(p201Amp)

    # Fase
    p10Pha = []
    p51Pha = []
    p201Pha = []

    for i in range(0, len(phaN)-v10, v10):
        sig = phaN[i:(i+v10)]
        frSig, psdSig = signal.welch(sig)
        p10Pha.append(stats.mean(frSig)*stats.mean(psdSig))
    phaP10Mean = stats.mean(p10Pha)
    phaP10Var = stats.variance(p10Pha)
    phaP10Std = stats.stdev(p10Pha)


    sig = []
    frSig = []
    psdSig = []    
    for i in range(0, len(phaN)-v51, v51):
        sig = phaN[i:(i+v51)]
        frSig, psdSig = signal.welch(sig)
        p51Pha.append(stats.mean(frSig)*stats.mean(psdSig))
    phaP51Mean = stats.mean(p51Pha)
    phaP51Var = stats.variance(p51Pha)
    phaP51Std = stats.stdev(p51Pha)

    sig = []
    frSig = []
    psdSig = []  
    for i in range(0, len(phaN)-v201, v201):
        sig = phaN[i:(i+v201)]
        frSig, psdSig = signal.welch(sig)
        p201Pha.append(stats.mean(frSig)*stats.mean(psdSig))
    phaP201Mean = stats.mean(p201Pha)
    phaP201Var = stats.variance(p201Pha)
    phaP201Std = stats.stdev(p201Pha)

    #Potencia promedio por cuartiles
    pase = m.floor(len(ampN)/4)

    #Aplitud
    q1Amp = ampN[0:pase]
    q2Amp = ampN[(pase):(pase*2)]
    q3Amp = ampN[((pase*2)):(pase*3)]
    q4Amp = ampN[((pase*3)):(pase*4)]

    meanQ1Amp = stats.mean(q1Amp)
    meanQ2Amp = stats.mean(q2Amp)
    meanQ3Amp = stats.mean(q3Amp)
    meanQ4Amp = stats.mean(q4Amp)
    varQ1Amp = stats.variance(q1Amp)
    varQ2Amp = stats.variance(q2Amp)
    varQ3Amp = stats.variance(q3Amp)
    varQ4Amp = stats.variance(q4Amp)
    stdQ1Amp = stats.stdev(q1Amp)
    stdQ2Amp = stats.stdev(q2Amp)
    stdQ3Amp = stats.stdev(q3Amp)
    stdQ4Amp = stats.stdev(q4Amp)

    # minQ1Amp = min(q1Amp)
    # maxQ1Amp = max(q1Amp)
    # minQ2Amp = min(q2Amp)
    # maxQ2Amp = max(q2Amp)
    # minQ3Amp = min(q3Amp)
    # maxQ3Amp = max(q3Amp)
    # minQ4Amp = min(q4Amp)
    # maxQ4Amp = max(q4Amp)

    q1PowAmp = []
    q2PowAmp = []
    q3PowAmp = []
    q4PowAmp = []

    frQ1Amp, psdQ1Amp = signal.welch(q1Amp)
    frQ2Amp, psdQ2Amp = signal.welch(q2Amp)
    frQ3Amp, psdQ3Amp = signal.welch(q3Amp)
    frQ4Amp, psdQ4Amp = signal.welch(q4Amp)

    for i in range(pase):
        q1PowAmp.append(stats.mean(frQ1Amp)*stats.mean(psdQ1Amp))
        q2PowAmp.append(stats.mean(frQ2Amp)*stats.mean(psdQ2Amp))
        q3PowAmp.append(stats.mean(frQ3Amp)*stats.mean(psdQ3Amp))
        q4PowAmp.append(stats.mean(frQ4Amp)*stats.mean(psdQ4Amp))
    meanQ1PowAmp = stats.mean(q1PowAmp)
    meanQ2PowAmp = stats.mean(q2PowAmp)
    meanQ3PowAmp = stats.mean(q3PowAmp)
    meanQ4PowAmp = stats.mean(q4PowAmp)

    #Fase
    q1Pha = phaN[0:pase]
    q2Pha = phaN[(pase):(pase*2)]
    q3Pha = phaN[((pase*2)):(pase*3)]
    q4Pha = phaN[((pase*3)):(pase*4)]

    meanQ1Pha = stats.mean(q1Pha)
    meanQ2Pha = stats.mean(q2Pha)
    meanQ3Pha = stats.mean(q3Pha)
    meanQ4Pha = stats.mean(q4Pha)
    varQ1Pha = stats.variance(q1Pha)
    varQ2Pha = stats.variance(q2Pha)
    varQ3Pha = stats.variance(q3Pha)
    varQ4Pha = stats.variance(q4Pha)
    stdQ1Pha = stats.stdev(q1Pha)
    stdQ2Pha = stats.stdev(q2Pha)
    stdQ3Pha = stats.stdev(q3Pha)
    stdQ4Pha = stats.stdev(q4Pha)

    # minQ1Pha = min(q1Pha)
    # maxQ1Pha = max(q1Pha)
    # minQ2Pha = min(q2Pha)
    # maxQ2Pha = max(q2Pha)
    # minQ3Pha = min(q3Pha)
    # maxQ3Pha = max(q3Pha)
    # minQ4Pha = min(q4Pha)
    # maxQ4Pha = max(q4Pha)

    q1PowPha = []
    q2PowPha = []
    q3PowPha = []
    q4PowPha = []

    frQ1Pha, psdQ1Pha = signal.welch(q1Pha)
    frQ2Pha, psdQ2Pha = signal.welch(q2Pha)
    frQ3Pha, psdQ3Pha = signal.welch(q3Pha)
    frQ4Pha, psdQ4Pha = signal.welch(q4Pha)

    for i in range(pase):
        q1PowPha.append(stats.mean(frQ1Pha)*stats.mean(psdQ1Pha))
        q2PowPha.append(stats.mean(frQ2Pha)*stats.mean(psdQ2Pha))
        q3PowPha.append(stats.mean(frQ3Pha)*stats.mean(psdQ3Pha))
        q4PowPha.append(stats.mean(frQ4Pha)*stats.mean(psdQ4Pha))
    meanQ1PowPha = stats.mean(q1PowPha)
    meanQ2PowPha = stats.mean(q2PowPha)
    meanQ3PowPha = stats.mean(q3PowPha)
    meanQ4PowPha = stats.mean(q4PowPha)
    
    #Entropía total
    ampEntropy = entr(ampN)
    phaEntropy = entr(phaN)

    ampEntropy = list(ampEntropy)
    phaEntropy = list(phaEntropy)

    ampEntropyMean = stats.mean(ampEntropy)
    ampEntropyVar = stats.variance(ampEntropy)
    ampEntropyStd = stats.stdev(ampEntropy)

    phaEntropyMean = stats.mean(phaEntropy)
    phaEntropyVar = stats.variance(phaEntropy)
    phaEntropyStd = stats.stdev(phaEntropy)

    #Función eurler total
    ampEuler = []
    for i in range(len(ampN)):
        ampEuler.append(m.exp(ampN[i]))
    
    phaEuler = []
    for i in range(len(phaN)):
        phaEuler.append(m.exp(phaN[i]))

    ampEulerMean = stats.mean(ampEuler)
    ampEulerVar = stats.variance(ampEuler)
    ampEulerStd = stats.stdev(ampEuler)

    phaEulerMean = stats.mean(phaEuler)
    phaEulerVar = stats.variance(phaEuler)
    phaEulerStd = stats.stdev(phaEuler)
    
    # Creación de diccionarios
    ampData = {
        "ampAfMaxMean" : ampAfMaxMean,
        "ampAfMaxVar" : ampAfMaxVar,
        "ampAfMaxStd" : ampAfMaxStd,
        "ampBfMaxMean" : ampBfMaxMean,
        "ampBfMaxVar" : ampBfMaxVar,
        "ampBfMaxStd" : ampBfMaxStd,
        "ampAfMinMean" : ampAfMinMean,
        "ampAfMinVar" : ampAfMinVar,
        "ampAfMinStd" : ampAfMinStd,
        "ampBfMinMean" : ampBfMinMean,
        "ampBfMinVar" : ampBfMinVar,
        "ampBfMinStd" : ampBfMinStd,
        "ampMean" : ampMean,
        "ampStd" : ampStd,
        "ampVar" : ampVar,
        "ampPowMean" : ampPowMean,
        "ampPowStd" : ampPowStd,
        "ampPowVar" : ampPowVar,
        "ampEntropyMean": ampEntropyMean,
        "ampEntropyStd": ampEntropyStd,
        "ampEntropyVar": ampEntropyVar,
        "ampEulerMean": ampEulerMean,
        "ampEulerStd": ampEulerStd,
        "ampEulerVar": ampEulerVar,
        "meanPowAmpAfMax" : meanPowAmpAfMax,
        "meanPowAmpAfMin" : meanPowAmpAfMin,
        "meanPowAmpBfMax" : meanPowAmpBfMax,
        "meanPowAmpBfMin" : meanPowAmpBfMin,
        "ampP10Mean" : ampP10Mean,
        "ampP10Var" : ampP10Var,
        "ampP10Std" : ampP10Std,
        "ampP51Mean" : ampP51Mean,
        "ampP51Var" : ampP51Var,
        "ampP51Std" : ampP51Std,
        "ampP201Mean" : ampP201Mean,
        "ampP201Var" : ampP201Var,
        "ampP201Std" : ampP201Std,
        "frecGloMaxAmp" : frecGloMaxAmp,
        "frecGloMinAmp" : frecGloMinAmp,
        # "maxQ1Amp" : maxQ1Amp,
        # "maxQ2Amp" : maxQ2Amp,
        # "maxQ3Amp" : maxQ3Amp,
        # "maxQ4Amp" : maxQ4Amp,
        # "minQ1Amp" : minQ1Amp,
        # "minQ2Amp" : minQ2Amp,
        # "minQ3Amp" : minQ3Amp,
        # "minQ4Amp" : minQ4Amp,
        "meanQ1PowAmp" : meanQ1PowAmp,
        "meanQ2PowAmp" : meanQ2PowAmp,
        "meanQ3PowAmp" : meanQ3PowAmp,
        "meanQ4PowAmp" : meanQ4PowAmp,
        "meanQ1Amp" : meanQ1Amp,
        "meanQ2Amp" : meanQ2Amp,
        "meanQ3Amp" : meanQ3Amp,
        "meanQ4Amp" : meanQ4Amp,
        "varQ1Amp" : varQ1Amp,
        "varQ2Amp" : varQ2Amp,
        "varQ3Amp" : varQ3Amp,
        "varQ4Amp" : varQ4Amp,
        "stdQ1Amp" : stdQ1Amp,
        "stdQ2Amp" : stdQ2Amp,
        "stdQ3Amp" : stdQ3Amp,
        "stdQ4Amp" : stdQ4Amp,
        "tMean" : tMean,
        "tVar" : tVar,
        "tStd" : tStd,
        "impMean" : impMean,
        "impStd" : impStd,
        "impVar" : impVar
    }

    phaData = {
        "phaAfMaxMean" : phaAfMaxMean,
        "phaAfMaxVar" : phaAfMaxVar,
        "phaAfMaxStd" : phaAfMaxStd,
        "phaBfMaxMean" : phaBfMaxMean,
        "phaBfMaxVar" : phaBfMaxVar,
        "phaBfMaxStd" : phaBfMaxStd,
        "phaAfMinMean" : phaAfMinMean,
        "phaAfMinVar" : phaAfMinVar,
        "phaAfMinStd" : phaAfMinStd,
        "phaBfMinMean" : phaBfMinMean,
        "phaBfMinVar" : phaBfMinVar,
        "phaBfMinStd" : phaBfMinStd,
        "phaMean" : phaMean,
        "phaStd" : phaStd,
        "phaVar" : phaVar,
        "meanPowPhaAfMax" : meanPowPhaAfMax,
        "meanPowPhaAfMin" : meanPowPhaAfMin,
        "meanPowPhaBfMax" : meanPowPhaBfMax,
        "meanPowPhaBfMin" : meanPowPhaBfMin,
        "phaP10Mean" : phaP10Mean,
        "phaP10Var" : phaP10Var,
        "phaP10Std" : phaP10Std,
        "phaP51Mean" : phaP51Mean,
        "phaP51Var" : phaP51Var,
        "phaP51Std" : phaP51Std,
        "phaP201Mean" : phaP201Mean,
        "phaP201Var" : phaP201Var,
        "phaP201Std" : phaP201Std,
        "frecGloMaxPha" : frecGloMaxPha,
        "frecGloMinPha" : frecGloMinPha,
        # "maxQ1Pha" : maxQ1Pha,
        # "maxQ2Pha" : maxQ2Pha,
        # "maxQ3Pha" : maxQ3Pha,
        # "maxQ4Pha" : maxQ4Pha,
        # "minQ1Pha" : minQ1Pha,
        # "minQ2Pha" : minQ2Pha,
        # "minQ3Pha" : minQ3Pha,
        # "minQ4Pha" : minQ4Pha,
        "phaPowMean" : phaPowMean,
        "phaPowStd" : phaPowStd,
        "phaPowVar" : phaPowVar,
        "phaEntropyMean": phaEntropyMean,
        "phaEntropyStd": phaEntropyStd,
        "phaEntropyVar": phaEntropyVar,
        "phaEulerMean": phaEulerMean,
        "phaEulerStd": phaEulerStd,
        "phaEulerVar": phaEulerVar,
        "meanQ1PowPha" : meanQ1PowPha,
        "meanQ2PowPha" : meanQ2PowPha,
        "meanQ3PowPha" : meanQ3PowPha,
        "meanQ4PowPha" : meanQ4PowPha,
        "meanQ1Pha" : meanQ1Pha,
        "meanQ2Pha" : meanQ2Pha,
        "meanQ3Pha" : meanQ3Pha,
        "meanQ4Pha" : meanQ4Pha,
        "varQ1Pha" : varQ1Pha,
        "varQ2Pha" : varQ2Pha,
        "varQ3Pha" : varQ3Pha,
        "varQ4Pha" : varQ4Pha,
        "stdQ1Pha" : stdQ1Pha,
        "stdQ2Pha" : stdQ2Pha,
        "stdQ3Pha" : stdQ3Pha,
        "stdQ4Pha" : stdQ4Pha,
        "tMean" : tMean,
        "tVar" : tVar,
        "tStd" : tStd,
        "impMean" : impMean,
        "impStd" : impStd,
        "impVar" : impVar
    }

    addInfo = {
        "temp" : temp,
        "frecImp" : frecImp,
        "real" : real,
        "img" : img,
        "imp" : imp
    }

    with open("infoInToma66.json", "w") as file:
        dicjs = json.dumps(new_data, indent=4)
        file.write(dicjs)

    with open("ampToma66.json", "w") as file:
        dicjs = json.dumps(ampData, indent=4)
        file.write(dicjs)

    with open("phaToma66.json", "w") as file:
        dicjs = json.dumps(phaData, indent=4)
        file.write(dicjs)
