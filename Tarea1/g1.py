import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph() #para hacer el grafico
pos={0:(1,0),1:(2,0),2:(3,0),3:(4,0),4:(1.5,.8),5:(3.5,.8),6:(2.5,1.6)} #agregar las coordenadas en el plano
labels={0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7'} #ponerle etiqueta a los vertices
Conexion=[(0,4),(1,4),(2,5),(3,5),(4,6),(5,6)] #hacer arcos

nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=range(7), node_color='g') #dibujar el nodo
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=Conexion,width=1) #dibujar el arco
nx.draw_networkx_labels(G,pos,labels,font_size=12)
plt.axis('off') #quitar coordenas
plt.savefig("g1.eps") #crear imagen
plt.show() #ver la imagen en pantalla

nx.draw (G)
plt.savefig("g1.png")


