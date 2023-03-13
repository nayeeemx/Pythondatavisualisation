import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import ImageTk,Image
from tkinter import filedialog
import os




def graph1():
   
    data = pd.read_csv('case_time_series.csv')

    Y = data.iloc[61:,1].values
    R = data.iloc[61:,3].values
    D = data.iloc[61:,5].values
    X = data.iloc[61:,0]
    plt.plot(X,Y)
   
    #graph display window
    window=tk.Toplevel()
    window.title('                                                          Graph 1')
    window=Canvas(window,width=550,height=450)
    window.pack()
    image=PhotoImage(file='C:\\PSG\\python\\graph1.PNG')
    window.create_image(100,100,anchor=NW,image=image)
    window.mainloop()


   

def graph2():
   
    data = pd.read_csv('case_time_series.csv')

    Y = data.iloc[61:,1].values
    R = data.iloc[61:,3].values
    D = data.iloc[61:,5].values
    X = data.iloc[61:,0]

    plt.figure(figsize=(25,8))

    ax = plt.axes()
    ax.grid(linewidth=0.4, color='#8f8f8f')

    ax.set_facecolor("black")
    ax.set_xlabel('\nDate',size=25,color='#4bb4f2')
    ax.set_ylabel('Number of Confirmed Cases\n',
    size=25,color='#4bb4f2')

    ax.plot(X,Y,
    color='#1F77B4',
    marker='o',
    linewidth=4,
    markersize=15,
    markeredgecolor='#035E9B')
   
    window=tk.Toplevel()
    window.title('                                                                                          Graph 2')
    window=Canvas(window,width=1200,height=450)
    window.pack()
    image=PhotoImage(file='C:\\PSG\\python\\graph2.PNG')
    window.create_image(0,0,anchor=NW,image=image)
    window.mainloop()




#3

def graph3():
   
    data = pd.read_csv('case_time_series.csv')

    Y = data.iloc[61:,1].values
    R = data.iloc[61:,3].values
    D = data.iloc[61:,5].values
    X = data.iloc[61:,0]

    plt.figure(figsize=(25,8))

    ax = plt.axes()
    ax.grid(linewidth=0.4, color='#8f8f8f')

    ax.set_facecolor("black")
    ax.set_xlabel('\nDate',size=25,color='#4bb4f2')
    ax.set_ylabel('Number of Confirmed Cases\n',
    size=25,color='#4bb4f2')

    plt.xticks(rotation='vertical',size='20',color='white')
    plt.yticks(size=20,color='white')
    plt.tick_params(size=20,color='white')

    for i,j in zip(X,Y):
        ax.annotate(str(j),xy=(i,j+100),color='white',size='13')
   
    ax.annotate('Second Lockdown 15th April',
    xy=(15.2, 860),
    xytext=(19.9,500),
    color='white',
    size='25',
    arrowprops=dict(color='white',
    linewidth=0.025))

    plt.title("COVID-19 IN : Daily Confirmed\n",
    size=50,color='#28a9ff')

    ax.plot(X,Y,
    color='#1F77B4',
    marker='o',
    linewidth=4,
    markersize=15,
    markeredgecolor='#035E9B')


    slices = [62, 142, 195]
    activities = ['Travel', 'Place Visit', 'Unknown']

    cols=['#4C8BE2','#00e061','#fe073a']
    exp = [0.2,0.02,0.02]

    plt.pie(slices,labels=activities,
    textprops=dict(size=25,color='black'),
    radius=3,
    colors=cols,
    autopct='%2.2f%%',
    explode=exp,
    shadow=True,
    startangle=90)

    plt.title('Transmission\n\n\n\n',color='#4fb4f2',size=40)
   
    window=tk.Toplevel()
    window.title('                                                    Graph 3')
    window=Canvas(window,width=550,height=450)
    window.pack()
    image=PhotoImage(file='C:\\PSG\\python\\graph3.PNG')
    window.create_image(50,50,anchor=NW,image=image)
    window.mainloop()



#4

def graph4():
   
    data = pd.read_csv('district.csv')
    data.head()

    re=data.iloc[:30,5].values
    de=data.iloc[:30,4].values
    co=data.iloc[:30,3].values
    x=list(data.iloc[:30,0])

    plt.figure(figsize=(25,10))
    ax=plt.axes()

    ax.set_facecolor('black')
    ax.grid(linewidth=0.4, color='#8f8f8f')


    plt.xticks(rotation='vertical',
    size='20',
    color='white')#ticks of X

    plt.yticks(size='20',color='white')


    ax.set_xlabel('\nDistrict',size=25,
    color='#4bb4f2')
    ax.set_ylabel('No. of cases\n',size=25,
    color='#4bb4f2')


    plt.tick_params(size=20,color='white')


    ax.set_title('Maharashtra District wise breakdown\n',
    size=50,color='#28a9ff')

    plt.bar(x,co,label='re')
    plt.bar(x,re,label='re',color='green')
    plt.bar(x,de,label='re',color='red')

    for i,j in zip(x,co):
        ax.annotate(str(int(j)),
    xy=(i,j+3),
    color='white',
    size='15')

    plt.legend(['Confirmed','Recovered','Deceased'],
    fontsize=20)
   
    window=tk.Toplevel()
    window.title('                                                                Graph 4')
    window=Canvas(window,width=650,height=450)
    window.pack()
    image=PhotoImage(file='C:\\PSG\\python\\graph4.PNG')
    window.create_image(0,0,anchor=NW,image=image)
    window.mainloop()



