import cmath
import time

def Quat_pros (Q1,Q2):
    if len(Q1) == 4 and len(Q2) == 4:
        Q3 = []
        Q3.append(Q1[0] * Q2[0] - Q1[1] * Q2[1] - Q1[2] * Q2[2] - Q1[3] * Q2[3])
        Q3.append(Q1[0] * Q2[1] + Q1[1] * Q2[0] + Q1[2] * Q2[3] - Q1[3] * Q2[2])
        Q3.append(Q1[0] * Q2[2] - Q1[1] * Q2[3] + Q1[2] * Q2[0] + Q1[3] * Q2[1])
        Q3.append(Q1[0] * Q2[3] + Q1[1] * Q2[2] - Q1[2] * Q2[1] + Q1[3] * Q2[0])
        return Q3
    else:
        return 0

def Vect_norm (V):
    if len(V) >= 1:
        Mod = 0
        for i in range(len(V)):
            Mod += V[i]*V[i]
        Mod = pow(Mod,1/2)
        for i in range(len(V)):
            V[i] = (V[i]/Mod)
        return V

H1 = [0.7071,0,0.7071,0]
H2 = [0,1,0,0]
H1r = [H1[0],-H1[1],-H1[2],-H1[3]]

print (H1,H1r,H2)

H3 = Quat_pros(H1,H2)
H3 = Quat_pros(H3,H1r)

V = [0 , 0, -9.8]
V = Vect_norm(V)

print (H3)


