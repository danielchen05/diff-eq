## Separable equations {#separation}

Look for a product $y'=g(t)h(y)$. First check each zero of $h$ for a constant solution. On an interval where $h(y)\ne0$, separate and integrate.

$$\frac{y'}{h(y)}=g(t)
\qquad\Longrightarrow\qquad
\int\frac{dy}{h(y)}=\int g(t)\,dt.$$

The left side follows by substitution in $\int\frac{y'(t)}{h(y(t))}\,dt$. Keep an integration constant, use the initial condition, and solve for $y$ if convenient. An implicit relation can be the cleanest answer.

### Example · An implicit initial value problem

For $y'=\frac{x}{1+y^2}$ with $y(0)=0$, multiply by $1+y^2$ and integrate. The initial data give $C=0$.

$$(1+y^2)\,dy=x\,dx
\qquad\Longrightarrow\qquad y+\frac{y^3}{3}=\frac{x^2}{2}.$$

Two other separations show where the interval matters. For $y'=-\frac{4t}{y}$, integrate $y\,dy=-4t\,dt$ to get $y^2+4t^2=C$. Choose a sign branch where $y\ne0$. For $y'=\frac{y}{x+1}$ with $y(0)=2$, integration gives $\ln|y|=\ln|x+1|+C$. The IVP selects $y=2(x+1)$ on $x>-1$.

## Linear equations and integrating factors {#integrating-factor}

Normalize to $y'+p(t)y=q(t)$ on an interval where the leading coefficient is nonzero. Read $p$ from the normalized equation.

$$\mu(t)=e^{\int p(t)\,dt},\qquad (\mu y)'=\mu q.$$

Multiply the **entire equation** by $\mu$. Its derivative satisfies $\mu'=p\mu$, so the left side is one product derivative. Integrate, then divide by $\mu$.

$$y(t)=\frac{1}{\mu(t)}\left(\int\mu(t)q(t)\,dt+C\right).$$

### Example · Recognizing the product derivative

For $y'+\frac{2}{x}y=\frac{\sin x}{x^2}$ on $x>0$, use $p(x)=\frac{2}{x}$ to get $\mu=x^2$. Thus $(x^2y)'=\sin x$, and

$$x^2y=-\cos x+C,\qquad y=\frac{-\cos x+C}{x^2}.$$

For $y'-y=xe^x$, the sign of $p=-1$ matters. Multiplying by $e^{-x}$ gives $(e^{-x}y)'=x$, so $y=e^x\!\left(\frac{x^2}{2}+C\right)$.

## Exact equations {#exact}

Write the equation as $M(x,y)\,dx+N(x,y)\,dy=0$. On an open rectangle with continuous first partials, test **$M_y=N_x$**. An exact equation has a potential $\phi$ satisfying $\phi_x=M$, $\phi_y=N$. Its solution curves are level curves $\phi(x,y)=C$.

1. Integrate $M$ in $x$, holding $y$ fixed. Write $\phi=\int M\,dx+h(y)$.
2. Differentiate that expression in $y$ and compare with $N$. Solve for $h'(y)$ and integrate.
3. Write $\phi=C$. If initial data are given, substitute them to find $C$.

### Example · Recovering the potential

For $(2xy+y^2)\,dx+(x^2+2xy)\,dy=0$, both cross-partials equal $2x+2y$. Integrating $M$ gives $\phi=x^2y+xy^2+h(y)$. Matching $\phi_y=x^2+2xy+h'(y)$ to $N$ gives $h'=0$. The solution is

$$x^2y+xy^2=C.$$

> An integrating factor can sometimes make a non-exact equation exact. Finding such a factor is outside the scope of these notes.
