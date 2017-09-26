# -*- coding: utf-8 -*-
"""交叉路口的红绿灯安排"""
__author__ = 'Huang Lun'


def coloring(G):  # 做图G的着色
    color = 0
    groups = set()
    verts = vertices(G)  # 取得G的所有顶点，依赖于图的表示
    while verts:  # 如果集合不空
        new_group = set()
        for v in list(verts):
            if not_adjacent_with_set(v, new_group, G):
                new_group.add(v)
                verts.remove(v)

        groups.add((color, new_group))
        color += 1
    return groups
