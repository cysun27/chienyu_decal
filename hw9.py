


import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import pandas as pd


# 1.1

df = pd.read_csv("c:/Users/chery/python_decal/chienyu_decal/GlobalLandTemperaturesByState.csv")

df = df[["dt", "AverageTemperature", "State"]]

df["dt"] = pd.to_datetime(df['dt'])
df = df[df["dt"].dt.year > 2000]

filtered_states = ["Wyoming", "Nebraska", "South Dakota"]
df = df[df["State"].isin(filtered_states)]

print(df.shape)

# 1.2 

df_avg_temp = df.groupby("dt")["AverageTemperature"].mean().reset_index()
df = df.drop("State", axis=1)
print(df.columns)

# 1.3

plt.plot(df_avg_temp["dt"], df_avg_temp["AverageTemperature"])

plt.xlabel("Date")
plt.ylabel("Average Temperature")
plt.title("Average Temperature Over Time")
plt.show()

# 1.4

start_date = df_avg_temp["dt"].min()
df_avg_temp["days_since_start"] = (df_avg_temp["dt"] - start_date).dt.days
print(start_date)

# 1.5, 1.6, 1.7

def temp_fit(x, A, T, t0, B):
    return A*np.cos((2*np.pi/T)*(x - t0)) + B

x = df_avg_temp["days_since_start"]
A_init = 20
T_init = 365
t0_init = 0
B_init = df_avg_temp["AverageTemperature"].mean()


pred = temp_fit(x, A_init, T_init, t0_init, B_init)

start_pars = [A_init, T_init, t0_init, B_init]
pars, cov = opt.curve_fit(temp_fit, df_avg_temp["days_since_start"], df_avg_temp["AverageTemperature"], p0 = start_pars)
[A, T, t0, B] = pars

pred = temp_fit(x, A, T, t0, B)

plt.xscale("linear")
plt.yscale("linear")
plt.plot(df_avg_temp["days_since_start"], df_avg_temp["AverageTemperature"])
# plt.scatter(df_avg_temp["days_since_start"], df_avg_temp["AverageTemperature"], label= "Data")
plt.plot(df_avg_temp["days_since_start"], pred, color="orange", label= "Fit Curve")
plt.show()

# 1.8, 1.9

std_errs = np.sqrt(np.diag(cov))

print(f"Best-fit values:")
print(f"A = {A:.6e} ± {std_errs[0]:.6e}")
print(f"T = {T:.6e} ± {std_errs[1]:.6e}")
print(f"t0 = {t0:.6e} ± {std_errs[2]:.6e}")
print(f"B = {B:.6e} ± {std_errs[3]:.6e}")
print("y =", A, "⋅cos( 2π /", T, ") ⋅(x -", t0,") +", B)

# 1.10

from astropy.table import Table

data = Table.read("c:/Users/chery/python_decal/chienyu_decal/global_SF6_MM.dat", format = "ascii")

df_SF6 = data.to_pandas()

 
df_SF6["date"] = df_SF6["SF6ottoyr"] + (df_SF6["SF6ottomon"] - 1) / 12
df_SF6 = df_SF6[["date","SF6ottoGLm", "SF6ottoGLsd"]]
print(df_SF6.columns)

plt.errorbar(df_SF6["date"], df_SF6["SF6ottoGLm"], yerr = df_SF6["SF6ottoGLsd"], fmt = 'o', markersize = 3, ecolor = 'darkblue', elinewidth = 1, capsize = 3, label = "SF₆ Global Mean with Error")

plt.xlabel("Year")
plt.ylabel("Global Mean SF₆ Concentration (ppt)")
plt.title("SF₆ Global Concentration Over Time")
plt.legend()
plt.tight_layout()
plt.show()

def sf6_fit(x, m, b):
    return m * x + b

df_clean = df_SF6[["date", "SF6ottoGLm", "SF6ottoGLsd" ]].dropna()

x = np.linspace(df_clean["date"].min(), df_clean["date"].max(), 217)
m_init = 0.0001
b_init = 100


pred = sf6_fit(x, m_init, b_init)

start_pars = [m_init, b_init]
pars, cov = opt.curve_fit(sf6_fit, df_clean["date"], df_clean["SF6ottoGLm"], p0 = start_pars)
[m, b] = pars

pred = sf6_fit(x, m, b)

plt.xscale("linear")
plt.yscale("linear")
plt.errorbar(df_SF6["date"], df_SF6["SF6ottoGLm"], yerr = df_SF6["SF6ottoGLsd"], fmt = 'o', markersize = 3, ecolor = 'darkblue', elinewidth = 1, capsize = 3, label = "SF₆ Global Mean with Error")
plt.plot(x, pred, color="orange", label= "Fit Curve")
plt.xlabel("Year")
plt.ylabel("Global Mean SF₆ Concentration (ppt)")
plt.title("SF₆ Global Concentration Over Time")
plt.legend()
plt.tight_layout()
plt.show()

std_errs = np.sqrt(np.diag(cov))
print(f"Best-fit values:")
print(f"m = {m:.6e} ± {std_errs[0]:.6e}")
print(f"b = {b:.6e} ± {std_errs[1]:.6e}")
print("y =", m, "* x +", b)

chi_squared = np.sum(((df_clean["SF6ottoGLm"] - pred) / df_clean["SF6ottoGLsd"]) ** 2)
degrees_of_freedom = df_clean['date'].count() - 2 

red_chi_squared = chi_squared / degrees_of_freedom
print(red_chi_squared)

# The linear model is not the best fit for the data based on the value of the reuced chi squared, ~12.71, which is much larger than 1.
# This indicates that the model is not capturing the trend of the data very well, or that the uncertainties are too small.