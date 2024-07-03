# %%
import sys
import mplcursors as mpc
import pyautogui as ptg
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
count=0
def prog(count):
    
    plt.ion

# %%
    data=pd.read_csv(r"worldometer_snapshots_April18_to_May18.csv")
    df=pd.DataFrame(data)
    df

# %%
    df.set_index("Date")
    df

# %%
    coun=ptg.prompt(text="Country Name")
    if coun==None:
        sys.exit(1)

# %%
    newd=df.loc[(df.Country == coun)]
    newd

# %%
    X=newd["Date"]
    X

# %%
    Y=newd["Total Cases"]
    Y

# %%
    plt.figure(figsize=(10,10))
    plt.title("TOTAL CASES ON EACH DAY")
    plt.ylabel("No. of Cases")
    plt.xlabel("Date")
    plt.xticks(rotation=90)
    plt.grid(axis="y")
    plt.bar(X,Y,color="#2E4053")
    plt.subplots_adjust(bottom=0.142)
    mpc.cursor(hover=True)
    plt.show()

# %%
    A=newd["Total Deaths"]
    A

# %%
    plt.figure(figsize=(10,10))
    plt.title("TOTAL DEATHS Due to Corona Virus ON EACH DAY")
    plt.ylabel("No. of Deaths")
    plt.xlabel("Date")
    plt.xticks(rotation=85)
    plt.grid(axis="y")
    plt.stem(X,A)
    plt.subplots_adjust(bottom=0.142)
    mpc.cursor(hover=True)
    plt.show()

# %%
    B=newd["Total Recovered"]
    B

# %%
    plt.figure(figsize=(10,10))
    plt.title("PERSONS RECOVERED ON EACH DAY")
    plt.ylabel("No. of Perspns")
    plt.xlabel("Date")
    plt.xticks(rotation=90)
    plt.grid(axis="y")
    plt.plot(X,B,color="purple")
    plt.subplots_adjust(bottom=0.142)
    mpc.cursor(hover=True)
    plt.show()
    
# %%
    C=newd["Active Cases"]
    C

# %%
    plt.figure(figsize=(10,10))
    plt.title("ACTIVE CASES ON EACH DAY")
    plt.ylabel("No. of Cases")
    plt.xlabel("Date")
    plt.xticks(rotation=90)
    plt.grid(axis="y")
    plt.bar(X,C,color="#1A5276")
    plt.subplots_adjust(bottom=0.142)
    mpc.cursor(hover=True)
    plt.show()

# %%
    D=newd["Total Tests"]
    D

# %%
    plt.figure(figsize=(10,10))
    plt.title("TOTAL TESTS DONE ON EACH DAY")
    plt.ylabel("No. of TESTS")
    plt.xlabel("Date")
    plt.xticks(rotation=90)
    plt.grid(axis="y")
    plt.stem(X,D,"dk")
    plt.subplots_adjust(bottom=0.142)
    mpc.cursor(hover=True)
    plt.show()
    count=count+1
    askng(count)

#%%
def askng(count):
    r=ptg.confirm(text="Do You want to search again ?",title="User Restart Choice",buttons=["Yes","No"])
    if r=="Yes":
        prog(count)
    else:
        sys.exit(1)

# %%
if count==0:
    prog(count)


    


