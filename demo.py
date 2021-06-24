# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:37:23 2021

@author: bruno
"""

import tkinter as tk
import math

class Test():
    def __init__(self):
        
        self.constants = []
        
        self.formula = 0
        
        self.root = tk.Tk()
        
        self.title = tk.Label(self.root, text = "Premium Calculator", font = "ar 15 bold")
        self.title.place(anchor="center")
        self.title.grid(row = 0, column = 2)
        
        self.age_value = tk.StringVar()
        self.bmi_value = tk.StringVar()
        self.pbf_value = tk.StringVar()
        self.children_value = tk.StringVar()
        self.smoker_value = tk.IntVar()
        self.premium_value = tk.StringVar()
        self.premium_value.set(str(self.formula) + '.-')
        self.checkvalue = tk.IntVar()
        
        
        self.age = tk.Label(self.root, text = "Age")
        self.bmi = tk.Label(self.root, text = "BMI")
        self.pbf = tk.Label(self.root, text = "Body Fat Percentage")
        self.children = tk.Label(self.root, text = "Amount of Children")
        self.smoker = tk.Checkbutton(self.root, text = "Smoker", variable = self.smoker_value)
        self.premium = tk.Label(self.root, text = "Predicted Costs:")
        
        self.canton = tk.Label(self.root, text = "Your Canton is Aargau!")
        
        self.checkbtn = tk.Checkbutton(text = "You agree with our Terms of Service", variable = self.checkvalue)
        self.checkbtn.grid(row = 7, column = 3)
        
        
        self.age_entry = tk.Entry(self.root, textvariable = self.age_value)
        self.bmi_entry = tk.Entry(self.root, textvariable = self.bmi_value)
        self.pbf_entry = tk.Entry(self.root, textvariable = self.pbf_value)
        self.children_entry = tk.Entry(self.root, textvariable = self.children_value)
        #self.smoker_entry = tk.Entry(self.root, textvariable = self.smoker_value)
        
        self.age_entry.grid(row=1, column=3)
        self.bmi_entry.grid(row=2, column=3)
        self.pbf_entry.grid(row=3, column=3)
        self.children_entry.grid(row=4, column=3)
        #self.smoker_entry.grid(row=4, column=3)
        
        self.age.grid(row = 1, column = 2)
        self.bmi.grid(row = 2, column = 2)
        self.pbf.grid(row = 3, column = 2)
        self.children.grid(row = 4, column = 2)
        self.smoker.grid(row = 6, column = 3)
        self.canton.grid(row = 5, column = 3)
        self.premium.grid(row = 12, column = 2)
        
        self.premium_label = tk.Label(self.root, textvariable=self.premium_value)
        self.premium_label.grid(row = 12, column = 3)

        self.button = tk.Button(self.root,
                                text="Predict Costs",
                                command=self.getvals)
        self.button.grid(row = 8, column = 3)
        
        

        self.root.mainloop()
    
        
    
    #Die Daten werden noch nicht validiert. Man geht davon aus, dass sie schon stimmen. (z.B. Zahlen (integer) für Alter)    
    
    def getvals(self):
        
        #first go through tree to find out to which cathegory it corresponds
        category = self.tree(float(self.age_value.get()), float(self.bmi_value.get()), float(self.children_value.get()), float(self.smoker_value.get()), float(self.pbf_value.get()), float(0), float(1), float(0), float(0))
        print(category)
        if category == 0.0:
            regression_value = self.regression_1(float(self.age_value.get()), float(self.bmi_value.get()), float(self.children_value.get()), float(self.smoker_value.get()), float(1), float(self.pbf_value.get()))
        elif category == 1.0:
            regression_value = self.regression_2(float(self.age_value.get()), float(self.bmi_value.get()), float(self.children_value.get()), float(self.smoker_value.get()), float(1), float(self.pbf_value.get()))
        else:
            regression_value =  self.regression_3(float(self.age_value.get()), float(self.bmi_value.get()), float(self.children_value.get()), float(self.smoker_value.get()), float(1), float(self.pbf_value.get()))
        
        self.premium_value.set(str(math.exp(regression_value)) + '.-')       


    #regression constants
    #noch mit np.exp hochrechnen
    def regression_1(self, age, bmi, children, smoker, canton, pbf):
        return age * 0.0197335 + bmi * 0.04229305 + children * 0.02384909 + smoker * 0.75578564 + canton * 0.05891112 + pbf * 0.01592228 + 5.832231201928893
    def regression_2(self, age, bmi, children, smoker, canton, pbf):
        return age * 0.02337388 + bmi * 0.07328484 + children * 0.02346498 + smoker * 0.83783636 + canton * 0.06517308 + pbf * 0.00268351 + 5.3945574155077445
    def regression_3(self, age, bmi, children, smoker, canton, pbf):
        return age * 8.94147230e-03 + bmi * 3.14761320e-02 + children * -2.00021533e-02 + smoker * 9.00832022e-18 + canton * 2.25844367e-02 + pbf * -2.80172846e-04 + 8.94780119237268

    

    #decision tree code from main notebook
    def tree(self, age, bmi, children, smoker, pbf, so, ag, bs, bl):
      if bmi <= 29.098000526428223:
        if smoker <= 0.5:
          if pbf <= 44.739999771118164:
            return 1.000000000;
          else:  # if pbf > 44.739999771118164
            if age <= 53.0:
              return 1.000000000;
            else:  # if age > 53.0
              return 0.000000000;
        else:  # if smoker > 0.5
          if age <= 54.5:
            if age <= 33.5:
              return 1.000000000;
            else:  # if age > 33.5
              if bmi <= 26.564000129699707:
                if bs <= 0.5:
                  return 1.000000000;
                else:  # if bs > 0.5
                  if pbf <= 34.045000076293945:
                    if children <= 2.5:
                      return 1.000000000;
                    else:  # if children > 2.5
                      if pbf <= 19.690000534057617:
                        return 1.000000000;
                      else:  # if pbf > 19.690000534057617
                        return 0.000000000;
                  else:  # if pbf > 34.045000076293945
                    return 0.000000000;
              else:  # if bmi > 26.564000129699707
                if children <= 0.5:
                  if pbf <= 23.22499942779541:
                    return 1.000000000;
                  else:  # if pbf > 23.22499942779541
                    return 0.000000000;
                else:  # if children > 0.5
                  return 0.000000000;
          else:  # if age > 54.5
            if pbf <= 9.980000019073486:
              return 1.000000000;
            else:  # if pbf > 9.980000019073486
              return 0.000000000;
      else:  # if bmi > 29.098000526428223
        if smoker <= 0.5:
          if age <= 45.5:
            if bmi <= 34.007999420166016:
              return 1.000000000;
            else:  # if bmi > 34.007999420166016
              if age <= 32.5:
                return 1.000000000;
              else:  # if age > 32.5
                if bmi <= 36.736000061035156:
                  if bs <= 0.5:
                    if pbf <= 56.92499923706055:
                      return 1.000000000;
                    else:  # if pbf > 56.92499923706055
                      return 0.000000000;
                  else:  # if bs > 0.5
                    return 0.000000000;
                else:  # if bmi > 36.736000061035156
                  return 0.000000000;
          else:  # if age > 45.5
            if bmi <= 33.06399917602539:
              if age <= 59.5:
                if bs <= 0.5:
                  if age <= 57.5:
                    return 1.000000000;
                  else:  # if age > 57.5
                    if bmi <= 31.848000526428223:
                      return 1.000000000;
                    else:  # if bmi > 31.848000526428223
                      if pbf <= 32.204999923706055:
                        return 0.000000000;
                      else:  # if pbf > 32.204999923706055
                        if age <= 58.5:
                          return 0.000000000;
                        else:  # if age > 58.5
                          return 1.000000000;
                else:  # if bs > 0.5
                  if pbf <= 46.97999954223633:
                    if bmi <= 31.77400016784668:
                      if age <= 55.0:
                        return 1.000000000;
                      else:  # if age > 55.0
                        if bmi <= 29.417999267578125:
                          return 1.000000000;
                        else:  # if bmi > 29.417999267578125
                          return 0.000000000;
                    else:  # if bmi > 31.77400016784668
                      return 0.000000000;
                  else:  # if pbf > 46.97999954223633
                    return 0.000000000;
              else:  # if age > 59.5
                if bmi <= 31.242000579833984:
                  if pbf <= 48.295000076293945:
                    if so <= 0.5:
                      return 1.000000000;
                    else:  # if so > 0.5
                      if bmi <= 30.239999771118164:
                        return 0.000000000;
                      else:  # if bmi > 30.239999771118164
                        return 1.000000000;
                  else:  # if pbf > 48.295000076293945
                    return 0.000000000;
                else:  # if bmi > 31.242000579833984
                  return 0.000000000;
            else:  # if bmi > 33.06399917602539
              if bmi <= 34.579999923706055:
                if age <= 55.0:
                  if bmi <= 33.191999435424805:
                    return 0.000000000;
                  else:  # if bmi > 33.191999435424805
                    if age <= 51.5:
                      if so <= 0.5:
                        return 1.000000000;
                      else:  # if so > 0.5
                        return 0.000000000;
                    else:  # if age > 51.5
                      return 1.000000000;
                else:  # if age > 55.0
                  return 0.000000000;
              else:  # if bmi > 34.579999923706055
                return 0.000000000;
        else:  # if smoker > 0.5
          if age <= 30.5:
            if age <= 22.5:
              if bmi <= 37.24800109863281:
                return 1.000000000;
              else:  # if bmi > 37.24800109863281
                return 0.000000000;
            else:  # if age > 22.5
              if pbf <= 30.84000015258789:
                if age <= 29.5:
                  return 1.000000000;
                else:  # if age > 29.5
                  if so <= 0.5:
                    return 1.000000000;
                  else:  # if so > 0.5
                    return 0.000000000;
              else:  # if pbf > 30.84000015258789
                return 0.000000000;
          else:  # if age > 30.5
            if bmi <= 31.395999908447266:
              return 0.000000000;
            else:  # if bmi > 31.395999908447266
              if age <= 49.0:
                if bmi <= 36.097999572753906:
                  return 0.000000000;
                else:  # if bmi > 36.097999572753906
                  return 0.000000000;
              else:  # if age > 49.0
                return 0.000000000;
app=Test()