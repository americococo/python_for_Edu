| 분류 | List | Dictionary |tuple|
| :--------: | :--------: | :--------: | :--------:|
| 생성 | list=[1,2,3] | dictionary={'one':1,'two':2}|tuple1=1,2,3<br>tuple1=(1,2,3)<br>tuple1=tuple(list1)|
| 호출 |  list[2] | dict['one']|tuple[1]|
| 삭제 |   del(list[0]) <br> list.remove(2)   | del(dict['one'])|불가능|
| 일괄 삭제|list.clear()|dict.clear()|불가능|
|탐색| 2 in list | 'two' in dict.keys() <br> 2in dict.values()|2 in tuple1|
|결합|list1+list2 | dict1.update(dict2)|tuple1+tuple2|
