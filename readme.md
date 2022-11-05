仓库使用方法，使用Python3.11 venv虚拟环境

source .venv/bin/activate

deactivate

以 $\int_0^4{\arcsin \sqrt{\frac{x}{x+1}}}$ 积分为例（不同算法的运行性能对比）：

参考的Burning1997/Adaptive-quadrature的自适应Simpson代码：
adapt-Simpson:  (3.5357435889673265+0j) 3.1254362987704464e-12
         33561 function calls (32071 primitive calls) in 0.017 seconds

书上的“笨拙版”自适应Simpson代码：
self-Simpson:  (3.5357435889671165+0j)
iteration times:  24
         150994974 function calls in 66.258 seconds

复化求积梯形法：
complex Trapezoid:  (3.5357435874215395+0j)
         3145735 function calls in 1.327 seconds

Richardson外推法：
simpson-Richardson:  (3.5357435887567252+0j)
complex-simpson-Richardson:  (3.535743588903797+0j)
         31457305 function calls in 13.658 seconds

Romberg算法：
Romberg:  (3.5357435889672533+0j)
iteration times:  25
         100663329 function calls in 45.528 seconds

Python内置Integral模块的quad函数：
inner-method:  (3.535743588970393, 2.6015380960586754e-09)
         703 function calls in 0.000 seconds

内置函数真的是碾压咱们所有的轮子！！
