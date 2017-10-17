"""
Permutations

In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.

"""
"""
求全排列的算法如下

需掌握的基本算法：

排列：就是从n个元素中同时取r个元素的排列，记做P(n,r)。（当r=n时，我们称P(n,n)=n!为全排列）例如我们有集合OR = {1,2,3,4},那么n = |OR| = 4,切规定r=3，那么P(4,3)就是：

{1,2,3}; {1,2,4}; {1,3,2}; {1,3,4};{1,4,2};{1,4,3};{2,1,3};{2,1,4}; {2,3,1}; {2,3,4}; {2,4,1}; {2,4,3}; {3,1,2}; {3,1,4}; {3,2,1}; {3,2,4}; {3,4,1}; {3,4,2}; {4,1,2}; {4,1,3}; {4,2,1}; {4,2,3}; {4,3,1}; {4,3,2}

算法如下：

int  n, r;
char used[MaxN];
int  p[MaxN];
 
void permute(int pos)
{ int i;
/*如果已是第r个元素了，则可打印r个元素的排列 */
    if (pos==r) {
        for (i=0; i<r; i++)
            cout << (p[i]+1);
        cout << endl;
        return;
    }
    for (i=0; i<n; i++)
        if (!used[i]) { /*如果第i个元素未用过*/
/*使用第i个元素，作上已用标记，目的是使以后该元素不可用*/
            used[i]++;
/*保存当前搜索到的第i个元素*/
            p[pos] = i;
/*递归搜索*/
           permute(pos+1);
 
/*恢复递归前的值，目的是使以后改元素可用*/
 used[i]--;
        }
}

"""

# coding:utf-8
# 输入字符 输出字符所有的可能组合 
# 去除重复 set()   排序  list.sort()

print(list(itertools.permutations([1,2,3,4],2)))
