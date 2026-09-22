# Traitement de l'image

## 1. Flou gaussien

Une matrice gaussienne **5×5** est utilisée comme noyau de convolution pour appliquer un flou à l'image en niveaux de gris.

## 2. Gradient d'intensité

Les opérateurs de **Sobel** sont utilisés avec deux noyaux de convolution :

* un pour le gradient horizontal ;
* un pour le gradient vertical.

La norme du gradient est ensuite calculée pour mettre en évidence les variations d'intensité et donc les contours.

## 3. Affichage

Les résultats sont affichés avec **Matplotlib** :

* image originale ;
* image après flou gaussien ;
* norme du gradient.
