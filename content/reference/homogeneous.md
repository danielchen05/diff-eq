## Characteristic roots and initial values {#real-roots}

For $y''+p(t)y'+q(t)y=g(t)$, specify both $y(t_0)$ and $y'(t_0)$. If $p,q,g$ are continuous on an open interval containing $t_0$, the IVP has a unique solution throughout that interval. Divide by the leading coefficient before you check continuity.

For a **homogeneous equation with constant coefficients**, substitute $y=e^{rt}$. Cancel the nonzero exponential to obtain the characteristic equation.

$$ay''+by'+cy=0\qquad\Longrightarrow\qquad ar^2+br+c=0,\quad a\ne0.$$

| Roots | General real solution |
|:---|:---|
| Distinct real $r_1,r_2$ | $C_1e^{r_1t}+C_2e^{r_2t}$ |
| Repeated real $r$ | $(C_1+C_2t)e^{rt}$ |
| Complex $\lambda\pm i\mu$, $\mu\ne0$ | $e^{\lambda t}(C_1\cos(\mu t)+C_2\sin(\mu t))$ |

For complex roots, Euler's formula $e^{i\theta}=\cos\theta+i\sin\theta$ gives the two real solutions. For a repeated root, the factor $t$ gives the second independent solution. Differentiate the general solution before applying the second initial condition. To recover an equation from a supplied solution family, read the roots from its exponential and trigonometric factors, form the characteristic polynomial, and read off the coefficients.

## Superposition and the Wronskian {#wronskian}

**Superposition.** If $y_1,y_2$ solve the same linear homogeneous ODE, every linear combination $C_1y_1+C_2y_2$ solves it. For a second-order ODE, two independent solutions form a **fundamental set**, and their linear combinations give the general solution.

Put each solution and its derivative in a column of $M(t)$. The **Wronskian** is its determinant. Evaluate all functions at the same $t$.

$$M(t)=\begin{pmatrix}y_1(t)&y_2(t)\\y_1'(t)&y_2'(t)\end{pmatrix}.$$
$$W(t)=\det M(t)=y_1y_2'-y_1'y_2.$$

For solutions of the same second-order linear homogeneous ODE with continuous normalized coefficients on an interval $I$, use these two tests.

- If $W(t_0)\ne0$ at **one point** $t_0\in I$, the solutions are linearly independent and form a **fundamental set** on $I$.
- If $W(t)=0$ at **every point** of $I$, the solutions are linearly dependent.

The nonzero test also proves independence for any two differentiable functions. The zero test above uses the shared ODE.

### Applying the initial conditions

Evaluate $M(t_0)$ and row-reduce to find the constants. The determinant of the coefficient matrix is $W(t_0)$.

$$M(t_0)\binom{C_1}{C_2}=\binom{y(t_0)}{y'(t_0)}.$$

The initial pairs $(1,0)$ and $(0,1)$ give another way to choose a fundamental set. The resulting initial-value matrix is the identity and its determinant is $1$.

## Abel's formula {#abel}

For $y''+p(t)y'+q(t)y=0$ with $p,q$ continuous on the interval,

$$W(t)=W(t_0)e^{-\int_{t_0}^{t}p(s)\,ds}.$$

## Repeated roots and reduction of order {#repeated-roots}

Use this when **one solution $y_1$ of the homogeneous equation is given** and the problem asks for a second independent solution. It also works for variable coefficients.

1. Set $y_2=v(t)y_1(t)$ on an interval where $y_1\ne0$. Differentiate twice and substitute in the homogeneous equation.
2. The terms containing $v$ cancel because $y_1$ is a solution. For $y''+py'+qy=0$, the remaining equation is $y_1v''+(2y_1'+py_1)v'=0$.
3. Set $w=v'$, solve the first-order equation for $w$, then integrate to obtain $v$. Keep a choice giving a solution independent of $y_1$.

### Recognizing the setup

For $t^2y''-3ty'+4y=0$ on $t>0$, the given solution is $y_1=t^2$. Start with $y_2=t^2v(t)$ and substitute into the original equation.
