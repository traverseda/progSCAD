use<progSCADversion.scad>;

if (version_num()<20150300) echo("progSCAD needs at least openscad version 2015.03");

//Len, but it starts counting from 0
zlen(list)
  len(list)-1
;

function listIndex(list)
  [for(i=[0:len(list)])[i,list[i]]];
;

function listDeIndex(list)
  [for (i=list) i[1]]
;

function listInsert(list, index, newEntry)
  concat([for (i=listIndex(list)) if (i[0]<index) i[1] ],[newEntry],[for (i=listIndex(list)) if (i[0]>=index)i[1]]);
;

function listPop(list, index)
  concat([for (i=listIndex(list)) if (i[0]<index) i[1]],[for (i=listIndex(list)) if (i[0]>index) i[1]])
;


//You can use values higher or lower then the actual index. It will wrap around. If your len(list)==10, and you say listWrap(list,-2), it should return list[8]
function listWrap(list, index)
 (index<len(list)&&index>0)?
   index:
   index>0?
     index%len(list):
     len(list)-index%len(list)
;
