import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
figure, axes = plt.subplots()
draw_circle = plt.Circle((1, 0), 2,fill=False,color="blue")
axes.set_aspect(1)
axes.add_artist(draw_circle)
plt.scatter(1,0,marker="x",color="black")
plt.text(1,0, "O", color='blue')
plt.axhline(y =2,color="green",label="Tangent")
plt.scatter(1,2,marker="x")
plt.text(1,2, "P(1,2)", color="red")
plt.axhline(y =-2,color="green")
plt.scatter(1,-2,marker="x")
plt.text(1,-2, "P2(1,-2)", color="red")
plt.axis('equal')


plt.yticks(np.arange(-3, 4, 1))
plt.xticks(np.arange(-3, 5 , 1))

blue_line = mlines.Line2D([], [], color='blue', label='circle')
cp=plt.legend(handles=[blue_line],bbox_to_anchor=(1, 1), loc='lower left', borderaxespad=0.)
plt.gca().add_artist(cp)
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0.)
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.grid()
plt.show()