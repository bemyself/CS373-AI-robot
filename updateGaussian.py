def updateGau(mu1, sig1, mu2, sig2):
    mu = 1.0 * (sig2*mu1+sig1*mu2)/(sig1+sig2)
    sig = 1.0 / (1.0 / sig1 + 1.0 / sig2)
    return mu, sig

print updateGau(10., 2., 13., 2.)
