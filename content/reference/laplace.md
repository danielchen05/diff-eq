## The Laplace transform {#laplace-definition}

The transform takes a function of $t$ to a function of $s$. Use the defining integral where it converges.

$$F(s)=\mathcal L\{f(t)\}(s)=\int_0^\infty e^{-st}f(t)\,dt.$$

## Solving an initial value problem {#laplace-ivp}

Write $Y(s)=\mathcal L\{y(t)\}(s)$. The derivative rules incorporate the initial data immediately.

$$\begin{aligned}
\mathcal L\{y'\}&=sY(s)-y(0),\\
\mathcal L\{y''\}&=s^2Y(s)-s\,y(0)-y'(0).
\end{aligned}$$

1. Transform both sides. For a second-order IVP, substitute **both** $y(0)$ and $y'(0)$.
2. Collect the terms containing $Y(s)$ and solve the resulting algebraic equation for $Y(s)$.
3. Decompose into partial fractions when helpful, then apply the inverse transform to obtain $y(t)$.

## Unit step functions {#steps}

A step at time $c$ switches from $0$ to $1$. For $c\ge0$, use

$$u_c(t)=\begin{cases}0,&t<c,\\1,&t\ge c,\end{cases}\qquad
\mathcal L\{u_c(t)\}(s)=\frac{e^{-cs}}{s},\quad s>0.$$

The switch time appears in the exponential. The choice of value at the single time $t=c$ leaves the transform unchanged.
