def katta_harf(matn):
    return matn.upper()

def teskari(matn):
    return matn[::-1]

def sozlar_soni(matn):
    return len(matn.split())

# iwlatiw

import matn_utils

matn = "Salom Python bilan ishlash"
print(matn_utils.katta_harf(matn))
print(matn_utils.teskari(matn))
print(matn_utils.sozlar_soni(matn))
