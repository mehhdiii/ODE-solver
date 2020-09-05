import matplotlib.pyplot as plt

def solver():
    print("enter step size: ", end = '')
    step_size = float(input())
    loop_range = int(10/step_size)
    #Enter speratble ODE's coefficients
    print("Enter ODE: dxdt = ", end = '')
    ODE_t = list(map(int, input('Enter numbers: ').split())) 
    print("enter initial condition: ", end = '')
    init_x = int(input())
    x=[]
    T = []
    dxdt = 0
    t = 0
    
   
    #using euler method to solve the given ODE
    for loop in range(0,loop_range):
        
        T.append(t)
        dxdt_temp = 0
        for index in range(len(ODE_t)):
            dxdt_temp += ((t**(len(ODE_t) - index - 1))*ODE_t[index])
            
        dxdt = dxdt_temp
        if(t == 0):
            x.append(dxdt*step_size + init_x)
        else:

            x.append(dxdt*step_size + x[len(x)-1]) 
        t+=step_size
    ODE_print = printer(ODE_t)
    plt.plot(T, x)
    plt.yscale('linear')
    plt.title(ODE_print)
    plt.show()


def printer(ODE_t):
     #for printing purposes:
    ODE_print = "ODE: dxdt = "
    for i in range(len(ODE_t)):
        if i!=len(ODE_t) -1:
            if(len(ODE_t) - i - 1!=1):
                
                ODE_print = ODE_print + str(ODE_t[i]) + "x^" + str(len(ODE_t) - i - 1) + "+"
            else:
                ODE_print = ODE_print + str(ODE_t[i]) + "x"  + "+"
        else:
            
            ODE_print+= str(ODE_t[i])
    return ODE_print
solver()