import numpy as np
import copy
from TestFunc import TestFunc
# Git deneme
# DE sınıfı oluşturuluyor


class DE:

    # Default parametreler
    def __init__(self, test_func, maxit=100, npop=20, F=0.2, cp=0.2):

        self.costfunc = test_func.costfunc
        self.nvar = test_func.nvar
        self.varmin = test_func.varmin
        self.varmax = test_func.varmax
        self.selectionType = 0

        self.maxit = maxit
        self.npop = npop
        self.F = F
        self.cp = cp

    # DE çalıştırılıyor
    def run(self):
        # Boş bireyler oluşturuluyor
        individual = {}
        individual["position"] = None
        individual["cost"] = None


        # En iyi çözümü tutan dictionary
        bestsol = individual
        bestsol["cost"] = np.inf
        # İlk popülasyon rasgele oluşturuluyor
        pop = [0] * self.npop

        for i in range(self.npop):
            pop[i] = {}
            pop[i]["position"] = np.random.uniform(self.varmin, self.varmax, self.nvar)
            pop[i]["cost"] = self.costfunc(pop[i]["position"])
            # En iyi çözüm (gerekliyse) güncelleniyor
            if pop[i]["cost"] < bestsol["cost"]:
                bestsol = copy.deepcopy(pop[i])

        # maxit boyutunda dizi tanımlanıyor (en iyi çözümlerin sonuçları tutulacak)
        bestcost = np.empty(self.maxit)


        # Algoritma çalışmaya başlıyor
        for it in range(self.maxit):
            for i in range(self.npop):
                # Mutasyon işlemi için 3 adet birey seçiliyor

                x = pop[i]["position"]
                A = np.random.permutation(self.npop)
                A = np.delete(A, i)
                a = A[1]
                b = A[2]
                c = A[3]
                # Mutasyon işlemi

                y = pop[a]["position"] + self.F * (pop[b]["position"] - pop[c]["position"])
                y = self.apply_bound(y, self.varmin, self.varmax)
                # Rekombinasyon işlemi

                z = np.zeros(len(x))
                j0 = np.random.randint(len(x))
                for j in range(len(x)):
                    if j0 == j or np.random.uniform(0,1) <= self.cp:
                        z[j] = y[j]
                    else:
                        z[j] = x[j]

                newSol = {}
                newSol["position"] = z
                newSol["cost"] = self.costfunc(newSol["position"])

                if newSol["cost"] < pop[i]["cost"]:
                    pop[i] = newSol
                    if pop[i]["cost"] < bestsol["cost"]:
                        bestsol = pop[i]
            bestcost[it] = bestsol["cost"]

        # Elde edilen çıktılar döndürülüyor

        out = {}
        out["pop"] = pop
        out["bestsol"] = bestsol
        out["bestcost"] = bestcost
        print(out["bestcost"])
        return out

        # Çözümleri problem uzayında tutan metot
    def apply_bound(self, x, varmin, varmax):
        min = np.zeros(30)
        min.fill(varmin)
        max = np.zeros(30)
        max.fill(varmax)
        x = np.maximum(x, min)
        x = np.minimum(x, max)
        return x
