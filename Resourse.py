# -*- coding: utf-8 -*-  
import os

global O2_m3                    #此项全局变量为O2含量，以体积为标识,一下类推
global N2_m3
global CO2_m3
global H2O_m3                   #此处为水蒸气，影响蒸发散热和蒸腾作用
global Ar_m3                    #用氩气代指所有稀有气体
global H2O_kg
global NH3_m3                   #氨气，用作制氮肥，NH3 + CO2 + H2O == NH4HCO3，来源为人动物排泄物，
                                #生物圈中浓度高于0.5%时会造成所有生物死亡
global Food_kg                  #仅针对人类的食物需要 1kg植物 = 0.5kgFood 1kg肉 = 0.8kgFood
global Meat_kg                  #一头猪80kg~100kg，视猪健康状态而定
global Plant_kg                 #按玉米算，一株玉米一年收成大概2~8个玉米（视肥料状态），从而推算出大概收成0.2~0.8kg玉米
                                #按水稻算，
global Trash_kg                 #从中得到氨气和水，植物可处理剩余，分离需要电力
global Electric_kWh             #电力来自于恒定的太阳能板，太阳能板每平方米功率为150W，默认设定中太阳能板面积为10m^2
#未完

'''
先把变量定完
具体影响因素到时候到wiki里再写

'''


global Trash_kg



class O2():

    def O2_Writer(x_m3):        #x_m3相当于x/m^3,此处不知道为什么不能加serf            
        O2_m3 = x_m3
        return O2_m3            # 函数检查通过
    
    def O2_x_100():             #此函数为检测O2百分比的
        return

