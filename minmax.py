def minmax(node,depth,type):
 if leafnode(node):
  
  return eval(node)
 if type==max:
  bestscore=-(math.inf)
  for child in range(1,nmbsucc(node)):
   value=minmax(succ(node,child),depth,min)
   if value>bestscore:
    bestscore=value
 if type==min:
  bestscore=math.inf
  for child in range(1,nmbsucc(node)):
   value=minmax(succ(node,child),depth+1,max)
   if value<bestscore
    bestscore=value
 return bestscore
