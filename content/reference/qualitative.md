## Existence and uniqueness {#existence}

For **linear** $y'+p(t)y=q(t)$ with $y(t_0)=y_0$, a unique solution exists on every open interval containing $t_0$ where $p,q$ are continuous. Normalize before finding this interval.

For a **nonlinear IVP** $y'=f(t,y)$ with $y(t_0)=y_0$, choose an **open rectangle around the initial point** $(t_0,y_0)$. The point must lie in its interior. Check continuity everywhere in that rectangle.

| What to check throughout the rectangle | What it guarantees near $t_0$ |
|:---|:---|
| $f$ is continuous | At least one local solution exists. |
| In addition, $f_y=\partial f/\partial y$ exists and is continuous | The local solution is unique. |

### Example · A singular line

For $y'=\frac{y}{x-2}$, the right side is undefined at $x=2$, so there is no classical solution through $(2,1)$. At $(0,-3)$ both $f$ and $f_y=\frac{1}{x-2}$ are continuous nearby. The normalized linear equation guarantees a unique solution on $(-\infty,2)$.

### Example · Initial data on a domain boundary

For $y'=\sqrt{x+y}$, the points $(0,0)$ and $(-1,1)$ lie on $x+y=0$. No open rectangle about either point lies in the real domain. In fact, let $u=x+y$. Then $u'=1+\sqrt u\ge1$. If $u(x_0)=0$, integrating just to the left would give $u(x)<0$. Neither IVP has a real solution on a two-sided interval about its initial point.

For $y'=e^x\cos y$, both $f$ and $f_y=-e^x\sin y$ are continuous on an open rectangle around each of the initial points $(0,\frac{\pi}{2})$ and $(1,0)$. Each IVP has a unique local solution. It extends to every finite $x$ because $|y'|\le e^x$ bounds the change in $y$ on every bounded interval.

## Autonomous equations and phase lines {#phase-lines}

For $y'=f(y)$, the slope depends only on $y$. Solve $f(y)=0$ for **equilibria**. Between consecutive equilibria, test the sign of $f$. Draw an arrow toward larger $y$ for $f>0$ and toward smaller $y$ for $f<0$.

| Arrows at the equilibrium | Classification |
|:---|:---|
| $\rightarrow\,\bullet\,\leftarrow$ Both point in | Stable |
| $\leftarrow\,\bullet\,\rightarrow$ Both point out | Unstable |
| $\rightarrow\,\bullet\,\rightarrow$ or $\leftarrow\,\bullet\,\leftarrow$ Both point the same way | Semi-stable |

A solution starting at an equilibrium stays there when uniqueness holds.

### Example · Reading long-term behavior from signs

For $z'=z(z-1)(2-z)$, the roots are $0,1,2$. From left to right the signs are $+,-,+,-$. The equilibria $0$ and $2$ are stable because both arrows point in. The equilibrium $1$ is unstable because both arrows point out. Starting at $-0.5$ or $0.5$ gives $z(t)\to0$. Starting at $3$ gives $z(t)\to2$.

{{figure:phase-z}}

For $z'=z(1-z)$, the equilibria are $0$ and $1$. Solutions increase toward $1$ for $0<z<1$ and decrease toward $1$ for $z>1$. An arrow toward infinity in another phase line can indicate finite-time blow-up. The phase line alone does not give the time to escape.

For $u'=(u^2+1)(u-4)$, the signs on either side of $4$ are $-,+$, so $4$ is unstable. From $u(0)=0$ or $u(0)=2$, the solution escapes to $-\infty$. From $u(0)=6$, it escapes to $+\infty$. Each escape occurs in finite time because $\int\frac{du}{\lvert u'\rvert}$ has a tail comparable to $\int\frac{du}{\lvert u\rvert^3}$.

For $P'=P(5-P)(P+2)$, the signs are $+,-,+,-$ across $-2,0,5$. The equilibria $-2$ and $5$ are stable, and $0$ is unstable. Initial values $1$ and $6$ both approach $5$. An initial value of $-3$ approaches $-2$.

## Bifurcation diagrams {#bifurcations}

A bifurcation diagram stacks the phase lines of $x'=f(x;c)$ as the parameter $c$ varies. A **bifurcation value** is a value of $c$ where the number or stability of equilibria changes.

1. Solve $f(x;c)=0$. Put $c$ on the horizontal axis and the equilibrium $x$ on the vertical axis. Plot each branch on the interval where it exists.
2. Look wherever two equilibrium branches meet and read the **horizontal coordinate**. That is the bifurcation value in these examples.
3. Draw a phase line just before, at, and just after each such value. Use the signs of $f$ to label the stable, unstable, and semi-stable equilibria.

For $x'=(x-1)(x^2+c)$, the branch $x=1$ exists for all $c$, and $x=\pm\sqrt{-c}$ exist for $c\le0$. The branches $x=1$ and $x=\sqrt{-c}$ meet at $(c,x)=(-1,1)$. The two square-root branches meet at $(0,0)$. The bifurcation values are $c=-1$ and $c=0$.

{{figure:bifurcation}}
