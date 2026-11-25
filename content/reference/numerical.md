## Euler's method {#euler}

For the IVP $y'=f(t,y)$, $y(t_0)=y_0$, approximate the curve by its tangent line over a step of length $h$. One exact starting value gives the approximation

$$y(t_0+h)\approx y_0+h f(t_0,y_0).$$

To take several steps, use the **current numerical point** at each step.

$$\begin{aligned}
t_{n+1}&=t_n+h,\\
y_{n+1}&=y_n+h f(t_n,y_n).
\end{aligned}$$

Read the slope at $(t_n,y_n)$, multiply by the step size, and add the increment to $y_n$. Use this new value to evaluate the next slope. The equality defines the iterate $y_{n+1}$, which approximates $y(t_{n+1})$.
