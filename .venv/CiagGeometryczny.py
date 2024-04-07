def ciag_gometryczny(n,a1=1,q=2):
    nty_wyraz= a1 * (q ** (n - 1))
    if q==1:
        suma = a1 * n
    else:
        suma = a1 * ((1 - q ** n) / (1 - q))
    print("N-ty wyraz ciagu wynosi: ", nty_wyraz)
    print("Suma ciagu geometrycznego wynosi: ", suma)
