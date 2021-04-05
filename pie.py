import matplotlib.pyplot as plt

hours = [2, 6, 1, 4, 2, 6, 2, 1]
activities = ['ready', 'school', 'rest', 'study', 'play', 'sleep', 'tv','yoga']
explodes = [0,0,0,0,0,0.2,0,0]
plt.pie(hours, labels=activities,explode= explodes)
plt.show()