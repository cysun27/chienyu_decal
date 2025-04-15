import numpy as np
import matplotlib.pyplot as plt


# 1 Introduction to Matplotlib

def make_sine_wave(x, A, w):
    return A*np.sin(w*x)

x_arr = np.linspace(0, 2*np.pi, 1000)
A = [0.5, 1, 1.5, 2, 2.5]
w = [1, 2, 3, 4, 5]

plt.figure(figsize=(8, 8))

for A, w in zip(A, w):
    y = make_sine_wave(x_arr, A, w)
    plt.plot(x_arr, y, label=f'A={A}, w={w}')

plt.title('Sine Waves for Different Amplitudes and Frequencies')
plt.xlabel('Angle')
plt.ylabel('Sine')
plt.legend()
plt.grid(True)
plt.show()



# 2 Data with Pandas

import pandas as pd

df = pd.read_csv("c:/Users/chery/python_decal/chienyu_decal/stars.csv")

print(df.loc[0:4])

rows, cols = df.shape
print("Number of rows =", rows)
print("Number of columns =", cols)

print(df.dtypes)

avg_mass = df["Mass (M☉)"].sum()/ rows
print(avg_mass)


avg_temp = df["Temperature (K)"].sum()/ rows
print(avg_temp)

max_rad = df.loc[df["Radius (R☉)"].idxmax()]
star_max_rad = max_rad["Name"]
print(star_max_rad)

m_type_stars = df[df["Spectral_Type"].str.startswith("M")]
m_type_stars_num = len(m_type_stars)
print(m_type_stars_num)

df_distance = df.sort_values("Distance (ly)")
print(df.loc[0:2])

m_type_stars.to_csv("m_type_stars.csv", index = False)



# 3 Seaborn!

import seaborn as sns

penguins = sns.load_dataset("penguins")

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

sns.scatterplot(x ='bill_length_mm', y ='bill_depth_mm', data = penguins, ax=axes[0], hue = "species")
axes[0].set_title("Bill Depth vs. Bill Length by Species")
axes[0].set_xlabel("Bill Length (mm)")
axes[0].set_ylabel("Bill Depth (mm)")
axes[0].legend(title = "Species", prop={'size': 8})


sns.histplot(x = "body_mass_g", data = penguins, bins = 20)
axes[1].set_title('Distribution of Body Mass')
axes[1].set_xlabel("Body Mass (g)")
axes[1].set_ylabel("Count")


plt.show()