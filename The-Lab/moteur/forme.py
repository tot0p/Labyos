import pygame
import cmath

# PARTIE 1.2 : CLASSES PREDEFINIES

class Point :
    """
    Cette classe définit un point prenant deux champs x et y.
    P.x est l'abscisse du point P.
    P.y est l'ordonnée du point P.
    On écrira P=Point(10,50) pour définir le point P de coordonnées (10,50).
    """
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    # Ajout Loïc
    def __eq__(self, other) :
        """
        Rend le P1 == P2 fonctionnel
        """
        if isinstance(other, Point) :
            return self.x == other.x and self.y == other.y
        return False

    # Ajout Loïc
    def __ne__(self, other) :
        """
        Rend le P1 != P2 fonctionnel
        """
        return not self.__eq__(other)

    # Ajout Loïc
    def __str__(self) :
        """
        Permet d'écrire des points dans la console
        """
        return "("+str(self.x)+", "+str(self.y)+")"

def draw_pixel(P,C,window) :
    """
    Affiche un pixel de couleur C au point P.
    """
    P.x = int(P.x); P.y = int(P.y)
    pygame.draw.line(window.window,C,(P.x,P.y),(P.x,P.y),1)


def draw_line(P,Q,C,window) :
    """
    Trace un segment de couleur C entre les points P et Q.
    """
    P.x = int(P.x); P.y = int(P.y)
    Q.x = int(Q.x); Q.y = int(Q.y)
    pygame.draw.line(window.window,C,(P.x,P.y),(Q.x,Q.y),1)


def draw_triangle(P,Q,R,C,window) :
    """
    Trace un triangle de couleur C et de sommets P, Q et R.
    """
    P.x = int(P.x); P.y = int(P.y)
    Q.x = int(Q.x); Q.y = int(Q.y)
    R.x = int(R.x); R.y = int(R.y)
    pygame.draw.polygon(window.window,C,([P.x,P.y],[Q.x,Q.y],[R.x,R.y]),1)


def draw_fill_triangle(P,Q,R,C,window) :
    """
    Trace un triangle de couleur C et de sommets P, Q et R.
    """
    P.x = int(P.x); P.y = int(P.y)
    Q.x = int(Q.x); Q.y = int(Q.y)
    R.x = int(R.x); R.y = int(R.y)
    pygame.draw.polygon(window.window,C,([P.x,P.y],[Q.x,Q.y],[R.x,R.y]),0)


def draw_rectangle(P,l,h,C,window) :
    """
    Trace un rectangle de couleur C, de centre P, de largeur l et de hauteur h.
    """
    pygame.draw.rect(window.window,C,(int(P.x-l/2),int(P.y-h/2),int(l),int(h)),1)


def draw_fill_rectangle(P,l,h,C,window) :
    """
    Trace un rectangle plein de couleur C, de centre P, de largeur l et
    de hauteur h.
    """
    pygame.draw.rect(window.window,C,(int(P.x-l/2),int(P.y-h/2),int(l),int(h)),0)


def draw_circle(P,r,C,window) :
    """
    Trace un cercle de couleur C, de centre P et de rayon r.
    """
    P.x = int(P.x); P.y = int(P.y)
    r=int(r)
    pygame.draw.circle(window.window,C,(P.x,P.y),r,1)


def draw_fill_circle(P,r,C,window) :
    """
    Trace un cercle plein de couleur C, de centre P et de rayon r.
    """
    P.x = int(P.x); P.y = int(P.y)
    r=int(r)
    pygame.draw.circle(window.window,C,(P.x,P.y),r,0)


def draw_ellipse(P,l,h,C,window) :
    """
    Trace une ellipse de couleur C inscrite dans un rectangle de centre P,
    de largeur l et de hauteur h.
    """
    pygame.draw.ellipse(window.window,C,(int(P.x-l/2),int(P.y-h/2),int(l),int(h)),1)


def draw_fill_ellipse(P,l,h,C,window) :
    """
    Trace une ellipse pleine de couleur C inscrite dans un rectangle de
    centre P, de largeur l et de hauteur h.
    """
    pygame.draw.ellipse(window.window,C,(int(P.x-l/2),int(P.y-h/2),int(l),int(h)),0)


def draw_arc(P,l,h,start,end,C,window) :
    """
    Trace une portion d'ellipse de couleur C inscrite dans un rectangle
    de centre P, de largeur l et de hauteur h.
    Les angles start et end sont donnés en radians et sont dans [0;2*pi[.
    """
    pygame.draw.arc(window.window,C,(int(P.x-l/2),int(P.y-h/2),int(l),int(h)),start,end,1)


def draw_sector(P,r,start,end,C,window) :
    """
    Trace un secteur angulaire d'origine P, de rayon r, d'angle end-start et
    de couleur C.
    Les angles start et end sont donnés en radians et sont dans [0;2*pi[.
    """
    draw_arc(P,2*r,2*r,start,end,C)
    draw_line(P,Point(P.x+r*cos(start),P.y-r*sin(start)),C)
    draw_line(P,Point(P.x+r*cos(end),P.y-r*sin(end)),C)


def draw_fill_sector(P,r,start,end,C,window) :
    """
    Trace un secteur angulaire plein d'origine P, de rayon r,
    d'angle end-start et de couleur C.
    Les angles start et end sont donnés en radians et sont dans [0;2*pi[.
    """
    for x in range(-r,r+1):
        for y in range(-r,r+1):
            z = complex(x,y)
            arg = cmath.phase(z)
            if arg < 0:
                arg += 2*pi
            if(abs(z) <= r and start <= arg <= end):
                draw_pixel(Point(P.x+x,P.y-y),C)