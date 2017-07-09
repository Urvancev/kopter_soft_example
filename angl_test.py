import math as m

def Mrotate (a,b,c):
    a *= float(3.14/180)
    b *= float(3.14/180)
    c *= float(3.14/180)

    A = [ [m.cos(a)*m.cos(c) - m.sin(a)*m.cos(b)*m.sin(c),-m.cos(a)*m.sin(c) - m.sin(a)*m.cos(b)*m.cos(c),m.sin(a)*m.sin(b)],
          [m.sin(a)*m.cos(c) + m.cos(a)*m.cos(b)*m.sin(c), -m.sin(a)*m.sin(c) + m.cos(a)*m.cos(b)*m.cos(c), -m.cos(a)*m.sin(b)],
          [m.sin(b)*m.sin(c), m.sin(b)*m.cos(c), m.cos(b)]]
    return A

def Mx_per(a):
    a *= float(3.14/180)

    A = [ [1, 0, 0], [0, m.cos(a),-m.sin(a)], [0,m.sin(a),m.cos(a)]]
    return A

def My_per(a):
    a *= float(3.14/180)

    A = [ [m.cos(a), 0, m.sin(a)], [0, 1,0], [-m.sin(a),0,m.cos(a)]]
    return A

def MxV (M,V):
    R = [0,0,0]
    R[0] = M[0][0]*V[0] + M[0][1]*V[1] + M[0][2]*V[2]
    R[1] = M[1][0]*V[0] + M[1][1]*V[1] + M[1][2]*V[2]
    R[2] = M[2][0]*V[0] + M[2][1]*V[1] + M[2][2]*V[2]
    return R

def TransM (M):
    M1 = [0,0,0]

    M1[0] = [M[0][0],M[1][0],M[2][0]]
    M1[1] = [M[0][1],M[1][1],M[2][1]]
    M1[2] = [M[0][2],M[1][2],M[2][2]]
    return M1

Ang_operator = [0,50,0]

print("operator command: ",Ang_operator)

Ang_pod = [0,0,0]


#Mx = Mx_per(Ang_pod[0])
My = My_per(Ang_pod[1])

#M_por_rot = Mrotate(Ang_pod[0],Ang_pod[1],Ang_pod[2])
#M_por_rot = TransM(M_por_rot)

#Ang_operator = MxV(Mx,Ang_operator)
Ang_operator = MxV(My,Ang_operator)

print("podves: ",Ang_pod)
print("operator command: ",Ang_operator)

Ang_pod[0] += Ang_operator[0]
Ang_pod[1] += Ang_operator[1]
Ang_pod[2] += Ang_operator[2]

print("podves: ",Ang_pod)

Ang_operator = [50,0,0]

#M_por_rot = Mrotate(Ang_pod[0],Ang_pod[1],Ang_pod[2])
#Mx = Mx_per(Ang_pod[0])
My = My_per(Ang_pod[1])

#Ang_operator = MxV(Mx,Ang_operator)
Ang_operator = MxV(My,Ang_operator)

#Ang_operator = MxV(M_por_rot,Ang_operator)

print("operator command: ",Ang_operator)

Ang_pod[0] += Ang_operator[0]
Ang_pod[1] += Ang_operator[1]
Ang_pod[2] += Ang_operator[2]

print("podves: ",Ang_pod)
