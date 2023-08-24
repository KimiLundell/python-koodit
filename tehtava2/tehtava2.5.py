leiviska = float(input("Anna leiviskät."))
naula = float(input("Anna naulat."))
luoti = float(input("Anna luodit."))

leiviskaNauloiksi = leiviska * 20
naulaLuodeiksi = naula * 32
luotiGramma = luoti * 13.3

leiviskaLuodeiksi = leiviskaNauloiksi * 32
leiviskaGramma = leiviskaLuodeiksi * 13.3
naulaGramma = naulaLuodeiksi * 13.3
grammat = luotiGramma + naulaGramma + leiviskaGramma
print(grammat)