def graph5():
    path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-25-2020.csv'
    df = pd.read_csv(path)
    df.head()
    df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)
    df.rename(columns={'Country_Region': "Country"}, inplace=True)
    df.head()
    world = df.groupby("Country")['Confirmed','Active','Recovered','Deaths'].sum().reset_index()
    world.head()
   ### Find top 20 countries with maximum number of confirmed cases
    top_20 = world.sort_values(by=['Confirmed'], ascending=False).head(20)
    ### Generate a Barplot
    plt.figure(figsize=(12,10))
    plot = sns.barplot(top_20['Confirmed'], top_20['Country'])
    for i,(value,name) in enumerate(zip(top_20['Confirmed'],top_20['Country'])):
        plot.text(value,i-0.05,f'{value:,.0f}',size=10)
    plt.show()
   
    window=tk.Toplevel()
    window.title('                                                               Graph 5')
    window=Canvas(window,width=600,height=450)
    window.pack()
    image=PhotoImage(file='C:\\PSG\\python\\graph5.PNG')
    window.create_image(30,30,anchor=NW,image=image)
    window.mainloop()





def graph6():
    path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-25-2020.csv'
    df = pd.read_csv(path)
    df.head()
    df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)
    df.rename(columns={'Country_Region': "Country"}, inplace=True)
    df.head()
    world = df.groupby("Country")['Confirmed','Active','Recovered','Deaths'].sum().reset_index()
    world.head()
    top_5 = world.sort_values(by=['Confirmed'], ascending=False).head()

    ### Generate a Barplot
    plt.figure(figsize=(15,5))
    confirmed = sns.barplot(top_5['Confirmed'], top_5['Country'], color = 'red', label='Confirmed')
    recovered = sns.barplot(top_5['Recovered'], top_5['Country'], color = 'green', label='Recovered')
   
    ### Adding Texts for barplots
    for i,(value,name) in enumerate(zip(top_5['Confirmed'],top_5['Country'])):
      confirmed.text(value,i-0.05,f'{value:,.0f}',size=9)
    for i,(value,name) in enumerate(zip(top_5['Recovered'],top_5['Country'])):
      recovered.text(value,i-0.05,f'{value:,.0f}',size=9)
    plt.legend(loc=4)
    plt.show()
   
    window=tk.Toplevel()
    window.title('                                                                                  Graph 6')
    window=Canvas(window,width=900,height=300)
    window.pack()
    image=PhotoImage(file='C:\\PSG\\python\\graph6.PNG')
    window.create_image(0,0,anchor=NW,image=image)
    window.mainloop()


       
if __name__=='__main__':
   
    window = tk.Tk()
   
    window.title("                                                                                                                                                                            COVID DATA ANALYSIS ")
    window.geometry('700x465')
    # window.configure(bg='#edeab4')
    bg = tk.PhotoImage(file = 'C:\\PSG\\python\\bg2.PNG')
 
    # Show image using label
    label1 = Label( window, image = bg)
    label1.place(x = 0, y = 0)

   
    label = tk.Label(window,text ="                            COVID-19 (Coronavirus) has affected day to day life and slowed down the global economy to a large extent.This pandemic has affected thousands of people in many ways.The year 2020 still seems to be a nightmare.\n\n",font=("Times", 10,),bg="#e6e5d9")
    label.grid(row=40,column=1)
 
    label = tk.Label(window,text = "Here are a few graphical analysis on covid data\n\n",font=("Times", 9,),bg="#e6e5d9")
    label.grid(row=60,column=1)
   
   
   
    label = tk.Label(window, text = " GRAPH 1: Jan 30 2020 - May 13 2020(Daily) vs total cases   ",font=("Times", 9, "italic"),bg="#e6e5d9")
    label.grid(row = 100, column = 1)
    tk.Button(window, text = "view", command = graph1).grid(row = 100, column = 2)
 
   
   

    label = tk.Label(window, text = " GRAPH 2: April - May 2020 vs Confirmed cases ",font=("Times", 9, "italic"),bg="#e6e5d9")
    label.grid(row = 140, column = 1)
    tk.Button(window, text = "view", command = graph2).grid(row = 140, column = 2)
   

    label = tk.Label(window, text = " GRAPH 3: Transmission modes during initial lockdowns ",font=("Times", 9, "italic"),bg="#e6e5d9")
    label.grid(row = 180, column = 1)
    tk.Button(window, text = "view", command = graph3).grid(row = 180, column = 2)
   
   

    label = tk.Label(window, text = " GRAPH 4: District in Maharashtra vs No of cases ",font=("Times", 9, "italic"),bg="#e6e5d9")
    label.grid(row = 220, column =1)
    tk.Button(window, text = "view", command = graph4).grid(row =220, column = 2)
   
    label = tk.Label(window, text = " GRAPH 5: Confirmed cases during initial lockdowns vs Countries ",font=("Times", 9, "italic"),bg="#e6e5d9")
    label.grid(row =260, column = 1)
    tk.Button(window, text = "view", command = graph5).grid(row = 260, column = 2)
   
   

    label = tk.Label(window, text = " GRAPH 6: Confirmed and recovered cases during initial lockdowns vs Countries ",font=("Times", 9, "italic"),bg="#e6e5d9")
    label.grid(row = 300, column = 1)
    tk.Button(window, text = "view", command = graph6).grid(row =300, column = 2)
   
    window.mainloop()
