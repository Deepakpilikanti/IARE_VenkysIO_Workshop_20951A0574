g_s=float(input("Enter gross salary:"))
f_d=float(input("Enter fedral deduction:"))
s_d=float(input("Enter state deduction:"))
p_p=float(input("Enter pension plan:"))
n=int(input("Enter no. of weeks:"))
t_d=((f_d+s_d+p_p)/100)*g_s
print("The Value is:", (g_s - t_d) * n)
