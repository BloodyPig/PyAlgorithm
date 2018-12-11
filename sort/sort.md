# 排序

根据[维基百科](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)中的算法顺序，学习实现以下的排序算法：

### 稳定的排序

- [冒泡排序](https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F)（bubble sort）— ![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)
- [插入排序](https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F)（insertion sort）—![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)
- [鸡尾酒排序](https://zh.wikipedia.org/wiki/%E9%B8%A1%E5%B0%BE%E9%85%92%E6%8E%92%E5%BA%8F)（cocktail sort）—![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)
- [桶排序](https://zh.wikipedia.org/wiki/%E6%A1%B6%E6%8E%92%E5%BA%8F)（bucket sort）—![O(n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/34109fe397fdcff370079185bfdb65826cb5565a)；需要![O(k)](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5ec39041121b14e8c2b1a986c9b04547b223e3c)额外空间
- [计数排序](https://zh.wikipedia.org/wiki/%E8%AE%A1%E6%95%B0%E6%8E%92%E5%BA%8F)（counting sort）—![O(n+k)](https://wikimedia.org/api/rest_v1/media/math/render/svg/cebd2e4442e56daa59f3fab79339f952122c29e8)；需要![O(n+k)](https://wikimedia.org/api/rest_v1/media/math/render/svg/cebd2e4442e56daa59f3fab79339f952122c29e8)额外空间
- [归并排序](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F)（merge sort）—![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1)；需要![O(n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/34109fe397fdcff370079185bfdb65826cb5565a)额外空间
- 原地[归并排序](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F)— ![{\displaystyle O(n\log _{2}n)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0c9fd155774e2c0e505f95ff07a4a0f76605bae7)如果使用最佳的现在版本
- [二叉排序树](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%8F%89%E6%8E%92%E5%BA%8F%E6%A0%91)排序（binary tree sort）— ![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1)期望时间；![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)最坏时间；需要![O(n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/34109fe397fdcff370079185bfdb65826cb5565a)额外空间
- [鸽巢排序](https://zh.wikipedia.org/wiki/%E9%B8%BD%E5%B7%A2%E6%8E%92%E5%BA%8F)（pigeonhole sort）—![O(n+k)](https://wikimedia.org/api/rest_v1/media/math/render/svg/cebd2e4442e56daa59f3fab79339f952122c29e8)；需要![O(k)](https://wikimedia.org/api/rest_v1/media/math/render/svg/f5ec39041121b14e8c2b1a986c9b04547b223e3c)额外空间
- [基数排序](https://zh.wikipedia.org/wiki/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F)（radix sort）—![{\displaystyle O(nk)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/16feb8341ea75a7bb8b3445959360dde7686db10)；需要![O(n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/34109fe397fdcff370079185bfdb65826cb5565a)额外空间
- [侏儒排序](https://zh.wikipedia.org/wiki/%E4%BE%8F%E5%84%92%E6%8E%92%E5%BA%8F)（gnome sort）— ![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)
- [图书馆排序](https://zh.wikipedia.org/wiki/%E5%9B%BE%E4%B9%A6%E9%A6%86%E6%8E%92%E5%BA%8F)（library sort）— ![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1)期望时间；![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)最坏时间；需要![{\displaystyle (1+\varepsilon )n}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0b18535a9414bcc2072d906174ce2d7ae80baeb0)额外空间
- [块排序](https://zh.wikipedia.org/w/index.php?title=%E5%A1%8A%E6%8E%92%E5%BA%8F&action=edit&redlink=1)（block sort）— ![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1)

### 不稳定的排序

- [选择排序](https://zh.wikipedia.org/wiki/%E9%81%B8%E6%93%87%E6%8E%92%E5%BA%8F)（selection sort）—![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)
- [希尔排序](https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F)（shell sort）—![O(n\log^2 n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/48c36489701bc8023db2f8d6bc809b14a7f8dd4e)
- [Clover排序算法](https://zh.wikipedia.org/w/index.php?title=Clover%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95&action=edit&redlink=1)（Clover sort）—![O(n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/34109fe397fdcff370079185bfdb65826cb5565a)期望时间，![O(n^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6cd9594a16cb898b8f2a2dff9227a385ec183392)最坏情况
- [梳排序](https://zh.wikipedia.org/wiki/%E6%A2%B3%E6%8E%92%E5%BA%8F) —![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1)
- [堆排序](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F)（heap sort）—![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1)
- [平滑排序](https://zh.wikipedia.org/w/index.php?title=%E5%B9%B3%E6%BB%91%E6%8E%92%E5%BA%8F&action=edit&redlink=1)（smooth sort）— ![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1)
- [快速排序](https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F)（quick sort）—![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1)
- [内省排序](https://zh.wikipedia.org/wiki/%E5%86%85%E7%9C%81%E6%8E%92%E5%BA%8F)（introsort）—![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1)
- [耐心排序](https://zh.wikipedia.org/wiki/%E8%80%90%E5%BF%83%E6%8E%92%E5%BA%8F)（patience sort）—![{\displaystyle O(n\log n+k)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/c9f1b7420b3d24b7300cd5378bafd652f35ef536)

