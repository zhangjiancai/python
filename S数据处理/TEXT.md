首先，创建一个以参数$w$为变量的代价函数

$$J\left( w  \right)=\frac{1}{2m}\sum\limits_{i=1}^{m}{{{\left( {{h}}\left( {{x}^{(i)}} \right)-{{y}^{(i)}} \right)}^{2}}}$$\[{{h}}\left( x \right)={{w}^{T}}X={{w }_{0}}{{x}_{0}}+{{w }_{1}}{{x}_{1}}+{{w }_{2}}{{x}_{2}}+...+{{w }_{n}}{{x}_{n}}\]

其中：

$$
{{h}}   \left( x \right)={{w}^{T}}X={{w }_{0}}{{x}_{0}}+{{w }_{1}}{{x}_{1}}+{{w }_{2}}{{x}_{2}}+...+{{w }_{n}}{{x}_{n}}
$$

$$
\begin{cases}
    a_{0}+a_{1}x_{0}+...+a_{n}x_{0}^{n}=y_{0} \\
    a_{0}+a_{1}x_{1}+...+a_{n}x_{1}^{n}=y_{1} \\
    \cdots\\
    a_{0}+a_{1}x_{n}+...+a_{n}x_{n}^{n}=y_{n}
\end{cases}
$$

$$
\left[  
\begin{array}{ccc|c}
    \psi(x) & g(x)   & \cdots  & a_{1n} \\
    \hline
    a_{21}  & a_{22} & \dots   & a_{2n} \\
    \vdots  & \vdots & \ddots  & \vdots \\
    a_{n1}  & a_{n2} & ...     & a_{nn}
\end{array}
\right]
$$