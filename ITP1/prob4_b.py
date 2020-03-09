# 円の面積と円周
import math

r = float(input())

circumference = 2 * math.pi * r
circle_area = math.pi * (r**2)

print("%f %f"%(circle_area, circumference))
