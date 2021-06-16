# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:37:23 2021

@author: bruno
"""

import tkinter as tk

class Test():
    def __init__(self):
        
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
    
        
    def getvals(self):
        category = self.tree(float(self.age_value.get()), float(self.bmi_value.get()), float(self.children_value.get()), float(self.smoker_value.get()), float(self.pbf_value.get()), float(0), float(1), float(0), float(0))
        print(category)
        if category == 0.0:
            regression_value = self.regression_1(float(self.age_value.get()), float(self.bmi_value.get()), float(self.children_value.get()), float(self.smoker_value.get()), float(1), float(self.pbf_value.get()))
        elif category == 1.0:
            regression_value = self.regression_2(float(self.age_value.get()), float(self.bmi_value.get()), float(self.children_value.get()), float(self.smoker_value.get()), float(1), float(self.pbf_value.get()))
        else:
            regression_value =  self.regression_3(float(self.age_value.get()), float(self.bmi_value.get()), float(self.children_value.get()), float(self.smoker_value.get()), float(1), float(self.pbf_value.get()))
        
        self.premium_value.set(str(regression_value) + '.-')       

    def regression_1(self, age, bmi, children, smoker, canton, pbf):
        return age * 84.57060902 + bmi * 338.30444212 + children * 80.96289322 + smoker * -3499.11480535 + canton * 242.9672478 + pbf * 140.52510273 - 3039.947639067678
    def regression_2(self, age, bmi, children, smoker, canton, pbf):
        return age * 380.98262826 + bmi * 1718.48155744 + children * 767.38693392 + smoker * -12472.71629991 + canton * 807.30743223 + pbf * 393.0261260 - 37942.867484692986
    def regression_3(self, age, bmi, children, smoker, canton, pbf):
        return age * -15.10083895 + bmi * 32.20836642 + children * 28.72929982 + smoker * 0 + canton * 24.55440541 + pbf * -98.29914818 + 41292.965416450555

    
    def tree(self, age, bmi, children, smoker, pbf, so, ag, bs, bl):
      if bmi <= 31.234000205993652:
        if smoker <= 0.5:
          if age <= 63.5:
            if bmi <= 31.046000480651855:
              if age <= 57.5:
                return 1.000000000;
              else:  # if age > 57.5
                if bmi <= 28.657999992370605:
                  return 1.000000000;
                else:  # if bmi > 28.657999992370605
                  if bs <= 0.5:
                    return 1.000000000;
                  else:  # if bs > 0.5
                    if pbf <= 44.69999885559082:
                      return 0.000000000;
                    else:  # if pbf > 44.69999885559082
                      return 1.000000000;
            else:  # if bmi > 31.046000480651855
              if children <= 2.5:
                return 1.000000000;
              else:  # if children > 2.5
                return 0.000000000;
          else:  # if age > 63.5
            if bmi <= 28.31599998474121:
              return 1.000000000;
            else:  # if bmi > 28.31599998474121
              if bmi <= 30.588000297546387:
                return 0.000000000;
              else:  # if bmi > 30.588000297546387
                return 1.000000000;
        else:  # if smoker > 0.5
          if age <= 53.5:
            if bmi <= 27.82200050354004:
              if age <= 40.5:
                if pbf <= 39.85499954223633:
                  return 1.000000000;
                else:  # if pbf > 39.85499954223633
                  if bs <= 0.5:
                    return 1.000000000;
                  else:  # if bs > 0.5
                    return 0.000000000;
              else:  # if age > 40.5
                if bmi <= 23.604000091552734:
                  return 1.000000000;
                else:  # if bmi > 23.604000091552734
                  if bmi <= 26.741999626159668:
                    if bs <= 0.5:
                      if children <= 2.0:
                        return 1.000000000;
                      else:  # if children > 2.0
                        return 0.000000000;
                    else:  # if bs > 0.5
                      if bmi <= 25.010000228881836:
                        return 0.000000000;
                      else:  # if bmi > 25.010000228881836
                        return 1.000000000;
                  else:  # if bmi > 26.741999626159668
                    return 0.000000000;
            else:  # if bmi > 27.82200050354004
              if age <= 29.5:
                return 1.000000000;
              else:  # if age > 29.5
                return 0.000000000;
          else:  # if age > 53.5
            if pbf <= 9.980000019073486:
              return 1.000000000;
            else:  # if pbf > 9.980000019073486
              return 0.000000000;
      else:  # if bmi > 31.234000205993652
        if age <= 35.5:
          if smoker <= 0.5:
            if pbf <= 58.7400016784668:
              return 1.000000000;
            else:  # if pbf > 58.7400016784668
              if age <= 31.0:
                return 1.000000000;
              else:  # if age > 31.0
                return 0.000000000;
          else:  # if smoker > 0.5
            if age <= 20.5:
              if bmi <= 37.24800109863281:
                return 1.000000000;
              else:  # if bmi > 37.24800109863281
                return 0.000000000;
            else:  # if age > 20.5
              return 0.000000000;
        else:  # if age > 35.5
          if bmi <= 33.06599998474121:
            if age <= 59.5:
              if smoker <= 0.5:
                if bs <= 0.5:
                  if age <= 57.5:
                    return 1.000000000;
                  else:  # if age > 57.5
                    if bmi <= 32.55999946594238:
                      return 1.000000000;
                    else:  # if bmi > 32.55999946594238
                      return 0.000000000;
                else:  # if bs > 0.5
                  if age <= 50.0:
                    return 1.000000000;
                  else:  # if age > 50.0
                    return 0.000000000;
              else:  # if smoker > 0.5
                if bs <= 0.5:
                  return 0.000000000;
                else:  # if bs > 0.5
                  if bmi <= 31.736000061035156:
                    return 0.000000000;
                  else:  # if bmi > 31.736000061035156
                    return 0.000000000;
            else:  # if age > 59.5
              if smoker <= 0.5:
                return 0.000000000;
              else:  # if smoker > 0.5
                if pbf <= 40.915000915527344:
                  return 0.000000000;
                else:  # if pbf > 40.915000915527344
                  return 0.000000000;
          else:  # if bmi > 33.06599998474121
            if smoker <= 0.5:
              if pbf <= 35.635000228881836:
                return 1.000000000;
              else:  # if pbf > 35.635000228881836
                if age <= 48.5:
                  if pbf <= 41.84499931335449:
                    if bs <= 0.5:
                      return 1.000000000;
                    else:  # if bs > 0.5
                      return 0.000000000;
                  else:  # if pbf > 41.84499931335449
                    if children <= 0.5:
                      return 1.000000000;
                    else:  # if children > 0.5
                      return 0.000000000;
                else:  # if age > 48.5
                  if bmi <= 34.1200008392334:
                    if ag <= 0.5:
                      return 0.000000000;
                    else:  # if ag > 0.5
                      if age <= 60.0:
                        return 1.000000000;
                      else:  # if age > 60.0
                        return 0.000000000;
                  else:  # if bmi > 34.1200008392334
                    return 0.000000000;
            else:  # if smoker > 0.5
              if age <= 47.5:
                if pbf <= 61.829999923706055:
                  return 0.000000000;
                else:  # if pbf > 61.829999923706055
                  return 0.000000000;
              else:  # if age > 47.5
                return 0.000000000;

app=Test()