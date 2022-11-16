# [7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

# Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.


# İlk olarak root'u yerleştiririz. Ardından dizinin 2. elemanının root'dan büyük mü yoksa küçük mü olduğunu kontrol
# ederiz. Büyükse ağacın root'umuzun altındaki sağ dalına, küçükse sol dalına yerleştiririz. Bu şekilde diğerlerini de
# sırasıyla yerleştirip ağacımızı oluştururuz.

# Öncelikle dengeli bir ağacımız olması yani average case durumumuza bakalım
# Root = 7

#          7
#        /   \
#       5     8
#     /  \     \
#    1    6     9
#   / \
#  0   3
#      /\
#     2  4

# Bu durumda Big-O gösterimimiz: O(logn) şeklindedir


# Şimdi de worst case durumumuza bakalım
# Burada da Root = 8 olsun

#                8
#               /  \
#              7   9
#             /
#            6
#           /
#          5
#         /
#        4
#       /
#      3
#     /
#    1
#   / \
#  0   2

# Bu durumda ise Big-O gösterimimiz: O(n) şeklindedir
