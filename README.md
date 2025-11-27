**Description**
Ce script Python calcule les racines d’un polynôme cubique dérivé de l'équation d’état cubique de Van der Waals.
Les racines correspondent aux volumes molaires possibles du fluide pour des conditions données de pression et température.
**L'Objectif**
L’équation d’état, une fois réarrangée, conduit à un polynôme du 3ème degré :  A*V**3 + B*V**2 + C*V + D = 0
Les solutions de cette équation permettent d’identifier :
un volume liquide,un volume gaz,et une racine non physique.
Ces volumes sont essentiels en thermodynamique pour comprendre les comportements de phase.
**Paramètres utilisés**
a = 0.3658 : constante de Van der Waals (attractions entre molécules)
b = 4.267×10⁻⁵ : volume propre des molécules
T = 300 K : température
R = 8.314 : constante des gaz parfaits
P = 50×10⁵ Pa : pression
Ces paramètres permettent de construire les coefficients du polynôme cubique.
**Calcul des coefficients du polynôme**
A = 1  
B = -(b+R*T/P)
C = a / P
D = a*b / P
**La fonction numpy.roots()**
numpy.roots(coefficients) est une fonction qui :
prend en entrée une liste de coefficients d’un polynôme,calcule automatiquement toutes les racines (réelles et complexes), utilise l’algorithme numérique de calcul de valeurs propres (méthode robuste et rapide).
Dans notre cas, elle renvoie les trois volumes molaires possibles, ce qui évite de résoudre l’équation cubique à la main.

